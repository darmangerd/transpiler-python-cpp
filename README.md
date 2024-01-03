# Vyper
A simple transpiler from Python to C++ with basic type checking.

## Description
project aimed at compiling Python code to C++ language has implemented several features to achieve its objective. First, we implemented basic arithmetic calculations, thus allowing the evaluation of simple mathematical operations in the compiled Python code.

Next, we implemented conditions (if, else) which allow for decision-making in the code based on certain conditions. This enables efficient control flow management in the compiled code.

We also implemented while loops to handle loops and iterations in the compiled code.

To ensure that the compiled code adheres to Python's semantic rules, we implemented semantic checking to detect syntax or semantic errors in the source code. We also implemented type checking to ensure that variables used in the code are appropriately used and data types are respected.

To enable the use of variables, we implemented the use and definition of variables in the compiled code.

We also implemented indentation to ensure that the compiled code is well-formatted and easy to read. Moreover, indentation is essential in Python.

Finally, to allow the use of functions in the compiled code, we implemented the use and definition of functions, including the print function to display results.

## Installation
Using pip:
```bash
pip install -r requirements.txt
```

Using pipenv:
```bash
pipenv install
pipenv shell
```

## Usage
To transpile a file, run the transpiler.py file with the file to compile as an argument:
```bash
python transpiler.py sources/main.py 
```
> Note: The compiler will output the compiled file in the `out` directory with the same path and name as the input file. And the AST will be genrated as a pdf file in the sources directory.

To use the lexer and parser, run the lexer.py and parser.py files with the file to compile as an argument:
```bash
python lexer.py sources/main.py
python parser.py sources/main.py
```