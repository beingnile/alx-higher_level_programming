# Python - Hello, World.

In this project, Python is explored as a programming language.
Each file solves a particular given problem metting all the stated constraints.  
In this project, however, only the basic fundamentals were looked into.

## Project tasks.

* [0-run](./0-run) - Bash script that runs a python file saved in the environment variable `$PYFILE`
* [1-run_inline](./1-run_inline) - Bash Script that runs an inline python code stored in `$PYFILE`
* [2-print.py](./2-print.py) - Python script that prints exactly `"Programming is like building a multilingual puzzle`
* [3-print_number.py](./3-print_number.py) - Print the integer stored in the variable `number`, followed by `Battery street`
* [4-print_float.py](./4-print_float.py) - Print the float stored in the variable `number` with a precision of 2 digits
* [5-print_string.py](./5-print_string.py) - Print 3 times a string stored in the variable `str`, followed by its first 9 characters
* [6-concat.py](./6-concat.py) - Print `Welcome to Holberton School!`
* [7-edges.py](./7-edges.py) - Split string in variable `word`
* [8-concat_edges.py](./8-concat_edges.py) - Print `object-oriented programming with Python`
* [9-easter_egg.py](./9-easter_egg.py) - Python script that prints “The Zen of Python”, by TimPeters
* [100-write.py](./100-write.py) - Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`

> Constraints for this task include:
> * Use the function `write` from the `sys` module
> * You are not allowed to use `print`
> * Your script should print to `stderr`
> * Your script should exit with the status code 1

* [101-compile](./101-compile) - Compiles a Python script file stored in `$PYFILE`
* [102-magic_calculation.py](./102-magic_calculation.py) - Python function that does exacly the same as the following bytecode:

```c

3	 0 LOAD_CONST		1 (98)
	 3 LOAD_FAST		0 (a)
	 6 LOAD_FAST		1 (b)
	 9 BINARY_POWER
	10 BINARY_ADD
	11 RETURN_VALUE

```

