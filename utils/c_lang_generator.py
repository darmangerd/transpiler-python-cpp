class CLangGenerator:
    def __init__(self, code: str = ""):
        self.code = code

    def newline(self, number: int = 1):
        self.code += "\n" * number
        return self

    def space(self, number: int = 1):
        self.code += " " * number
        return self

    def preprend(self, code: str):
        self.code = code + self.code
        return self

    def include(self, name: str):
        self.write(f"#include <{name}>", semicolon=False)
        return self

    def use_namespace(self, name: str):
        self.write(f"using namespace {name}")
        return self

    def indent(self, level: int = 1, size: int = 4):
        new_code = ""
        lines = self.code.split("\n")

        for line in lines[:-1]:
            new_code += " " * size * level + line + "\n"

        self.code = new_code

        return self

    def semicolon(self):
        self.code += ";"
        return self

    def write(self, text: str, newline: bool = True, semicolon: bool = True):
        self.code += text

        if semicolon:
            self.semicolon()

        if newline:
            self.newline()

        return self

    def remove_last_char(self):
        self.code = self.code[:-1]
        return self

    def start_block(self, semicolon: bool = False, newline: bool = True):
        self.write("{", semicolon=semicolon, newline=newline)
        return self

    def end_block(self, semicolon: bool = False, newline: bool = True):
        self.write("}", semicolon=semicolon, newline=newline)
        return self

    def assign(self, name: str, value: str, type: str = None, declare: bool = True):
        if not declare:
            self.write(f"{name} = {value}")
        else:
            self.write(f"{type} {name} = {value}")

        return self

    def call_function(self, name: str, args: str):
        self.write(f"{name}({args})")
        return self

    def stream(self, name: str, value: str):
        self.write(f"{name} << {value} << endl")
        return self

    def return_statement(self, value: str):
        self.write(f"return {value}")
        return self

    def while_loop(self, condition, body: str):
        self.write(f"while ({condition}) ", semicolon=False, newline=False)
        self.start_block()
        self.add(body.indent())
        self.end_block()

        return self

    def lambda_function(self, name: str, args: str, body: str, type: str = None):
        if type:
            self.write(f"auto {name} = [] ({args}) -> {type} ",
                       semicolon=False, newline=False)
        else:
            self.write(f"auto {name} = [] ({args}) ",
                       semicolon=False, newline=False)

        self.start_block()
        self.add(body.indent())
        self.end_block(semicolon=True)

        return self

    def define_function(self, type: str, name: str, args: str, body: str):
        self.write(f"{type} {name}({args}) ", semicolon=False, newline=False)
        self.start_block()
        self.add(body.indent())
        self.end_block()

        return self

    def print(self, value: str):
        self.write(f"printf({value})")
        return self

    def print_string(self, value: str):
        self.print(f'"{value}"')
        return self

    def print_int(self, value: str):
        self.print(f'"{value} %d", {value}')
        return self

    def print_float(self, value: str):
        self.print(f'"{value} %f", {value}')
        return self

    def print_newline(self):
        self.print(r'\n')
        return self

    def __add__(self, other):
        return CLangGenerator(self.code + other.code, semicolon=False)

    def add(self, other, semicolon: bool = False, newline: bool = False):
        self.write(
            other.code,
            semicolon=semicolon,
            newline=newline
        )
        return self

    def main(self, body):
        self.write("int main() ", semicolon=False, newline=False)
        self.start_block()
        self.add(body.indent())
        self.end_block()

        return self

    def condition(self, condition: str, true_block, else_block=None):
        self.write(f"if ({condition}) ", semicolon=False, newline=False)
        self.start_block()
        self.add(true_block.indent())

        if else_block:
            self.write("} else ", semicolon=False, newline=False)
            self.start_block()
            self.add(else_block.indent())
            self.end_block()
        else:
            self.end_block()

        return self

    def to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(self.code)

    def __str__(self):
        return self.code

    def __repr__(self):
        return str(self)
