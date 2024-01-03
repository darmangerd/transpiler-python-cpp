from yacc import parse
from typing import Callable
from utils.c_lang_generator import CLangGenerator
import utils.ast as AST
import glob


class CTranspiler:
    def __init__(self, path: str) -> None:
        self.path = path
        self.files = glob.glob(path)
        self.types = {}
        self.functions = {}

    def dfs(self, root: AST.Node, func: Callable[[AST.Node], None]) -> None:
        stack = [root]

        while stack:
            node = stack.pop()
            func(node)
            for child in node.children:
                stack.insert(0, child)

    def _convert_type(self, string_type: str) -> str:
        if hasattr(string_type, "tok"):
            string_type = string_type.tok

        if string_type == "int":
            return "int"
        if string_type == "float":
            return "float"
        if string_type == "bool":
            return "bool"
        if string_type == "str":
            return "string"
        if string_type == "auto":
            return "auto"
        
        return string_type
    
    def _verify_assignment(self, node: AST.Node) -> None:
        if node.type == "assign":
            if node.init_type == "var":
                raise Exception("Cannot reassign variable")
    
    def _get_type(self, node: AST.Node, nested_types = {}) -> str:
        if node.type == "type":
            return self._convert_type(node.tok)

        if hasattr(node, "tok"):
            if nested_types is not None and node.tok in nested_types:
                return self._convert_type(nested_types[node.tok])
            elif node.tok in self.types:
                return self._convert_type(self.types[node.tok])
        
        if hasattr(node, "value_type"):
            return self._convert_type(node.value_type)

        raise Exception(f"Cannot get type for: {node}, variable might not be declared")

    def _determine_operation(self, node: AST.Node, nested_types = {}) -> str:
        generator = CLangGenerator()

        if node.type == "token":
            if isinstance(node.tok, bool):
                return str(node.tok).lower()

            return str(node.tok)

        elif node.type == "value":
            if node.value_type == "int":
                return f"{node.tok}"
            elif node.value_type == "float":
                return f"{node.tok}f"
            elif node.value_type == "bool":
                return str(node.tok).lower()
            elif node.value_type == "string":
                return f"{node.tok}"

        elif node.type == "op":
            if self._get_type(node.children[0], nested_types) != self._get_type(node.children[1], nested_types):
                raise Exception(f"Cannot operate different types for: {node.children[0]} {node.op} {node.children[1]}")

            node.value_type = self._get_type(node.children[0], nested_types)

            return self._determine_operation(node.children[0], nested_types) + f" {node.op} " + self._determine_operation(node.children[1], nested_types)

        elif node.type == "assign":
            name = self._determine_operation(node.children[0], nested_types)
            value = self._determine_operation(node.children[1], nested_types)

            if node.children[1].value_type:
                if self._get_type(node.children[0], nested_types) != self._get_type(node.children[1], nested_types):
                    raise Exception(f"Cannot assign different types for: {node.children[0]} and {node.children[1]}")

            if node.init_type:
                self.types[name] = node.children[0].value_type

            generator.assign(type="auto", declare=bool(
                node.init_type), name=name, value=value)

        elif node.type == "call":
            args = ", ".join([self._determine_operation(o, nested_types)
                             for o in node.children])
            
            if node.tok in self.functions:
                function = self.functions[node.tok]
                for i in range(len(node.children)):
                    if self._get_type(node.children[i], nested_types) != self._get_type(function[list(function.keys())[i]]):
                        raise Exception(f"Cannot call function with different types for: {node.children[i]} and {function[list(function.keys())[i]]}")

            if node.tok == "print":
                generator.stream("cout", args)
            else:
                generator.call_function(node.tok, args)

        elif node.type == "arg":
            return f"{self._convert_type(node.value_type.tok)} {node.tok}"

        elif node.type == "program":
            for child in node.children:
                generator.add(CLangGenerator(self._convert_ast_to_c(child, nested_types)))

        elif node.type == "def":
            args = ", ".join([self._determine_operation(o, nested_types)
                             for o in node.args.children])
            
            self.functions[node.tok] = {node.args.children[i].tok: node.args.children[i].value_type for i in range(len(node.args.children))}

            nested_types = {}
            for arg in node.args.children:
                nested_types[arg.tok] = arg.value_type
            
            body = CLangGenerator(
                self._convert_ast_to_c(node.children[0], nested_types))
            generator.lambda_function(node.tok, args, body)

        elif node.type == "return":
            generator.return_statement(
                self._determine_operation(node.children[0], nested_types))

        elif node.type == "while":
            condition = self._determine_operation(node.children[0], nested_types)
            body = CLangGenerator(
                self._convert_ast_to_c(node.children[1], nested_types))
            generator.while_loop(condition, body)

        elif node.type == "if":
            condition = self._determine_operation(node.children[0], nested_types)
            body = CLangGenerator(
                self._convert_ast_to_c(node.children[1], nested_types))

            else_body = None
            if len(node.children) == 3:
                else_body = CLangGenerator(
                    self._convert_ast_to_c(node.children[2], nested_types))

            generator.condition(condition, body, else_body)

        return generator.code

    def _convert_ast_to_c(self, node: AST.Node, nested_types = {}) -> str:
        line = self._determine_operation(node, nested_types)
        return line

    def _transpile_file(self, file: str) -> str:
        content = open(file).read()
        ast = parse(content)
        c_code = self._convert_ast_to_c(ast)

        code = CLangGenerator()
        code.include("iostream")
        code.use_namespace("std")
        code.main(CLangGenerator(c_code))
        return code

    def transpile(self, out_dir: str = None) -> None:
        files = [(file, self._transpile_file(file)) for file in self.files]

        if out_dir is not None:
            for file, code in files:
                # Write to file and create path if necessary
                import pathlib
                pathlib.Path(f"{out_dir}/{file}").parent.mkdir(
                    parents=True, exist_ok=True)

                with open(f"{out_dir}/{file}".replace(".py", ".cpp"), "w") as f:
                    f.write(code.code)

        return files


if __name__ == "__main__":
    import sys

    transpiler = CTranspiler(sys.argv[1])
    result = transpiler.transpile(out_dir="out")
    print(result)
