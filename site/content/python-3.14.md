# Python 3.14 — Learning & Reference Guide

> A comprehensive, beginner-to-advanced Python learning resource and quick-reference guide.
> Covers fundamentals, intermediate patterns, advanced techniques, recipes, and what's new in 3.14.

---

## Table of Contents

- **Beginner Track** — Python Fundamentals (9 sections)
- **Intermediate Track** — Levelling Up (5 sections)
- **Advanced Track** — Professional Python (5 sections)
- **Recipes & Quick-Reference Cheatsheets**
- **What's New in Python 3.14**
- **Appendix: Resources & Further Reading**

---

## Beginner Track — Python Fundamentals

The beginner track takes you from zero to writing real Python scripts. Every section includes
explanations, examples, common mistakes, and practice ideas.

---

### Getting Started: Installing Python & Running Code

**Goal:** Get Python installed and run your very first lines of code.

#### Installing Python

1. Go to **https://www.python.org/downloads/** and download the latest Python 3.14.x installer.
2. **Windows:** Run the installer. **Check** "Add Python to PATH" before clicking Install.
3. **macOS:** Use the `.pkg` installer or Homebrew: `brew install python@3.14`.
4. **Linux:** Most distros include Python. Otherwise: `sudo apt install python3.14` (Debian/Ubuntu).

Verify the installation in a terminal:

```bash
python --version
# Should print: Python 3.14.x
```

#### The Python REPL (interactive shell)

Open a terminal and type `python` (or `python3`):

```bash
python
```

You get an interactive prompt (`>>>`). Try typing:

```python
>>> 2 + 3
5
>>> "hello".upper()
'HELLO'
>>> "hi" * 3
'hihihi'
>>> quit()
```

The REPL is perfect for quick experiments. Use it constantly as you learn.

#### Running a script file

Create a file called `main.py` with any text editor:

```python
print("Hello from Python 3.14!")
```

Run it from your terminal:

```bash
python main.py
```

You should see `Hello from Python 3.14!` printed.

#### Choosing an editor

Any editor works, but these are popular for Python:
- **VS Code** (free, excellent Python extension, integrated terminal).
- **PyCharm** (powerful IDE with debugging, refactoring).
- **Thonny** (simple, beginner-friendly, built-in debugger).

Pick one and stick with it as you work through this guide.

---

### Understanding How Python Executes Your Code

**Goal:** Understand what happens behind the scenes when you run Python, so you can reason about errors, performance, and how your code actually executes.

---

#### Interpreted vs compiled — what does it mean?

Programming languages fall on a spectrum:
- **Compiled languages** (C, Rust, Go) are translated into machine code *before* you run them. You run the compiled binary directly.
- **Interpreted languages** (Python, JavaScript, Ruby) are translated *while* the program runs.

Python sits in the middle — it's **compiled to bytecode, then interpreted**:

```
Your code (.py) → Python compiler → Bytecode (.pyc) → Python Virtual Machine → Output
```

When you run `python main.py`, here's what happens step by step:

1. **Lexing/Parsing**: Python reads your `.py` file and checks the syntax is valid. If you have a `SyntaxError`, it fails here — your code never even starts running.
2. **Compilation to bytecode**: Python translates your code into a compact format called **bytecode** — a set of low-level instructions. This gets cached in `__pycache__/` folders as `.pyc` files.
3. **Execution**: The **Python Virtual Machine (PVM)** reads and executes the bytecode instructions one by one.

**Why does this matter to you?**
- You never need to manually compile anything — just run `python your_file.py`.
- If Python can't even *read* your code (syntax error), the error appears *before* any code runs.
- If an error happens *during* execution (like dividing by zero), Python has already started running — some `print()` calls may have executed before the crash.

Example showing this distinction:

```python
print("This will print")
print("This will also print")
x = 1 / 0  # ZeroDivisionError happens HERE at runtime
print("This will NEVER print")
```

Output:
```
This will print
This will also print
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    x = 1 / 0
ZeroDivisionError: division by zero
```

The first two prints worked because the error is a *runtime* error, not a *syntax* error.

Compare with a syntax error:

```python
print("Will this print?")
def broken(    # <-- missing closing parenthesis
```

Output:
```
  File "main.py", line 2
    def broken(
              ^
SyntaxError: unexpected EOF while parsing
```

Nothing prints — Python couldn't even compile the file.

---

#### Top-to-bottom execution

Python executes statements from top to bottom, in order:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

```
Step 1
Step 2
Step 3
```

This means:
- You must **define** a variable before you **use** it.
- You must **define** a function before you **call** it.

```python
# This WORKS — greeting is defined before use
greeting = "Hello"
print(greeting)

# This FAILS — age hasn't been defined yet
print(age)  # NameError: name 'age' is not defined
age = 25
```

---

#### Variables are references (labels, not boxes)

This is one of the most important mental models in Python. **Variables are NOT boxes that store values.** Instead, they are **labels (sticky notes) that point to objects in memory.**

```python
a = [1, 2, 3]
b = a           # b points to the SAME list, not a copy!

b.append(4)
print(a)        # [1, 2, 3, 4] — a changed too!
```

Think of it like this:
- `a = [1, 2, 3]` creates a list object somewhere in memory, then puts a label "a" on it.
- `b = a` puts another label "b" on that **same** object.
- When you modify through `b`, you're modifying the same object that `a` points to.

If you want an independent copy:

```python
a = [1, 2, 3]
b = a.copy()    # or: b = list(a)  or: b = a[:]

b.append(4)
print(a)        # [1, 2, 3] — a is unchanged
print(b)        # [1, 2, 3, 4]
```

**Why does this matter?**
- It's the #1 source of bugs for beginners: you think you copied something but you just created another reference.
- It explains why functions can modify lists passed to them (they receive a reference, not a copy).
- It's why `==` and `is` are different:

```python
a = [1, 2]
b = [1, 2]

print(a == b)   # True — same VALUE
print(a is b)   # False — different OBJECTS in memory
```

---

#### Everything in Python is an object

In Python, literally **everything** is an object — numbers, strings, functions, modules, even types themselves:

```python
x = 42
print(type(x))        # <class 'int'>

name = "Harry"
print(type(name))     # <class 'str'>

print(type(print))    # <class 'builtin_function_or_method'>
print(type(type))     # <class 'type'>
```

Every object has:
- A **type** (what kind of thing it is)
- A **value** (the actual data)
- An **identity** (a unique ID — checked with `is`)

```python
x = 42
print(type(x))    # <class 'int'>
print(id(x))      # some number like 140234567890 (memory address)
```

**Why does this matter?**
- You can pass functions as arguments, store them in variables, etc. (this becomes powerful later).
- Methods like `"hello".upper()` work because `"hello"` is an object of type `str`, and `str` has an `upper` method.

---

#### Garbage collection (basics)

When no variable points to an object anymore, Python automatically **frees the memory**. You don't need to worry about this — just know it happens:

```python
x = [1, 2, 3]   # list created, x points to it
x = "hello"      # x now points to a string; the list has no references
                  # → Python automatically cleans up the list
```

You'll almost never need to think about this, but it's why Python is easier than C/C++ — you don't manually free memory.

---

#### The `__pycache__` folder

After Python compiles your code to bytecode, it caches it:

```
my_project/
  main.py
  utils.py
  __pycache__/
    main.cpython-314.pyc
    utils.cpython-314.pyc
```

- These `.pyc` files make subsequent runs faster (Python skips the compilation step).
- You can safely delete `__pycache__/` — Python will recreate it.
- Add `__pycache__/` to your `.gitignore` file.

---

#### Mini-project: Explore how Python runs code

Try this experiment yourself:

```python
# experiment.py — run this and observe the output order

print("1. Before function definition")

def my_func():
    print("3. Inside function (only when called)")

print("2. After function definition, before call")

my_func()

print("4. After function call")
```

Expected output:
```
1. Before function definition
2. After function definition, before call
3. Inside function (only when called)
4. After function call
```

**Key takeaway:** `def` only *defines* the function — it doesn't run the body. The body runs when you *call* it with `my_func()`.

---

### Syntax, Variables & Fundamental Data Types

**Goal:** Master the building blocks of every Python program — how code is structured, how you store data, and what types of data exist.

---

#### Whitespace & indentation

Python uses **indentation** (spaces) to define which lines belong together (called a "block"):

```python
age = 20

if age >= 18:
    print("adult")      # ← this line is INSIDE the if block (4 spaces)
    print("can vote")   # ← this too
else:
    print("minor")      # ← this is inside the else block

print("done")           # ← this is OUTSIDE both blocks (no indentation)
```

**Rules:**
- Use **4 spaces** per indentation level (PEP 8 standard).
- **Never** mix tabs and spaces — configure your editor to insert spaces when you press Tab.
- After any line ending with `:` (if, else, for, while, def, class), the next line must be indented.

**Common errors:**

```python
# IndentationError — forgot to indent
if True:
print("oops")  # ERROR: expected an indented block

# IndentationError — inconsistent indentation
if True:
    print("line 1")
      print("line 2")  # ERROR: unexpected indent (6 spaces instead of 4)
```

---

#### Comments — talk to your future self

```python
# This is a single-line comment — Python ignores it completely

x = 10  # You can also put comments after code

# Multi-line comments are just multiple single-line comments:
# This explains something
# that takes several lines
```

**Guidelines for good comments:**
- Explain **why**, not **what** (the code shows what):

```python
# BAD comment — just repeats the code:
x = x + 1  # add 1 to x

# GOOD comment — explains the reason:
x = x + 1  # compensate for zero-based indexing in the display
```

- Use comments for **complex logic**, **business rules**, and **non-obvious decisions**.
- If you need lots of comments, consider renaming variables/functions to be clearer instead.

**Docstrings** (covered more in B5) are a special kind of comment for functions and classes:

```python
def calculate_tax(income: float) -> float:
    """Calculate UK income tax based on 2024 tax bands."""
    ...
```

---

#### Variables — names that point to values

A variable is a **name** that refers to a value. You create one with `=` (the assignment operator):

```python
age = 25           # 'age' now refers to the integer 25
name = "Harry"     # 'name' refers to the string "Harry"
pi = 3.14159       # 'pi' refers to a float
is_student = True  # 'is_student' refers to a boolean
```

**Variables can be reassigned** — they're just labels:

```python
x = 10
print(x)    # 10
x = "hello"
print(x)    # "hello" — x now points to a string instead of an int
```

Python is **dynamically typed** — you don't declare a type. The type comes from the value, not the variable name.

**Naming rules:**
- Must start with a letter or underscore: `count`, `_private`, `myVar`
- Can contain letters, digits, underscores: `item_2`, `MAX_SIZE`
- Case-sensitive: `name`, `Name`, and `NAME` are three different variables
- Cannot use Python keywords: `if`, `for`, `class`, `return`, etc.

**Naming conventions (PEP 8):**

```python
# Regular variables and functions: snake_case
user_name = "Alice"
total_price = 99.50
def calculate_total(): ...

# Constants (values that shouldn't change): UPPER_SNAKE_CASE
MAX_RETRIES = 3
DATABASE_URL = "localhost:5432"
PI = 3.14159

# Classes: PascalCase (CapWords)
class UserProfile: ...
class ShoppingCart: ...

# Private/internal: leading underscore
_internal_counter = 0
def _helper_function(): ...
```

**Multiple assignment:**

```python
# Assign multiple variables at once
x, y, z = 1, 2, 3

# Swap two variables (no temp needed!)
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# Same value to multiple variables
x = y = z = 0
```

---

#### Numbers — int, float, and complex

**Integers (`int`)** — whole numbers, unlimited size:

```python
count = 42
negative = -7
big = 1_000_000_000   # underscores as visual separators (same as 1000000000)
binary = 0b1010        # binary literal = 10
hexadecimal = 0xFF     # hex literal = 255
octal = 0o77           # octal literal = 63
```

Python integers can be **arbitrarily large** — no overflow:

```python
huge = 2 ** 1000  # a number with 302 digits — Python handles it fine
print(len(str(huge)))  # 302
```

**Floats (`float`)** — decimal numbers, limited precision:

```python
price = 19.99
temperature = -4.5
scientific = 6.022e23   # 6.022 x 10^23 (Avogadro's number)
small = 1.5e-10         # 0.00000000015
```

**WARNING — floating point precision:**

```python
print(0.1 + 0.2)         # 0.30000000000000004 (NOT 0.3!)
print(0.1 + 0.2 == 0.3)  # False!
```

This is not a Python bug — it's how ALL computers store decimals. For exact decimal arithmetic, use the `decimal` module:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 (exact)
```

**Complex numbers** (rarely needed, but Python has them):

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

**Useful number functions:**

```python
abs(-5)          # 5 (absolute value)
round(3.7)       # 4
round(3.14159, 2)  # 3.14 (round to 2 decimal places)
min(3, 1, 4)     # 1
max(3, 1, 4)     # 4
pow(2, 10)       # 1024 (same as 2 ** 10)
divmod(17, 5)    # (3, 2) — quotient and remainder
```

**Type conversion between numbers:**

```python
int(3.9)    # 3 (truncates toward zero, does NOT round)
int(-3.9)   # -3
float(42)   # 42.0
int("123")  # 123 (string to int)
float("3.14")  # 3.14 (string to float)
```

---

#### Strings — text data

Strings are **sequences of characters**, immutable (cannot be changed in place).

**Creating strings:**

```python
single = 'Hello'
double = "Hello"           # exactly the same as single quotes
multiline = """This spans
multiple lines."""
raw = r"C:\new\folder"     # raw string — backslashes are literal
```

**Escape characters:**

```python
print("Line 1\nLine 2")   # \n = newline
print("Column1\tColumn2")  # \t = tab
print("She said \"hi\"")   # \" = literal quote
print("Path: C:\\Users")    # \\ = literal backslash
```

**String indexing and slicing:**

```python
s = "Python"
print(s[0])     # 'P' (first character)
print(s[-1])    # 'n' (last character)
print(s[1:4])   # 'yth' (characters 1, 2, 3)
print(s[:3])    # 'Pyt' (first 3)
print(s[3:])    # 'hon' (from index 3 to end)
print(s[::-1])  # 'nohtyP' (reversed)
```

**f-strings (formatted string literals)** — the modern way to build strings:

```python
name = "Harry"
age = 25
print(f"My name is {name} and I am {age} years old.")
# My name is Harry and I am 25 years old.

# You can put any expression inside the braces:
print(f"Next year I'll be {age + 1}")
print(f"Name uppercase: {name.upper()}")

# Formatting numbers:
price = 49.5
print(f"Price: ${price:.2f}")         # Price: $49.50
print(f"Big number: {1000000:,}")     # Big number: 1,000,000
print(f"Percentage: {0.856:.1%}")     # Percentage: 85.6%

# Padding and alignment:
print(f"{'left':<20}|")    # left                |
print(f"{'right':>20}|")   #                right|
print(f"{'center':^20}|")  #       center       |
```

**Essential string methods** (strings have ~47 methods — here are the ones you'll use constantly):

```python
s = "  Hello, World!  "

# Cleaning up
s.strip()        # 'Hello, World!' (remove whitespace from both ends)
s.lstrip()       # 'Hello, World!  ' (left strip only)
s.rstrip()       # '  Hello, World!' (right strip only)

# Case changes
"hello".upper()       # 'HELLO'
"HELLO".lower()       # 'hello'
"hello world".title() # 'Hello World'
"hello world".capitalize()  # 'Hello world'

# Searching
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True
"Hello World".find("World")  # 6 (index where found, -1 if not)
"Hello World".count("l")    # 3

# Checking content
"hello".isalpha()    # True (only letters)
"12345".isdigit()    # True (only digits)
"hello123".isalnum() # True (letters or digits)
"   ".isspace()      # True (only whitespace)

# Replacing
"Hello World".replace("World", "Python")  # 'Hello Python'

# Splitting and joining
"a,b,c".split(",")           # ['a', 'b', 'c']
"hello world".split()        # ['hello', 'world'] (splits on whitespace)
", ".join(["a", "b", "c"])   # 'a, b, c'
"\n".join(["line1", "line2"]) # 'line1\nline2'
```

**String immutability:**

```python
s = "Hello"
# s[0] = "h"   # TypeError: 'str' object does not support item assignment

# Instead, create a new string:
s = "h" + s[1:]   # "hello"
```

**Practical example — parsing user input:**

```python
raw_input = "  Harry Gomm  "
clean = raw_input.strip()
first, last = clean.split(" ")
email = f"{first.lower()}.{last.lower()}@example.com"
print(email)  # harry.gomm@example.com
```

---

#### Booleans — True and False

Booleans represent truth values. There are exactly two: `True` and `False`.

```python
is_raining = True
has_umbrella = False
```

Booleans come from comparisons:

```python
5 > 3       # True
5 == 3      # False
5 != 3      # True
"a" < "b"   # True (alphabetical comparison)
```

Boolean operators:

```python
True and True    # True
True and False   # False
True or False    # True
not True         # False
```

**Short-circuit evaluation:**

```python
# Python stops evaluating as soon as it knows the result:
True or expensive_function()    # Never calls expensive_function
False and expensive_function()  # Never calls expensive_function
```

This is a common pattern:

```python
# Safe: only access name if user is not None
if user is not None and user.name == "admin":
    grant_access()
```

---

#### None — the "nothing" value

`None` is Python's special "no value" / "empty" / "not set" value:

```python
result = None   # we don't have a result yet

def find_user(name):
    users = {"alice": 30, "bob": 25}
    return users.get(name)  # returns None if key not found

user = find_user("charlie")
if user is None:
    print("User not found")
```

**Always use `is` (not `==`) to compare with None:**

```python
x = None
if x is None:      # correct
    print("empty")

if x == None:      # works but bad style — use 'is'
    print("empty")
```

---

#### Type checking and conversion

**Check the type of a value:**

```python
x = 42
print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(x, (int, float)))  # True (is it int OR float?)
```

**Convert between types:**

```python
# String to Number
int("42")       # 42
float("3.14")   # 3.14
int("0xFF", 16) # 255 (parse hex string)

# Number to String
str(42)         # "42"
str(3.14)       # "3.14"

# int and float
int(3.9)        # 3 (truncates, does NOT round!)
float(42)       # 42.0

# To bool
bool(0)         # False
bool(1)         # True
bool("")        # False (empty string is falsy)
bool("hello")   # True (non-empty string is truthy)
bool([])        # False (empty list is falsy)
bool([1, 2])    # True (non-empty list is truthy)
```

**Common conversion mistake:**

```python
age_text = input("Enter age: ")  # input() ALWAYS returns a string
# age_text + 1  # TypeError: can only concatenate str to str

age = int(age_text)  # convert to int first
print(age + 1)       # now it works
```

---

#### Operators — complete reference

**Arithmetic operators:**

```python
10 + 3    # 13   (addition)
10 - 3    # 7    (subtraction)
10 * 3    # 30   (multiplication)
10 / 3    # 3.33 (true division — always returns float)
10 // 3   # 3    (floor division — rounds down to int)
10 % 3    # 1    (modulus — remainder of division)
10 ** 3   # 1000 (exponentiation — 10 to the power of 3)
```

**Assignment operators (shortcuts):**

```python
x = 10
x += 3    # x = x + 3 -> 13
x -= 2    # x = x - 2 -> 11
x *= 4    # x = x * 4 -> 44
x /= 2    # x = x / 2 -> 22.0
x //= 3   # x = x // 3 -> 7.0
x %= 5    # x = x % 5 -> 2.0
x **= 3   # x = x ** 3 -> 8.0
```

**Comparison operators:**

```python
5 == 5    # True  (equal)
5 != 3    # True  (not equal)
5 > 3     # True  (greater than)
5 < 3     # False (less than)
5 >= 5    # True  (greater than or equal)
5 <= 3    # False (less than or equal)

# Chained comparisons (Python unique feature):
x = 5
1 < x < 10    # True (is x between 1 and 10?)
1 < x < 3     # False
```

**Identity operators:**

```python
a = [1, 2]
b = a           # same object
c = [1, 2]     # different object, same value

a is b          # True (same object in memory)
a is c          # False (different objects)
a == c          # True (same value)
a is not c      # True
```

**Membership operators:**

```python
"h" in "hello"       # True
3 in [1, 2, 3]       # True
"x" not in "hello"   # True
"key" in {"key": 1}  # True (checks dict keys)
```

**Operator precedence (most important to know):**
1. `**` (exponent)
2. `* / // %`
3. `+ -`
4. `== != < > <= >=`
5. `not`
6. `and`
7. `or`

**When in doubt, use parentheses:**

```python
# Unclear:
result = 2 + 3 * 4 ** 2

# Clear:
result = 2 + (3 * (4 ** 2))  # = 2 + (3 * 16) = 2 + 48 = 50
```

---

#### Mini-project: Personal info card

Build a script that demonstrates everything from this section:

```python
# personal_info.py — demonstrates B2 concepts

# Variables (2.3)
first_name = "Harry"
last_name = "Gomm"
age = 25
height_m = 1.78
is_student = True
favourite_languages = ["Python", "JavaScript"]

# Type checking (2.8)
print(f"Name type: {type(first_name)}")  # <class 'str'>
print(f"Age type: {type(age)}")          # <class 'int'>

# f-string formatting (2.5)
full_name = f"{first_name} {last_name}"
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Height: {height_m:.1f}m")
print(f"Student: {'Yes' if is_student else 'No'}")
print(f"Languages: {', '.join(favourite_languages)}")

# Operators (2.9)
birth_year = 2026 - age
print(f"Born approximately: {birth_year}")

bmi = 75 / (height_m ** 2)
print(f"BMI (if 75kg): {bmi:.1f}")

# String methods (2.5)
email = f"{first_name.lower()}.{last_name.lower()}@email.com"
print(f"Email: {email}")

# None (2.7)
middle_name = None
if middle_name is None:
    print("No middle name on file")

# Boolean logic (2.6)
can_vote = age >= 18
can_drive = age >= 17
print(f"Can vote: {can_vote}, Can drive: {can_drive}")
print(f"Can vote AND drive: {can_vote and can_drive}")
```

---

#### Practice exercises

1. **Type explorer**: Write a script that creates one variable of each type (int, float, str, bool, None, list, dict) and prints its type and value.
2. **String manipulator**: Ask the user for their full name, then print it in uppercase, lowercase, title case, and reversed.
3. **Calculator**: Ask for two numbers and print the result of all arithmetic operations (+, -, *, /, //, %, **).
4. **Temperature converter**: Convert between Celsius and Fahrenheit using the formula `F = C * 9/5 + 32`.

---

### Collections: Lists, Tuples, Dictionaries & Sets

**Goal:** Master Python's four core container types. You'll use lists and dicts in virtually every program, so this section is intentionally deep with mental models, examples, performance notes, and projects.

---

#### Overview — when to use what

| Type | Ordered? | Mutable? | Duplicates? | Best for |
|------|----------|----------|-------------|----------|
| `list` | Yes | Yes | Yes | Sequences: items in order |
| `tuple` | Yes | No | Yes | Fixed records, dict keys, function returns |
| `dict` | Yes (insertion) | Yes | keys: No | Labeled data, lookups by key |
| `set` | No | Yes | No | Membership tests, deduplication |

**Mental model:**
- **list** = a row of items in a specific order (like a shopping list).
- **tuple** = a fixed package of values (like GPS coordinates).
- **dict** = a lookup table (like a phone book — look up by name, get number).
- **set** = a bag of unique items (like a jar of marbles where no two are the same colour).

---

#### Lists — ordered, mutable sequences

**Creating lists:**

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]   # can mix types (but usually don't)
nested = [[1, 2], [3, 4], [5, 6]]  # list of lists
from_range = list(range(10))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Accessing elements:**

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits[0]     # 'apple' (first element)
fruits[-1]    # 'elderberry' (last element)
fruits[-2]    # 'date' (second from last)
```

**Slicing — extract sublists:**

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]     # [2, 3, 4] (index 2 up to but NOT including 5)
nums[:3]      # [0, 1, 2] (first 3 elements)
nums[7:]      # [7, 8, 9] (from index 7 to end)
nums[::2]     # [0, 2, 4, 6, 8] (every 2nd element)
nums[1::2]    # [1, 3, 5, 7, 9] (odd-indexed elements)
nums[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
nums[3:7]     # [3, 4, 5, 6]
```

**Slicing pattern:** `list[start:stop:step]` — start is inclusive, stop is exclusive.

**Modifying lists:**

```python
tasks = ["buy milk", "write code", "exercise"]

# Add items
tasks.append("read book")            # add to end
tasks.insert(1, "check email")       # insert at specific position
tasks.extend(["cook dinner", "sleep"])  # add multiple items

# Remove items
tasks.remove("exercise")             # remove first occurrence by value
last = tasks.pop()                    # remove and return last item
second = tasks.pop(1)                # remove and return item at index 1
del tasks[0]                         # delete by index (no return)
tasks.clear()                        # remove all items
```

**Important: `append` vs `extend`:**

```python
a = [1, 2, 3]
a.append([4, 5])   # [1, 2, 3, [4, 5]] — adds the LIST as one element!
a = [1, 2, 3]
a.extend([4, 5])   # [1, 2, 3, 4, 5] — adds each element individually
```

**Sorting:**

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()              # sorts in place: [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns a NEW list (doesn't modify original):
original = [3, 1, 4]
new_sorted = sorted(original)  # [1, 3, 4]
print(original)                # [3, 1, 4] — unchanged

# Sort by custom key:
words = ["banana", "apple", "cherry"]
words.sort(key=len)  # sort by length: ['apple', 'banana', 'cherry']

names = ["Charlie", "alice", "Bob"]
names.sort(key=str.lower)  # case-insensitive: ['alice', 'Bob', 'Charlie']
```

**Useful list operations:**

```python
nums = [3, 1, 4, 1, 5]

len(nums)          # 5 (length)
sum(nums)          # 14
min(nums)          # 1
max(nums)          # 5
nums.count(1)      # 2 (how many times 1 appears)
nums.index(4)      # 2 (first index where 4 appears)
nums.reverse()     # reverses in place
4 in nums          # True (membership test)
7 in nums          # False
```

**List comprehensions — the Pythonic way to build lists:**

```python
# Instead of:
squares = []
for n in range(10):
    squares.append(n ** 2)

# Write:
squares = [n ** 2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a condition (filter):
evens = [n for n in range(20) if n % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform and filter:
long_upper = [name.upper() for name in ["alice", "bob", "charlie"] if len(name) > 3]
# ['ALICE', 'CHARLIE']

# Nested comprehension (flatten a list of lists):
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

**Iterating with index — `enumerate`:**

```python
fruits = ["apple", "banana", "cherry"]

# Instead of:
for i in range(len(fruits)):
    print(i, fruits[i])

# Use enumerate:
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start counting from 1:
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

**Iterating over two lists — `zip`:**

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Copying lists (important!):**

```python
original = [1, 2, 3]

# These create REFERENCES (not copies):
alias = original           # alias IS original
alias.append(4)
print(original)            # [1, 2, 3, 4] — modified!

# These create SHALLOW copies:
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# For nested lists, use DEEP copy:
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0].append(99)
print(nested)  # [[1, 2], [3, 4]] — unchanged
```

---

#### Tuples — ordered, immutable sequences

Tuples are like lists but **cannot be modified** after creation:

```python
point = (10, 20)
rgb = (255, 128, 0)
singleton = (42,)     # note the comma — without it, (42) is just 42
empty = ()
```

**Unpacking** (very common pattern):

```python
x, y = (10, 20)    # x=10, y=20
name, age, city = ("Harry", 25, "Cardiff")

# Swap variables:
a, b = b, a
```

**When to use tuples vs lists:**

| Use a tuple | Use a list |
|---|---|
| Data won't change (coordinates, RGB) | Data will grow/shrink (todo items, search results) |
| Returning multiple values from a function | Collecting items in a loop |
| Using as a dict key (tuples are hashable) | Sorting, filtering, modifying |

```python
# Tuple as dict key (lists can't do this):
locations = {}
locations[(51.5, -3.2)] = "Cardiff"
locations[(51.5, -0.1)] = "London"

# Returning multiple values:
def divide(a, b):
    return a // b, a % b   # returns a tuple

quotient, remainder = divide(17, 5)
print(quotient, remainder)  # 3 2
```

**Named tuples (readable tuples):**

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)    # 10 20 — access by name instead of index
```

---

#### Dicts — key-value mappings

Dicts are your go-to for **labeled data** (like JSON objects, config files, database records).

**Creating dicts:**

```python
empty = {}
user = {"name": "Alice", "age": 30, "city": "London"}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)
```

**Accessing values:**

```python
user = {"name": "Alice", "age": 30}

user["name"]              # 'Alice'
# user["email"]           # KeyError! Key doesn't exist

user.get("email")         # None (no error)
user.get("email", "N/A")  # 'N/A' (default if missing)
```

**Modifying dicts:**

```python
user = {"name": "Alice", "age": 30}

user["email"] = "alice@example.com"  # add new key
user["age"] = 31                      # update existing key
del user["age"]                       # remove key

# Pop: remove and return value
email = user.pop("email")
# Pop with default (no error if missing):
phone = user.pop("phone", "N/A")

# Update with another dict:
user.update({"age": 31, "city": "London"})
```

**Iterating over dicts:**

```python
user = {"name": "Alice", "age": 30, "city": "London"}

# Keys (default):
for key in user:
    print(key)

# Values:
for value in user.values():
    print(value)

# Both:
for key, value in user.items():
    print(f"{key}: {value}")
```

**Dict comprehensions:**

```python
# Square numbers:
squares = {n: n ** 2 for n in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter:
passing = {name: score for name, score in
           [("Alice", 85), ("Bob", 42), ("Charlie", 91)]
           if score >= 50}
# {'Alice': 85, 'Charlie': 91}

# Invert a dict:
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

**Checking for keys:**

```python
user = {"name": "Alice", "age": 30}

"name" in user      # True
"email" in user     # False
"email" not in user # True
```

**`setdefault` — get or set if missing:**

```python
# Count words without checking if key exists:
text = "the cat sat on the mat the cat"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# Group items:
students = [("Alice", "Maths"), ("Bob", "Science"), ("Alice", "English")]
by_student = {}
for name, subject in students:
    by_student.setdefault(name, []).append(subject)
print(by_student)
# {'Alice': ['Maths', 'English'], 'Bob': ['Science']}
```

**Nested dicts (very common in real code):**

```python
users = {
    "alice": {"age": 30, "city": "London", "scores": [85, 92, 78]},
    "bob": {"age": 25, "city": "Cardiff", "scores": [90, 88, 95]},
}

print(users["alice"]["city"])         # 'London'
print(users["bob"]["scores"][-1])     # 95 (last score)

# Safe nested access:
def get_nested(data, *keys, default=None):
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data

print(get_nested(users, "alice", "city"))    # 'London'
print(get_nested(users, "charlie", "city"))  # None
```

---

#### Sets — unique, unordered collections

**Creating sets:**

```python
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} — duplicates removed
empty_set = set()  # NOT {} — that creates an empty dict!
```

**Set operations:**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b     # {1, 2, 3, 4, 5, 6}  — union
a & b     # {3, 4}               — intersection
a - b     # {1, 2}               — difference (in a but not b)
a ^ b     # {1, 2, 5, 6}         — symmetric difference
```

**Modifying sets:**

```python
s = {1, 2, 3}
s.add(4)               # {1, 2, 3, 4}
s.discard(2)           # {1, 3, 4} — no error if not present
s.remove(3)            # {1, 4} — KeyError if not present
s.update({5, 6})       # {1, 4, 5, 6}
```

**Real-world uses:**

```python
# Remove duplicates from a list (preserving order):
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
seen = set()
unique = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique.append(item)
print(unique)  # [3, 1, 4, 5, 9, 2, 6]

# Find common elements:
my_friends = {"alice", "bob", "charlie", "diana"}
your_friends = {"bob", "diana", "eve", "frank"}
mutual = my_friends & your_friends
print(mutual)  # {'bob', 'diana'}

# Fast membership testing:
valid_codes = {"A1", "B2", "C3", "D4"}  # set lookup is O(1)
user_code = "B2"
if user_code in valid_codes:
    print("Valid!")
```

**Set comprehensions:**

```python
# Unique first letters:
names = ["Alice", "Bob", "Anna", "Charlie", "Alex"]
first_letters = {name[0] for name in names}
# {'A', 'B', 'C'}
```

---

#### Performance cheat sheet

| Operation | list | dict | set |
|-----------|------|------|-----|
| Access by index | O(1) | N/A | N/A |
| Access by key | N/A | O(1) | N/A |
| Search (is x in?) | O(n) slow | O(1) fast | O(1) fast |
| Add item | O(1)* | O(1) | O(1) |
| Remove item | O(n) | O(1) | O(1) |

**Rule of thumb:** If you're checking "is this item in my collection?" more than a few times, use a **set or dict** instead of a list.

---

#### Mini-project A: Contact book

```python
# contact_book.py — demonstrates dicts, lists, and sets

contacts = {}

def add_contact(name, phone, tags=None):
    contacts[name] = {
        "phone": phone,
        "tags": set(tags) if tags else set()
    }

def find_by_tag(tag):
    return [name for name, info in contacts.items() if tag in info["tags"]]

def show_all():
    if not contacts:
        print("No contacts yet.")
        return
    for name, info in sorted(contacts.items()):
        tags = ", ".join(info["tags"]) if info["tags"] else "none"
        print(f"  {name}: {info['phone']} (tags: {tags})")

# Usage:
add_contact("Alice", "07700-111111", ["work", "python"])
add_contact("Bob", "07700-222222", ["friend", "python"])
add_contact("Charlie", "07700-333333", ["work"])

print("All contacts:")
show_all()

print("\nPython contacts:")
for name in find_by_tag("python"):
    print(f"  {name}")

print("\nWork contacts:")
for name in find_by_tag("work"):
    print(f"  {name}")
```

---

#### Mini-project B: Student grade tracker

```python
# grade_tracker.py — nested dicts, list operations, f-strings

students = {}

def add_grade(student, subject, score):
    if student not in students:
        students[student] = {}
    if subject not in students[student]:
        students[student][subject] = []
    students[student][subject].append(score)

def get_average(student):
    all_scores = []
    for scores in students.get(student, {}).values():
        all_scores.extend(scores)
    return sum(all_scores) / len(all_scores) if all_scores else 0

def report(student):
    if student not in students:
        print(f"{student}: No records found.")
        return
    print(f"\n--- Report for {student} ---")
    for subject, scores in students[student].items():
        avg = sum(scores) / len(scores)
        print(f"  {subject}: scores={scores}, avg={avg:.1f}")
    overall = get_average(student)
    print(f"  Overall average: {overall:.1f}")

# Usage:
add_grade("Alice", "Maths", 85)
add_grade("Alice", "Maths", 90)
add_grade("Alice", "English", 78)
add_grade("Bob", "Maths", 72)
add_grade("Bob", "Science", 88)

report("Alice")
report("Bob")

# Find top student:
averages = {name: get_average(name) for name in students}
top = max(averages, key=averages.get)
print(f"\nTop student: {top} (avg: {averages[top]:.1f})")
```

---

#### Practice exercises

1. **List manipulation**: Create a list of 10 random numbers. Print them sorted, reversed, and with duplicates removed.
2. **Word frequency counter**: Given a paragraph of text, count how many times each word appears using a dict.
3. **Set operations**: Given two lists of student names from two classes, find students in both classes, only in class A, and only in class B.
4. **Nested structure**: Build a dict representing a simple shopping cart where keys are product names and values are dicts with "price" and "quantity". Write a function to calculate the total.

---

### Control Flow: Conditionals, Loops & Logic

**Goal:** Master the tools that let your program make decisions and repeat actions. Control flow is the "brain" of every program.

---

#### `if` / `elif` / `else` — making decisions

The most basic decision: "if something is true, do this":

```python
age = 20

if age >= 18:
    print("You are an adult")
```

Add alternatives with `elif` (else if) and `else`:

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} = Grade {grade}")
```

**How Python evaluates this:**
1. Check `score >= 90` -- False, skip.
2. Check `score >= 80` -- False, skip.
3. Check `score >= 70` -- True, execute this block, **skip all remaining elif/else**.

**Important:** Only ONE block executes — the first one that matches.

**Nested ifs:**

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the show!")
    elif age >= 13:
        print("Welcome! Parental guidance advised.")
    else:
        print("Sorry, too young for this show.")
else:
    print("Please buy a ticket first.")
```

**Ternary expression (one-line if):**

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"

# Useful in f-strings:
print(f"You are {'old enough' if age >= 18 else 'too young'}")
```

---

#### Truthiness — what counts as True or False?

`if` doesn't require an actual boolean — anything can be tested:

**Falsy values (treated as False):**
- `False`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)
- `None`

**Everything else is Truthy:**
- Any non-zero number
- Any non-empty string, list, dict, etc.

```python
# Common pattern — check if a list has items:
items = []
if items:
    print("Has items")
else:
    print("Empty list")     # this runs

# Check if a string is non-empty:
name = input("Enter name: ")
if name:
    print(f"Hello, {name}")
else:
    print("You didn't enter a name")
```

**This lets you write cleaner code:**

```python
# Instead of:
if len(my_list) > 0:
    ...

# Write:
if my_list:
    ...

# Instead of:
if name != "":
    ...

# Write:
if name:
    ...
```

---

#### `for` loops — iterating over sequences

`for` loops go through each item in a sequence one at a time:

```python
# Loop over a list:
colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)

# Loop over a string:
for char in "Python":
    print(char)

# Loop over a range of numbers:
for i in range(5):    # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):     # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 20, 3): # 0, 3, 6, 9, 12, 15, 18
    print(i)

for i in range(10, 0, -1): # 10, 9, 8, ..., 1 (countdown)
    print(i)
```

**Common loop patterns:**

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Pattern 1: enumerate — index + value
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# Pattern 2: zip — iterate two lists together
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Pattern 3: reversed
for name in reversed(names):
    print(name)

# Pattern 4: sorted
for name in sorted(names):
    print(name)

# Pattern 5: dict iteration
user = {"name": "Alice", "age": 30, "city": "London"}
for key, value in user.items():
    print(f"{key}: {value}")
```

**Building results with loops:**

```python
# Accumulate a total:
prices = [10.99, 5.50, 23.00, 8.75]
total = 0
for price in prices:
    total += price
print(f"Total: ${total:.2f}")

# Build a new list:
names = ["alice", "bob", "charlie"]
upper_names = []
for name in names:
    upper_names.append(name.upper())

# Same thing with a comprehension (preferred):
upper_names = [name.upper() for name in names]
```

---

#### `while` loops — repeat until a condition is False

```python
count = 0
while count < 5:
    print(count)
    count += 1
# Prints: 0, 1, 2, 3, 4
```

**Common while loop patterns:**

```python
# Pattern 1: Input validation loop
while True:
    age_text = input("Enter your age: ")
    if age_text.isdigit() and int(age_text) > 0:
        age = int(age_text)
        break
    print("Please enter a valid positive number.")

# Pattern 2: Countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# Pattern 3: Processing until empty
tasks = ["task1", "task2", "task3"]
while tasks:
    current = tasks.pop(0)
    print(f"Processing: {current}")
print("All done!")
```

**DANGER — infinite loops:**

```python
# This will run forever! (press Ctrl+C to stop)
while True:
    print("Help, I'm stuck!")

# Common mistake — forgetting to update the condition:
x = 0
while x < 10:
    print(x)
    # OOPS: forgot x += 1, so x is always 0 and the loop never ends
```

---

#### `break`, `continue`, and `for-else`

**`break` — exit the loop immediately:**

```python
# Search for a number:
numbers = [4, 7, 2, 9, 1, 5]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checked {num}...")
```

Output:
```
Checked 4...
Checked 7...
Checked 2...
Found 9!
```

**`continue` — skip to the next iteration:**

```python
# Print only odd numbers:
for n in range(10):
    if n % 2 == 0:
        continue    # skip even numbers
    print(n)
# Prints: 1, 3, 5, 7, 9
```

**`for-else` — runs if loop completed without break:**

```python
search_list = [2, 4, 6, 8]
target = 5

for item in search_list:
    if item == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in list")
# Prints: "5 not found in list"
```

---

#### `match` / `case` — structural pattern matching (Python 3.10+)

Pattern matching is like a powerful `if/elif` chain for matching shapes of data:

```python
command = input("Enter command: ")

match command:
    case "quit" | "exit":
        print("Goodbye!")
    case "help":
        print("Available commands: quit, help, status")
    case "status":
        print("All systems operational")
    case _:
        print(f"Unknown command: {command}")
```

**Matching with values:**

```python
def describe_http_status(code):
    match code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status: {code}"

print(describe_http_status(404))  # "Not Found"
```

**Matching with structure:**

```python
def process_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On x-axis at x={x}")
        case (0, y):
            print(f"On y-axis at y={y}")
        case (x, y):
            print(f"Point at ({x}, {y})")

process_point((0, 0))   # Origin
process_point((5, 0))   # On x-axis at x=5
process_point((3, 4))   # Point at (3, 4)
```

**Matching with guards:**

```python
def classify_age(age):
    match age:
        case n if n < 0:
            return "Invalid"
        case n if n < 13:
            return "Child"
        case n if n < 18:
            return "Teenager"
        case n if n < 65:
            return "Adult"
        case _:
            return "Senior"
```

**Matching dicts/mappings:**

```python
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"Click at ({x}, {y})")
        case {"type": "keypress", "key": key}:
            print(f"Key pressed: {key}")
        case {"type": t}:
            print(f"Unknown event type: {t}")

handle_event({"type": "click", "x": 100, "y": 200})
handle_event({"type": "keypress", "key": "Enter"})
```

---

#### Nested loops

```python
# Multiplication table:
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4d}", end="")
    print()  # new line after each row
```

Output:
```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

**Practical example — finding pairs:**

```python
names = ["Alice", "Bob", "Charlie"]
# Find all unique pairs:
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        print(f"{names[i]} & {names[j]}")
# Alice & Bob
# Alice & Charlie
# Bob & Charlie
```

---

#### The walrus operator `:=` (Python 3.8+)

The walrus operator assigns a value AND returns it in the same expression:

```python
# Without walrus:
line = input("Enter text: ")
while line != "quit":
    print(f"You said: {line}")
    line = input("Enter text: ")

# With walrus (cleaner):
while (line := input("Enter text: ")) != "quit":
    print(f"You said: {line}")
```

Another example — filtering and keeping the result:

```python
data = [1, 5, 12, 3, 18, 7, 25]

# Only keep doubled values greater than 10:
long_results = [y for x in data if (y := x * 2) > 10]
print(long_results)  # [24, 36, 14, 50]
```

---

#### Mini-project: Number guessing game

```python
import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        # Input validation loop:
        while True:
            guess_text = input(f"Attempt {attempts + 1}/{max_attempts}: ")
            if guess_text.isdigit():
                guess = int(guess_text)
                if 1 <= guess <= 100:
                    break
            print("Please enter a number between 1 and 100.")

        attempts += 1

        if guess == secret:
            print(f"\nCorrect! You got it in {attempts} attempt(s)!")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"({remaining} attempts remaining)\n")
    else:
        print(f"\nOut of attempts! The number was {secret}.")

guessing_game()
```

---

#### Mini-project: Simple menu system

```python
def menu_system():
    items = []

    while True:
        print("\n--- Todo Manager ---")
        print("1. Add item")
        print("2. View items")
        print("3. Mark complete")
        print("4. Quit")

        choice = input("Choose (1-4): ").strip()

        match choice:
            case "1":
                item = input("Enter todo: ").strip()
                if item:
                    items.append({"text": item, "done": False})
                    print(f"Added: {item}")
                else:
                    print("Item cannot be empty.")

            case "2":
                if not items:
                    print("No items yet.")
                else:
                    for i, item in enumerate(items, 1):
                        status = "[x]" if item["done"] else "[ ]"
                        print(f"  {i}. {status} {item['text']}")

            case "3":
                if not items:
                    print("No items to mark.")
                else:
                    for i, item in enumerate(items, 1):
                        status = "[x]" if item["done"] else "[ ]"
                        print(f"  {i}. {status} {item['text']}")
                    idx_text = input("Mark which item? (number): ")
                    if idx_text.isdigit():
                        idx = int(idx_text) - 1
                        if 0 <= idx < len(items):
                            items[idx]["done"] = True
                            print(f"Marked '{items[idx]['text']}' as done!")
                        else:
                            print("Invalid number.")

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter 1-4.")

menu_system()
```

---

#### Practice exercises

1. **FizzBuzz**: Print numbers 1-100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both, print "FizzBuzz".
2. **Password validator**: Ask the user for a password. Keep asking until it's at least 8 characters, contains a digit, and contains an uppercase letter.
3. **Triangle printer**: Ask for a number `n` and print a right triangle of `*` characters with `n` rows.
4. **Prime finder**: Write a function that checks if a number is prime using a loop. Find all primes up to 100.
5. **Pattern matching**: Create a simple calculator that takes input like "5 + 3" and uses `match/case` to perform the operation.

---

### Functions: Building Reusable Code

**Goal:** Encapsulate logic into reusable functions. Functions are the most important tool for organising your code — they let you name a piece of logic, test it independently, and reuse it everywhere.

---

#### Why functions matter

Without functions, code becomes repetitive and hard to maintain:

```python
# Without functions — repeating the same logic:
price1 = 100
tax1 = price1 * 0.2
total1 = price1 + tax1
print(f"Item 1: ${total1:.2f}")

price2 = 250
tax2 = price2 * 0.2
total2 = price2 + tax2
print(f"Item 2: ${total2:.2f}")

# With a function — write once, use many times:
def calculate_total(price, tax_rate=0.2):
    tax = price * tax_rate
    return price + tax

print(f"Item 1: ${calculate_total(100):.2f}")
print(f"Item 2: ${calculate_total(250):.2f}")
print(f"Item 3 (reduced): ${calculate_total(50, 0.05):.2f}")
```

---

#### Defining and calling functions

```python
def function_name(parameter1, parameter2):
    """Docstring: explains what the function does."""
    # body — indented code
    result = parameter1 + parameter2
    return result    # send a value back to the caller

# Calling the function:
answer = function_name(3, 5)
print(answer)  # 8
```

**Functions without `return`** implicitly return `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Harry")
print(result)  # None
```

**Returning multiple values** (returns a tuple):

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"17 / 5 = {q} remainder {r}")
```

**Early return** (exit function early based on a condition):

```python
def find_first_negative(numbers):
    """Return the first negative number, or None if none found."""
    for n in numbers:
        if n < 0:
            return n      # exits the function immediately
    return None           # only reached if no negative found

print(find_first_negative([3, 7, -2, 5]))  # -2
print(find_first_negative([3, 7, 5]))      # None
```

---

#### Parameters — every variation explained

**Positional arguments:**

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("Harry", "Gomm")        # positional — order matters
greet("Gomm", "Harry")        # wrong order gives "Hello, Gomm Harry!"
```

**Keyword arguments:**

```python
greet(last_name="Gomm", first_name="Harry")  # order doesn't matter with keywords
```

**Default values:**

```python
def power(base, exponent=2):
    """Raise base to exponent (default: squared)."""
    return base ** exponent

power(5)       # 25 (uses default exponent=2)
power(5, 3)    # 125
power(2, 10)   # 1024
```

**WARNING — mutable default arguments:**

```python
# WRONG — this is a common Python gotcha:
def add_item(item, items=[]):    # default list shared between calls!
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] — SURPRISE! The list persists!

# CORRECT — use None as default:
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b'] — fresh list each time
```

**`*args` — variable positional arguments:**

```python
def total(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)  # numbers is a tuple

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100
```

**`**kwargs` — variable keyword arguments:**

```python
def build_profile(**info):
    """Build a user profile from arbitrary keyword arguments."""
    for key, value in info.items():
        print(f"  {key}: {value}")

build_profile(name="Alice", age=30, city="London")
# name: Alice
# age: 30
# city: London
```

**Combining all parameter types:**

```python
def example(pos1, pos2, /, normal, *args, kw_only, **kwargs):
    """
    pos1, pos2       — positional only (before /)
    normal           — positional or keyword
    *args            — extra positional args
    kw_only          — keyword only (after *)
    **kwargs         — extra keyword args
    """
    pass
```

**Keyword-only arguments (after `*`):**

```python
def connect(host, port, *, timeout=30, retries=3):
    """timeout and retries MUST be passed as keywords."""
    print(f"Connecting to {host}:{port} (timeout={timeout})")

connect("localhost", 8080)                     # OK
connect("localhost", 8080, timeout=10)         # OK
# connect("localhost", 8080, 10)              # TypeError!
```

---

#### Scope — where variables live (LEGB rule)

Python looks up variable names in this order:
1. **L**ocal — inside the current function
2. **E**nclosing — inside enclosing functions (closures)
3. **G**lobal — at the module/file level
4. **B**uilt-in — Python's built-in names (`print`, `len`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)     # "local" — found at Local level

    inner()
    print(x)         # "enclosing" — found at Enclosing level

outer()
print(x)             # "global" — found at Global level
```

**Modifying outer variables** (generally avoid at beginner level):

```python
counter = 0

def increment():
    global counter    # tells Python to use the global variable
    counter += 1

increment()
increment()
print(counter)  # 2
```

**Best practice:** Avoid `global`. Instead, pass values in and return them out:

```python
def increment(counter):
    return counter + 1

count = 0
count = increment(count)  # 1
count = increment(count)  # 2
```

---

#### Docstrings — documenting your functions

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Body weight in kilograms.
        height_m: Height in metres.

    Returns:
        BMI as a float, rounded to 1 decimal place.

    Examples:
        >>> calculate_bmi(75, 1.78)
        23.7
    """
    return round(weight_kg / (height_m ** 2), 1)
```

You can read a function's docstring:

```python
help(calculate_bmi)  # prints the docstring
print(calculate_bmi.__doc__)  # access it as a string
```

---

#### Lambda functions (anonymous functions)

Lambdas are tiny one-expression functions, useful for `sort`, `filter`, `map`:

```python
# Regular function:
def double(x):
    return x * 2

# Same thing as a lambda:
double = lambda x: x * 2

print(double(5))  # 10
```

**Where lambdas shine — as arguments:**

```python
# Sort by last name:
people = ["Harry Gomm", "Alice Smith", "Bob Jones"]
people.sort(key=lambda name: name.split()[-1])
print(people)  # ['Harry Gomm', 'Bob Jones', 'Alice Smith']

# Filter even numbers:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8]

# Transform each element:
doubled = list(map(lambda x: x * 2, [1, 2, 3]))
print(doubled)  # [2, 4, 6]
```

**Note:** Prefer list comprehensions over `map`/`filter` in most cases:

```python
# Comprehension (clearer):
evens = [x for x in nums if x % 2 == 0]
doubled = [x * 2 for x in [1, 2, 3]]
```

---

#### Type hints — communicate intent

Type hints don't enforce types — they're documentation for humans and tools:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def find_user(user_id: int) -> dict | None:
    """Return user dict or None if not found."""
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)
```

**Benefits:**
- Your editor gives better autocomplete and error detection.
- Code is self-documenting.
- Tools like `mypy` can catch type errors before you run your code.

---

#### Recursion — functions that call themselves

A recursive function solves a problem by calling itself with a simpler version:

```python
def factorial(n: int) -> int:
    """Calculate n! (n factorial) recursively."""
    if n <= 1:       # base case — stops the recursion
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120 = 5 * 4 * 3 * 2 * 1
```

**How it works step by step:**
```
factorial(5) -> 5 * factorial(4)
                    -> 4 * factorial(3)
                         -> 3 * factorial(2)
                              -> 2 * factorial(1)
                                   -> 1 (base case!)
                              -> 2 * 1 = 2
                         -> 3 * 2 = 6
                    -> 4 * 6 = 24
               -> 5 * 24 = 120
```

**Practical recursion example — flatten a nested list:**

```python
def flatten(nested_list):
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))  # recursive call
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], [5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

**Practical recursion example — directory tree printer:**

```python
import os

def print_tree(path, prefix=""):
    """Print a directory tree structure."""
    entries = sorted(os.listdir(path))
    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = i == len(entries) - 1
        connector = "+-- " if is_last else "|-- "
        print(f"{prefix}{connector}{entry}")
        if os.path.isdir(full_path):
            extension = "    " if is_last else "|   "
            print_tree(full_path, prefix + extension)

# print_tree(".")  # prints your project structure
```

**Caution:** Python has a recursion limit (default: 1000). For very deep recursion, use iteration instead.

---

#### First-class functions — functions as values

In Python, functions are objects. You can store them in variables, pass them as arguments, and return them from other functions:

```python
# Store a function in a variable:
def shout(text):
    return text.upper() + "!"

yell = shout  # yell is now another name for shout
print(yell("hello"))  # "HELLO!"

# Pass a function as an argument:
def apply(func, value):
    return func(value)

print(apply(shout, "hello"))    # "HELLO!"
print(apply(len, [1, 2, 3]))   # 3

# Return a function from a function:
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15
```

**Use case — strategy pattern:**

```python
def sort_by_name(person):
    return person["name"]

def sort_by_age(person):
    return person["age"]

people = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
]

# Choose sorting strategy:
print(sorted(people, key=sort_by_name))
print(sorted(people, key=sort_by_age))
```

---

#### Mini-project: Unit converter library

```python
# converters.py

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def kg_to_lbs(kg: float) -> float:
    return kg * 2.20462

def lbs_to_kg(lbs: float) -> float:
    return lbs / 2.20462

def km_to_miles(km: float) -> float:
    return km * 0.621371

def miles_to_km(miles: float) -> float:
    return miles / 0.621371

def convert(value: float, from_unit: str, to_unit: str) -> float | None:
    """
    Generic converter supporting multiple unit pairs.
    Returns the converted value, or None if unsupported.
    """
    conversions = {
        ("c", "f"): celsius_to_fahrenheit,
        ("f", "c"): fahrenheit_to_celsius,
        ("kg", "lbs"): kg_to_lbs,
        ("lbs", "kg"): lbs_to_kg,
        ("km", "miles"): km_to_miles,
        ("miles", "km"): miles_to_km,
    }

    key = (from_unit.lower(), to_unit.lower())
    func = conversions.get(key)
    if func:
        return round(func(value), 2)
    return None


# Interactive usage:
if __name__ == "__main__":
    print("=== Unit Converter ===")
    print(f"100 C = {convert(100, 'c', 'f')} F")
    print(f"72 F = {convert(72, 'f', 'c')} C")
    print(f"80kg = {convert(80, 'kg', 'lbs')} lbs")
    print(f"10km = {convert(10, 'km', 'miles')} miles")
```

---

#### Mini-project: Text statistics tool

```python
# text_stats.py — demonstrates functions, dicts, sorting

def count_words(text: str) -> int:
    """Count the number of words in the text."""
    return len(text.split())

def count_sentences(text: str) -> int:
    """Count sentences (ending with . ! or ?)."""
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return max(count, 1)  # at least 1

def word_frequencies(text: str) -> dict[str, int]:
    """Return a dict of word -> frequency."""
    words = text.lower().split()
    # Strip punctuation from each word
    clean_words = []
    for w in words:
        cleaned = ""
        for ch in w:
            if ch.isalnum():
                cleaned += ch
        if cleaned:
            clean_words.append(cleaned)

    freq = {}
    for word in clean_words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the top N most frequent words."""
    freq = word_frequencies(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

def analyse(text: str) -> None:
    """Print a full analysis of the text."""
    print("=== Text Analysis ===")
    print(f"Characters: {len(text)}")
    print(f"Words: {count_words(text)}")
    print(f"Sentences: {count_sentences(text)}")
    print(f"Avg words/sentence: {count_words(text) / count_sentences(text):.1f}")
    print(f"\nTop 5 words:")
    for word, count in top_n_words(text):
        print(f"  '{word}': {count} times")

# Usage:
sample = """
Python is a programming language. Python is used for web development,
data science, automation, and more. Python is known for its simple
syntax and readability. Many developers love Python because it is
easy to learn and powerful to use.
"""
analyse(sample)
```

---

#### Practice exercises

1. **Palindrome checker**: Write `is_palindrome(text)` that returns True if text reads the same forwards and backwards (ignoring spaces and case).
2. **Password generator**: Write a function that generates a random password of a given length with uppercase, lowercase, digits, and symbols.
3. **Statistics functions**: Write `mean()`, `median()`, and `mode()` functions for a list of numbers.
4. **Higher-order functions**: Write a function `apply_to_all(func, items)` that applies a function to every item in a list and returns the results.
5. **Compose functions**: Write `compose(f, g)` that returns a new function `h` where `h(x) = f(g(x))`.

---

### Modules, Packages & Project Structure

**Goal:** Organise code across multiple files, install external packages, and structure real projects.

---

#### What is a module?

A module is simply a `.py` file. When you `import` it, Python runs the file and makes its names available:

```python
# math_utils.py
PI = 3.14159

def area_circle(radius: float) -> float:
    return PI * radius ** 2

def area_rectangle(width: float, height: float) -> float:
    return width * height
```

```python
# main.py
import math_utils

print(math_utils.PI)                    # 3.14159
print(math_utils.area_circle(5))        # 78.53975

# Or import specific names:
from math_utils import area_circle, PI
print(area_circle(5))

# Or import with an alias:
import math_utils as mu
print(mu.area_circle(5))
```

**Import styles and when to use them:**

```python
import math               # use as math.sqrt() — clear origin
from math import sqrt     # use as sqrt() — convenient but less clear
from math import *        # imports everything — AVOID (pollutes namespace)
import numpy as np        # alias — standard convention for known libraries
```

---

#### `__name__` and `__main__` — the script guard

When Python runs a file directly, it sets `__name__` to `"__main__"`. When a file is imported, `__name__` is set to the module name:

```python
# greetings.py
def hello(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# This block only runs if this file is executed directly (not imported):
if __name__ == "__main__":
    hello("World")
    farewell("World")
```

```bash
python greetings.py    # Runs the if block
```

```python
# other_file.py
import greetings        # Does NOT run the if block
greetings.hello("Harry")  # Just uses the functions
```

**Why this matters:** Without the guard, importing the module would trigger test code.

---

#### Python's built-in modules (the standard library)

Python comes with a massive standard library. Here are modules you'll use often:

```python
import os               # file paths, environment variables
import sys              # system parameters, argv, exit
import math             # sqrt, sin, cos, pi,  ceil, floor
import random           # random numbers, choices, shuffle
import datetime         # dates and times
import json             # JSON encoding/decoding
import pathlib          # modern file path handling
import collections      # Counter, defaultdict, namedtuple
import re               # regular expressions
import string           # string constants (ascii_letters, digits)
import csv              # CSV file reading/writing
import itertools        # efficient looping tools
import functools        # higher-order function tools
```

**Examples:**

```python
import math
print(math.sqrt(16))       # 4.0
print(math.pi)             # 3.141592653589793
print(math.ceil(3.2))      # 4
print(math.floor(3.9))     # 3

import random
print(random.randint(1, 10))           # random int between 1 and 10
print(random.choice(["a", "b", "c"]))  # random element from list
items = [1, 2, 3, 4, 5]
random.shuffle(items)                   # shuffles in place
print(random.sample(range(100), 5))    # 5 unique random numbers

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))  # "2026-02-16 14:30"
birthday = datetime.date(2000, 6, 15)
age_days = (datetime.date.today() - birthday).days
print(f"Days alive: {age_days}")

import json
data = {"name": "Alice", "scores": [85, 92, 78]}
json_string = json.dumps(data, indent=2)  # dict to JSON string
print(json_string)
parsed = json.loads(json_string)           # JSON string to dict
print(parsed["name"])                      # "Alice"

from collections import Counter
words = "the cat sat on the mat the cat".split()
freq = Counter(words)
print(freq.most_common(3))  # [('the', 3), ('cat', 2), ('sat', 1)]

from collections import defaultdict
groups = defaultdict(list)
for name, dept in [("Alice", "Engineering"), ("Bob", "Sales"), ("Charlie", "Engineering")]:
    groups[dept].append(name)
print(dict(groups))  # {'Engineering': ['Alice', 'Charlie'], 'Sales': ['Bob']}
```

---

#### Installing external packages with pip

**pip** is Python's package installer. It downloads packages from PyPI (Python Package Index):

```bash
# Install a package:
pip install requests

# Install a specific version:
pip install requests==2.31.0

# Install from a requirements file:
pip install -r requirements.txt

# Show installed packages:
pip list

# Show info about a package:
pip show requests

# Uninstall:
pip uninstall requests
```

**Using installed packages:**

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())       # parsed JSON data
```

**Popular packages to know about:**

| Package | Purpose |
|---------|---------|
| `requests` | HTTP requests (APIs) |
| `flask` / `fastapi` | Web frameworks |
| `pandas` | Data analysis |
| `numpy` | Numerical computing |
| `pytest` | Testing |
| `black` | Code formatter |
| `python-dotenv` | Environment variables |

---

#### Virtual environments — isolate your projects

Virtual environments give each project its own set of packages:

```bash
# Create a virtual environment:
python -m venv .venv

# Activate it:
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Your prompt changes:
# (.venv) C:\my_project>

# Install packages (go into .venv, not system-wide):
pip install requests flask

# Save your dependencies:
pip freeze > requirements.txt

# Deactivate when done:
deactivate
```

**Your `requirements.txt` might look like:**

```text
requests==2.31.0
flask==3.0.0
python-dotenv==1.0.0
```

**Workflow for a new project:**

```bash
mkdir my_project
cd my_project
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install requests         # install what you need
pip freeze > requirements.txt
```

**Workflow for cloning someone else's project:**

```bash
git clone https://github.com/user/project.git
cd project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Always add `.venv/` to your `.gitignore`.**

---

#### Project structure — how to organise real projects

**Small script (1-2 files):**

```
my_script/
  main.py
  helpers.py
```

**Small-to-medium project:**

```
my_project/
  .venv/                  # virtual environment (git-ignored)
  .gitignore
  README.md
  requirements.txt
  main.py                 # entry point
  config.py               # settings/constants
  utils/
    __init__.py
    file_utils.py
    string_utils.py
  data/
    input.csv
  tests/
    test_utils.py
```

**What is `__init__.py`?**

It marks a folder as a Python **package** (a collection of modules):

```python
# utils/__init__.py — can be empty, or can export key names:
from .file_utils import read_csv
from .string_utils import clean_text
```

```python
# main.py
from utils import read_csv, clean_text
```

**Relative imports within a package:**

```python
# Inside utils/string_utils.py:
from .file_utils import read_csv   # . means "this package"
from ..config import SETTINGS      # .. means "parent package"
```

---

#### The `.gitignore` file for Python projects

```text
# .gitignore

# Virtual environment
.venv/
venv/
env/

# Bytecode cache
__pycache__/
*.pyc

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env

# Distribution
dist/
build/
*.egg-info/
```

---

#### Mini-project: Multi-file calculator

```
calculator/
  main.py
  operations.py
  history.py
```

```python
# operations.py
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b
```

```python
# history.py
_history: list[str] = []

def add_entry(entry: str) -> None:
    _history.append(entry)

def show_history() -> None:
    if not _history:
        print("No history yet.")
    else:
        for i, entry in enumerate(_history, 1):
            print(f"  {i}. {entry}")

def clear_history() -> None:
    _history.clear()
    print("History cleared.")
```

```python
# main.py
from operations import add, subtract, multiply, divide
import history

def main():
    print("=== Calculator ===")
    print("Operations: +, -, *, /")
    print("Commands: history, clear, quit\n")

    while True:
        user_input = input("> ").strip()

        if user_input == "quit":
            print("Goodbye!")
            break
        elif user_input == "history":
            history.show_history()
            continue
        elif user_input == "clear":
            history.clear_history()
            continue

        # Parse: "5 + 3"
        parts = user_input.split()
        if len(parts) != 3:
            print("Format: <number> <operator> <number>")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Invalid numbers.")
            continue

        ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
        if op not in ops:
            print(f"Unknown operator: {op}")
            continue

        result = ops[op](a, b)
        if result is None:
            print("Error: division by zero")
        else:
            line = f"{a} {op} {b} = {result}"
            print(line)
            history.add_entry(line)

if __name__ == "__main__":
    main()
```

---

#### Mini-project: Package explorer

```python
# package_explorer.py — explore Python's standard library

import importlib
import pkgutil

def explore_module(module_name: str) -> None:
    """Show all public functions/classes in a module."""
    try:
        mod = importlib.import_module(module_name)
    except ImportError:
        print(f"Module '{module_name}' not found")
        return

    print(f"\n=== {module_name} ===")

    # Get all public names
    names = [n for n in dir(mod) if not n.startswith("_")]

    # Categorise
    functions = []
    classes = []
    others = []

    for name in names:
        obj = getattr(mod, name)
        if callable(obj):
            if isinstance(obj, type):
                classes.append(name)
            else:
                functions.append(name)
        else:
            others.append(name)

    if classes:
        print(f"\nClasses ({len(classes)}):")
        for name in classes:
            print(f"  {name}")

    if functions:
        print(f"\nFunctions ({len(functions)}):")
        for name in functions:
            print(f"  {name}")

    if others:
        print(f"\nConstants/Other ({len(others)}):")
        for name in others[:10]:  # limit to 10
            print(f"  {name}")

if __name__ == "__main__":
    for mod_name in ["math", "random", "string", "os.path"]:
        explore_module(mod_name)
```

---

#### Practice exercises

1. **Module creation**: Create a `string_tools.py` module with functions: `reverse(s)`, `count_vowels(s)`, `is_palindrome(s)`. Import and use them from `main.py`.
2. **Virtual env practice**: Create a new project with a virtual environment, install `requests`, and write a script that fetches a random joke from an API.
3. **Project scaffold**: Create a project with the medium structure above. Write a `config.py` with constants and a `utils/` package with at least two modules.
4. **Standard library explorer**: Write a script that imports 5 different standard library modules and demonstrates one useful function from each.

---

### File I/O, Error Handling & Practice Projects

**Goal:** Handle user interaction, file operations, and errors gracefully. These are essential skills for writing real programs.

---

#### Console input and output

**`input()` always returns a string:**

```python
name = input("What is your name? ")
print(f"Hello, {name}!")

# IMPORTANT: input returns a string, so convert for numbers:
age_text = input("How old are you? ")
age = int(age_text)           # convert to int (may raise ValueError)
print(f"Next year you'll be {age + 1}")
```

**`print()` — more than you think:**

```python
# Basic:
print("Hello")

# Multiple arguments (separated by spaces by default):
print("Name:", name, "Age:", age)

# Custom separator:
print("2026", "02", "16", sep="-")  # 2026-02-16

# Custom end (default is newline):
print("Loading", end="")
print("...", end="")
print(" Done!")
# Output: Loading... Done!

# Print to a file:
with open("log.txt", "w") as f:
    print("Log entry 1", file=f)
    print("Log entry 2", file=f)
```

**Input validation pattern:**

```python
def get_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Keep asking until the user enters a valid integer in range."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print(f"'{text}' is not a valid integer. Try again.")
            continue

        if min_val is not None and value < min_val:
            print(f"Must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"Must be at most {max_val}.")
            continue

        return value

age = get_int("Enter your age (1-150): ", 1, 150)
```

---

#### Reading and writing files

**Writing a file:**

```python
# Write mode ("w") — creates file or overwrites existing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Append mode ("a") — adds to end of existing file
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Line 3\n")
```

**Reading a file:**

```python
# Read entire file as one string:
with open("output.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Read line by line (memory efficient for large files):
with open("output.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip removes the trailing newline

# Read all lines into a list:
with open("output.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

**File modes explained:**

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or **overwrites** existing. |
| `"a"` | Append. Creates file or adds to end. |
| `"x"` | Exclusive create. Fails if file already exists. |
| `"rb"` / `"wb"` | Read/write in binary mode (for images, PDFs). |
| `"r+"` | Read and write. File must exist. |

**Always use `encoding="utf-8"`** unless you have a specific reason not to.

**The `with` statement (context manager):**

The `with` statement ensures the file is properly closed even if an error occurs:

```python
# WITH 'with' (correct):
with open("file.txt") as f:
    data = f.read()
# File is automatically closed here

# WITHOUT 'with' (error-prone):
f = open("file.txt")
data = f.read()
f.close()    # If an error occurs before this, the file stays open!
```

**Working with paths using pathlib (modern approach):**

```python
from pathlib import Path

# Create a path object:
data_dir = Path("data")
file_path = data_dir / "input.txt"    # Path("data/input.txt")

# Check if file exists:
if file_path.exists():
    content = file_path.read_text(encoding="utf-8")
    print(content)

# Write to file:
output = Path("output") / "result.txt"
output.parent.mkdir(parents=True, exist_ok=True)  # create dirs if needed
output.write_text("Hello from pathlib!", encoding="utf-8")

# List all .py files in current directory:
for py_file in Path(".").glob("**/*.py"):
    print(py_file)
```

---

#### Working with CSV files

```python
import csv

# Writing CSV:
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "London"],
    ["Bob", 25, "Cardiff"],
    ["Charlie", 35, "Edinburgh"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV:
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header row
    for row in reader:
        name, age, city = row
        print(f"{name} is {age} and lives in {city}")

# Reading as dicts (using header as keys):
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']}: {row['City']}")
```

---

#### Working with JSON files

```python
import json

# Writing JSON:
data = {
    "users": [
        {"name": "Alice", "age": 30, "active": True},
        {"name": "Bob", "age": 25, "active": False},
    ],
    "total": 2,
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Reading JSON:
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

for user in loaded["users"]:
    status = "active" if user["active"] else "inactive"
    print(f"{user['name']} ({status})")
```

---

#### Exceptions — handling errors gracefully

When something goes wrong, Python raises an **exception**:

```python
# Common exceptions:
int("abc")              # ValueError: invalid literal
x = 1 / 0              # ZeroDivisionError
my_list = [1, 2, 3]
my_list[10]             # IndexError: list index out of range
my_dict = {}
my_dict["key"]          # KeyError: 'key'
print(undefined_var)    # NameError
open("nonexistent.txt") # FileNotFoundError
"hello" + 5             # TypeError
```

**`try` / `except` — catch and handle errors:**

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

**`try` / `except` / `else` / `finally`:**

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
    content = None
else:
    # Runs ONLY if no exception occurred
    print(f"Read {len(content)} characters")
finally:
    # ALWAYS runs, whether or not an exception occurred
    print("Cleanup done")
```

| Block | When it runs |
|-------|-------------|
| `try` | Always attempted |
| `except` | Only if an exception matches |
| `else` | Only if NO exception occurred |
| `finally` | ALWAYS (cleanup code) |

**Catching the exception object:**

```python
try:
    value = int("abc")
except ValueError as e:
    print(f"Error occurred: {e}")
    # "Error occurred: invalid literal for int() with base 10: 'abc'"
```

**Catching multiple exception types:**

```python
try:
    risky_operation()
except (ValueError, TypeError, KeyError) as e:
    print(f"Caught error: {type(e).__name__}: {e}")
```

**Common exception hierarchy (the ones you'll see most):**

```
BaseException
  +-- Exception
        +-- ValueError     -- wrong value type/format
        +-- TypeError      -- wrong type for operation
        +-- KeyError       -- dict key not found
        +-- IndexError     -- list index out of range
        +-- NameError      -- variable not defined
        +-- AttributeError -- object missing attribute/method
        +-- FileNotFoundError -- file doesn't exist
        +-- IOError        -- input/output problem
        +-- ZeroDivisionError
        +-- ImportError    -- module not found
        +-- RuntimeError   -- generic runtime error
        +-- StopIteration  -- iterator exhausted
```

**Raising exceptions:**

```python
def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0-150, got {age}")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(e)  # "age must be 0-150, got -5"
```

**Custom exceptions:**

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount:.2f} -- balance is ${balance:.2f}"
        )

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100.00, 150.00)
except InsufficientFundsError as e:
    print(e)  # "Cannot withdraw $150.00 -- balance is $100.00"
    print(f"Balance: {e.balance}, Attempted: {e.amount}")
```

---

#### Reading tracebacks — don't fear the error!

When Python crashes, it prints a **traceback**. Read it from **bottom to top**:

```python
# example.py
def process(data):
    return data["name"].upper()

def load_and_process():
    user = {"age": 30}   # oops, no "name" key
    return process(user)

load_and_process()
```

```
Traceback (most recent call last):
  File "example.py", line 8, in <module>     <-- 3. Program started here
    load_and_process()
  File "example.py", line 6, in load_and_process  <-- 2. Called this
    return process(user)
  File "example.py", line 2, in process       <-- 1. Error happened HERE
    return data["name"].upper()
KeyError: 'name'                               <-- THE ACTUAL ERROR
```

**Reading order:** Start at the last line (the error), then look at the line just above it (where it happened).

---

#### Logging — better than print for real apps

```python
import logging

# Configure logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),  # also print to console
    ],
)

logger = logging.getLogger(__name__)

# Use different log levels:
logger.debug("Detailed diagnostic info")
logger.info("General information")
logger.warning("Something might be wrong")
logger.error("Something went wrong")
logger.critical("Something went very wrong")

# In practice:
def divide(a, b):
    logger.debug(f"divide({a}, {b}) called")
    if b == 0:
        logger.error(f"Division by zero: {a}/{b}")
        return None
    result = a / b
    logger.info(f"{a}/{b} = {result}")
    return result
```

---

#### Mini-project: Simple journal app

```python
# journal.py — files, exceptions, input, control flow, JSON

import json
import datetime
import os

JOURNAL_FILE = "journal.json"

def load_entries() -> list:
    """Load journal entries from file."""
    if not os.path.exists(JOURNAL_FILE):
        return []
    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read journal file. Starting fresh.")
        return []

def save_entries(entries: list) -> None:
    """Save journal entries to file."""
    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)

def add_entry(entries: list) -> None:
    """Add a new journal entry."""
    entry_text = input("Write your entry:\n> ").strip()
    if not entry_text:
        print("Empty entry -- not saved.")
        return

    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "text": entry_text,
    }
    entries.append(entry)
    save_entries(entries)
    print("Entry saved!")

def view_entries(entries: list) -> None:
    """View all journal entries."""
    if not entries:
        print("No journal entries yet.")
        return

    for i, entry in enumerate(entries, 1):
        dt = datetime.datetime.fromisoformat(entry["timestamp"])
        formatted = dt.strftime("%Y-%m-%d %H:%M")
        print(f"\n[{i}] {formatted}")
        print(f"    {entry['text']}")

def search_entries(entries: list) -> None:
    """Search journal entries by keyword."""
    keyword = input("Search for: ").strip().lower()
    if not keyword:
        return

    matches = [e for e in entries if keyword in e["text"].lower()]
    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for entry in matches:
            dt = datetime.datetime.fromisoformat(entry["timestamp"])
            print(f"  [{dt.strftime('%Y-%m-%d')}] {entry['text'][:60]}...")
    else:
        print("No matches found.")

def delete_entry(entries: list) -> None:
    """Delete a journal entry by number."""
    view_entries(entries)
    if not entries:
        return

    try:
        idx = int(input("\nDelete entry number: ")) - 1
        if 0 <= idx < len(entries):
            removed = entries.pop(idx)
            save_entries(entries)
            print(f"Deleted entry from {removed['timestamp'][:10]}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    entries = load_entries()
    print(f"=== Simple Journal ({len(entries)} entries) ===")

    while True:
        print("\n1. New entry  2. View all  3. Search  4. Delete  5. Quit")
        choice = input("Choose: ").strip()

        match choice:
            case "1": add_entry(entries)
            case "2": view_entries(entries)
            case "3": search_entries(entries)
            case "4": delete_entry(entries)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

---

#### Mini-project: File organiser

```python
# file_organiser.py — organise files in a directory by extension

from pathlib import Path
import shutil

EXTENSION_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".csv", ".xlsx"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".xml", ".yaml"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Video": {".mp4", ".avi", ".mkv", ".mov", ".wmv"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
}

def get_category(extension: str) -> str:
    """Determine the category for a file extension."""
    ext = extension.lower()
    for category, extensions in EXTENSION_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"

def organise(directory: str, dry_run: bool = True) -> None:
    """Organise files in a directory into category folders."""
    source = Path(directory)
    if not source.is_dir():
        print(f"Error: '{directory}' is not a valid directory")
        return

    files = [f for f in source.iterdir() if f.is_file()]
    if not files:
        print("No files to organise.")
        return

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Organising {len(files)} files:\n")

    moved = 0
    for file_path in files:
        category = get_category(file_path.suffix)
        dest_dir = source / category
        dest_file = dest_dir / file_path.name

        action = "Would move" if dry_run else "Moving"
        print(f"  {action}: {file_path.name} -> {category}/")

        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(dest_file))
            moved += 1

    if dry_run:
        print(f"\n[DRY RUN] Would move {len(files)} files.")
        print("Run with dry_run=False to actually move files.")
    else:
        print(f"\nMoved {moved} files.")

if __name__ == "__main__":
    target = input("Directory to organise: ").strip()
    organise(target, dry_run=True)  # preview first

    confirm = input("\nProceed? (yes/no): ").strip().lower()
    if confirm == "yes":
        organise(target, dry_run=False)
```

---

#### Practice exercises

1. **Safe calculator**: Build a calculator that handles all possible errors (invalid input, division by zero) with clear error messages.
2. **File word counter**: Write a program that reads a text file and prints: total words, total lines, unique words, and the 5 most common words.
3. **CSV to JSON converter**: Read a CSV file and write its contents as a JSON file. Handle missing files and malformed data.
4. **Config file parser**: Write a function that reads `key=value` format, returns a dict. Handle missing files and malformed lines.
5. **Multi-file logger**: Write a logging module that appends timestamped messages to a log file. Use it from another script.

---

### Essential Fundamentals: Must-Know Python Basics

**Goal:** Cover a few core ideas that beginners often miss but use constantly: truthiness, membership, built‑ins, mutability, reading errors, and basic style.

#### Truthiness (what counts as True/False)

In `if` and `while` conditions, Python treats many values as **False** even if they are not literally `False`:

These are considered **False**:
- `False`
- `None`
- `0`, `0.0`, `0j`
- Empty containers: `""`, `[]`, `()`, `{}`, `set()`, `range(0)`

Everything else is considered **True**.

```python
items = []

if items:
    print("we have items")
else:
    print("empty")   # this runs because [] is falsy
```

This is why you often see patterns like:

```python
if name:       # checks for non-empty string
    print("Hello", name)
```

#### Membership with `in`

`in` checks if an element is contained in a container:

```python
nums = [1, 2, 3]
print(2 in nums)       # True
print(5 in nums)       # False

text = "python"
print("py" in text)   # True
```

With dicts, `in` checks **keys** by default:

```python
user = {"name": "Alice", "age": 30}

print("name" in user)   # True
print("Alice" in user)  # False (value, not key)
```

#### Core built‑ins you will use everywhere

Some built‑in functions are so common that you should recognise them early:

```python
nums = [3, 1, 4]

print(len(nums))        # length -> 3
print(min(nums))        # minimum -> 1
print(max(nums))        # maximum -> 4
print(sum(nums))        # sum -> 8

print(sorted(nums))     # [1, 3, 4]
print(sorted(nums, reverse=True))  # [4, 3, 1]
```

Type inspection:

```python
value = 3.14
print(type(value))                # <class 'float'>
print(isinstance(value, float))   # True
```

`range` creates a sequence of numbers (often used in loops):

```python
for i in range(3):   # 0, 1, 2
    print(i)
```

#### Mutability basics

Some types are **mutable** (can be changed in place), others are **immutable** (any change creates a new object):

- Mutable: `list`, `dict`, `set`, `bytearray`.
- Immutable: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`.

Example — lists are mutable:

```python
nums = [1, 2, 3]
nums.append(4)   # modifies the same list
```

Example — strings are immutable:

```python
name = "harry"
upper = name.upper()

print(name)   # 'harry'  (unchanged)
print(upper)  # 'HARRY'  (new string)
```

This is why methods on strings usually **return a new value** instead of changing the original.

#### Reading tracebacks (error messages)

When Python crashes, it shows a **traceback**. Learning to read it is critical.

Example error:

```text
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

How to read this:
- Last line shows the **exception type** and message.
- The line above (with file name and line number) tells you **where** in your code it happened.

Habit: when you see a traceback, read **bottom‑up** and go to that file and line.

#### Very light style guide (PEP 8 basics)

At beginner level, just remember a few habits:

- Use 4 spaces for indentation (never tabs).
- Keep lines roughly under 79–100 characters.
- `snake_case` for functions/variables, `CapWords` for classes.
- Put imports at the top of the file.

Example:

```python
import math


def area_circle(radius: float) -> float:
    return math.pi * radius * radius
```

These habits make your code look like "normal" Python and make it easier to read tutorials and other people's code.

---

## Intermediate Track — Levelling Up

Now that you've mastered the basics, the intermediate track focuses on writing production‑quality code: better organization, testing, working with data, and using Python's vast standard library.


### Advanced Function Techniques

**Goal:** Master function signatures, closures, decorators, generators, and functional programming patterns so you can write clean, composable, reusable code.

---

#### Positional-only and keyword-only parameters

Python 3.8+ introduced two markers in function signatures: `/` and `*`. Everything **before** `/` is positional-only, and everything **after** `*` is keyword-only.

```python
def greet(name, /, greeting="Hello", *, loud=False):
    """
    name      : positional-only  (caller MUST NOT write name=...)
    greeting  : normal           (positional or keyword)
    loud      : keyword-only     (caller MUST write loud=...)
    """
    msg = f"{greeting}, {name}!"
    return msg.upper() if loud else msg

# Valid calls
greet("Alice")                          # Hello, Alice!
greet("Alice", "Hi")                    # Hi, Alice!
greet("Alice", greeting="Hi")           # Hi, Alice!
greet("Alice", loud=True)               # HELLO, ALICE!

# Invalid calls
# greet(name="Alice")     # TypeError: positional-only
# greet("Alice", True)    # TypeError: loud is keyword-only
```

**Why does this matter?** API designers use positional-only to keep parameter names as internal implementation details, so renaming them later won't break callers. Keyword-only parameters prevent accidental positional mistakes for boolean flags.

**Real-world example — database query function:**

```python
def query(sql, /, *, params=None, timeout=30, fetch_all=True):
    """
    sql is positional-only so we can rename internal variable freely.
    All options are keyword-only for clarity at the call site.
    """
    print(f"Running: {sql} | params={params} | timeout={timeout}")

query("SELECT * FROM users", params={"active": True}, timeout=10)
```

---

#### `*args` and `**kwargs` in depth

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dict. Together, they let you write functions that accept any combination of arguments.

```python
def debug_call(*args, **kwargs):
    """Print everything that was passed in."""
    print(f"Positional: {args}")
    print(f"Keyword:    {kwargs}")

debug_call(1, 2, 3, x=10, y=20)
# Positional: (1, 2, 3)
# Keyword:    {'x': 10, 'y': 20}
```

**Forwarding arguments** — this pattern is essential for decorators and wrapper functions:

```python
def log_and_call(func, *args, **kwargs):
    """Call func with whatever arguments were given, logging first."""
    print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
    return func(*args, **kwargs)

def add(a, b):
    return a + b

result = log_and_call(add, 3, 5)  # Calling add with args=(3, 5), kwargs={}
print(result)                      # 8
```

**Combining with positional-only and keyword-only:**

```python
def flexible(required, /, *args, option=False, **kwargs):
    """Demonstrates all parameter kinds together."""
    print(f"required={required}, args={args}, option={option}, kwargs={kwargs}")

flexible("hello", 1, 2, 3, option=True, extra="data")
# required=hello, args=(1, 2, 3), option=True, kwargs={'extra': 'data'}
```

**Unpacking into function calls:**

```python
def create_user(name, age, email):
    return {"name": name, "age": age, "email": email}

# Unpack a list as positional args
data = ["Alice", 30, "alice@example.com"]
user = create_user(*data)

# Unpack a dict as keyword args
data_dict = {"name": "Bob", "age": 25, "email": "bob@example.com"}
user2 = create_user(**data_dict)
```

---

#### Closures and nested functions

A **closure** is an inner function that captures and remembers variables from its enclosing scope, even after the outer function has finished executing.

```python
def make_multiplier(factor):
    """Return a function that multiplies its argument by factor."""
    def multiply(x):
        return x * factor   # 'factor' is captured from the enclosing scope
    return multiply

times3 = make_multiplier(3)
times7 = make_multiplier(7)
print(times3(10))   # 30
print(times7(10))   # 70
```

**How it works internally:** Python stores captured variables in `__closure__`:

```python
print(times3.__closure__[0].cell_contents)  # 3
```

**The `nonlocal` keyword** — lets inner functions modify captured variables (not just read them):

```python
def make_counter(start=0):
    count = start
    def increment(step=1):
        nonlocal count      # without this, assignment would create a LOCAL count
        count += step
        return count
    return increment

counter = make_counter(10)
print(counter())     # 11
print(counter())     # 12
print(counter(5))    # 17
```

**Practical use — configuration factory:**

```python
def make_formatter(prefix, suffix=""):
    """Create a string formatter with fixed prefix and suffix."""
    def format_value(value):
        return f"{prefix}{value}{suffix}"
    return format_value

dollar = make_formatter("$", " USD")
euro   = make_formatter("EUR ", "")

print(dollar(42.50))    # $42.5 USD
print(euro(42.50))      # EUR 42.5
```

**Common pitfall — closures over loop variables:**

```python
# BUG: all functions share the same 'i' variable
funcs = []
for i in range(5):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [4, 4, 4, 4, 4] — NOT [0, 1, 2, 3, 4]

# FIX: use a default argument to capture the current value
funcs = []
for i in range(5):
    funcs.append(lambda i=i: i)    # default arg captures current i

print([f() for f in funcs])  # [0, 1, 2, 3, 4]
```

---

#### Decorators — from basics to advanced

A **decorator** is a function that takes a function and returns a modified version of it. The `@decorator` syntax is just syntactic sugar.

**Basic decorator pattern:**

```python
import functools

def log_calls(func):
    """Log every call to the decorated function."""
    @functools.wraps(func)   # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"-> {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b

print(add(2, 3))
# -> add((2, 3), {})
# <- add returned 5
# 5

# Without @functools.wraps, add.__name__ would be "wrapper"
print(add.__name__)   # add
print(add.__doc__)    # Add two numbers.
```

> **Always use `@functools.wraps`** in your decorators. Without it, the wrapped function loses its identity (name, docstring, type hints), which breaks help(), documentation tools, and debugging.

**Decorator with parameters** — you need an extra layer of nesting:

```python
import functools
import time

def retry(max_attempts=3, delay=1.0):
    """Retry the decorated function up to max_attempts times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url):
    """Simulate a flaky network call."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return {"status": "ok"}

# Usage
try:
    result = fetch_data("https://api.example.com/data")
    print(result)
except ConnectionError as e:
    print(f"All retries failed: {e}")
```

**Stacking decorators** — decorators can be layered; they apply bottom-to-top:

```python
import functools
import time

def timer(func):
    """Measure execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

def validate_positive(func):
    """Ensure all positional args are positive numbers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper

@timer                # applied second (outermost)
@validate_positive    # applied first (innermost)
def compute(x, y):
    time.sleep(0.1)
    return x ** y

print(compute(2, 10))     # compute took 0.10xxs  -> 1024
# compute(-1, 2)          # ValueError: Negative value not allowed: -1
```

**Class-based decorators** — use `__call__` for stateful decorators:

```python
import functools

class CountCalls:
    """Decorator that counts how many times a function is called."""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")   # say_hello has been called 1 times \n Hello, Alice!
say_hello("Bob")     # say_hello has been called 2 times \n Hello, Bob!
print(say_hello.count)  # 2
```

---

#### Generator functions and `yield`

A **generator function** uses `yield` instead of `return`. Each call to `next()` resumes execution right after the last `yield`. Generators are **lazy** — they produce values on demand without storing the entire sequence in memory.

```python
def count_up(start, end):
    """Yield integers from start to end (inclusive)."""
    current = start
    while current <= end:
        yield current
        current += 1

# Using the generator
for num in count_up(1, 5):
    print(num, end=" ")     # 1 2 3 4 5
```

**Why generators matter — memory efficiency:**

```python
import sys

# List: stores ALL values in memory
big_list = [x * x for x in range(1_000_000)]
print(sys.getsizeof(big_list))     # ~8 MB

# Generator: stores only the formula, produces values on demand
big_gen = (x * x for x in range(1_000_000))
print(sys.getsizeof(big_gen))      # ~200 bytes (!)
```

**`yield from` — delegating to sub-generators:**

```python
def flatten(nested_list):
    """Recursively flatten a nested list."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)   # delegate to recursive call
        else:
            yield item

data = [1, [2, 3, [4, 5]], [6], 7]
print(list(flatten(data)))   # [1, 2, 3, 4, 5, 6, 7]
```

**Generator as a pipeline:**

```python
def read_lines(filename):
    """Yield lines from a file, stripping whitespace."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    """Skip lines starting with #."""
    for line in lines:
        if not line.startswith("#"):
            yield line

def parse_csv_line(lines):
    """Split each line by comma."""
    for line in lines:
        yield line.split(",")

# Chain generators into a pipeline — no intermediate lists!
# pipeline = parse_csv_line(filter_comments(read_lines("data.csv")))
# for row in pipeline:
#     print(row)
```

**Sending values into generators with `.send()`:**

```python
def running_average():
    """Generator that computes running average of sent values."""
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        if value is not None:
            total += value
            count += 1
            average = total / count

avg = running_average()
next(avg)            # prime the generator (advances to first yield)
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
```

---

#### Recursion

A **recursive function** calls itself. Every recursive function needs a **base case** (when to stop) and a **recursive case** (how to break the problem down).

```python
def factorial(n):
    """Calculate n! recursively."""
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))    # 120  (5 * 4 * 3 * 2 * 1)
```

**Recursion limit:** Python has a default recursion limit of 1000. You can check and change it:

```python
import sys
print(sys.getrecursionlimit())    # 1000
# sys.setrecursionlimit(5000)     # increase if needed (be careful!)
```

**Tail recursion workaround — use iteration when possible:**

```python
def factorial_iterative(n):
    """Iterative factorial (no recursion limit issues)."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Binary search — classic recursive algorithm:**

```python
def binary_search(arr, target, low=0, high=None):
    """Find target in sorted array using binary search."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1   # not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 7))    # 3 (index)
print(binary_search(nums, 8))    # -1 (not found)
```

---

#### First-class functions and higher-order patterns

Functions are objects in Python — you can assign them to variables, store them in data structures, and pass them as arguments.

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Store functions in a dictionary
styles = {"shout": shout, "whisper": whisper}

# Call dynamically
user_choice = "shout"
print(styles[user_choice]("hello"))   # HELLO
```

**`map()`, `filter()`, `reduce()` — functional programming basics:**

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: apply a function to every element
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter: keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# reduce: accumulate values left-to-right
total = reduce(lambda acc, x: acc + x, numbers, 0)
# 55

# Equivalent comprehensions (often more Pythonic):
doubled_comp = [x * 2 for x in numbers]
evens_comp   = [x for x in numbers if x % 2 == 0]
total_builtin = sum(numbers)
```

**`sorted()` with key functions:**

```python
students = [
    {"name": "Alice", "grade": 88, "age": 22},
    {"name": "Bob", "grade": 95, "age": 20},
    {"name": "Charlie", "grade": 88, "age": 21},
]

# Sort by grade (descending), then by name (ascending) for ties
from operator import itemgetter
sorted_students = sorted(students, key=lambda s: (-s["grade"], s["name"]))
for s in sorted_students:
    print(f"{s['name']}: {s['grade']}")
# Bob: 95
# Alice: 88
# Charlie: 88
```

---

#### `functools` essentials

```python
import functools

# --- partial: freeze some arguments ---
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube   = functools.partial(power, exponent=3)
print(square(5))   # 25
print(cube(3))     # 27

# --- lru_cache: automatic memoization ---
@functools.lru_cache(maxsize=256)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))                   # 12586269025 (instant!)
print(fibonacci.cache_info())          # CacheInfo(hits=48, misses=51, ...)

# --- reduce: left fold ---
from functools import reduce
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)   # 120

# --- total_ordering: fill in comparison methods ---
@functools.total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    # total_ordering auto-generates __le__, __gt__, __ge__!

s1 = Student("Alice", 88)
s2 = Student("Bob", 95)
print(s1 < s2)    # True
print(s1 >= s2)   # False
```

---

#### Mini-project 1: Plugin system using decorators

Build a registry of plugins that can be loaded and executed dynamically.

```python
"""
plugin_system.py — A simple plugin architecture using decorators.

This pattern is used in real frameworks like Flask (@app.route),
pytest (@pytest.fixture), and Click (@click.command).
"""
import functools

# Global registry: maps plugin name -> function
_plugins = {}

def plugin(name=None):
    """Register a function as a named plugin."""
    def decorator(func):
        plugin_name = name or func.__name__
        _plugins[plugin_name] = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

def list_plugins():
    """Return list of registered plugin names."""
    return list(_plugins.keys())

def run_plugin(name, *args, **kwargs):
    """Execute a plugin by name."""
    if name not in _plugins:
        raise KeyError(f"Unknown plugin: {name}. Available: {list_plugins()}")
    return _plugins[name](*args, **kwargs)

# --- Register some plugins ---

@plugin(name="uppercase")
def make_upper(text):
    """Convert text to uppercase."""
    return text.upper()

@plugin(name="reverse")
def reverse_text(text):
    """Reverse the text."""
    return text[::-1]

@plugin(name="word_count")
def count_words(text):
    """Count words in text."""
    words = text.split()
    return {"total_words": len(words), "unique_words": len(set(words))}

@plugin()   # uses function name as plugin name
def censor(text, bad_words=None):
    """Replace bad words with asterisks."""
    if bad_words is None:
        bad_words = ["spam", "eggs"]
    for word in bad_words:
        text = text.replace(word, "*" * len(word))
    return text

# --- Demo ---

if __name__ == "__main__":
    print("Available plugins:", list_plugins())
    # ['uppercase', 'reverse', 'word_count', 'censor']

    sample = "Hello World spam eggs foo"

    for name in list_plugins():
        result = run_plugin(name, sample)
        print(f"  {name}: {result}")

    # Interactive mode
    while True:
        choice = input("\nPlugin name (or 'quit'): ").strip()
        if choice == "quit":
            break
        text = input("Text: ").strip()
        try:
            print(f"Result: {run_plugin(choice, text)}")
        except KeyError as e:
            print(e)
```

**What you practised:** Decorators with optional parameters, a global registry pattern, `*args`/`**kwargs` forwarding, `functools.wraps`.

---

#### Mini-project 2: Lazy data pipeline with generators

Build a composable pipeline that processes large datasets without loading everything into memory.

```python
"""
data_pipeline.py — Generator-based data pipeline.

Demonstrates:
- Generator functions
- yield / yield from
- Pipeline composition
- Memory-efficient processing
"""
import time
import random

# --- Stage 1: data source generators ---

def generate_sensor_data(sensor_id, count=100):
    """Simulate a temperature sensor producing readings over time."""
    for i in range(count):
        yield {
            "sensor_id": sensor_id,
            "timestamp": time.time(),
            "reading": round(20.0 + random.gauss(0, 5), 2),  # ~20C +/- 5
            "seq": i,
        }

def merge_sensors(*generators):
    """Interleave readings from multiple sensors."""
    import heapq
    # Use heapq.merge would need sortable items; we'll round-robin instead
    active = list(generators)
    while active:
        next_active = []
        for gen in active:
            try:
                yield next(gen)
            except StopIteration:
                continue
            else:
                next_active.append(gen)
        active = next_active

# --- Stage 2: transformation generators ---

def add_celsius_to_fahrenheit(readings):
    """Add a fahrenheit field to each reading."""
    for r in readings:
        r["fahrenheit"] = round(r["reading"] * 9 / 5 + 32, 2)
        yield r

def tag_anomalies(readings, low=10.0, high=30.0):
    """Flag readings outside the normal range."""
    for r in readings:
        temp = r["reading"]
        r["anomaly"] = temp < low or temp > high
        yield r

# --- Stage 3: filter generators ---

def only_anomalies(readings):
    """Yield only anomalous readings."""
    for r in readings:
        if r.get("anomaly"):
            yield r

# --- Stage 4: sink (consumer) ---

def print_readings(readings, limit=None):
    """Print readings, optionally limiting to 'limit' items."""
    count = 0
    for r in readings:
        sensor = r["sensor_id"]
        temp_c = r["reading"]
        temp_f = r.get("fahrenheit", "N/A")
        flag = " [ANOMALY]" if r.get("anomaly") else ""
        print(f"  Sensor {sensor}: {temp_c}C / {temp_f}F{flag}")
        count += 1
        if limit and count >= limit:
            break
    print(f"  (Displayed {count} readings)")

# --- Compose the pipeline ---

if __name__ == "__main__":
    print("=== Full pipeline: 3 sensors, 50 readings each ===")

    # Build source
    source = merge_sensors(
        generate_sensor_data("A", 50),
        generate_sensor_data("B", 50),
        generate_sensor_data("C", 50),
    )

    # Chain transformations (nothing executes yet — all lazy!)
    pipeline = add_celsius_to_fahrenheit(source)
    pipeline = tag_anomalies(pipeline, low=12.0, high=28.0)

    # Consume: only now do values flow through
    print_readings(pipeline, limit=20)

    print("\n=== Anomalies only ===")
    source2 = merge_sensors(
        generate_sensor_data("X", 200),
        generate_sensor_data("Y", 200),
    )
    pipeline2 = tag_anomalies(
        add_celsius_to_fahrenheit(source2),
        low=12.0, high=28.0,
    )
    anomalies = only_anomalies(pipeline2)
    print_readings(anomalies, limit=10)
```

**What you practised:** Generator functions, `yield` and `yield from`, lazy evaluation, composable pipeline stages, memory-efficient data processing.

---


### Deep Dive: Modules, Imports & Package Development

**Goal:** Understand Python's import system, create your own packages, manage dependencies, and structure real-world projects professionally.

---

#### How Python imports work — the full picture

When you write `import mymodule`, Python goes through these steps:

1. **Check `sys.modules` cache** — if the module was already imported, return the cached version (modules are only executed once).
2. **Find the module** — search through finders in `sys.meta_path`.
3. **Load the module** — execute its code and create a module object.
4. **Cache it** — store in `sys.modules` for future imports.

```python
import sys

# See all currently imported modules
print(list(sys.modules.keys())[:10])

# Check the search path
for p in sys.path:
    print(p)
```

**The search order for `sys.path`:**

1. The directory containing the running script (or the current directory in interactive mode).
2. Directories in the `PYTHONPATH` environment variable.
3. Installation-dependent default directories (site-packages, etc.).

```python
import sys

# You can add custom directories at runtime
sys.path.insert(0, "/path/to/my/libs")

# But it's better to use packages and virtual environments!
```

---

#### Import styles and when to use each

```python
# Style 1: Import the whole module
import os
os.path.join("a", "b")        # explicit, clear where join comes from

# Style 2: Import specific names
from os.path import join, exists
join("a", "b")                 # shorter, but less obvious origin

# Style 3: Import with alias
import numpy as np             # common convention for large libraries
import pandas as pd

# Style 4: Wildcard import (AVOID in production code)
from os.path import *          # imports everything — pollutes namespace
```

**Best practices:**
- Prefer `import module` for standard library and large packages.
- Use `from module import name` when you use a specific name many times.
- Use aliases (`as`) only for widely-accepted conventions (`np`, `pd`, `plt`).
- **Never** use `from x import *` in production code — it makes it impossible to track where names come from.

---

#### Package structure — building your own

A **package** is a directory containing an `__init__.py` file. Packages let you organize related modules into a hierarchy.

```text
myproject/
    __init__.py              # makes myproject a package
    config.py                # configuration settings
    models/
        __init__.py          # makes models a sub-package
        user.py
        product.py
    services/
        __init__.py
        auth.py
        payment.py
    utils/
        __init__.py
        helpers.py
        validators.py
    cli.py                   # command-line interface
```

**`__init__.py` — what goes in it?**

The `__init__.py` file runs when the package is imported. It can:

```python
# myproject/__init__.py

# 1. Be empty (minimum required to mark folder as package)

# 2. Define package-level imports for convenience
from .config import settings
from .models.user import User

# 3. Define __all__ to control "from myproject import *"
__all__ = ["settings", "User"]

# 4. Run initialization code
print("myproject package loaded")
```

```python
# Now users can do:
from myproject import User          # instead of from myproject.models.user import User
from myproject import settings      # instead of from myproject.config import settings
```

---

#### Relative vs absolute imports

**Absolute imports** use the full path from the project root:

```python
# In myproject/services/auth.py
from myproject.models.user import User
from myproject.utils.helpers import hash_password
```

**Relative imports** use dots to reference the current package:

```python
# In myproject/services/auth.py
from ..models.user import User          # go up one level, then into models
from ..utils.helpers import hash_password

# In myproject/models/product.py
from .user import User                  # same directory (models/)
from . import user                      # import the module itself
```

**Rules for relative imports:**
- `.` = current package
- `..` = parent package
- `...` = grandparent package
- Relative imports **only work inside packages** (not in scripts run directly).

```python
# This will FAIL if you run: python myproject/services/auth.py
# Relative imports require the module to be part of a package.
# Run from outside: python -m myproject.services.auth
```

---

#### The `__all__` variable

`__all__` controls what `from module import *` exports. It's also used by documentation tools and IDEs.

```python
# mymodule.py
__all__ = ["public_function", "PublicClass"]

def public_function():
    """This will be imported by 'from mymodule import *'."""
    pass

def _private_helper():
    """Leading underscore = private by convention (not imported by *)."""
    pass

class PublicClass:
    pass

class _InternalClass:
    pass
```

**In `__init__.py`, `__all__` controls the package's public API:**

```python
# mypackage/__init__.py
from .module_a import func_a, func_b
from .module_b import ClassX

__all__ = ["func_a", "func_b", "ClassX"]
```

---

#### Namespace packages (PEP 420)

Python 3.3+ supports **namespace packages** — packages **without** `__init__.py`. This allows a single logical package to be split across multiple directories.

```text
# Two separate directories, both contributing to "mypkg":

/path/one/
    mypkg/
        module_a.py      # no __init__.py!

/path/two/
    mypkg/
        module_b.py      # no __init__.py!
```

If both paths are in `sys.path`, you can do:

```python
from mypkg import module_a
from mypkg import module_b
```

**When to use:** Plugin systems, large organizations splitting a package across repos. For most projects, regular packages with `__init__.py` are fine.

---

#### Creating a pip-installable package

To make your package installable with `pip install`, you need a `pyproject.toml`:

```text
my-awesome-tool/
    pyproject.toml
    README.md
    LICENSE
    src/
        awesome_tool/
            __init__.py
            core.py
            cli.py
    tests/
        test_core.py
```

**`pyproject.toml` — the modern way (replaces setup.py):**

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "awesome-tool"
version = "1.0.0"
description = "A short description of your tool"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "click>=8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
    "mypy",
]

[project.scripts]
awesome = "awesome_tool.cli:main"    # creates 'awesome' command
```

**Build and install:**

```bash
# Install in development mode (editable)
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"

# Build distribution files
pip install build
python -m build
# Creates dist/awesome_tool-1.0.0.tar.gz and dist/awesome_tool-1.0.0-py3-none-any.whl
```

---

#### Virtual environments in practice

Virtual environments isolate project dependencies so different projects don't conflict.

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Your prompt changes to show the active venv:
# (.venv) $ pip install requests

# Deactivate when done
deactivate
```

**Managing dependencies with `requirements.txt`:**

```bash
# Record current packages
pip freeze > requirements.txt

# Install on another machine
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```text
requests==2.31.0
click==8.1.7
rich>=13.0,<14.0
python-dotenv~=1.0.0
```

**Version specifiers:**
| Syntax | Meaning |
|--------|---------|
| `==2.31.0` | Exact version |
| `>=2.28` | Minimum version |
| `>=2.28,<3.0` | Range |
| `~=1.0.0` | Compatible release (>=1.0.0, <1.1.0) |

---

#### The `if __name__ == "__main__"` pattern revisited

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This block ONLY runs when the file is executed directly
# It does NOT run when the file is imported as a module
if __name__ == "__main__":
    print("Calculator demo:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 1 = {subtract(5, 1)}")
```

```python
# other_file.py
from calculator import add    # calculator.py is imported, __name__ is "calculator"
print(add(10, 20))           # 30 — the demo code does NOT run
```

---

#### Mini-project 1: CLI tool as an installable package

Build a simple task manager that can be installed with pip and run from the command line.

```text
task-manager/
    pyproject.toml
    src/
        taskman/
            __init__.py
            storage.py
            cli.py
```

```python
# src/taskman/__init__.py
"""Taskman — a simple CLI task manager."""
__version__ = "1.0.0"
```

```python
# src/taskman/storage.py
"""Handles reading and writing tasks to a JSON file."""
import json
from pathlib import Path

DEFAULT_FILE = Path.home() / ".taskman_tasks.json"

def load_tasks(path=DEFAULT_FILE):
    """Load tasks from JSON file. Returns empty list if file missing."""
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    return json.loads(text)

def save_tasks(tasks, path=DEFAULT_FILE):
    """Save tasks list to JSON file."""
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")

def add_task(title, priority="medium"):
    """Add a new task and save."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    return task

def complete_task(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            return t
    return None

def list_tasks(show_done=False):
    """Return tasks, optionally including completed ones."""
    tasks = load_tasks()
    if not show_done:
        tasks = [t for t in tasks if not t["done"]]
    return tasks
```

```python
# src/taskman/cli.py
"""Command-line interface for taskman."""
import sys
from . import __version__
from .storage import add_task, complete_task, list_tasks

def print_usage():
    print(f"taskman v{__version__}")
    print("Usage:")
    print("  taskman add <title> [--priority high|medium|low]")
    print("  taskman list [--all]")
    print("  taskman done <id>")
    print("  taskman --version")

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print_usage()
        return

    if args[0] == "--version":
        print(f"taskman v{__version__}")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Error: provide a task title")
            return
        title = args[1]
        priority = "medium"
        if "--priority" in args:
            idx = args.index("--priority")
            if idx + 1 < len(args):
                priority = args[idx + 1]
        task = add_task(title, priority)
        print(f"Added task #{task['id']}: {task['title']} [{task['priority']}]")

    elif command == "list":
        show_all = "--all" in args
        tasks = list_tasks(show_done=show_all)
        if not tasks:
            print("No tasks!" if not show_all else "No tasks at all!")
            return
        for t in tasks:
            status = "[x]" if t["done"] else "[ ]"
            print(f"  {status} #{t['id']} {t['title']} ({t['priority']})")

    elif command == "done":
        if len(args) < 2:
            print("Error: provide a task ID")
            return
        task_id = int(args[1])
        task = complete_task(task_id)
        if task:
            print(f"Completed: #{task['id']} {task['title']}")
        else:
            print(f"Task #{task_id} not found")

    else:
        print(f"Unknown command: {command}")
        print_usage()

if __name__ == "__main__":
    main()
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "taskman"
version = "1.0.0"
description = "A simple CLI task manager"
requires-python = ">=3.10"

[project.scripts]
taskman = "taskman.cli:main"
```

After `pip install -e .`, you can run `taskman add "Buy groceries"` from anywhere!

**What you practised:** Package structure, `__init__.py`, relative imports, `pyproject.toml`, console entry points, JSON file storage.

---

#### Mini-project 2: Dynamic module loader (plugin discovery)

Build a system that automatically discovers and loads Python modules from a plugins directory.

```python
"""
plugin_loader.py — Automatically discover and load plugin modules.

Demonstrates:
- importlib for dynamic imports
- pathlib for file discovery
- Package/module concepts
- The __all__ pattern
"""
import importlib
import importlib.util
from pathlib import Path

class PluginLoader:
    """Discover and load plugin modules from a directory."""

    def __init__(self, plugin_dir):
        self.plugin_dir = Path(plugin_dir)
        self.plugins = {}   # name -> module

    def discover(self):
        """Find all .py files in the plugin directory."""
        if not self.plugin_dir.is_dir():
            print(f"Plugin directory not found: {self.plugin_dir}")
            return []
        files = sorted(self.plugin_dir.glob("*.py"))
        return [f for f in files if not f.name.startswith("_")]

    def load(self, filepath):
        """Dynamically import a module from a file path."""
        name = filepath.stem    # filename without extension
        spec = importlib.util.spec_from_file_location(name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.plugins[name] = module
        return module

    def load_all(self):
        """Discover and load all plugins."""
        for filepath in self.discover():
            try:
                mod = self.load(filepath)
                print(f"  Loaded plugin: {filepath.name}")

                # Call setup() if the plugin defines it
                if hasattr(mod, "setup"):
                    mod.setup()
            except Exception as e:
                print(f"  Failed to load {filepath.name}: {e}")

    def run(self, name, *args, **kwargs):
        """Run a plugin's main() function."""
        if name not in self.plugins:
            raise KeyError(f"Plugin '{name}' not loaded")
        mod = self.plugins[name]
        if not hasattr(mod, "main"):
            raise AttributeError(f"Plugin '{name}' has no main() function")
        return mod.main(*args, **kwargs)

    def list_plugins(self):
        """Show all loaded plugins and their docstrings."""
        for name, mod in self.plugins.items():
            doc = (mod.__doc__ or "No description").strip().split("\n")[0]
            print(f"  {name}: {doc}")


# --- Example usage ---
if __name__ == "__main__":
    loader = PluginLoader("./plugins")
    print("Discovering plugins...")
    loader.load_all()
    print("\nLoaded plugins:")
    loader.list_plugins()
```

Create a `plugins/` directory with sample plugins:

```python
# plugins/hello.py
"""Greets the user."""

def setup():
    print("    hello plugin initialized")

def main(name="World"):
    return f"Hello, {name}!"
```

```python
# plugins/stats.py
"""Calculate basic statistics."""

def main(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    sorted_nums = sorted(numbers)
    median = sorted_nums[n // 2] if n % 2 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    return {"count": n, "mean": round(mean, 2), "median": median}
```

**What you practised:** `importlib` dynamic imports, `pathlib` for discovery, module introspection with `hasattr`, plugin architecture patterns.

---


### Error Handling, Testing & Debugging Mastery

**Goal:** Write robust, testable, and debuggable code. Master exception handling, build reliable test suites with pytest, and learn systematic debugging techniques.

---

#### Python's exception hierarchy

All exceptions inherit from `BaseException`. The ones you'll catch most often inherit from `Exception`:

```text
BaseException
  +-- SystemExit              # raised by sys.exit()
  +-- KeyboardInterrupt       # Ctrl+C
  +-- GeneratorExit
  +-- Exception
       +-- StopIteration
       +-- ArithmeticError
       |    +-- ZeroDivisionError
       |    +-- OverflowError
       +-- AttributeError
       +-- EOFError
       +-- ImportError
       |    +-- ModuleNotFoundError
       +-- LookupError
       |    +-- IndexError
       |    +-- KeyError
       +-- NameError
       +-- OSError
       |    +-- FileNotFoundError
       |    +-- PermissionError
       |    +-- FileExistsError
       +-- TypeError
       +-- ValueError
       +-- RuntimeError
       |    +-- RecursionError
       +-- UnicodeError
```

> **Rule of thumb:** Catch `Exception` subclasses, never catch `BaseException` (you'd swallow `KeyboardInterrupt` and `SystemExit`).

---

#### Advanced exception handling patterns

**Multiple except blocks — order matters (most specific first):**

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Invalid types: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None
    else:
        # Runs ONLY if no exception was raised
        print(f"Division successful: {result}")
        return result
    finally:
        # ALWAYS runs, even if an exception was raised or return was called
        print("Division operation complete")

safe_divide(10, 3)    # successful
safe_divide(10, 0)    # ZeroDivisionError
safe_divide("a", 2)   # TypeError
```

**Catching and re-raising:**

```python
import logging

logger = logging.getLogger(__name__)

def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise    # re-raise the SAME exception with original traceback

def process_config():
    try:
        return process_file("config.json")
    except FileNotFoundError:
        # handle at a higher level
        return {"defaults": True}
```

**Exception chaining with `raise ... from ...`:**

```python
class ConfigError(Exception):
    """Application configuration error."""
    pass

def load_config(path):
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigError(f"Config file missing: {path}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"Config file is not valid JSON: {path}") from e

# The traceback will show BOTH exceptions:
# FileNotFoundError: [Errno 2] No such file or directory: 'config.json'
# The above exception was the direct cause of:
# ConfigError: Config file missing: config.json
```

**Custom exception hierarchies:**

```python
class AppError(Exception):
    """Base exception for our application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed for '{field}': {message}")

class NotFoundError(AppError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource_type, resource_id):
        self.resource_type = resource_type
        self.resource_id = resource_id
        super().__init__(f"{resource_type} #{resource_id} not found")

class AuthError(AppError):
    """Raised when authentication or authorization fails."""
    pass

# Usage
def get_user(user_id):
    if user_id < 0:
        raise ValidationError("user_id", "must be a positive integer")
    # ... database lookup ...
    raise NotFoundError("User", user_id)

def handle_request(user_id):
    try:
        user = get_user(user_id)
    except ValidationError as e:
        print(f"Bad request: {e.field} — {e.message}")
    except NotFoundError as e:
        print(f"404: {e.resource_type} {e.resource_id} not found")
    except AppError as e:
        print(f"Application error: {e}")
```

---

#### Context managers and `with` statements

Context managers ensure resources are properly cleaned up, even if exceptions occur. The `with` statement calls `__enter__` on entry and `__exit__` on exit.

**Built-in examples:**

```python
# File handling — file is ALWAYS closed, even if an error occurs
with open("data.txt", "r") as f:
    content = f.read()
# f is now closed

# Multiple context managers
with open("input.txt") as src, open("output.txt", "w") as dst:
    dst.write(src.read())

# Threading locks
import threading
lock = threading.Lock()
with lock:
    # critical section — lock is automatically released
    pass
```

**Writing your own context manager with a class:**

```python
class Timer:
    """Context manager that measures execution time."""
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self   # this is what 'as' binds to

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
# Elapsed: 0.0312s

print(f"Exact time: {t.elapsed}")
```

**Writing context managers with `contextlib`:**

```python
from contextlib import contextmanager
import os

@contextmanager
def temporary_directory_change(path):
    """Temporarily change the working directory."""
    original = os.getcwd()
    try:
        os.chdir(path)
        yield path       # control returns to the 'with' block here
    finally:
        os.chdir(original)   # ALWAYS restore, even on exception

with temporary_directory_change("/tmp"):
    print(os.getcwd())   # /tmp
print(os.getcwd())       # back to original

@contextmanager
def suppress_print():
    """Redirect stdout to suppress print output."""
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout

with suppress_print():
    print("This won't appear")
print("This will appear")
```

---

#### Testing with `unittest`

`unittest` is Python's built-in test framework, inspired by Java's JUnit.

```python
# test_calculator.py
import unittest

# Code under test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestCalculator(unittest.TestCase):
    """Tests for calculator functions."""

    def setUp(self):
        """Run before EACH test method."""
        self.test_data = [(1, 2, 3), (0, 0, 0), (-1, 1, 0)]

    def tearDown(self):
        """Run after EACH test method."""
        pass   # cleanup if needed

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_with_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_from_test_data(self):
        for a, b, expected in self.test_data:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.3333, places=3)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    def test_add_returns_correct_type(self):
        result = add(1, 2)
        self.assertIsInstance(result, int)

if __name__ == "__main__":
    unittest.main()
```

**Common assertions:**

| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertIsInstance(a, b)` | `isinstance(a, b)` |
| `assertRaises(Exc)` | exception raised |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |

---

#### Testing with `pytest` — the modern way

`pytest` is more concise, more powerful, and the standard for most Python projects.

**Install:** `pip install pytest`

**Basic tests — just use `assert`:**

```python
# test_math_ops.py

def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_returns_int():
    assert isinstance(add(1, 2), int)
```

Run: `pytest test_math_ops.py -v`

**Testing exceptions:**

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

**Parametrized tests — run the same test with different data:**

```python
import pytest

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
    ("ab", False),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
```

**Fixtures — reusable test setup:**

```python
import pytest
import json
from pathlib import Path

@pytest.fixture
def sample_users():
    """Provide sample user data for tests."""
    return [
        {"name": "Alice", "age": 30, "active": True},
        {"name": "Bob", "age": 25, "active": False},
        {"name": "Charlie", "age": 35, "active": True},
    ]

@pytest.fixture
def temp_json_file(tmp_path, sample_users):
    """Create a temporary JSON file with sample data."""
    filepath = tmp_path / "users.json"
    filepath.write_text(json.dumps(sample_users))
    return filepath

def test_load_users(temp_json_file):
    """Test loading users from a JSON file."""
    data = json.loads(temp_json_file.read_text())
    assert len(data) == 3
    assert data[0]["name"] == "Alice"

def test_filter_active_users(sample_users):
    """Test filtering for active users."""
    active = [u for u in sample_users if u["active"]]
    assert len(active) == 2
    assert all(u["active"] for u in active)
```

**Fixture scopes:**

```python
@pytest.fixture(scope="function")   # default: runs for each test
def per_test():
    return []

@pytest.fixture(scope="module")     # runs once per test file
def db_connection():
    conn = create_connection()
    yield conn           # yield = teardown happens after
    conn.close()

@pytest.fixture(scope="session")    # runs once for entire test suite
def app_config():
    return load_config()
```

**Markers — categorize and select tests:**

```python
import pytest

@pytest.mark.slow
def test_large_computation():
    """This test takes a long time."""
    result = sum(range(100_000_000))
    assert result > 0

@pytest.mark.integration
def test_api_call():
    """Requires network access."""
    pass

# Run only slow tests:   pytest -m slow
# Skip slow tests:       pytest -m "not slow"
```

---

#### Mocking and patching

**Mocking** replaces real objects with fake ones during testing. This lets you test code in isolation without side effects (network calls, file I/O, databases).

```python
# api_client.py
import requests

def get_user(user_id):
    """Fetch user from API."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

def get_username(user_id):
    """Get just the username."""
    user = get_user(user_id)
    return user["username"]
```

```python
# test_api_client.py
from unittest.mock import patch, MagicMock
from api_client import get_username

def test_get_username():
    # Create a mock response object
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com"
    }
    mock_response.raise_for_status.return_value = None

    # Patch requests.get to return our mock
    with patch("api_client.requests.get", return_value=mock_response) as mock_get:
        result = get_username(1)

        assert result == "alice"
        mock_get.assert_called_once_with("https://api.example.com/users/1")
```

**Patching with decorators:**

```python
from unittest.mock import patch
import api_client

@patch("api_client.requests.get")
def test_get_user_error(mock_get):
    """Test that HTTP errors are propagated."""
    mock_get.return_value.raise_for_status.side_effect = Exception("500 Server Error")

    import pytest
    with pytest.raises(Exception, match="500"):
        api_client.get_user(999)
```

**Mocking file operations:**

```python
from unittest.mock import mock_open, patch

def read_config(path):
    with open(path) as f:
        return f.read()

def test_read_config():
    fake_content = '{"debug": true}'
    with patch("builtins.open", mock_open(read_data=fake_content)):
        result = read_config("config.json")
        assert result == '{"debug": true}'
```

---

#### Debugging with `breakpoint()` and `pdb`

Python 3.7+ provides `breakpoint()` as a convenient way to enter the debugger.

```python
def find_bug(items):
    total = 0
    for i, item in enumerate(items):
        total += item["value"]
        breakpoint()       # execution pauses here — interactive debugger
        if total > 100:
            return i
    return -1
```

**Essential pdb commands:**

| Command | Shortcut | Action |
|---------|----------|--------|
| `next` | `n` | Execute next line (step over) |
| `step` | `s` | Step into function call |
| `continue` | `c` | Continue until next breakpoint |
| `print expr` | `p expr` | Print expression value |
| `pretty-print` | `pp expr` | Pretty-print complex objects |
| `list` | `l` | Show source code around current line |
| `where` | `w` | Show call stack |
| `up` | `u` | Move up one frame in call stack |
| `down` | `d` | Move down one frame |
| `quit` | `q` | Exit debugger |
| `break N` | `b N` | Set breakpoint at line N |
| `clear` | `cl` | Clear breakpoints |

**Conditional breakpoints:**

```python
for i in range(1000):
    result = complex_calculation(i)
    if result < 0:
        breakpoint()    # only pause when something unexpected happens
```

**Post-mortem debugging** — debug after an exception:

```python
import pdb

try:
    buggy_code()
except Exception:
    pdb.post_mortem()     # enter debugger at the point of failure
```

---

#### Assertions and defensive programming

Use `assert` for catching programmer errors (not user input errors):

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)

# assert statements are removed when Python runs with -O (optimize) flag
# NEVER use assert for input validation — use if/raise instead!
```

**When to use assert vs raise:**

```python
# Use ASSERT for internal logic checks (programmer mistakes)
def _internal_process(data):
    assert isinstance(data, list), "Bug: expected list"
    assert len(data) > 0, "Bug: empty data"
    # ...

# Use RAISE for input validation (user/caller mistakes)
def public_api(user_input):
    if not isinstance(user_input, str):
        raise TypeError(f"Expected string, got {type(user_input).__name__}")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty")
```

---

#### Mini-project 1: Test-driven development — URL shortener

Build a URL shortener using TDD: write the test first, then make it pass.

```python
# url_shortener.py
"""A simple in-memory URL shortener."""
import hashlib
import string

class URLShortener:
    """Shortens long URLs and resolves short codes back to originals."""

    BASE62 = string.digits + string.ascii_letters

    def __init__(self, domain="http://short.ly"):
        self.domain = domain
        self._url_to_code = {}    # long URL -> short code
        self._code_to_url = {}    # short code -> long URL

    def _generate_code(self, url, length=6):
        """Generate a short code from a URL using hashing."""
        hash_hex = hashlib.md5(url.encode()).hexdigest()
        hash_int = int(hash_hex, 16)
        code = []
        for _ in range(length):
            code.append(self.BASE62[hash_int % 62])
            hash_int //= 62
        return "".join(code)

    def shorten(self, long_url):
        """Shorten a URL. Returns the same short URL for duplicate inputs."""
        if not long_url or not long_url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL: must start with http:// or https://")

        if long_url in self._url_to_code:
            code = self._url_to_code[long_url]
        else:
            code = self._generate_code(long_url)
            # Handle collisions
            while code in self._code_to_url and self._code_to_url[code] != long_url:
                code = self._generate_code(long_url + code)
            self._url_to_code[long_url] = code
            self._code_to_url[code] = long_url

        return f"{self.domain}/{code}"

    def resolve(self, short_url):
        """Resolve a short URL back to the original."""
        code = short_url.split("/")[-1]
        if code not in self._code_to_url:
            raise KeyError(f"Short code '{code}' not found")
        return self._code_to_url[code]

    @property
    def count(self):
        """Number of stored URLs."""
        return len(self._code_to_url)
```

```python
# test_url_shortener.py
"""TDD tests for URL shortener — written BEFORE the implementation."""
import pytest
from url_shortener import URLShortener

@pytest.fixture
def shortener():
    return URLShortener(domain="http://short.ly")

class TestShorten:
    def test_returns_short_url(self, shortener):
        result = shortener.shorten("https://www.example.com/very/long/path")
        assert result.startswith("http://short.ly/")
        assert len(result.split("/")[-1]) == 6

    def test_same_url_gives_same_code(self, shortener):
        url = "https://www.example.com/page"
        result1 = shortener.shorten(url)
        result2 = shortener.shorten(url)
        assert result1 == result2

    def test_different_urls_give_different_codes(self, shortener):
        r1 = shortener.shorten("https://example.com/a")
        r2 = shortener.shorten("https://example.com/b")
        assert r1 != r2

    def test_invalid_url_raises(self, shortener):
        with pytest.raises(ValueError, match="Invalid URL"):
            shortener.shorten("not-a-url")

    def test_empty_url_raises(self, shortener):
        with pytest.raises(ValueError):
            shortener.shorten("")

class TestResolve:
    def test_resolve_known_url(self, shortener):
        original = "https://www.python.org"
        short = shortener.shorten(original)
        assert shortener.resolve(short) == original

    def test_resolve_unknown_raises(self, shortener):
        with pytest.raises(KeyError, match="not found"):
            shortener.resolve("http://short.ly/zzzzzz")

class TestCount:
    def test_starts_empty(self, shortener):
        assert shortener.count == 0

    def test_count_after_additions(self, shortener):
        shortener.shorten("https://a.com")
        shortener.shorten("https://b.com")
        shortener.shorten("https://a.com")  # duplicate
        assert shortener.count == 2

# Run: pytest test_url_shortener.py -v
```

**What you practised:** TDD workflow (test first, implement, refactor), pytest fixtures, `pytest.raises`, class-based test organization, parametrized assertions.

---

#### Mini-project 2: Robust file processor with full error handling

Build a file processor that reads CSV files, validates data, and handles every possible error gracefully.

```python
"""
file_processor.py — Robust CSV file processor.

Demonstrates:
- Custom exception hierarchy
- Context managers (with statement)
- Comprehensive error handling
- Logging for diagnostics
- Data validation patterns
"""
import csv
import logging
from pathlib import Path
from contextlib import contextmanager

# --- Custom exceptions ---

class ProcessingError(Exception):
    """Base class for processing errors."""
    pass

class FileAccessError(ProcessingError):
    """Cannot read or write a file."""
    pass

class ValidationError(ProcessingError):
    """Data does not meet validation rules."""
    def __init__(self, row_num, field, message):
        self.row_num = row_num
        self.field = field
        super().__init__(f"Row {row_num}, field '{field}': {message}")

# --- Logging setup ---

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("file_processor")

# --- Context manager for tracking ---

@contextmanager
def processing_stats():
    """Track processing statistics."""
    stats = {"processed": 0, "errors": 0, "skipped": 0}
    try:
        yield stats
    finally:
        logger.info(
            f"Processing complete: {stats['processed']} processed, "
            f"{stats['errors']} errors, {stats['skipped']} skipped"
        )

# --- Validation ---

def validate_row(row_num, row, required_fields):
    """Validate a single row of data."""
    errors = []
    for field in required_fields:
        if field not in row or not row[field].strip():
            errors.append(ValidationError(row_num, field, "missing or empty"))

    if "age" in row:
        try:
            age = int(row["age"])
            if age < 0 or age > 150:
                errors.append(ValidationError(row_num, "age", f"out of range: {age}"))
        except ValueError:
            errors.append(ValidationError(row_num, "age", f"not a number: {row['age']}"))

    if "email" in row:
        if "@" not in row["email"]:
            errors.append(ValidationError(row_num, "email", "invalid format"))

    return errors

# --- Main processor ---

def process_csv(input_path, output_path=None):
    """
    Read a CSV file, validate each row, and optionally write valid rows
    to an output file.
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileAccessError(f"Input file not found: {input_path}")
    if not input_path.suffix == ".csv":
        raise FileAccessError(f"Expected .csv file, got: {input_path.suffix}")

    required_fields = ["name", "age", "email"]
    valid_rows = []

    with processing_stats() as stats:
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row_num, row in enumerate(reader, start=2):  # +2 for header
                    errors = validate_row(row_num, row, required_fields)

                    if errors:
                        stats["errors"] += len(errors)
                        for err in errors:
                            logger.warning(str(err))
                        stats["skipped"] += 1
                        continue

                    # Transform valid data
                    valid_rows.append({
                        "name": row["name"].strip().title(),
                        "age": int(row["age"]),
                        "email": row["email"].strip().lower(),
                    })
                    stats["processed"] += 1

        except UnicodeDecodeError as e:
            raise FileAccessError(f"File encoding error: {e}") from e
        except csv.Error as e:
            raise ProcessingError(f"CSV parsing error: {e}") from e

    # Write output
    if output_path and valid_rows:
        output_path = Path(output_path)
        try:
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "age", "email"])
                writer.writeheader()
                writer.writerows(valid_rows)
            logger.info(f"Wrote {len(valid_rows)} valid rows to {output_path}")
        except PermissionError as e:
            raise FileAccessError(f"Cannot write to {output_path}: {e}") from e

    return valid_rows


# --- Demo ---
if __name__ == "__main__":
    # Create sample input
    sample_csv = Path("sample_input.csv")
    sample_csv.write_text(
        "name,age,email\n"
        "Alice,30,alice@example.com\n"
        "Bob,invalid_age,bob@example.com\n"
        ",25,no-name@example.com\n"
        "Charlie,200,charlie@example.com\n"
        "Diana,28,not-an-email\n"
        "Eve,22,eve@example.com\n"
    )

    try:
        results = process_csv("sample_input.csv", "clean_output.csv")
        print(f"\nValid records: {len(results)}")
        for r in results:
            print(f"  {r['name']} (age {r['age']}) — {r['email']}")
    except ProcessingError as e:
        print(f"Processing failed: {e}")
    finally:
        sample_csv.unlink(missing_ok=True)
```

**What you practised:** Custom exception hierarchy, exception chaining, context managers, logging, CSV processing, `pathlib`, validation patterns, `finally` cleanup.

---


### Working with Files, Databases & Data Formats

**Goal:** Work with files, paths, serialization formats, and databases professionally. Master `pathlib` for cross-platform file operations, and learn to handle JSON, CSV, TOML, SQLite, binary data, and temporary files.

---

#### `pathlib` — the modern way to work with files and directories

`pathlib` (Python 3.4+) provides an object-oriented interface for filesystem paths. It replaces the older `os.path` module and is the recommended approach.

**Creating and manipulating paths:**

```python
from pathlib import Path

# Create path objects
home = Path.home()                    # e.g., /home/alice or C:\Users\alice
cwd = Path.cwd()                     # current working directory
data = Path("data") / "2024" / "results.csv"   # join with /

print(data)              # data/2024/results.csv  (OS-appropriate separators)
print(data.parent)       # data/2024
print(data.name)         # results.csv
print(data.stem)         # results
print(data.suffix)       # .csv
print(data.suffixes)     # ['.csv']  (handles .tar.gz: ['.tar', '.gz'])
print(data.parts)        # ('data', '2024', 'results.csv')
```

**Checking existence and type:**

```python
from pathlib import Path

p = Path("some_file.txt")

p.exists()       # True/False
p.is_file()      # True if it's a regular file
p.is_dir()       # True if it's a directory
p.is_symlink()   # True if it's a symbolic link
p.is_absolute()  # True if the path is absolute
```

**Reading and writing files:**

```python
from pathlib import Path

# Write text (creates file, overwrites if exists)
Path("output.txt").write_text("Hello, World!", encoding="utf-8")

# Read text
content = Path("output.txt").read_text(encoding="utf-8")
print(content)   # Hello, World!

# Write bytes (for binary data)
Path("data.bin").write_bytes(b"\x00\x01\x02\x03")

# Read bytes
raw = Path("data.bin").read_bytes()
print(raw)       # b'\x00\x01\x02\x03'
```

**Directory operations:**

```python
from pathlib import Path

# Create directories (parents=True is like mkdir -p)
Path("output/reports/2024").mkdir(parents=True, exist_ok=True)

# List directory contents
for item in Path(".").iterdir():
    kind = "DIR " if item.is_dir() else "FILE"
    print(f"  {kind}  {item.name}")

# Glob patterns (find files matching a pattern)
for py_file in Path("src").glob("*.py"):        # only in src/
    print(py_file)

for py_file in Path("src").rglob("*.py"):       # recursive (all subdirs)
    print(py_file)

# Count files by extension
from collections import Counter
extensions = Counter(f.suffix for f in Path(".").rglob("*") if f.is_file())
print(extensions)   # Counter({'.py': 42, '.txt': 13, '.json': 5, ...})
```

**Renaming, moving, and deleting:**

```python
from pathlib import Path

# Rename
Path("old_name.txt").rename("new_name.txt")

# Move (rename to a different directory)
Path("file.txt").rename(Path("archive") / "file.txt")

# Replace (overwrite destination if it exists)
Path("temp.txt").replace("target.txt")

# Delete a file
Path("temp.txt").unlink(missing_ok=True)    # missing_ok avoids FileNotFoundError

# Delete a directory (must be empty)
Path("empty_dir").rmdir()
```

**Resolving and comparing paths:**

```python
from pathlib import Path

p = Path("../sibling/file.txt")
print(p.resolve())           # absolute path: /Users/alice/sibling/file.txt

# Check if one path is inside another
child = Path("/home/alice/projects/app/main.py")
parent = Path("/home/alice/projects")
print(child.is_relative_to(parent))   # True (Python 3.9+)
print(child.relative_to(parent))      # app/main.py
```

---

#### `shutil` — high-level file operations

`shutil` handles operations that `pathlib` can't do alone, like copying files and removing non-empty directories.

```python
import shutil
from pathlib import Path

# Copy a file (preserves metadata)
shutil.copy2("source.txt", "backup.txt")

# Copy an entire directory tree
shutil.copytree("src", "src_backup", dirs_exist_ok=True)

# Remove a directory tree (DANGEROUS — no undo!)
shutil.rmtree("old_project")

# Move files or directories
shutil.move("file.txt", "archive/file.txt")

# Get disk usage
usage = shutil.disk_usage("/")
print(f"Total: {usage.total // (1024**3)} GB")
print(f"Free:  {usage.free // (1024**3)} GB")
```

---

#### JSON — deep dive

JSON is the most common data interchange format. Python's `json` module handles serialization (Python -> JSON) and deserialization (JSON -> Python).

**Type mapping:**

| Python | JSON |
|--------|------|
| `dict` | `object {}` |
| `list`, `tuple` | `array []` |
| `str` | `string ""` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

**Basic reading and writing:**

```python
import json
from pathlib import Path

# Python dict -> JSON string
data = {"name": "Alice", "scores": [95, 87, 92], "active": True}
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string -> Python dict
parsed = json.loads(json_string)
print(parsed["name"])   # Alice

# Write to file
Path("data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")

# Read from file
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

**Custom serialization — handling non-JSON types:**

```python
import json
from datetime import datetime, date
from pathlib import Path

class CustomEncoder(json.JSONEncoder):
    """Handle types that json module can't serialize by default."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj, set):
            return sorted(list(obj))
        if isinstance(obj, bytes):
            import base64
            return base64.b64encode(obj).decode("ascii")
        return super().default(obj)

data = {
    "timestamp": datetime.now(),
    "tags": {"python", "tutorial"},
    "config_path": Path("config") / "settings.json",
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_str)
```

**Custom deserialization with `object_hook`:**

```python
import json
from datetime import datetime

def date_decoder(dct):
    """Convert ISO date strings back to datetime objects."""
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

json_str = '{"name": "Alice", "created": "2024-01-15T10:30:00"}'
result = json.loads(json_str, object_hook=date_decoder)
print(type(result["created"]))   # <class 'datetime.datetime'>
```

**Pretty-printing and sorting keys:**

```python
import json

data = {"z_key": 1, "a_key": 2, "m_key": {"nested": True}}
print(json.dumps(data, indent=4, sort_keys=True))
# {
#     "a_key": 2,
#     "m_key": {
#         "nested": true
#     },
#     "z_key": 1
# }
```

---

#### CSV — advanced usage

**Writing with different dialects and options:**

```python
import csv

rows = [
    {"name": "Alice Smith", "salary": 75000, "department": "Engineering"},
    {"name": "Bob Jones", "salary": 68000, "department": "Marketing"},
    {"name": 'Charlie "Chuck" Brown', "salary": 82000, "department": "Engineering"},
]

# Standard CSV
with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "salary", "department"])
    writer.writeheader()
    writer.writerows(rows)

# Tab-separated (TSV)
with open("employees.tsv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "salary", "department"],
                            delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
```

**Reading with error handling:**

```python
import csv
from pathlib import Path

def read_csv_safe(filepath, required_columns=None):
    """Read a CSV file with validation."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Validate columns
        if required_columns:
            missing = set(required_columns) - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"Missing columns: {missing}")

        for row_num, row in enumerate(reader, start=2):
            rows.append(row)

    return rows

# Usage
try:
    data = read_csv_safe("employees.csv", required_columns=["name", "salary"])
    for row in data:
        print(f"{row['name']}: ${row['salary']}")
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
```

---

#### TOML — configuration files (Python 3.11+)

TOML (Tom's Obvious Minimal Language) is the standard format for Python project configuration (`pyproject.toml`). Python 3.11+ includes `tomllib` for reading.

```python
# Reading TOML (Python 3.11+)
import tomllib
from pathlib import Path

toml_content = """
[project]
name = "my-app"
version = "1.0.0"
description = "A sample application"

[project.dependencies]
requests = ">=2.28"
click = ">=8.0"

[tool.pytest]
testpaths = ["tests"]
verbose = true

[database]
host = "localhost"
port = 5432
name = "myapp_db"
"""

# Parse from string
config = tomllib.loads(toml_content)
print(config["project"]["name"])        # my-app
print(config["database"]["port"])       # 5432
print(config["tool"]["pytest"]["verbose"])  # True

# Parse from file
# with open("pyproject.toml", "rb") as f:   # note: "rb" (binary mode!)
#     config = tomllib.load(f)
```

For writing TOML, use the third-party `tomli-w` package: `pip install tomli-w`.

---

#### SQLite — embedded database deep dive

SQLite is a serverless SQL database that stores everything in a single file. It's included with Python and perfect for small-to-medium applications.

```python
import sqlite3
from pathlib import Path
from contextlib import closing

DB_PATH = "app.db"

def init_database():
    """Create tables if they don't exist."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER CHECK(age > 0 AND age < 150),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                body TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        conn.commit()

def add_user(name, email, age):
    """Insert a user. Returns the new user's ID."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        try:
            cursor = conn.execute(
                "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                (name, email, age)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Cannot add user: {e}")
            return None

def get_users(min_age=0):
    """Fetch users, optionally filtering by minimum age."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row   # access columns by name
        cursor = conn.execute(
            "SELECT * FROM users WHERE age >= ? ORDER BY name",
            (min_age,)
        )
        return [dict(row) for row in cursor.fetchall()]

def search_users(query):
    """Search users by name (case-insensitive)."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            "SELECT * FROM users WHERE name LIKE ?",
            (f"%{query}%",)
        )
        return [dict(row) for row in cursor.fetchall()]
```

**Using context managers with SQLite:**

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection(db_path="app.db"):
    """Context manager for database connections with auto-commit/rollback."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# Usage — clean and safe:
with get_db_connection() as conn:
    conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                 ("Alice", "alice@example.com", 30))
    # auto-commits on success, auto-rollbacks on exception
```

**Transactions for multiple operations:**

```python
def transfer_posts(from_user_id, to_user_id):
    """Transfer all posts from one user to another (atomic operation)."""
    with get_db_connection() as conn:
        # Both operations succeed or both fail
        conn.execute(
            "UPDATE posts SET user_id = ? WHERE user_id = ?",
            (to_user_id, from_user_id)
        )
        conn.execute(
            "DELETE FROM users WHERE id = ?",
            (from_user_id,)
        )
        # commit happens automatically when 'with' block exits
```

---

#### Binary files and `struct`

For reading/writing binary data (images, network protocols, file headers):

```python
import struct

# Pack Python values into bytes
# 'I' = unsigned int, 'f' = float, '10s' = 10-byte string
header = struct.pack('If10s', 42, 3.14, b'HelloWorld')
print(header)       # b'*\x00\x00\x00\xc3\xf5H@HelloWorld'
print(len(header))  # 18 bytes

# Unpack bytes back to Python values
magic, version, name = struct.unpack('If10s', header)
print(magic)        # 42
print(version)      # 3.140000104904175 (float precision)
print(name)         # b'HelloWorld'
```

**Reading a BMP image header:**

```python
import struct
from pathlib import Path

def read_bmp_header(filepath):
    """Read basic info from a BMP image file header."""
    data = Path(filepath).read_bytes()

    # BMP header: 2-byte magic, 4-byte file size, 4 reserved, 4-byte offset
    magic = data[0:2]
    if magic != b'BM':
        raise ValueError("Not a BMP file")

    file_size, = struct.unpack_from('<I', data, 2)    # little-endian uint32
    width, = struct.unpack_from('<i', data, 18)        # signed int32
    height, = struct.unpack_from('<i', data, 22)
    bpp, = struct.unpack_from('<H', data, 28)          # uint16 (bits per pixel)

    return {
        "file_size": file_size,
        "width": width,
        "height": height,
        "bits_per_pixel": bpp,
    }
```

---

#### Temporary files and directories

`tempfile` creates temporary files and directories that are automatically cleaned up.

```python
import tempfile
from pathlib import Path

# Temporary file (auto-deleted when closed)
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    f.write('{"key": "value"}')
    temp_path = f.name
    print(f"Temp file: {temp_path}")

# Read and then clean up
content = Path(temp_path).read_text()
Path(temp_path).unlink()

# Temporary directory (auto-deleted when context exits)
with tempfile.TemporaryDirectory() as tmpdir:
    tmp = Path(tmpdir)
    (tmp / "data.txt").write_text("temporary data")
    print(list(tmp.iterdir()))
# tmpdir and all contents are deleted here
```

---

#### `pickle` — Python object serialization

`pickle` can serialize almost any Python object to bytes and back. It's Python-specific (not portable like JSON).

```python
import pickle
from pathlib import Path

# Serialize complex objects
data = {
    "users": [{"name": "Alice", "scores": {95, 87, 92}}],
    "metadata": {"version": 2, "valid": True},
}

# Save to file
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load from file
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded["users"][0]["scores"])   # {87, 92, 95} (set preserved!)
```

> **Security warning:** NEVER unpickle data from untrusted sources. Pickle can execute arbitrary code during deserialization. Use JSON for data from external sources.

---

#### Mini-project 1: Personal contact database

Build a contact manager backed by SQLite with full CRUD operations.

```python
"""
contacts.py — Personal contact database using SQLite.

Demonstrates:
- SQLite with context managers
- pathlib for file handling
- JSON export/import
- Comprehensive error handling
- CRUD operations
"""
import sqlite3
import json
from pathlib import Path
from contextlib import contextmanager
from datetime import datetime

DB_FILE = Path.home() / ".contacts.db"

@contextmanager
def get_db():
    """Database connection context manager."""
    conn = sqlite3.connect(str(DB_FILE))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Create tables if they don't exist."""
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                category TEXT DEFAULT 'general',
                notes TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                updated_at TEXT DEFAULT (datetime('now'))
            )
        """)
        db.execute("""
            CREATE INDEX IF NOT EXISTS idx_contacts_name
            ON contacts(name COLLATE NOCASE)
        """)

def add_contact(name, email=None, phone=None, category="general", notes=None):
    """Add a new contact. Returns the contact ID."""
    with get_db() as db:
        cursor = db.execute(
            """INSERT INTO contacts (name, email, phone, category, notes)
               VALUES (?, ?, ?, ?, ?)""",
            (name, email, phone, category, notes)
        )
        return cursor.lastrowid

def search_contacts(query):
    """Search contacts by name, email, or phone."""
    with get_db() as db:
        pattern = f"%{query}%"
        rows = db.execute(
            """SELECT * FROM contacts
               WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
               ORDER BY name COLLATE NOCASE""",
            (pattern, pattern, pattern)
        ).fetchall()
        return [dict(r) for r in rows]

def update_contact(contact_id, **fields):
    """Update specific fields of a contact."""
    allowed = {"name", "email", "phone", "category", "notes"}
    updates = {k: v for k, v in fields.items() if k in allowed}
    if not updates:
        return False

    updates["updated_at"] = datetime.now().isoformat()
    set_clause = ", ".join(f"{k} = ?" for k in updates)

    with get_db() as db:
        db.execute(
            f"UPDATE contacts SET {set_clause} WHERE id = ?",
            (*updates.values(), contact_id)
        )
        return True

def delete_contact(contact_id):
    """Delete a contact by ID."""
    with get_db() as db:
        cursor = db.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        return cursor.rowcount > 0

def list_contacts(category=None):
    """List all contacts, optionally filtered by category."""
    with get_db() as db:
        if category:
            rows = db.execute(
                "SELECT * FROM contacts WHERE category = ? ORDER BY name",
                (category,)
            ).fetchall()
        else:
            rows = db.execute("SELECT * FROM contacts ORDER BY name").fetchall()
        return [dict(r) for r in rows]

def export_json(filepath):
    """Export all contacts to a JSON file."""
    contacts = list_contacts()
    Path(filepath).write_text(json.dumps(contacts, indent=2), encoding="utf-8")
    return len(contacts)

def import_json(filepath):
    """Import contacts from a JSON file."""
    data = json.loads(Path(filepath).read_text(encoding="utf-8"))
    count = 0
    for c in data:
        add_contact(
            name=c["name"],
            email=c.get("email"),
            phone=c.get("phone"),
            category=c.get("category", "general"),
            notes=c.get("notes"),
        )
        count += 1
    return count

def stats():
    """Get contact database statistics."""
    with get_db() as db:
        total = db.execute("SELECT COUNT(*) FROM contacts").fetchone()[0]
        categories = db.execute(
            "SELECT category, COUNT(*) as cnt FROM contacts GROUP BY category ORDER BY cnt DESC"
        ).fetchall()
        return {
            "total": total,
            "categories": {r["category"]: r["cnt"] for r in categories}
        }

# --- CLI Interface ---
if __name__ == "__main__":
    init_db()

    # Demo
    print("Adding sample contacts...")
    add_contact("Alice Johnson", "alice@example.com", "555-0101", "work")
    add_contact("Bob Smith", "bob@example.com", "555-0102", "friend")
    add_contact("Charlie Brown", "charlie@example.com", None, "family")
    add_contact("Alice Williams", "awilliams@example.com", "555-0201", "work")

    print(f"\nAll contacts ({stats()['total']} total):")
    for c in list_contacts():
        print(f"  [{c['id']}] {c['name']} | {c['email']} | {c['category']}")

    print("\nSearch 'alice':")
    for c in search_contacts("alice"):
        print(f"  {c['name']} — {c['email']}")

    print(f"\nStats: {stats()}")

    # Export
    exported = export_json("contacts_backup.json")
    print(f"\nExported {exported} contacts to contacts_backup.json")
```

**What you practised:** SQLite CRUD, context managers, `pathlib`, JSON import/export, parameterized queries, index creation, `sqlite3.Row`.

---

#### Mini-project 2: Automatic file organizer

Build a script that watches a directory and organizes files into subfolders by type.

```python
"""
file_organizer.py — Organize files into category folders.

Demonstrates:
- pathlib for all file operations
- shutil for moving files
- defaultdict for grouping
- Configuration via dict
- Dry-run mode for safety
"""
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# File category rules
CATEGORIES = {
    "Images":    {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx"},
    "Code":      {".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".rs"},
    "Data":      {".json", ".csv", ".xml", ".yaml", ".yml", ".toml", ".sql", ".db"},
    "Archives":  {".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"},
    "Media":     {".mp3", ".mp4", ".avi", ".mkv", ".wav", ".flac", ".mov"},
}

def categorize_file(filepath):
    """Determine the category for a file based on its extension."""
    ext = filepath.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"

def scan_directory(source_dir):
    """Scan a directory and group files by category."""
    source = Path(source_dir)
    if not source.is_dir():
        raise FileNotFoundError(f"Directory not found: {source}")

    groups = defaultdict(list)
    for item in source.iterdir():
        if item.is_file() and not item.name.startswith("."):
            category = categorize_file(item)
            groups[category].append(item)

    return dict(groups)

def organize(source_dir, dry_run=True):
    """
    Move files into category sub-folders.

    Args:
        source_dir: Directory to organize
        dry_run: If True, only print what would happen (no actual moves)
    """
    groups = scan_directory(source_dir)
    source = Path(source_dir)
    moved = 0
    errors = 0

    print(f"{'[DRY RUN] ' if dry_run else ''}Organizing {source}...")
    print(f"Found {sum(len(v) for v in groups.values())} files in {len(groups)} categories\n")

    for category, files in sorted(groups.items()):
        dest_dir = source / category
        print(f"  {category}/ ({len(files)} files)")

        if not dry_run:
            dest_dir.mkdir(exist_ok=True)

        for f in sorted(files, key=lambda p: p.name.lower()):
            dest = dest_dir / f.name

            # Handle name conflicts
            if dest.exists():
                stem = f.stem
                suffix = f.suffix
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                dest = dest_dir / f"{stem}_{timestamp}{suffix}"

            print(f"    {f.name} -> {category}/{dest.name}")

            if not dry_run:
                try:
                    shutil.move(str(f), str(dest))
                    moved += 1
                except Exception as e:
                    print(f"    ERROR: {e}")
                    errors += 1

    print(f"\n{'Would move' if dry_run else 'Moved'}: {moved if not dry_run else sum(len(v) for v in groups.values())} files")
    if errors:
        print(f"Errors: {errors}")

    return groups

def summary_report(source_dir):
    """Generate a summary of the directory's file types."""
    groups = scan_directory(source_dir)
    total_size = 0
    print(f"\nDirectory summary: {source_dir}")
    print("-" * 50)
    for category, files in sorted(groups.items()):
        cat_size = sum(f.stat().st_size for f in files)
        total_size += cat_size
        print(f"  {category:12s}  {len(files):4d} files  {cat_size / 1024:.1f} KB")
    print("-" * 50)
    print(f"  {'TOTAL':12s}  {sum(len(v) for v in groups.values()):4d} files  {total_size / 1024:.1f} KB")


if __name__ == "__main__":
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    mode = sys.argv[2] if len(sys.argv) > 2 else "dry"

    summary_report(target)
    print()

    if mode == "run":
        organize(target, dry_run=False)
    else:
        organize(target, dry_run=True)
        print("\nTo actually move files, run: python file_organizer.py <dir> run")
```

**What you practised:** `pathlib` for all file operations, `shutil.move`, `defaultdict`, file categorization, dry-run safety pattern, conflict resolution with timestamps.

---


### Python Standard Library: Essential Modules

**Goal:** Know the most useful modules in Python's standard library so you never reinvent the wheel. This section covers `collections`, `itertools`, `functools`, `datetime`, `re`, `dataclasses`, `typing`, `contextlib`, `os`/`subprocess`, and `logging` in depth with practical examples.

---

#### `collections` — specialized container types

The `collections` module provides high-performance container data types that go beyond the built-in `list`, `dict`, `set`, and `tuple`.

**`Counter` — count occurrences of anything:**

```python
from collections import Counter

# Count word frequencies
words = "the cat sat on the mat the cat".split()
word_counts = Counter(words)
print(word_counts)
# Counter({'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1})

print(word_counts.most_common(2))    # [('the', 3), ('cat', 2)]
print(word_counts["the"])            # 3
print(word_counts["dog"])            # 0 (missing keys return 0, not KeyError)

# Count characters in a string
char_counts = Counter("mississippi")
print(char_counts)
# Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})

# Arithmetic with Counters
inventory = Counter(apples=5, oranges=3)
sold = Counter(apples=2, oranges=1)
remaining = inventory - sold
print(remaining)    # Counter({'apples': 3, 'oranges': 2})

# Find most common elements across multiple sources
all_words = Counter()
for sentence in ["I like cats", "I like dogs", "cats are great"]:
    all_words.update(sentence.split())
print(all_words.most_common(3))   # [('I', 2), ('like', 2), ('cats', 2)]
```

**`defaultdict` — dict with automatic default values:**

```python
from collections import defaultdict

# Group items by category
animals = [
    ("mammal", "cat"), ("mammal", "dog"), ("bird", "eagle"),
    ("reptile", "snake"), ("bird", "parrot"), ("mammal", "whale"),
]

# Without defaultdict:
groups_old = {}
for category, animal in animals:
    if category not in groups_old:
        groups_old[category] = []
    groups_old[category].append(animal)

# With defaultdict (much cleaner):
groups = defaultdict(list)
for category, animal in animals:
    groups[category].append(animal)

print(dict(groups))
# {'mammal': ['cat', 'dog', 'whale'], 'bird': ['eagle', 'parrot'], 'reptile': ['snake']}

# defaultdict with int (for counting)
letter_count = defaultdict(int)
for char in "hello world":
    letter_count[char] += 1
print(dict(letter_count))

# defaultdict with set (for unique collections)
user_tags = defaultdict(set)
user_tags["alice"].add("python")
user_tags["alice"].add("python")   # duplicate — set ignores it
user_tags["alice"].add("javascript")
print(dict(user_tags))   # {'alice': {'python', 'javascript'}}

# Nested defaultdict (for building trees)
tree = defaultdict(lambda: defaultdict(list))
tree["2024"]["January"].append("New Year")
tree["2024"]["March"].append("Spring")
print(dict(tree["2024"]))   # {'January': ["New Year"], 'March': ['Spring']}
```

**`deque` — double-ended queue (fast appends and pops on both ends):**

```python
from collections import deque

# Regular list: append/pop on right is O(1), but insert/pop on left is O(n)
# deque: O(1) for both ends!

dq = deque([1, 2, 3])
dq.append(4)          # add to right:  [1, 2, 3, 4]
dq.appendleft(0)      # add to left:   [0, 1, 2, 3, 4]
dq.pop()              # remove right:  4
dq.popleft()          # remove left:   0
print(list(dq))       # [1, 2, 3]

# Rotate
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)           # rotate right by 2
print(list(dq))        # [4, 5, 1, 2, 3]
dq.rotate(-2)          # rotate left by 2
print(list(dq))        # [1, 2, 3, 4, 5]

# Bounded deque (fixed max size — oldest items drop off)
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
    print(f"  Added {i}: {list(recent)}")
# Added 0: [0]
# Added 1: [0, 1]
# Added 2: [0, 1, 2]
# Added 3: [1, 2, 3]      <- 0 dropped off
# Added 4: [2, 3, 4]      <- 1 dropped off
```

**Use case: sliding window with deque:**

```python
from collections import deque

def sliding_window_max(nums, k):
    """Find the maximum in each sliding window of size k."""
    result = []
    window = deque()   # stores indices

    for i, num in enumerate(nums):
        # Remove indices outside the window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove smaller elements from the back
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(sliding_window_max(nums, 3))   # [3, 3, 5, 5, 6, 7]
```

**`namedtuple` — self-documenting tuples:**

```python
from collections import namedtuple

# Create a named tuple type
Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "red green blue alpha")

p = Point(3, 4)
print(p.x, p.y)           # 3 4 (access by name)
print(p[0], p[1])         # 3 4 (still works as a regular tuple)

# Immutable — can't reassign
# p.x = 10  # AttributeError!

# Create modified copy
p2 = p._replace(x=10)
print(p2)   # Point(x=10, y=4)

# Convert to dict
print(p._asdict())   # {'x': 3, 'y': 4}

# Practical example
Record = namedtuple("Record", ["name", "age", "email"])
records = [
    Record("Alice", 30, "alice@example.com"),
    Record("Bob", 25, "bob@example.com"),
]
for r in records:
    print(f"{r.name} is {r.age} years old")
```

**`ChainMap` — search through multiple dicts:**

```python
from collections import ChainMap

defaults = {"color": "blue", "size": "medium", "debug": False}
user_settings = {"color": "red"}
cli_flags = {"debug": True}

# ChainMap searches dicts in order (first match wins)
config = ChainMap(cli_flags, user_settings, defaults)
print(config["color"])    # red    (found in user_settings)
print(config["debug"])    # True   (found in cli_flags)
print(config["size"])     # medium (found in defaults)

# Useful for layered configuration systems
```

---

#### `itertools` — iterator building blocks

`itertools` provides memory-efficient tools for working with iterators. These are essential for processing large datasets.

**Infinite iterators:**

```python
from itertools import count, cycle, repeat

# count: infinite counter
for i in count(10, 2):    # start=10, step=2
    if i > 20:
        break
    print(i, end=" ")     # 10 12 14 16 18 20

# cycle: repeat a sequence forever
colors = cycle(["red", "green", "blue"])
for i in range(7):
    print(next(colors), end=" ")
# red green blue red green blue red

# repeat: repeat a value
list(repeat("hello", 3))   # ['hello', 'hello', 'hello']
```

**Combinatoric iterators:**

```python
from itertools import product, permutations, combinations, combinations_with_replacement

# product: cartesian product (like nested for loops)
print(list(product("AB", [1, 2])))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# All dice roll combinations
dice_rolls = list(product(range(1, 7), repeat=2))
print(f"2-dice outcomes: {len(dice_rolls)}")   # 36

# permutations: all orderings
print(list(permutations([1, 2, 3])))
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

# combinations: subsets of size k (order doesn't matter)
print(list(combinations([1, 2, 3, 4], 2)))
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# combinations_with_replacement: allow repeated elements
print(list(combinations_with_replacement("AB", 2)))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]
```

**Terminating iterators (the most useful ones):**

```python
from itertools import chain, islice, groupby, starmap, compress, takewhile, dropwhile, accumulate, zip_longest

# chain: flatten multiple iterables into one
list(chain([1, 2], [3, 4], [5]))           # [1, 2, 3, 4, 5]
list(chain.from_iterable([[1, 2], [3]]))   # [1, 2, 3]

# islice: slice an iterator (no negative indices)
from itertools import count
list(islice(count(0), 5, 10))    # [5, 6, 7, 8, 9]

# groupby: group consecutive elements (INPUT MUST BE SORTED by key!)
data = [
    ("Engineering", "Alice"), ("Engineering", "Bob"),
    ("Marketing", "Charlie"), ("Marketing", "Diana"),
    ("Engineering", "Eve"),
]
data.sort(key=lambda x: x[0])   # MUST sort first!
for dept, members in groupby(data, key=lambda x: x[0]):
    print(f"  {dept}: {[m[1] for m in members]}")
# Engineering: ['Alice', 'Bob', 'Eve']
# Marketing: ['Charlie', 'Diana']

# starmap: like map, but unpacks argument tuples
list(starmap(pow, [(2, 3), (3, 2), (10, 3)]))   # [8, 9, 1000]

# accumulate: running totals (or any binary function)
list(accumulate([1, 2, 3, 4, 5]))            # [1, 3, 6, 10, 15]
list(accumulate([2, 3, 4], lambda a, b: a * b))  # [2, 6, 24]

# takewhile / dropwhile
list(takewhile(lambda x: x < 5, [1, 3, 5, 2, 1]))    # [1, 3]
list(dropwhile(lambda x: x < 5, [1, 3, 5, 2, 1]))    # [5, 2, 1]

# compress: filter by selector
list(compress("ABCDEF", [1, 0, 1, 0, 1, 1]))   # ['A', 'C', 'E', 'F']

# zip_longest: zip with fill value for unequal lengths
list(zip_longest([1, 2, 3], "ab", fillvalue="-"))
# [(1, 'a'), (2, 'b'), (3, '-')]
```

---

#### `dataclasses` — structured data made easy

`dataclasses` (Python 3.7+) automatically generate `__init__`, `__repr__`, `__eq__`, and more from class annotations.

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import Optional

@dataclass
class User:
    name: str
    age: int
    email: str
    active: bool = True              # default value
    tags: list = field(default_factory=list)   # mutable default

# Auto-generated __init__, __repr__, __eq__
user = User("Alice", 30, "alice@example.com")
print(user)         # User(name='Alice', age=30, email='alice@example.com', active=True, tags=[])
print(user.name)    # Alice

# Equality based on values (not identity)
user2 = User("Alice", 30, "alice@example.com")
print(user == user2)   # True

# Convert to dict or tuple
print(asdict(user))    # {'name': 'Alice', 'age': 30, 'email': 'alice@example.com', ...}
print(astuple(user))   # ('Alice', 30, 'alice@example.com', True, [])
```

**Frozen (immutable) dataclasses:**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
# p.x = 10  # FrozenInstanceError!

# Can be used as dict keys and in sets (hashable)
points = {Point(0, 0): "origin", Point(1, 1): "diagonal"}
```

**Post-init processing and computed fields:**

```python
from dataclasses import dataclass, field
import math

@dataclass
class Circle:
    radius: float
    area: float = field(init=False)         # not in __init__
    circumference: float = field(init=False)

    def __post_init__(self):
        """Called after auto-generated __init__."""
        self.area = math.pi * self.radius ** 2
        self.circumference = 2 * math.pi * self.radius

c = Circle(5)
print(f"Area: {c.area:.2f}")           # 78.54
print(f"Circumference: {c.circumference:.2f}")  # 31.42
```

**Ordering (comparable dataclasses):**

```python
from dataclasses import dataclass

@dataclass(order=True)
class Priority:
    level: int
    name: str

tasks = [Priority(3, "Low"), Priority(1, "Critical"), Priority(2, "Normal")]
print(sorted(tasks))
# [Priority(level=1, name='Critical'), Priority(level=2, name='Normal'), Priority(level=3, name='Low')]
```

**Inheritance with dataclasses:**

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class BaseModel:
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    id: int = field(default=0)

@dataclass
class Product(BaseModel):
    name: str = ""
    price: float = 0.0
    in_stock: bool = True

p = Product(name="Widget", price=9.99)
print(p)   # Product(created_at='2024-...', id=0, name='Widget', price=9.99, in_stock=True)
```

---

#### `re` — regular expressions

Regular expressions match patterns in text. Python's `re` module is powerful but can be complex.

**Basic patterns:**

```python
import re

text = "Contact us at support@example.com or sales@example.com"

# Find all email addresses
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)
print(emails)   # ['support@example.com', 'sales@example.com']

# Search for first match
match = re.search(r'\d{3}-\d{4}', "Call 555-1234 or 555-5678")
if match:
    print(match.group())    # 555-1234
    print(match.start())    # 5
    print(match.end())      # 13
```

**Common pattern elements:**

| Pattern | Matches |
|---------|---------|
| `.` | Any character except newline |
| `\d` | Digit `[0-9]` |
| `\w` | Word character `[a-zA-Z0-9_]` |
| `\s` | Whitespace |
| `\b` | Word boundary |
| `^` / `$` | Start / end of string |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n,m}` | n to m repetitions |
| `[abc]` | Character class |
| `[^abc]` | Negated character class |
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |
| `(?P<name>...)` | Named group |

**Named groups and substitution:**

```python
import re

# Named groups for structured extraction
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, "Date: 2024-03-15")
if match:
    print(match.group("year"))    # 2024
    print(match.groupdict())      # {'year': '2024', 'month': '03', 'day': '15'}

# Substitution
text = "Hello World! Hello Python!"
result = re.sub(r'Hello', 'Hi', text)
print(result)   # Hi World! Hi Python!

# Substitution with function
def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double_number, "I have 3 cats and 5 dogs")
print(result)   # I have 6 cats and 10 dogs
```

**Compile for reuse (faster with repeated use):**

```python
import re

# Compile once, use many times
email_pattern = re.compile(r'^[\w.+-]+@[\w-]+\.[\w.]+$')

emails_to_check = ["user@example.com", "invalid@@email", "test@test.co.uk"]
for email in emails_to_check:
    valid = "VALID" if email_pattern.match(email) else "INVALID"
    print(f"  {email}: {valid}")
```

---

#### `os` and `subprocess` — system interaction

```python
import os
import subprocess

# Environment variables
print(os.environ.get("HOME", "N/A"))
print(os.environ.get("PATH", "N/A"))

# Current process info
print(os.getpid())        # process ID
print(os.cpu_count())     # number of CPU cores

# Run external commands with subprocess
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,     # capture stdout and stderr
    text=True,               # return strings instead of bytes
    timeout=10               # max seconds to wait
)
print(result.stdout)         # Python 3.14.x
print(result.returncode)     # 0 = success

# Check command output
try:
    output = subprocess.check_output(["git", "status", "--short"], text=True)
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
except FileNotFoundError:
    print("git is not installed")
```

---

#### `logging` — structured, configurable logging

Logging is far superior to `print()` for production code. It supports levels, formatting, multiple outputs, and can be turned on/off without code changes.

**Basic setup:**

```python
import logging

# Configure once at application startup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a logger for this module
logger = logging.getLogger(__name__)

logger.debug("Detailed information for debugging")
logger.info("General information about program flow")
logger.warning("Something unexpected but not yet an error")
logger.error("Something failed")
logger.critical("Application cannot continue")
```

**Logging levels (from least to most severe):**

| Level | Value | Use case |
|-------|-------|----------|
| `DEBUG` | 10 | Detailed diagnostic info |
| `INFO` | 20 | Confirmation things work as expected |
| `WARNING` | 30 | Something unexpected happened |
| `ERROR` | 40 | A function failed |
| `CRITICAL` | 50 | Application cannot continue |

**Logging to files with rotation:**

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file="app.log", level=logging.INFO):
    """Configure logging with both console and file output."""
    logger = logging.getLogger()
    logger.setLevel(level)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        "[%(levelname)s] %(message)s"
    ))

    # File handler with rotation (max 5 MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
    ))

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger
```

**Logging exceptions:**

```python
import logging

logger = logging.getLogger(__name__)

def risky_operation():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("Division failed")   # includes full traceback
        # or: logger.error("Division failed", exc_info=True)
```

---

#### `contextlib` — context manager utilities

```python
from contextlib import contextmanager, suppress, redirect_stdout
import io

# suppress: silently ignore specific exceptions
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("might_not_exist.txt")
# No error even if file doesn't exist

# redirect_stdout: capture print output
f = io.StringIO()
with redirect_stdout(f):
    print("This goes to the buffer")
captured = f.getvalue()
print(f"Captured: {captured!r}")

# closing: ensure .close() is called
from contextlib import closing
from urllib.request import urlopen

# with closing(urlopen("https://python.org")) as page:
#     html = page.read()

# ExitStack: manage a dynamic number of context managers
from contextlib import ExitStack

def open_multiple_files(filenames):
    with ExitStack() as stack:
        files = [stack.enter_context(open(fn)) for fn in filenames]
        # all files are open here
        for f in files:
            print(f.name)
    # all files automatically closed here
```

---

#### Mini-project 1: Log analyzer

Build a tool that parses log files, extracts patterns, and generates reports.

```python
"""
log_analyzer.py — Parse and analyze log files.

Demonstrates:
- re (regular expressions) for parsing
- Counter and defaultdict for aggregation
- dataclasses for structured data
- datetime for time parsing
- Generator pipeline for memory efficiency
"""
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    source: str
    message: str

@dataclass
class LogReport:
    total_entries: int = 0
    level_counts: dict = field(default_factory=dict)
    error_messages: list = field(default_factory=list)
    entries_by_hour: dict = field(default_factory=dict)
    top_sources: list = field(default_factory=list)
    time_range: tuple = field(default=None)

# Standard log format: 2024-01-15 10:30:45 [ERROR] myapp.views: Something broke
LOG_PATTERN = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
    r'(?P<time>\d{2}:\d{2}:\d{2})\s+'
    r'\[(?P<level>\w+)\]\s+'
    r'(?P<source>[\w.]+):\s+'
    r'(?P<message>.+)'
)

def parse_line(line):
    """Parse a single log line into a LogEntry."""
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    d = match.groupdict()
    return LogEntry(
        timestamp=datetime.strptime(f"{d['date']} {d['time']}", "%Y-%m-%d %H:%M:%S"),
        level=d["level"],
        source=d["source"],
        message=d["message"],
    )

def parse_log_file(filepath):
    """Generator: yield LogEntry objects from a log file."""
    for line in Path(filepath).read_text(encoding="utf-8").splitlines():
        entry = parse_line(line)
        if entry:
            yield entry

def analyze(entries):
    """Analyze a stream of log entries and return a report."""
    report = LogReport()
    level_counter = Counter()
    source_counter = Counter()
    hourly = defaultdict(int)
    timestamps = []

    for entry in entries:
        report.total_entries += 1
        level_counter[entry.level] += 1
        source_counter[entry.source] += 1
        hourly[entry.timestamp.hour] += 1
        timestamps.append(entry.timestamp)

        if entry.level in ("ERROR", "CRITICAL"):
            report.error_messages.append(
                f"[{entry.timestamp}] {entry.source}: {entry.message}"
            )

    report.level_counts = dict(level_counter.most_common())
    report.top_sources = source_counter.most_common(5)
    report.entries_by_hour = dict(sorted(hourly.items()))
    if timestamps:
        report.time_range = (min(timestamps), max(timestamps))

    return report

def print_report(report):
    """Display the analysis report."""
    print("=" * 60)
    print("LOG ANALYSIS REPORT")
    print("=" * 60)

    if report.time_range:
        start, end = report.time_range
        print(f"Time range: {start} to {end}")

    print(f"Total entries: {report.total_entries}")
    print(f"\nLevel distribution:")
    for level, count in report.level_counts.items():
        bar = "#" * (count * 40 // report.total_entries)
        print(f"  {level:10s} {count:5d}  {bar}")

    print(f"\nTop sources:")
    for source, count in report.top_sources:
        print(f"  {source:20s} {count:5d}")

    print(f"\nActivity by hour:")
    for hour, count in report.entries_by_hour.items():
        bar = "#" * (count * 30 // max(report.entries_by_hour.values()))
        print(f"  {hour:02d}:00  {count:4d}  {bar}")

    if report.error_messages:
        print(f"\nErrors and critical issues ({len(report.error_messages)}):")
        for msg in report.error_messages[:10]:
            print(f"  {msg}")
        if len(report.error_messages) > 10:
            print(f"  ... and {len(report.error_messages) - 10} more")


# --- Generate sample log data for demo ---

def generate_sample_log(filepath, num_entries=200):
    """Generate a realistic sample log file."""
    import random
    levels = ["DEBUG"] * 30 + ["INFO"] * 50 + ["WARNING"] * 12 + ["ERROR"] * 6 + ["CRITICAL"] * 2
    sources = ["app.views", "app.models", "app.auth", "db.pool", "api.client", "cache.redis"]
    messages = {
        "DEBUG": ["Processing request", "Cache lookup", "Query executed in 0.003s"],
        "INFO": ["User logged in", "Request completed", "Page rendered", "Task started"],
        "WARNING": ["Slow query detected", "Cache miss rate high", "Retry attempt 2"],
        "ERROR": ["Connection refused", "Timeout after 30s", "Invalid input data"],
        "CRITICAL": ["Database connection lost", "Out of memory"],
    }

    lines = []
    base = datetime(2024, 1, 15, 8, 0, 0)
    for i in range(num_entries):
        level = random.choice(levels)
        source = random.choice(sources)
        msg = random.choice(messages[level])
        ts = base.replace(
            hour=random.randint(8, 22),
            minute=random.randint(0, 59),
            second=random.randint(0, 59),
        )
        lines.append(f"{ts.strftime('%Y-%m-%d %H:%M:%S')} [{level}] {source}: {msg}")

    lines.sort()   # sort by timestamp
    Path(filepath).write_text("\n".join(lines), encoding="utf-8")
    return num_entries


if __name__ == "__main__":
    log_file = "sample.log"
    print(f"Generating {log_file}...")
    n = generate_sample_log(log_file)
    print(f"Generated {n} log entries\n")

    entries = parse_log_file(log_file)
    report = analyze(entries)
    print_report(report)

    Path(log_file).unlink()
```

**What you practised:** Regular expressions, `Counter`, `defaultdict`, `dataclasses`, `datetime`, generators, report formatting.

---

#### Mini-project 2: Data pipeline with `itertools`

Build a composable data processing pipeline using itertools to analyze sales data.

```python
"""
sales_pipeline.py — Data pipeline using itertools and collections.

Demonstrates:
- itertools (groupby, chain, starmap, accumulate)
- collections (Counter, defaultdict, namedtuple)
- Generator-based lazy processing
- Data aggregation patterns
"""
from itertools import groupby, chain, accumulate, islice
from collections import Counter, defaultdict, namedtuple
from operator import attrgetter
import csv
import io

# --- Data types ---
Sale = namedtuple("Sale", ["date", "product", "category", "quantity", "price"])

# --- Sample data ---
SAMPLE_CSV = """date,product,category,quantity,price
2024-01-10,Widget A,Electronics,5,29.99
2024-01-10,Widget B,Electronics,3,49.99
2024-01-10,Gadget X,Home,2,15.99
2024-01-11,Widget A,Electronics,8,29.99
2024-01-11,Book Y,Books,12,9.99
2024-01-11,Gadget X,Home,4,15.99
2024-01-12,Widget B,Electronics,6,49.99
2024-01-12,Book Y,Books,20,9.99
2024-01-12,Book Z,Books,7,14.99
2024-01-13,Widget A,Electronics,3,29.99
2024-01-13,Gadget X,Home,1,15.99
2024-01-13,Book Y,Books,15,9.99
2024-01-14,Widget A,Electronics,10,29.99
2024-01-14,Widget B,Electronics,4,49.99
2024-01-14,Gadget X,Home,6,15.99
2024-01-14,Book Z,Books,3,14.99
"""

def parse_sales(csv_text):
    """Parse CSV text into Sale namedtuples."""
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    for row in reader:
        yield Sale(
            date=row["date"],
            product=row["product"],
            category=row["category"],
            quantity=int(row["quantity"]),
            price=float(row["price"]),
        )

# --- Pipeline stages ---

def add_revenue(sales):
    """Yield (sale, revenue) pairs."""
    for sale in sales:
        revenue = sale.quantity * sale.price
        yield sale, round(revenue, 2)

def filter_min_revenue(sale_revenues, min_rev=50.0):
    """Keep only sales with revenue >= min_rev."""
    for sale, rev in sale_revenues:
        if rev >= min_rev:
            yield sale, rev

# --- Analysis functions ---

def revenue_by_category(sales):
    """Calculate total revenue per category."""
    all_sales = list(sales)   # need to iterate multiple times
    totals = defaultdict(float)
    for sale in all_sales:
        totals[sale.category] += sale.quantity * sale.price
    return dict(sorted(totals.items(), key=lambda x: -x[1]))

def daily_running_total(sales):
    """Calculate running total of revenue by day."""
    all_sales = sorted(sales, key=attrgetter("date"))
    daily = defaultdict(float)
    for sale in all_sales:
        daily[sale.date] += sale.quantity * sale.price

    dates = sorted(daily.keys())
    amounts = [daily[d] for d in dates]
    running = list(accumulate(amounts))

    return list(zip(dates, amounts, running))

def top_products(sales, n=3):
    """Find the top N products by total quantity sold."""
    quantities = Counter()
    for sale in sales:
        quantities[sale.product] += sale.quantity
    return quantities.most_common(n)

def category_breakdown(sales):
    """Group sales by category and show stats."""
    all_sales = sorted(sales, key=attrgetter("category"))
    result = {}
    for category, group in groupby(all_sales, key=attrgetter("category")):
        items = list(group)
        total_qty = sum(s.quantity for s in items)
        total_rev = sum(s.quantity * s.price for s in items)
        unique_products = len(set(s.product for s in items))
        result[category] = {
            "total_quantity": total_qty,
            "total_revenue": round(total_rev, 2),
            "unique_products": unique_products,
            "avg_order_value": round(total_rev / len(items), 2),
        }
    return result


if __name__ == "__main__":
    # Parse the data
    sales = list(parse_sales(SAMPLE_CSV))
    print(f"Total sales records: {len(sales)}")

    # Revenue by category
    print("\n--- Revenue by Category ---")
    for cat, rev in revenue_by_category(sales).items():
        print(f"  {cat:15s}  ${rev:>8.2f}")

    # Top products
    print("\n--- Top Products (by quantity) ---")
    for product, qty in top_products(sales):
        print(f"  {product:15s}  {qty} units")

    # Daily running total
    print("\n--- Daily Revenue & Running Total ---")
    for date, daily, running in daily_running_total(sales):
        print(f"  {date}  daily: ${daily:>7.2f}  running: ${running:>8.2f}")

    # Category breakdown
    print("\n--- Category Breakdown ---")
    for cat, stats in category_breakdown(sales).items():
        print(f"  {cat}:")
        for key, val in stats.items():
            label = key.replace("_", " ").title()
            print(f"    {label}: {val}")

    # Pipeline demo: filter high-value sales
    print("\n--- High-Value Sales (revenue >= $100) ---")
    pipeline = filter_min_revenue(add_revenue(iter(sales)), min_rev=100.0)
    for sale, rev in pipeline:
        print(f"  {sale.date} {sale.product:12s} qty={sale.quantity} rev=${rev}")
```

**What you practised:** `namedtuple`, `groupby`, `accumulate`, `Counter`, `defaultdict`, `attrgetter`, generator pipelines, CSV parsing, data aggregation.

---

## Advanced Track — Professional Python

The advanced track covers topics that separate good Python code from great Python code: object‑oriented design, type safety, concurrency, and performance.


### Object-Oriented Programming Mastery

**Goal:** Go beyond basic classes. Master inheritance patterns, the Method Resolution Order (MRO), abstract base classes, protocols, descriptors, slots, metaclasses, and advanced dataclass usage.

---

#### Inheritance — single, multiple, and the MRO

**Single inheritance** is straightforward:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

rex = Dog("Rex")
print(rex.speak())     # Rex says Woof
print(rex.fetch("ball"))  # Rex fetches the ball!
```

**Multiple inheritance** — a class can inherit from more than one parent:

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")

donald = Duck("Donald")
print(donald.speak())   # Donald says Quack
print(donald.fly())     # Donald is flying!
print(donald.swim())    # Donald is swimming!
```

**Method Resolution Order (MRO)** — when multiple parents define the same method, Python uses the C3 linearization algorithm to determine which one to call:

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):      # inherits from both B and C
    pass

d = D()
print(d.who())       # B  (B comes before C in the MRO)
print(D.__mro__)     # (D, B, C, A, object)
# D -> B -> C -> A -> object

# You can also use:
print(D.mro())
```

**`super()` in multiple inheritance** — `super()` follows the MRO, not just the direct parent:

```python
class Base:
    def __init__(self):
        print("Base.__init__")

class Left(Base):
    def __init__(self):
        print("Left.__init__")
        super().__init__()      # calls Right.__init__ (MRO!), not Base

class Right(Base):
    def __init__(self):
        print("Right.__init__")
        super().__init__()      # calls Base.__init__

class Child(Left, Right):
    def __init__(self):
        print("Child.__init__")
        super().__init__()

Child()
# Output:
# Child.__init__
# Left.__init__
# Right.__init__    <-- super() in Left calls Right, not Base!
# Base.__init__
```

---

#### Abstract Base Classes (ABCs)

ABCs define an interface that subclasses **must** implement. They can't be instantiated directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass

    def describe(self):
        """Concrete method — shared by all subclasses."""
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()   # TypeError: Can't instantiate abstract class
c = Circle(5)
r = Rectangle(3, 4)
print(c.describe())    # Circle: area=78.54, perimeter=31.42
print(r.describe())    # Rectangle: area=12.00, perimeter=14.00

# Check if something implements the interface
print(isinstance(c, Shape))      # True
print(isinstance("hello", Shape))  # False
```

**Abstract properties:**

```python
from abc import ABC, abstractmethod

class DatabaseBackend(ABC):
    @property
    @abstractmethod
    def connection_string(self):
        """Must return the database connection string."""
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

class SQLiteBackend(DatabaseBackend):
    def __init__(self, db_path):
        self._db_path = db_path

    @property
    def connection_string(self):
        return f"sqlite:///{self._db_path}"

    def connect(self):
        import sqlite3
        return sqlite3.connect(self._db_path)

    def execute(self, query):
        conn = self.connect()
        return conn.execute(query)
```

---

#### Protocols — structural subtyping (duck typing made formal)

Protocols (Python 3.8+) define interfaces based on **structure** rather than inheritance. If an object has the right methods, it satisfies the protocol — no need to explicitly inherit.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self, canvas: str) -> None:
        ...

class Circle:
    def draw(self, canvas: str) -> None:
        print(f"Drawing circle on {canvas}")

class Square:
    def draw(self, canvas: str) -> None:
        print(f"Drawing square on {canvas}")

class Text:
    # No draw method — doesn't satisfy Drawable!
    def render(self, output: str) -> None:
        print(f"Rendering text to {output}")

def render_all(items: list[Drawable], canvas: str) -> None:
    for item in items:
        item.draw(canvas)

# Both work even though they don't inherit from Drawable
render_all([Circle(), Square()], "main_canvas")

# Runtime check (requires @runtime_checkable)
print(isinstance(Circle(), Drawable))   # True
print(isinstance(Text(), Drawable))     # False
```

**Protocol vs ABC:**
| Feature | ABC | Protocol |
|---------|-----|----------|
| Requires inheritance | Yes | No |
| Runtime `isinstance` check | Always | Only with `@runtime_checkable` |
| Works with third-party types | No (must subclass) | Yes (structural) |
| Best for | Your own class hierarchy | Type checking, duck typing |

---

#### Descriptors — controlling attribute access

Descriptors are the mechanism behind `@property`, `@classmethod`, `@staticmethod`, and `__slots__`. They're objects that define `__get__`, `__set__`, and/or `__delete__`.

```python
class Validated:
    """A descriptor that validates values on assignment."""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name             # automatically set by Python
        self.storage_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self              # accessed from the class itself
        return getattr(obj, self.storage_name, None)

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}, got {value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}, got {value}")
        setattr(obj, self.storage_name, value)

class Product:
    price = Validated(min_value=0)
    quantity = Validated(min_value=0, max_value=10000)
    rating = Validated(min_value=0, max_value=5)

    def __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price          # calls Validated.__set__
        self.quantity = quantity
        self.rating = rating

p = Product("Widget", 9.99, 100, 4.5)
print(p.price)                   # 9.99
# p.price = -5                   # ValueError: price must be >= 0, got -5
# p.rating = 6                   # ValueError: rating must be <= 5, got 6
```

---

#### `__slots__` — memory-efficient objects

By default, Python stores instance attributes in a per-object `__dict__` (dictionary). `__slots__` tells Python to use a fixed-size structure instead, saving memory.

```python
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ("x", "y")   # no __dict__ will be created

    def __init__(self, x, y):
        self.x = x
        self.y = y

r = RegularPoint(1, 2)
s = SlottedPoint(1, 2)

import sys
print(sys.getsizeof(r.__dict__))   # ~104 bytes for the dict alone
# s.__dict__                        # AttributeError: no __dict__!

# You can't add arbitrary attributes to slotted objects
# s.z = 3   # AttributeError
r.z = 3     # works fine with regular class
```

**When to use `__slots__`:**
- Thousands or millions of instances (significant memory savings)
- You know all attributes at class definition time
- You don't need dynamic attribute assignment

**`__slots__` with inheritance:**

```python
class Base:
    __slots__ = ("x",)

class Child(Base):
    __slots__ = ("y",)     # inherits 'x' from Base, adds 'y'

c = Child()
c.x = 1
c.y = 2
# c.z = 3   # AttributeError
```

---

#### Metaclasses — classes that create classes

A **metaclass** is a class whose instances are classes. Just as a class defines how instances behave, a metaclass defines how classes behave.

```python
class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, url="sqlite:///app.db"):
        self.url = url
        print(f"Connecting to {url}")

# Only creates one instance
db1 = Database()          # Connecting to sqlite:///app.db
db2 = Database()          # no output — reuses existing
print(db1 is db2)         # True
```

**Metaclass for automatic registration:**

```python
class PluginRegistry(type):
    """Auto-register subclasses in a global registry."""
    plugins = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:   # don't register the base class itself
            PluginRegistry.plugins[name] = cls
        return cls

class BasePlugin(metaclass=PluginRegistry):
    def run(self):
        raise NotImplementedError

class PDFExporter(BasePlugin):
    def run(self):
        return "Exporting to PDF"

class CSVExporter(BasePlugin):
    def run(self):
        return "Exporting to CSV"

print(PluginRegistry.plugins)
# {'PDFExporter': <class 'PDFExporter'>, 'CSVExporter': <class 'CSVExporter'>}

# Instantiate by name
exporter = PluginRegistry.plugins["PDFExporter"]()
print(exporter.run())   # Exporting to PDF
```

> **Note:** Metaclasses are powerful but rarely needed. Prefer decorators, ABCs, or `__init_subclass__` for most use cases.

**`__init_subclass__` — the simpler alternative (Python 3.6+):**

```python
class Plugin:
    _registry = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        name = plugin_name or cls.__name__
        Plugin._registry[name] = cls

class JSONExporter(Plugin, plugin_name="json"):
    def run(self):
        return "Exporting JSON"

class XMLExporter(Plugin, plugin_name="xml"):
    def run(self):
        return "Exporting XML"

print(Plugin._registry)
# {'json': <class 'JSONExporter'>, 'xml': <class 'XMLExporter'>}
```

---

#### Dunder methods deep dive

Python uses "dunder" (double-underscore) methods to make custom classes work with built-in operations.

**Arithmetic operators:**

```python
class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):    # handles: 3 * vector
        return self.__mul__(scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __iter__(self):
        yield self.x
        yield self.y

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)       # Vector(4, 6)
print(v1 - v2)       # Vector(2, 2)
print(v1 * 3)        # Vector(9, 12)
print(3 * v1)        # Vector(9, 12)  -- uses __rmul__
print(abs(v1))        # 5.0
print(list(v1))       # [3, 4]  -- uses __iter__
```

**Container protocol (make your class behave like a list/dict):**

```python
class Row:
    """A dict-like row that also supports attribute access."""

    def __init__(self, **data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, key):
        return key in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        items = ", ".join(f"{k}={v!r}" for k, v in self._data.items())
        return f"Row({items})"

    def __getattr__(self, name):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"No attribute '{name}'")

row = Row(name="Alice", age=30, email="alice@example.com")
print(row["name"])      # Alice   (uses __getitem__)
print(row.age)          # 30      (uses __getattr__)
print(len(row))         # 3       (uses __len__)
print("email" in row)   # True    (uses __contains__)
for key in row:         #         (uses __iter__)
    print(f"  {key}: {row[key]}")
```

---

#### Advanced dataclass patterns

**`dataclass` with validators and custom `__post_init__`:**

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Employee:
    """Employee with validation and computed fields."""
    name: str
    email: str
    department: str
    salary: float
    hire_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    employee_id: Optional[str] = field(default=None)

    def __post_init__(self):
        # Validation
        if not self.name.strip():
            raise ValueError("name cannot be empty")
        if "@" not in self.email:
            raise ValueError(f"Invalid email: {self.email}")
        if self.salary < 0:
            raise ValueError(f"Salary cannot be negative: {self.salary}")

        # Normalize
        self.name = self.name.strip().title()
        self.email = self.email.strip().lower()
        self.department = self.department.strip().upper()

        # Generate ID if not provided
        if self.employee_id is None:
            import hashlib
            hash_input = f"{self.name}{self.email}".encode()
            self.employee_id = hashlib.md5(hash_input).hexdigest()[:8]

    @property
    def annual_salary(self):
        return self.salary * 12

emp = Employee("  alice johnson  ", "Alice@Example.COM", "engineering", 5000)
print(emp)
# Employee(name='Alice Johnson', email='alice@example.com', department='ENGINEERING', ...)
print(emp.annual_salary)   # 60000
```

**Dataclass with `__slots__` (Python 3.10+):**

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Point3D:
    x: float
    y: float
    z: float

# Memory-efficient AND has all dataclass features
p = Point3D(1.0, 2.0, 3.0)
print(p)    # Point3D(x=1.0, y=2.0, z=3.0)
```

---

#### Mini-project 1: Object-relational mapper (ORM)

Build a simple ORM that maps Python classes to SQLite tables.

```python
"""
mini_orm.py — A simple ORM using descriptors, metaclasses, and dataclasses.

Demonstrates:
- Descriptors for column definitions
- Metaclass for auto-table creation
- Context managers for database connections
- ABC for base model
"""
import sqlite3
from contextlib import contextmanager

DB_PATH = ":memory:"   # in-memory database for demo

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

class Column:
    """Descriptor representing a database column."""
    def __init__(self, col_type="TEXT", primary_key=False, nullable=True):
        self.col_type = col_type
        self.primary_key = primary_key
        self.nullable = nullable

    def __set_name__(self, owner, name):
        self.name = name
        self.storage = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage, None)

    def __set__(self, obj, value):
        setattr(obj, self.storage, value)

    def sql_definition(self):
        parts = [self.name, self.col_type]
        if self.primary_key:
            parts.append("PRIMARY KEY AUTOINCREMENT")
        if not self.nullable and not self.primary_key:
            parts.append("NOT NULL")
        return " ".join(parts)

class ModelMeta(type):
    """Metaclass that auto-creates database tables."""
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        # Collect columns
        columns = {}
        for attr_name, attr_val in namespace.items():
            if isinstance(attr_val, Column):
                columns[attr_name] = attr_val
        cls._columns = columns

        # Set table name
        cls._table_name = namespace.get("_table_name", name.lower() + "s")

        # Create table
        if columns:   # skip base class
            col_defs = ", ".join(c.sql_definition() for c in columns.values())
            sql = f"CREATE TABLE IF NOT EXISTS {cls._table_name} ({col_defs})"
            with get_connection() as conn:
                conn.execute(sql)

        return cls

class Model(metaclass=ModelMeta):
    """Base model with CRUD operations."""

    def save(self):
        """Insert or update this record."""
        cols = [n for n in self._columns if not self._columns[n].primary_key]
        vals = [getattr(self, n) for n in cols]
        placeholders = ", ".join("?" * len(cols))
        col_names = ", ".join(cols)

        with get_connection() as conn:
            cursor = conn.execute(
                f"INSERT INTO {self._table_name} ({col_names}) VALUES ({placeholders})",
                vals
            )
            # Set the auto-generated ID
            for name, col in self._columns.items():
                if col.primary_key:
                    setattr(self, name, cursor.lastrowid)
        return self

    @classmethod
    def find_all(cls):
        """Return all records."""
        with get_connection() as conn:
            rows = conn.execute(f"SELECT * FROM {cls._table_name}").fetchall()
            results = []
            for row in rows:
                obj = cls.__new__(cls)
                for name in cls._columns:
                    setattr(obj, name, row[name])
                results.append(obj)
            return results

    @classmethod
    def find_by_id(cls, record_id):
        """Find a single record by primary key."""
        pk = next(n for n, c in cls._columns.items() if c.primary_key)
        with get_connection() as conn:
            row = conn.execute(
                f"SELECT * FROM {cls._table_name} WHERE {pk} = ?",
                (record_id,)
            ).fetchone()
            if not row:
                return None
            obj = cls.__new__(cls)
            for name in cls._columns:
                setattr(obj, name, row[name])
            return obj

    def __repr__(self):
        attrs = ", ".join(f"{n}={getattr(self, n)!r}" for n in self._columns)
        return f"{self.__class__.__name__}({attrs})"


# --- Define models ---

class User(Model):
    _table_name = "users"
    id = Column("INTEGER", primary_key=True)
    name = Column("TEXT", nullable=False)
    email = Column("TEXT", nullable=False)
    age = Column("INTEGER")

class Post(Model):
    _table_name = "posts"
    id = Column("INTEGER", primary_key=True)
    title = Column("TEXT", nullable=False)
    body = Column("TEXT")
    author_id = Column("INTEGER")


# --- Demo ---
if __name__ == "__main__":
    # Create users
    alice = User()
    alice.name = "Alice"
    alice.email = "alice@example.com"
    alice.age = 30
    alice.save()

    bob = User()
    bob.name = "Bob"
    bob.email = "bob@example.com"
    bob.age = 25
    bob.save()

    # Create posts
    post = Post()
    post.title = "Hello World"
    post.body = "This is my first post"
    post.author_id = alice.id
    post.save()

    # Query
    print("All users:")
    for u in User.find_all():
        print(f"  {u}")

    print(f"\nFind user 1: {User.find_by_id(1)}")

    print("\nAll posts:")
    for p in Post.find_all():
        print(f"  {p}")
```

**What you practised:** Descriptors, metaclasses, context managers, SQLite, `__repr__`, classmethod/staticmethod patterns.

---

#### Mini-project 2: Event system with observer pattern

Build a publish-subscribe event system using OOP principles.

```python
"""
event_system.py — Publish-subscribe event system.

Demonstrates:
- Observer pattern
- Weak references
- Decorators with classes
- Type hints with Protocol
- dataclasses for event objects
"""
from dataclasses import dataclass, field
from typing import Any, Callable
from datetime import datetime
import functools
import weakref

@dataclass
class Event:
    """Base event with metadata."""
    name: str
    data: Any = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class EventBus:
    """Central event dispatcher — the core of the observer pattern."""

    def __init__(self):
        self._handlers: dict[str, list[Callable]] = {}
        self._history: list[Event] = []

    def on(self, event_name):
        """Decorator to register an event handler."""
        def decorator(func):
            self.subscribe(event_name, func)
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def subscribe(self, event_name, handler):
        """Register a handler for an event."""
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)

    def unsubscribe(self, event_name, handler):
        """Remove a handler."""
        if event_name in self._handlers:
            self._handlers[event_name] = [
                h for h in self._handlers[event_name] if h is not handler
            ]

    def emit(self, event_name, data=None):
        """Emit an event, calling all registered handlers."""
        event = Event(name=event_name, data=data)
        self._history.append(event)

        handlers = self._handlers.get(event_name, [])
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                print(f"Handler error for '{event_name}': {e}")

        # Also trigger wildcard handlers
        for handler in self._handlers.get("*", []):
            try:
                handler(event)
            except Exception as e:
                print(f"Wildcard handler error: {e}")

    def get_history(self, event_name=None, limit=None):
        """Get event history, optionally filtered."""
        events = self._history
        if event_name:
            events = [e for e in events if e.name == event_name]
        if limit:
            events = events[-limit:]
        return events


# --- Create a global event bus ---
bus = EventBus()

# --- Register handlers using decorator ---

@bus.on("user.login")
def handle_login(event):
    print(f"  [Auth] User logged in: {event.data['username']}")

@bus.on("user.login")
def track_login(event):
    print(f"  [Analytics] Login tracked at {event.timestamp}")

@bus.on("user.logout")
def handle_logout(event):
    print(f"  [Auth] User logged out: {event.data['username']}")

@bus.on("order.placed")
def process_order(event):
    order = event.data
    total = sum(item['price'] * item['qty'] for item in order['items'])
    print(f"  [Orders] New order #{order['id']} — total: ${total:.2f}")

@bus.on("order.placed")
def send_confirmation(event):
    print(f"  [Email] Confirmation sent for order #{event.data['id']}")

@bus.on("*")
def global_logger(event):
    print(f"  [Log] Event: {event.name}")


# --- Demo ---
if __name__ == "__main__":
    print("=== User Login ===")
    bus.emit("user.login", {"username": "alice", "ip": "192.168.1.1"})

    print("\n=== Place Order ===")
    bus.emit("order.placed", {
        "id": 1001,
        "user": "alice",
        "items": [
            {"name": "Widget", "price": 29.99, "qty": 2},
            {"name": "Gadget", "price": 49.99, "qty": 1},
        ]
    })

    print("\n=== User Logout ===")
    bus.emit("user.logout", {"username": "alice"})

    print(f"\n=== Event History ({len(bus.get_history())} events) ===")
    for event in bus.get_history():
        print(f"  {event.timestamp} | {event.name}")
```

**What you practised:** Observer pattern, decorator-based registration, dataclasses for events, wildcard subscriptions, error-resilient dispatch.

---


### Type Hints, Generics & Static Analysis

**Goal:** Write self-documenting code with type annotations. Use `mypy` for static analysis. Understand generics, overloads, `TypeVar`, `ParamSpec`, and Python 3.12+ type syntax.

---

#### Why type hints?

Type hints make your code:
- **Self-documenting** — readers know what types to pass and expect
- **Safer** — static analysis catches bugs before runtime
- **IDE-friendly** — better autocomplete, refactoring, and navigation

Type hints are **optional** and **not enforced at runtime**. They're metadata for tools.

```python
# Without type hints — what does this function accept? Return?
def process(data, count):
    ...

# With type hints — completely clear
def process(data: list[str], count: int) -> dict[str, int]:
    ...
```

---

#### Basic type annotations

```python
# Variables
name: str = "Alice"
age: int = 30
height: float = 5.7
active: bool = True

# Function signatures
def greet(name: str, loud: bool = False) -> str:
    msg = f"Hello, {name}!"
    return msg.upper() if loud else msg

# None return type
def log_message(msg: str) -> None:
    print(f"[LOG] {msg}")
```

**Built-in generic types (Python 3.9+):**

```python
# Modern syntax (3.9+) — use built-in types directly
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95, "Bob": 87}
coordinates: tuple[float, float] = (3.14, 2.71)
unique_ids: set[int] = {1, 2, 3}

# Variable-length tuple
values: tuple[int, ...] = (1, 2, 3, 4, 5)

# Nested types
user_groups: dict[str, list[str]] = {
    "admins": ["alice", "bob"],
    "users": ["charlie", "diana"],
}
```

**For Python 3.8 and earlier:**

```python
from typing import List, Dict, Tuple, Set

names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 95}
# Python 3.9+ lets you use list[str], dict[str, int] directly
```

---

#### `Optional`, `Union`, and the `|` syntax

```python
from typing import Optional, Union

# Optional[X] is shorthand for Union[X, None]
def find_user(user_id: int) -> Optional[dict]:
    """Returns user dict or None if not found."""
    ...

# Union: can be one of multiple types
def process(value: Union[str, int]) -> str:
    return str(value)

# Python 3.10+ pipe syntax (recommended)
def find_user_modern(user_id: int) -> dict | None:
    ...

def process_modern(value: str | int) -> str:
    return str(value)
```

---

#### `TypeVar` — generic type parameters

`TypeVar` lets you write functions that preserve type relationships.

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    """Return the first item. Type is preserved."""
    return items[0]

# mypy knows the return type:
name = first(["Alice", "Bob"])    # type: str
number = first([1, 2, 3])         # type: int
```

**Bounded TypeVar — restrict allowed types:**

```python
from typing import TypeVar

# T must be str or a subclass of str
T = TypeVar("T", bound=str)

def to_upper(value: T) -> T:
    return value.upper()

to_upper("hello")     # OK
# to_upper(42)         # mypy error: int is not a subclass of str
```

**Constrained TypeVar:**

```python
from typing import TypeVar

# T must be exactly int or float
Number = TypeVar("Number", int, float)

def double(x: Number) -> Number:
    return x * 2

double(5)      # OK, returns int
double(3.14)   # OK, returns float
# double("hi")  # mypy error
```

---

#### Python 3.12+ type parameter syntax

Python 3.12 introduced a new, cleaner syntax for generics:

```python
# Old style (all Python versions)
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]

# New style (Python 3.12+) — no TypeVar needed!
def first[T](items: list[T]) -> T:
    return items[0]

# Generic classes
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Type aliases (3.12+)
type Vector = list[float]
type Matrix = list[Vector]
type UserID = int
type Callback[T] = Callable[[T], None]
```

---

#### `Callable` — typing functions and callbacks

```python
from typing import Callable

# A function that takes (int, int) and returns int
Operation = Callable[[int, int], int]

def apply(op: Operation, a: int, b: int) -> int:
    return op(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply(add, 3, 5)   # 8

# Function that takes no args and returns None
Callback = Callable[[], None]

# Function with any signature
AnyFunc = Callable[..., int]
```

---

#### `TypedDict` — typed dictionaries

Regular `dict[str, Any]` loses type information for individual keys. `TypedDict` preserves it.

```python
from typing import TypedDict, NotRequired

class UserProfile(TypedDict):
    name: str
    age: int
    email: str
    bio: NotRequired[str]       # optional key (Python 3.11+)

def create_profile(data: UserProfile) -> str:
    return f"{data['name']} ({data['age']})"

# mypy knows the exact keys and value types
profile: UserProfile = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
}

# mypy would flag:
# bad: UserProfile = {"name": "Alice", "age": "thirty", "email": "a@b.com"}
# TypeError: age should be int, not str
```

---

#### `Literal` — restrict to specific values

```python
from typing import Literal

def set_direction(direction: Literal["north", "south", "east", "west"]) -> None:
    print(f"Moving {direction}")

set_direction("north")    # OK
# set_direction("up")     # mypy error: "up" is not a valid value

# Useful for configuration options
def open_file(path: str, mode: Literal["r", "w", "a", "rb", "wb"]) -> None:
    ...
```

---

#### `overload` — multiple function signatures

When a function's return type depends on its input type, use `@overload`:

```python
from typing import overload

@overload
def parse(value: str) -> dict: ...
@overload
def parse(value: bytes) -> dict: ...
@overload
def parse(value: int) -> str: ...

def parse(value):
    """Actual implementation."""
    if isinstance(value, str):
        import json
        return json.loads(value)
    elif isinstance(value, bytes):
        import json
        return json.loads(value.decode())
    elif isinstance(value, int):
        return str(value)

# mypy knows:
# parse("{}") returns dict
# parse(42) returns str
```

---

#### `ParamSpec` and `Concatenate` — typing decorators

`ParamSpec` (Python 3.10+) lets you type decorators that preserve the wrapped function's signature.

```python
from typing import ParamSpec, TypeVar, Callable
import functools
import time

P = ParamSpec("P")
R = TypeVar("R")

def timer(func: Callable[P, R]) -> Callable[P, R]:
    """A properly typed decorator — preserves function signature."""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def compute(x: int, y: int) -> int:
    return x ** y

# mypy knows compute still takes (int, int) -> int
result = compute(2, 10)
```

---

#### Using `mypy` for static analysis

**Install:** `pip install mypy`

```python
# example.py
def add(a: int, b: int) -> int:
    return a + b

result = add(1, "two")   # Bug! Passing str instead of int
```

```bash
$ mypy example.py
example.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

**mypy configuration in `pyproject.toml`:**

```toml
[tool.mypy]
python_version = "3.12"
strict = true                    # enable all strict checks
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true    # require type hints on all functions

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false   # relax rules for test files
```

**Common mypy flags:**

| Flag | Effect |
|------|--------|
| `--strict` | Enable all optional checks |
| `--ignore-missing-imports` | Don't error on missing stubs |
| `--show-error-codes` | Show error codes (e.g., `[arg-type]`) |
| `--disallow-any-generics` | Require generic parameters |
| `--check-untyped-defs` | Check functions without annotations |

---

#### Type narrowing

`mypy` understands control flow and narrows types:

```python
def process(value: str | int | None) -> str:
    if value is None:
        return "nothing"
    # mypy: value is str | int

    if isinstance(value, str):
        return value.upper()    # mypy: value is str
    # mypy: value is int
    return str(value * 2)
```

**`TypeGuard` for custom type narrowing:**

```python
from typing import TypeGuard

def is_string_list(val: list) -> TypeGuard[list[str]]:
    """Check if all items are strings."""
    return all(isinstance(item, str) for item in val)

def process(items: list) -> None:
    if is_string_list(items):
        # mypy knows items is list[str] here
        print(", ".join(items))   # safe — join expects Iterable[str]
```

---

#### Mini-project 1: Typed configuration system

Build a configuration library with full type safety.

```python
"""
typed_config.py — Type-safe configuration with validation.

Demonstrates:
- TypedDict for structured configs
- Literal for valid options
- overload for flexible API
- Generic types
- mypy-compatible patterns
"""
from typing import TypedDict, Literal, Any, overload, TypeVar, Generic
from dataclasses import dataclass, field
from pathlib import Path
import json

# --- Type definitions ---

class DatabaseConfig(TypedDict):
    host: str
    port: int
    name: str
    user: str
    password: str

class ServerConfig(TypedDict):
    host: str
    port: int
    debug: bool
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]

class AppConfig(TypedDict):
    app_name: str
    version: str
    environment: Literal["development", "staging", "production"]
    database: DatabaseConfig
    server: ServerConfig

# --- Generic config store ---

T = TypeVar("T")

class ConfigStore(Generic[T]):
    """Type-safe configuration store with dot-notation access."""

    def __init__(self, data: T):
        self._data = data

    @overload
    def get(self, key: str) -> Any: ...
    @overload
    def get(self, key: str, default: T) -> T: ...

    def get(self, key, default=None):
        """Get a config value by dot-separated key path."""
        parts = key.split(".")
        current: Any = self._data
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part, default)
            else:
                return default
        return current

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self._data, indent=indent)

    @classmethod
    def from_json(cls, path: str | Path) -> "ConfigStore":
        data = json.loads(Path(path).read_text())
        return cls(data)


# --- Validation ---

def validate_config(config: AppConfig) -> list[str]:
    """Validate configuration and return list of issues."""
    issues: list[str] = []

    if not config["app_name"].strip():
        issues.append("app_name is empty")

    db = config["database"]
    if db["port"] < 1 or db["port"] > 65535:
        issues.append(f"Invalid database port: {db['port']}")

    srv = config["server"]
    if srv["port"] < 1 or srv["port"] > 65535:
        issues.append(f"Invalid server port: {srv['port']}")

    if config["environment"] == "production" and srv["debug"]:
        issues.append("Debug mode should not be enabled in production")

    return issues

# --- Demo ---

if __name__ == "__main__":
    config: AppConfig = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "environment": "development",
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_dev",
            "user": "admin",
            "password": "secret",
        },
        "server": {
            "host": "0.0.0.0",
            "port": 8000,
            "debug": True,
            "log_level": "DEBUG",
        },
    }

    issues = validate_config(config)
    if issues:
        print("Config issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Config is valid!")

    store = ConfigStore(config)
    print(f"\nApp: {store.get('app_name')}")
    print(f"DB Host: {store.get('database.host')}")
    print(f"Log Level: {store.get('server.log_level')}")
    print(f"\n{store.to_json()}")
```

**What you practised:** TypedDict, Literal, overload, Generic[T], TypeVar, dot-path configuration access, config validation.

---

#### Mini-project 2: Type-safe command dispatcher

Build a command router where each command's arguments are type-checked.

```python
"""
type_safe_dispatch.py — Type-safe command dispatcher.

Demonstrates:
- ParamSpec for decorator typing
- Callable types
- Runtime type checking with annotations
- Registration pattern with generics
"""
from typing import Callable, Any, get_type_hints
import functools
import inspect

class CommandDispatcher:
    """Register and dispatch commands with type validation."""

    def __init__(self):
        self._commands: dict[str, Callable] = {}

    def command(self, name: str | None = None):
        """Decorator to register a command."""
        def decorator(func: Callable) -> Callable:
            cmd_name = name or func.__name__
            self._commands[cmd_name] = func
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def dispatch(self, command_name: str, **kwargs: Any) -> Any:
        """Dispatch a command with runtime type checking."""
        if command_name not in self._commands:
            available = ", ".join(sorted(self._commands))
            raise KeyError(f"Unknown command: {command_name}. Available: {available}")

        func = self._commands[command_name]
        hints = get_type_hints(func)

        # Validate argument types at runtime
        sig = inspect.signature(func)
        errors = []
        for param_name, param in sig.parameters.items():
            if param_name in kwargs and param_name in hints:
                expected = hints[param_name]
                actual = type(kwargs[param_name])
                if not isinstance(kwargs[param_name], expected):
                    errors.append(
                        f"  {param_name}: expected {expected.__name__}, "
                        f"got {actual.__name__}"
                    )

        if errors:
            raise TypeError(
                f"Type errors in '{command_name}':\n" + "\n".join(errors)
            )

        return func(**kwargs)

    def list_commands(self) -> list[dict]:
        """List all registered commands with their signatures."""
        result = []
        for name, func in sorted(self._commands.items()):
            hints = get_type_hints(func)
            sig = inspect.signature(func)
            result.append({
                "name": name,
                "doc": (func.__doc__ or "").strip(),
                "params": {
                    p: hints.get(p, Any).__name__
                    for p in sig.parameters
                },
                "returns": hints.get("return", Any).__name__,
            })
        return result

# --- Define commands ---

cli = CommandDispatcher()

@cli.command("greet")
def greet_user(name: str, times: int) -> str:
    """Greet a user multiple times."""
    return (f"Hello, {name}! " * times).strip()

@cli.command("calc")
def calculate(a: float, b: float, operation: str) -> float:
    """Perform a calculation."""
    ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b else float("inf")}
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return ops[operation]

@cli.command()
def echo(message: str) -> str:
    """Echo back the message."""
    return message

# --- Demo ---
if __name__ == "__main__":
    print("Available commands:")
    for cmd in cli.list_commands():
        params = ", ".join(f"{k}: {v}" for k, v in cmd["params"].items())
        print(f"  {cmd['name']}({params}) -> {cmd['returns']}")
        if cmd["doc"]:
            print(f"    {cmd['doc']}")

    print("\n--- Dispatching ---")
    print(cli.dispatch("greet", name="Alice", times=3))
    print(cli.dispatch("calc", a=10.0, b=3.0, operation="+"))
    print(cli.dispatch("echo", message="Hello!"))

    print("\n--- Type error demo ---")
    try:
        cli.dispatch("greet", name=42, times="three")
    except TypeError as e:
        print(f"Caught: {e}")
```

**What you practised:** `get_type_hints`, `inspect.signature`, runtime type checking, decorator-based registration, command dispatch pattern.

---


### Concurrency: Threading, Multiprocessing & Async I/O

**Goal:** Understand threads, processes, and asyncio. Know when to use each model for I/O-bound and CPU-bound workloads.

---

#### The GIL — why it matters

Python has a **Global Interpreter Lock (GIL)** that allows only one thread to execute Python bytecode at a time. This means:

- **Threads DO help** for I/O-bound work (network, file, database) — while one thread waits for I/O, another can run.
- **Threads DON'T help** for CPU-bound work (math, data processing) — only one thread runs at a time.
- **Processes** bypass the GIL entirely — each process has its own interpreter and memory.

> **Python 3.13+ note:** PEP 703 introduces an experimental free-threaded build (`--disable-gil`), but it's not yet the default in 3.14.

| Work type | Best model | Why |
|-----------|-----------|-----|
| I/O-bound (network, files) | `asyncio` or `threading` | Concurrent waiting |
| CPU-bound (math, parsing) | `multiprocessing` | True parallelism |
| Mixed | Process pool + async I/O | Combine both |

---

#### Threading — concurrent I/O

```python
import threading
import time
import requests

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def fetch_url(url, results, index):
    """Fetch a URL and store the result."""
    start = time.perf_counter()
    response = requests.get(url)
    elapsed = time.perf_counter() - start
    results[index] = {
        "url": url,
        "status": response.status_code,
        "time": round(elapsed, 2),
    }

# Sequential: ~4 seconds
start = time.perf_counter()
results_seq = [None] * len(urls)
for i, url in enumerate(urls):
    fetch_url(url, results_seq, i)
print(f"Sequential: {time.perf_counter() - start:.2f}s")

# Threaded: ~1 second (all requests happen concurrently)
start = time.perf_counter()
results_thr = [None] * len(urls)
threads = []
for i, url in enumerate(urls):
    t = threading.Thread(target=fetch_url, args=(url, results_thr, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()     # wait for all threads to complete
print(f"Threaded: {time.perf_counter() - start:.2f}s")
```

**`ThreadPoolExecutor` — the modern way:**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch(url):
    import requests
    response = requests.get(url)
    return {"url": url, "status": response.status_code}

urls = ["https://httpbin.org/delay/1"] * 4

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    # Submit all tasks
    futures = {pool.submit(fetch, url): url for url in urls}

    # Process results as they complete
    for future in as_completed(futures):
        result = future.result()
        print(f"  {result['url']}: {result['status']}")

print(f"Total: {time.perf_counter() - start:.2f}s")   # ~1s

# Simpler: map (preserves order)
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, urls))
```

**Thread safety — locks and synchronization:**

```python
import threading

counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:          # only one thread can enter this block at a time
            counter += 1

threads = [threading.Thread(target=increment, args=(100_000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")   # Always 400000 with lock
```

---

#### Multiprocessing — true parallelism for CPU-bound work

```python
from multiprocessing import Pool
import time
import math

def is_prime(n):
    """Check if a number is prime (CPU-intensive)."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(100_000, 200_000))

# Sequential
start = time.perf_counter()
results_seq = [is_prime(n) for n in numbers]
seq_time = time.perf_counter() - start
print(f"Sequential: {seq_time:.2f}s, {sum(results_seq)} primes")

# Parallel (uses multiple CPU cores)
start = time.perf_counter()
with Pool() as pool:   # defaults to CPU count
    results_par = pool.map(is_prime, numbers)
par_time = time.perf_counter() - start
print(f"Parallel:   {par_time:.2f}s, {sum(results_par)} primes")
print(f"Speedup:    {seq_time / par_time:.1f}x")
```

**`ProcessPoolExecutor` (same API as ThreadPoolExecutor):**

```python
from concurrent.futures import ProcessPoolExecutor
import math

def heavy_computation(n):
    """Simulate CPU-intensive work."""
    return sum(math.factorial(i) for i in range(n))

inputs = [100, 200, 300, 400, 500]

with ProcessPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(heavy_computation, inputs))
    for inp, res in zip(inputs, results):
        print(f"  factorial sum({inp}): {res} (digits: {len(str(res))})")
```

**Shared state between processes:**

```python
from multiprocessing import Process, Value, Array, Queue

def worker(shared_counter, queue, worker_id):
    """Worker process that shares state."""
    for i in range(10):
        with shared_counter.get_lock():
            shared_counter.value += 1
        queue.put(f"Worker {worker_id}: item {i}")

# Shared counter (integer)
counter = Value('i', 0)

# Queue for communication
queue = Queue()

processes = [Process(target=worker, args=(counter, queue, i)) for i in range(3)]
for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Shared counter: {counter.value}")   # 30

# Drain queue
while not queue.empty():
    print(f"  {queue.get()}")
```

---

#### asyncio — coroutine-based concurrency

`asyncio` is Python's async framework. It uses **coroutines** (defined with `async def`) and **await** to handle I/O concurrently in a single thread.

```python
import asyncio
import time

async def fetch_data(name, delay):
    """Simulate an async I/O operation."""
    print(f"  [{name}] Starting (will take {delay}s)...")
    await asyncio.sleep(delay)    # non-blocking sleep
    print(f"  [{name}] Done!")
    return f"{name}: result after {delay}s"

async def main():
    start = time.perf_counter()

    # Run tasks concurrently with gather
    results = await asyncio.gather(
        fetch_data("API call", 2),
        fetch_data("Database query", 1),
        fetch_data("File read", 0.5),
    )

    elapsed = time.perf_counter() - start
    print(f"\nAll done in {elapsed:.2f}s (not {2+1+0.5}s)")
    for r in results:
        print(f"  {r}")

asyncio.run(main())
# Total time: ~2s (limited by slowest task, not sum)
```

**`async for` and `async with`:**

```python
import asyncio

# Async generator
async def async_countdown(start):
    """Yield countdown numbers asynchronously."""
    for i in range(start, 0, -1):
        await asyncio.sleep(0.1)
        yield i

async def demo():
    # Async for loop
    async for num in async_countdown(5):
        print(f"  {num}...")
    print("  Liftoff!")

asyncio.run(demo())
```

**`asyncio.create_task` — fire and forget:**

```python
import asyncio

async def background_task(name, duration):
    await asyncio.sleep(duration)
    print(f"  Background task '{name}' finished after {duration}s")

async def main():
    # Create tasks (they start immediately)
    task1 = asyncio.create_task(background_task("cleanup", 2))
    task2 = asyncio.create_task(background_task("backup", 3))

    # Do other work while tasks run
    print("Main: doing other work...")
    await asyncio.sleep(1)
    print("Main: still working...")

    # Wait for specific tasks if needed
    await task1
    await task2

asyncio.run(main())
```

**Timeouts and cancellation:**

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)
    return "done"

async def main():
    # Timeout
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Operation timed out!")

    # Cancel a task
    task = asyncio.create_task(slow_operation())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())
```

**Semaphores — limit concurrency:**

```python
import asyncio

async def fetch_with_limit(semaphore, url, session_id):
    """Limit concurrent requests using a semaphore."""
    async with semaphore:
        print(f"  [{session_id}] Fetching {url}")
        await asyncio.sleep(1)   # simulate request
        print(f"  [{session_id}] Done")
        return f"Result from {url}"

async def main():
    semaphore = asyncio.Semaphore(3)   # max 3 concurrent tasks

    tasks = [
        fetch_with_limit(semaphore, f"https://api.example.com/{i}", i)
        for i in range(10)
    ]

    results = await asyncio.gather(*tasks)
    print(f"\nCompleted {len(results)} requests")

asyncio.run(main())
```

---

#### Real-world async: HTTP client with `aiohttp`

```python
"""
async_fetcher.py — Async HTTP client demo.

Requires: pip install aiohttp

Demonstrates:
- aiohttp for async HTTP requests
- asyncio.gather for concurrent requests
- Semaphore for rate limiting
- Error handling in async code
"""
import asyncio
# import aiohttp  # pip install aiohttp

async def fetch_url(session, url, semaphore):
    """Fetch a single URL with rate limiting."""
    async with semaphore:
        try:
            async with session.get(url, timeout=10) as response:
                text = await response.text()
                return {
                    "url": url,
                    "status": response.status,
                    "length": len(text),
                }
        except Exception as e:
            return {"url": url, "error": str(e)}

async def fetch_many(urls, max_concurrent=5):
    """Fetch multiple URLs concurrently."""
    semaphore = asyncio.Semaphore(max_concurrent)
    # async with aiohttp.ClientSession() as session:
    #     tasks = [fetch_url(session, url, semaphore) for url in urls]
    #     return await asyncio.gather(*tasks)
    # placeholder for demo without aiohttp:
    results = []
    for url in urls:
        await asyncio.sleep(0.1)
        results.append({"url": url, "status": 200, "length": 1000})
    return results

async def main():
    urls = [
        "https://python.org",
        "https://docs.python.org/3/",
        "https://pypi.org",
        "https://github.com",
        "https://stackoverflow.com",
    ]

    import time
    start = time.perf_counter()
    results = await fetch_many(urls, max_concurrent=3)
    elapsed = time.perf_counter() - start

    print(f"Fetched {len(results)} URLs in {elapsed:.2f}s\n")
    for r in results:
        if "error" in r:
            print(f"  FAIL  {r['url']}: {r['error']}")
        else:
            print(f"  {r['status']}  {r['url']} ({r['length']} bytes)")

# asyncio.run(main())
```

---

#### Mini-project 1: Async task queue

Build a producer-consumer task queue using asyncio.

```python
"""
async_task_queue.py — Producer-consumer pattern with asyncio.

Demonstrates:
- asyncio.Queue
- Producer-consumer pattern
- Task cancellation
- Graceful shutdown
- Multiple workers
"""
import asyncio
import random
import time
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Task:
    id: int
    name: str
    duration: float   # simulated processing time
    created_at: float = field(default_factory=time.time)

@dataclass
class Result:
    task_id: int
    worker_id: int
    success: bool
    message: str
    processing_time: float

async def producer(queue: asyncio.Queue, num_tasks: int):
    """Generate tasks and put them in the queue."""
    for i in range(num_tasks):
        task = Task(
            id=i + 1,
            name=f"task_{i+1}",
            duration=random.uniform(0.5, 2.0),
        )
        await queue.put(task)
        print(f"  [Producer] Queued task #{task.id} ({task.duration:.1f}s)")
        await asyncio.sleep(random.uniform(0.1, 0.5))

    # Signal workers to stop (one None per worker)
    print("  [Producer] All tasks queued, sending stop signals")

async def worker(worker_id: int, queue: asyncio.Queue, results: list):
    """Process tasks from the queue."""
    while True:
        task = await queue.get()

        if task is None:
            queue.task_done()
            print(f"  [Worker {worker_id}] Received stop signal")
            break

        start = time.perf_counter()
        print(f"  [Worker {worker_id}] Processing task #{task.id}...")

        # Simulate work
        try:
            await asyncio.sleep(task.duration)

            # Randomly fail some tasks
            if random.random() < 0.1:
                raise RuntimeError("Random failure!")

            elapsed = time.perf_counter() - start
            results.append(Result(
                task_id=task.id,
                worker_id=worker_id,
                success=True,
                message="completed",
                processing_time=round(elapsed, 2),
            ))
            print(f"  [Worker {worker_id}] Completed task #{task.id} in {elapsed:.2f}s")

        except Exception as e:
            elapsed = time.perf_counter() - start
            results.append(Result(
                task_id=task.id,
                worker_id=worker_id,
                success=False,
                message=str(e),
                processing_time=round(elapsed, 2),
            ))
            print(f"  [Worker {worker_id}] Task #{task.id} FAILED: {e}")

        finally:
            queue.task_done()

async def main():
    num_tasks = 10
    num_workers = 3

    queue: asyncio.Queue[Task | None] = asyncio.Queue(maxsize=5)
    results: list[Result] = []

    start = time.perf_counter()

    # Start workers
    workers = [
        asyncio.create_task(worker(i + 1, queue, results))
        for i in range(num_workers)
    ]

    # Start producer
    await producer(queue, num_tasks)

    # Send stop signals
    for _ in range(num_workers):
        await queue.put(None)

    # Wait for all workers to finish
    await asyncio.gather(*workers)

    elapsed = time.perf_counter() - start

    # Report
    print(f"\n{'='*50}")
    print(f"RESULTS — {num_tasks} tasks, {num_workers} workers, {elapsed:.2f}s total")
    print(f"{'='*50}")
    succeeded = sum(1 for r in results if r.success)
    failed = sum(1 for r in results if not r.success)
    print(f"  Succeeded: {succeeded}")
    print(f"  Failed:    {failed}")
    if results:
        avg_time = sum(r.processing_time for r in results) / len(results)
        print(f"  Avg time:  {avg_time:.2f}s")

asyncio.run(main())
```

**What you practised:** `asyncio.Queue`, producer-consumer pattern, multiple concurrent workers, graceful shutdown, error handling in async code.

---

#### Mini-project 2: Parallel file processor

Compare threading, multiprocessing, and asyncio for processing files.

```python
"""
parallel_benchmark.py — Compare concurrency models.

Demonstrates:
- threading.Thread + ThreadPoolExecutor
- multiprocessing.Pool + ProcessPoolExecutor
- asyncio for I/O
- Performance comparison
"""
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
import os

# --- CPU-bound task ---
def compute_hash(data: bytes) -> str:
    """CPU-intensive: compute SHA-256 hash 1000 times."""
    result = data
    for _ in range(1000):
        result = hashlib.sha256(result).digest()
    return result.hex()

# --- Generate test data ---
test_data = [os.urandom(1024) for _ in range(20)]

def benchmark_sequential():
    """Sequential processing."""
    start = time.perf_counter()
    results = [compute_hash(d) for d in test_data]
    elapsed = time.perf_counter() - start
    return elapsed, len(results)

def benchmark_threads():
    """Thread pool processing."""
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(compute_hash, test_data))
    elapsed = time.perf_counter() - start
    return elapsed, len(results)

def benchmark_processes():
    """Process pool processing."""
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(compute_hash, test_data))
    elapsed = time.perf_counter() - start
    return elapsed, len(results)

async def benchmark_async_io():
    """Async I/O simulation (to show it's best for I/O, not CPU)."""
    async def simulate_io(data):
        await asyncio.sleep(0.05)   # simulate network delay
        return hashlib.sha256(data).hexdigest()

    start = time.perf_counter()
    tasks = [simulate_io(d) for d in test_data]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    return elapsed, len(results)


if __name__ == "__main__":
    print("Benchmarking concurrency models...")
    print(f"Tasks: {len(test_data)} hash computations\n")

    seq_time, _ = benchmark_sequential()
    print(f"  Sequential:      {seq_time:.3f}s (baseline)")

    thr_time, _ = benchmark_threads()
    print(f"  ThreadPool(4):   {thr_time:.3f}s ({seq_time/thr_time:.1f}x)")

    proc_time, _ = benchmark_processes()
    print(f"  ProcessPool(4):  {proc_time:.3f}s ({seq_time/proc_time:.1f}x)")

    io_time, _ = asyncio.run(benchmark_async_io())
    print(f"  Async I/O sim:   {io_time:.3f}s (I/O-bound scenario)")

    print(f"\nConclusion:")
    print(f"  CPU-bound work -> ProcessPool is fastest ({seq_time/proc_time:.1f}x speedup)")
    print(f"  I/O-bound work -> asyncio or ThreadPool")
    print(f"  Threads don't help CPU-bound work due to the GIL")
```

**What you practised:** Threading, multiprocessing, asyncio, `concurrent.futures`, benchmarking, understanding when to use each concurrency model.

---


### Performance Optimisation & Profiling

**Goal:** Measure first, optimise second. Learn to find bottlenecks, profile code, and apply targeted optimisations.

---

#### The golden rule: profile before you optimise

> *"Premature optimisation is the root of all evil."* — Donald Knuth

1. **Write correct code first.**
2. **Measure** to find the actual bottleneck.
3. **Optimise** only the bottleneck.
4. **Measure again** to confirm the improvement.

---

#### `time` and `timeit` — quick benchmarks

```python
import time

# time.perf_counter — wall-clock time (highest resolution)
start = time.perf_counter()
total = sum(range(1_000_000))
elapsed = time.perf_counter() - start
print(f"sum(range(1M)): {elapsed:.4f}s")

# time.process_time — CPU time only (ignores sleep/IO)
start = time.process_time()
total = sum(range(1_000_000))
cpu_time = time.process_time() - start
print(f"CPU time: {cpu_time:.4f}s")
```

**`timeit` — reliable micro-benchmarks:**

```python
import timeit

# Time a single expression (runs it many times)
result = timeit.timeit(
    stmt="sum(range(1000))",
    number=10_000,
)
print(f"sum(range(1000)) × 10k: {result:.3f}s")

# Compare alternatives
list_comp_time = timeit.timeit(
    stmt="[x**2 for x in range(1000)]",
    number=10_000,
)
map_time = timeit.timeit(
    stmt="list(map(lambda x: x**2, range(1000)))",
    number=10_000,
)
print(f"List comprehension: {list_comp_time:.3f}s")
print(f"map + lambda:       {map_time:.3f}s")

# With setup code
dict_time = timeit.timeit(
    stmt="d.get('missing', 0)",
    setup="d = {str(i): i for i in range(1000)}",
    number=1_000_000,
)
print(f"dict.get: {dict_time:.3f}s for 1M lookups")
```

**Command-line usage:**

```bash
# Quick micro-benchmark from terminal
python -m timeit "'-'.join(str(n) for n in range(100))"
python -m timeit "'-'.join(map(str, range(100)))"
```

---

#### `cProfile` — function-level profiling

```python
import cProfile
import pstats
from io import StringIO

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def process_numbers(count):
    results = []
    for i in range(count):
        results.append(fibonacci_recursive(20))
        results.append(fibonacci_iterative(20))
    return results

# Profile with cProfile
profiler = cProfile.Profile()
profiler.enable()
process_numbers(100)
profiler.disable()

# Print sorted stats
stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(15)   # top 15 functions
print(stream.getvalue())
```

**Save and analyse profile data:**

```python
import cProfile
import pstats

# Save profile to file
cProfile.run('process_numbers(100)', 'profile_output.prof')

# Load and analyse
stats = pstats.Stats('profile_output.prof')
stats.strip_dirs()                    # remove path info
stats.sort_stats('tottime')           # sort by total time in function
stats.print_stats(10)                 # top 10

stats.sort_stats('calls')             # sort by call count
stats.print_callers('fibonacci')      # who calls fibonacci?
stats.print_callees('process_numbers')  # what does process_numbers call?
```

**Command line:**

```bash
python -m cProfile -s cumulative my_script.py
python -m cProfile -o output.prof my_script.py
```

---

#### Memory profiling

**`sys.getsizeof` — quick size check:**

```python
import sys

data = {
    "int":        42,
    "float":      3.14,
    "str (5)":    "hello",
    "str (100)":  "x" * 100,
    "list (10)":  list(range(10)),
    "list (1000)": list(range(1000)),
    "dict (10)":  {i: i for i in range(10)},
    "set (10)":   set(range(10)),
    "tuple (10)": tuple(range(10)),
}

print(f"{'Type':<15} {'Size (bytes)':>12}")
print("-" * 28)
for name, obj in data.items():
    print(f"{name:<15} {sys.getsizeof(obj):>12,}")
```

> **Warning:** `sys.getsizeof` shows the *shallow* size only — it doesn't count the size of contained objects.

**`__slots__` for memory-efficient classes:**

```python
import sys

class PointRegular:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class PointSlots:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

regular = PointRegular(1, 2, 3)
slotted = PointSlots(1, 2, 3)

print(f"Regular: {sys.getsizeof(regular)} bytes + {sys.getsizeof(regular.__dict__)} (dict)")
print(f"Slotted: {sys.getsizeof(slotted)} bytes (no __dict__)")

# Memory difference scales with millions of objects
import time

start = time.perf_counter()
regular_list = [PointRegular(i, i+1, i+2) for i in range(100_000)]
reg_time = time.perf_counter() - start

start = time.perf_counter()
slotted_list = [PointSlots(i, i+1, i+2) for i in range(100_000)]
slot_time = time.perf_counter() - start

print(f"\n100K objects creation:")
print(f"  Regular: {reg_time:.3f}s")
print(f"  Slotted: {slot_time:.3f}s")
```

**Generators vs lists for memory:**

```python
import sys

# List: stores ALL values in memory
big_list = [x**2 for x in range(1_000_000)]
print(f"List: {sys.getsizeof(big_list):,} bytes")

# Generator: computes values on-the-fly
big_gen = (x**2 for x in range(1_000_000))
print(f"Generator: {sys.getsizeof(big_gen):,} bytes")

# Both produce the same results
print(f"Sum from list: {sum(big_list)}")
print(f"Sum from gen:  {sum(x**2 for x in range(1_000_000))}")
```

---

#### Common optimisation techniques

**1. Use built-in functions (C-implemented, much faster):**

```python
import timeit

numbers = list(range(10_000))

# Slow: Python loop
def sum_loop(nums):
    total = 0
    for n in nums:
        total += n
    return total

# Fast: built-in sum() (implemented in C)
print(f"Python loop:  {timeit.timeit(lambda: sum_loop(numbers), number=1000):.3f}s")
print(f"Built-in sum: {timeit.timeit(lambda: sum(numbers), number=1000):.3f}s")
```

**2. Dictionary lookups instead of linear search:**

```python
import timeit

data = list(range(10_000))
data_set = set(data)
data_dict = {x: True for x in data}

# O(n) linear search
print(f"list 'in':  {timeit.timeit(lambda: 9999 in data, number=10000):.3f}s")

# O(1) hash lookups
print(f"set 'in':   {timeit.timeit(lambda: 9999 in data_set, number=10000):.3f}s")
print(f"dict 'in':  {timeit.timeit(lambda: 9999 in data_dict, number=10000):.3f}s")
```

**3. String concatenation:**

```python
import timeit

# Slow: string concatenation in a loop (creates new string each time)
def concat_loop(n):
    result = ""
    for i in range(n):
        result += str(i) + ", "
    return result

# Fast: join (allocates once)
def concat_join(n):
    return ", ".join(str(i) for i in range(n))

n = 10_000
print(f"+=  loop: {timeit.timeit(lambda: concat_loop(n), number=100):.3f}s")
print(f"join():   {timeit.timeit(lambda: concat_join(n), number=100):.3f}s")
```

**4. `functools.lru_cache` — memoisation:**

```python
import functools
import time

# Without cache: exponential time
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# With cache: linear time
@functools.lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

start = time.perf_counter()
fib_slow(30)
slow_time = time.perf_counter() - start

start = time.perf_counter()
fib_fast(30)
fast_time = time.perf_counter() - start

print(f"Without cache: {slow_time:.3f}s")
print(f"With cache:    {fast_time:.6f}s")
print(f"Speedup:       {slow_time / fast_time:.0f}x")

# Cache stats
print(f"\nCache info: {fib_fast.cache_info()}")
```

**5. `collections.deque` for queue operations:**

```python
import timeit
from collections import deque

# list.pop(0) is O(n) — shifts all elements
def list_queue():
    q = list(range(1000))
    while q:
        q.pop(0)

# deque.popleft() is O(1) — doubly-linked list
def deque_queue():
    q = deque(range(1000))
    while q:
        q.popleft()

print(f"list.pop(0):     {timeit.timeit(list_queue, number=1000):.3f}s")
print(f"deque.popleft(): {timeit.timeit(deque_queue, number=1000):.3f}s")
```

**6. Local variables are faster than global:**

```python
import timeit

global_list = list(range(100))

def access_global():
    total = 0
    for x in global_list:
        total += x
    return total

def access_local():
    local_list = list(range(100))
    total = 0
    for x in local_list:
        total += x
    return total

print(f"Global variable: {timeit.timeit(access_global, number=100_000):.3f}s")
print(f"Local variable:  {timeit.timeit(access_local, number=100_000):.3f}s")
```

**7. Algorithmic complexity matters most:**

```python
import time

def find_duplicates_naive(items):
    """O(n²) — check every pair."""
    duplicates = []
    for i, a in enumerate(items):
        for b in items[i+1:]:
            if a == b and a not in duplicates:
                duplicates.append(a)
    return duplicates

def find_duplicates_set(items):
    """O(n) — use a set for tracking."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

# Small data: both are fast
data = list(range(5000)) + list(range(2500))

start = time.perf_counter()
find_duplicates_naive(data)
naive_time = time.perf_counter() - start

start = time.perf_counter()
find_duplicates_set(data)
set_time = time.perf_counter() - start

print(f"O(n²) naive: {naive_time:.3f}s")
print(f"O(n) set:    {set_time:.6f}s")
print(f"Speedup:     {naive_time / set_time:.0f}x")
```

---

#### Profiling a real application

```python
"""
profile_demo.py — Profile a realistic data processing pipeline.

Shows how to identify bottlenecks in multi-stage processing.
"""
import cProfile
import pstats
import random
import json
import hashlib
from io import StringIO

# Stage 1: Generate data
def generate_records(count):
    """Simulate loading records."""
    return [
        {
            "id": i,
            "name": f"user_{i}",
            "email": f"user_{i}@example.com",
            "score": random.randint(0, 100),
            "data": "x" * random.randint(100, 1000),
        }
        for i in range(count)
    ]

# Stage 2: Validate
def validate_records(records):
    """Check each record is valid."""
    valid = []
    for record in records:
        if "@" in record["email"] and 0 <= record["score"] <= 100:
            valid.append(record)
    return valid

# Stage 3: Transform (intentionally slow)
def transform_records(records):
    """Transform records — includes a hidden bottleneck."""
    transformed = []
    for record in records:
        # BOTTLENECK: serialise to JSON and hash (unnecessarily heavy)
        json_str = json.dumps(record, sort_keys=True)
        record["hash"] = hashlib.sha256(json_str.encode()).hexdigest()
        record["score_grade"] = (
            "A" if record["score"] >= 90 else
            "B" if record["score"] >= 80 else
            "C" if record["score"] >= 70 else
            "D" if record["score"] >= 60 else
            "F"
        )
        transformed.append(record)
    return transformed

# Stage 4: Aggregate
def aggregate_results(records):
    """Compute summary statistics."""
    grades = {}
    for record in records:
        grade = record["score_grade"]
        grades[grade] = grades.get(grade, 0) + 1
    return {
        "total": len(records),
        "grades": grades,
        "avg_score": sum(r["score"] for r in records) / len(records),
    }

def pipeline(count):
    records = generate_records(count)
    valid = validate_records(records)
    transformed = transform_records(valid)
    summary = aggregate_results(transformed)
    return summary

# Profile the pipeline
profiler = cProfile.Profile()
profiler.enable()
result = pipeline(10_000)
profiler.disable()

stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(20)
print(stream.getvalue())

print(f"\nResult: {result}")
```

---

#### Mini-project 1: Performance testing framework

Build a reusable benchmarking tool that compares function implementations.

```python
"""
bench.py — Micro-benchmarking framework.

Demonstrates:
- Decorators for benchmarking
- Statistical analysis (mean, std dev, median)
- Comparison reports
- Context managers for timing
"""
import time
import statistics
import functools
from contextlib import contextmanager
from dataclasses import dataclass, field

@dataclass
class BenchmarkResult:
    name: str
    times: list[float] = field(default_factory=list)

    @property
    def mean(self) -> float:
        return statistics.mean(self.times)

    @property
    def median(self) -> float:
        return statistics.median(self.times)

    @property
    def stdev(self) -> float:
        return statistics.stdev(self.times) if len(self.times) > 1 else 0

    @property
    def min_time(self) -> float:
        return min(self.times)

    @property
    def max_time(self) -> float:
        return max(self.times)

class Benchmark:
    """Benchmarking framework for comparing function implementations."""

    def __init__(self, iterations: int = 100, warmup: int = 5):
        self.iterations = iterations
        self.warmup = warmup
        self.results: dict[str, BenchmarkResult] = {}

    def register(self, name: str | None = None):
        """Decorator to register a function for benchmarking."""
        def decorator(func):
            bench_name = name or func.__name__
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            wrapper._bench_name = bench_name
            wrapper._original = func
            return wrapper
        return decorator

    @contextmanager
    def timer(self, label: str):
        """Context manager for timing a block of code."""
        start = time.perf_counter()
        yield
        elapsed = time.perf_counter() - start
        if label not in self.results:
            self.results[label] = BenchmarkResult(name=label)
        self.results[label].times.append(elapsed)

    def run(self, func, *args, name: str | None = None, **kwargs):
        """Run a function through the benchmark."""
        bench_name = name or getattr(func, '_bench_name', func.__name__)

        # Warmup
        for _ in range(self.warmup):
            func(*args, **kwargs)

        # Benchmark
        result = BenchmarkResult(name=bench_name)
        for _ in range(self.iterations):
            start = time.perf_counter()
            func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            result.times.append(elapsed)

        self.results[bench_name] = result
        return result

    def compare(self, *funcs, args=(), kwargs=None):
        """Benchmark multiple functions with the same arguments."""
        kwargs = kwargs or {}
        for func in funcs:
            self.run(func, *args, **kwargs)
        return self.report()

    def report(self) -> str:
        """Generate a comparison report."""
        if not self.results:
            return "No results yet."

        lines = []
        lines.append(f"\n{'='*70}")
        lines.append(f"BENCHMARK RESULTS ({self.iterations} iterations, {self.warmup} warmup)")
        lines.append(f"{'='*70}")
        lines.append(
            f"{'Name':<25} {'Mean':>10} {'Median':>10} "
            f"{'StdDev':>10} {'Min':>10} {'vs Best':>10}"
        )
        lines.append("-" * 75)

        # Sort by mean time
        sorted_results = sorted(self.results.values(), key=lambda r: r.mean)
        best_mean = sorted_results[0].mean if sorted_results else 1

        for result in sorted_results:
            ratio = result.mean / best_mean
            lines.append(
                f"{result.name:<25} {result.mean*1000:>9.3f}ms "
                f"{result.median*1000:>9.3f}ms {result.stdev*1000:>9.3f}ms "
                f"{result.min_time*1000:>9.3f}ms {ratio:>9.1f}x"
            )

        lines.append(f"\n  Fastest: {sorted_results[0].name}")
        return "\n".join(lines)


# --- Demo: Compare sorting algorithms ---
import random

bench = Benchmark(iterations=50, warmup=5)

data = [random.randint(0, 10_000) for _ in range(5_000)]

def sort_builtin(data):
    return sorted(data)

def sort_bubble_partial(data):
    """Bubble sort (first 500 elements only — full would be too slow)."""
    arr = data[:500]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sort_insertion(data):
    """Insertion sort (first 500 elements only)."""
    arr = data[:500]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

bench.compare(sort_builtin, sort_bubble_partial, sort_insertion, args=(data,))
print(bench.report())
```

**What you practised:** `time.perf_counter`, statistical analysis, decorator patterns, context managers, comparison reporting.

---

#### Mini-project 2: Code optimiser challenge

A poorly-written program that you can optimise stage by stage.

```python
"""
optimise_me.py — Deliberately slow code to practice optimisation.

Each version fixes one bottleneck. Run and compare times.

Challenge: identify and fix each bottleneck before reading the solution.
"""
import time
import random
import hashlib
from functools import lru_cache
from collections import Counter

# Generate test data
random.seed(42)
words = [f"word_{random.randint(0, 999)}" for _ in range(50_000)]
numbers = [random.randint(1, 10_000) for _ in range(10_000)]

# --- Version 0: Unoptimised ---
def word_frequency_v0(words):
    """Count word frequencies. SLOW: O(n²) in check."""
    freq = {}
    for word in words:
        count = 0
        for w in words:     # O(n) scan for EACH word
            if w == word:
                count += 1
        freq[word] = count
    return freq

# --- Version 1: Use dict properly ---
def word_frequency_v1(words):
    """Count word frequencies. BETTER: O(n) with dict."""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# --- Version 2: Use Counter ---
def word_frequency_v2(words):
    """Count word frequencies. BEST: Counter is C-optimised."""
    return Counter(words)

# --- Version 0: Naive duplicate finder ---
def find_unique_v0(items):
    """Find unique items. SLOW: string concat + 'in' on list."""
    result = ""
    seen = []
    for item in items:
        if item not in seen:     # O(n) search in list
            result += str(item) + ","   # O(n) string copy
            seen.append(item)
    return result

# --- Version 1: Use set + join ---
def find_unique_v1(items):
    """Find unique items. FAST: set lookup + join."""
    seen = set()
    unique = []
    for item in items:
        if item not in seen:     # O(1) set lookup
            unique.append(str(item))
            seen.add(item)
    return ",".join(unique)      # single allocation

# --- Version 2: Preserve order with dict.fromkeys ---
def find_unique_v2(items):
    """Find unique items. FASTEST: dict.fromkeys preserves order."""
    return ",".join(str(x) for x in dict.fromkeys(items))


def run_comparison(name, funcs, *args):
    """Run and compare multiple implementations."""
    print(f"\n--- {name} ---")
    times = []
    for func in funcs:
        # Use a subset for slow versions
        if "_v0" in func.__name__:
            test_args = tuple(arg[:2000] if isinstance(arg, list) else arg for arg in args)
            label = f"{func.__name__} (2K subset)"
        else:
            test_args = args
            label = f"{func.__name__} ({len(args[0]):,} items)"

        start = time.perf_counter()
        result = func(*test_args)
        elapsed = time.perf_counter() - start
        times.append((label, elapsed))
        print(f"  {label:<35} {elapsed:.4f}s")

    if len(times) > 1:
        fastest = min(times, key=lambda t: t[1])
        print(f"  Winner: {fastest[0]}")


if __name__ == "__main__":
    print("CODE OPTIMISATION CHALLENGE\n")

    run_comparison(
        "Word Frequency",
        [word_frequency_v0, word_frequency_v1, word_frequency_v2],
        words,
    )

    run_comparison(
        "Find Unique Items",
        [find_unique_v0, find_unique_v1, find_unique_v2],
        numbers,
    )

    print("\n\nKey takeaways:")
    print("  1. Use the right data structure (set/dict for lookups)")
    print("  2. Avoid string concatenation in loops (use join)")
    print("  3. collections.Counter is optimised in C")
    print("  4. Algorithmic complexity matters more than micro-optimisation")
    print("  5. ALWAYS measure before optimising")
```

**What you practised:** Identifying bottlenecks, algorithmic complexity, `collections.Counter`, set-based lookups, string join pattern, stepwise optimisation approach.

---


### Security Best Practices for Python Applications

**Goal:** Write code that handles secrets, user input, and network interactions safely. Understand common vulnerability patterns and how to prevent them.

---

#### Why security matters for every Python developer

Security isn't just for web developers. Any program that:

- Reads user input (CLI tools, scripts)
- Connects to a database
- Makes network requests
- Stores passwords or API keys
- Processes files from untrusted sources

…needs to handle security correctly.

---

#### Handling secrets and credentials

**Never hard-code secrets:**

```python
# BAD — secrets in source code (will end up in git)
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"

# GOOD — read from environment variables
import os

API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set")
```

**Using `.env` files (for development):**

```python
"""
.env file (NEVER commit this — add to .gitignore):
    API_KEY=sk-1234567890abcdef
    DB_PASSWORD=admin123
    DEBUG=true
"""

# Manual .env loader (no dependencies)
def load_env(filepath=".env"):
    """Load environment variables from a .env file."""
    try:
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, _, value = line.partition("=")
                    os.environ[key.strip()] = value.strip().strip('"').strip("'")
    except FileNotFoundError:
        pass   # .env is optional

load_env()
api_key = os.environ.get("API_KEY", "")
```

**The `secrets` module — cryptographically secure randomness:**

```python
import secrets
import string

# Generate secure tokens
token = secrets.token_hex(32)        # 64-char hex string
url_token = secrets.token_urlsafe(32)  # URL-safe base64 string
random_bytes = secrets.token_bytes(32)  # 32 random bytes

print(f"Hex token:     {token}")
print(f"URL-safe token: {url_token}")

# Secure random integer
secure_int = secrets.randbelow(100)   # 0 to 99
print(f"Secure random int: {secure_int}")

# Secure password generator
def generate_password(length=16):
    """Generate a cryptographically secure password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Ensure at least one of each category
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    # Fill remaining length
    password += [secrets.choice(alphabet) for _ in range(length - 4)]
    # Shuffle to avoid predictable positions
    import random
    system_random = random.SystemRandom()   # also cryptographically secure
    system_random.shuffle(password)
    return "".join(password)

print(f"\nGenerated password: {generate_password()}")
print(f"Generated password: {generate_password(24)}")
```

> **Important:** Never use `random` for security. `random` uses a **deterministic** PRNG (Mersenne Twister). Always use `secrets` for tokens, passwords, and authentication.

**Secure comparison (timing-attack safe):**

```python
import secrets
import hmac

# BAD — vulnerable to timing attacks
def check_token_bad(provided, expected):
    return provided == expected   # short-circuits on first wrong byte

# GOOD — constant-time comparison
def check_token_good(provided, expected):
    return hmac.compare_digest(provided.encode(), expected.encode())

expected_token = secrets.token_hex(32)
print(f"Token: {expected_token}")
print(f"Valid: {check_token_good(expected_token, expected_token)}")
print(f"Invalid: {check_token_good('wrong', expected_token)}")
```

---

#### Password hashing

**Never store passwords in plain text.** Always hash them.

```python
import hashlib
import secrets

def hash_password(password: str) -> str:
    """Hash a password with a random salt using SHA-256.

    Returns 'salt:hash' string.
    """
    salt = secrets.token_hex(16)
    pw_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{pw_hash}"

def verify_password(password: str, stored: str) -> bool:
    """Verify a password against a stored 'salt:hash' string."""
    salt, expected_hash = stored.split(":")
    actual_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return hmac.compare_digest(actual_hash, expected_hash)

# Usage
import hmac

stored = hash_password("my_secret_password")
print(f"Stored: {stored}")
print(f"Verify correct:  {verify_password('my_secret_password', stored)}")
print(f"Verify wrong:    {verify_password('wrong_password', stored)}")
```

**Better: use `hashlib.scrypt` or `hashlib.pbkdf2_hmac` (key stretching):**

```python
import hashlib
import secrets
import hmac

def hash_password_secure(password: str) -> str:
    """Hash a password with PBKDF2 (recommended for production)."""
    salt = secrets.token_bytes(16)
    key = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode(),
        salt=salt,
        iterations=600_000,    # OWASP recommendation (2023)
    )
    return f"{salt.hex()}:{key.hex()}"

def verify_password_secure(password: str, stored: str) -> bool:
    """Verify a password against a PBKDF2 hash."""
    salt_hex, key_hex = stored.split(":")
    salt = bytes.fromhex(salt_hex)
    expected_key = bytes.fromhex(key_hex)
    actual_key = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode(),
        salt=salt,
        iterations=600_000,
    )
    return hmac.compare_digest(actual_key, expected_key)

stored = hash_password_secure("my_secret_password")
print(f"Stored: {stored}")
print(f"Verify correct: {verify_password_secure('my_secret_password', stored)}")
print(f"Verify wrong:   {verify_password_secure('wrong_password', stored)}")
```

---

#### Input validation and sanitisation

**Never trust user input:**

```python
def get_positive_integer(prompt: str) -> int:
    """Safely get a positive integer from user input."""
    while True:
        raw = input(prompt)
        # Strip whitespace
        raw = raw.strip()
        # Check it's a valid integer
        try:
            value = int(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Try again.")
            continue
        # Check range
        if value <= 0:
            print(f"  Must be positive. Got {value}.")
            continue
        return value

def validate_email(email: str) -> bool:
    """Basic email validation."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def sanitise_filename(filename: str) -> str:
    """Remove dangerous characters from a filename."""
    import re
    # Remove path traversal attempts
    filename = filename.replace("..", "").replace("/", "").replace("\\", "")
    # Keep only safe characters
    filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    # Limit length
    return filename[:255]

# Examples
print(validate_email("user@example.com"))    # True
print(validate_email("not-an-email"))         # False
print(sanitise_filename("../../../etc/passwd"))  # etcpasswd
print(sanitise_filename("my file (1).txt"))      # my_file__1_.txt
```

**Path traversal prevention:**

```python
from pathlib import Path

UPLOAD_DIR = Path("/app/uploads")

def safe_file_path(user_filename: str) -> Path:
    """Safely resolve a user-provided filename within a base directory.

    Prevents path traversal attacks like '../../etc/passwd'.
    """
    # Sanitise the filename
    safe_name = Path(user_filename).name   # removes directory components

    # Resolve and check it's within the allowed directory
    full_path = (UPLOAD_DIR / safe_name).resolve()

    if not str(full_path).startswith(str(UPLOAD_DIR.resolve())):
        raise ValueError(f"Path traversal attempt detected: {user_filename}")

    return full_path

# Safe
print(safe_file_path("document.pdf"))       # /app/uploads/document.pdf

# Attack blocked
print(safe_file_path("../../../etc/passwd"))  # /app/uploads/passwd (name only)
```

---

#### SQL injection prevention

```python
import sqlite3

# BAD — SQL injection vulnerability
def get_user_bad(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # NEVER do this — user input directly in SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# What an attacker could send:
# username = "'; DROP TABLE users; --"
# Resulting SQL:
# SELECT * FROM users WHERE username = ''; DROP TABLE users; --'

# GOOD — parameterised queries
def get_user_good(username):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # Parameters are handled safely by the database driver
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

# Complete safe database example
def demo_safe_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL
        )
    """)

    # Safe insert — always use parameterised queries
    users = [
        ("alice", "alice@example.com"),
        ("bob", "bob@example.com"),
        ("charlie", "charlie@example.com"),
    ]
    cursor.executemany(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        users,
    )

    # Safe search
    search_term = "ali"   # could come from user input
    cursor.execute(
        "SELECT * FROM users WHERE username LIKE ?",
        (f"%{search_term}%",),
    )
    results = cursor.fetchall()
    for row in results:
        print(f"  Found: {row}")

    # Even this is safe (attacker can't inject SQL)
    evil_input = "'; DROP TABLE users; --"
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (evil_input,),
    )
    print(f"  Evil query returned: {cursor.fetchall()}")   # [] (no results, no damage)

    conn.close()

demo_safe_db()
```

---

#### Serialisation dangers

```python
import pickle
import json

# DANGEROUS: pickle can execute arbitrary code
class MaliciousPayload:
    """Demonstrates why pickle is dangerous with untrusted data."""
    def __reduce__(self):
        # This could run ANY command: os.system("rm -rf /")
        return (print, ("HACKED! This could have been malicious code.",))

# NEVER unpickle data from untrusted sources
# data = pickle.loads(untrusted_bytes)   # DANGEROUS

# SAFE alternatives for data exchange:
# 1. JSON (only supports basic types)
safe_data = json.dumps({"key": "value", "number": 42})
parsed = json.loads(safe_data)
print(f"  JSON: {parsed}")

# 2. If you must use pickle, restrict allowed classes
import io

class RestrictedUnpickler(pickle.Unpickler):
    """Only allow specific safe classes to be unpickled."""
    ALLOWED_CLASSES = {
        'builtins': {'dict', 'list', 'set', 'tuple', 'str', 'int', 'float', 'bool'},
    }

    def find_class(self, module, name):
        allowed = self.ALLOWED_CLASSES.get(module, set())
        if name in allowed:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(
            f"Forbidden: {module}.{name}"
        )

def safe_loads(data: bytes):
    """Safely unpickle data with class restrictions."""
    return RestrictedUnpickler(io.BytesIO(data)).load()

# Safe data works
safe_bytes = pickle.dumps({"key": [1, 2, 3]})
print(f"  Safe unpickle: {safe_loads(safe_bytes)}")

# Malicious data is blocked
try:
    evil_bytes = pickle.dumps(MaliciousPayload())
    safe_loads(evil_bytes)
except pickle.UnpicklingError as e:
    print(f"  Blocked: {e}")
```

---

#### `subprocess` safety

```python
import subprocess
import shlex

# BAD — shell injection vulnerability
def run_bad(user_input):
    # NEVER use shell=True with user input
    subprocess.run(f"echo {user_input}", shell=True)

# What an attacker could send:
# user_input = "; rm -rf /"
# Resulting command: echo ; rm -rf /

# GOOD — pass arguments as a list (no shell interpretation)
def run_safe(user_input):
    subprocess.run(["echo", user_input])   # treated as a single argument

# GOOD — if you must use shell=True, escape properly
def run_shell_safe(user_input):
    escaped = shlex.quote(user_input)
    subprocess.run(f"echo {escaped}", shell=True)

# Demo
run_safe("hello; rm -rf /")
# Output: hello; rm -rf /   (treated as literal text, not a command)
```

---

#### Logging safely

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# BAD — logging sensitive data
def login_bad(username, password):
    logger.info(f"Login attempt: {username} / {password}")   # password in logs!

# GOOD — never log secrets
def login_good(username, password):
    logger.info(f"Login attempt for user: {username}")
    # Process login...
    logger.info(f"Login successful for user: {username}")

# Sanitise data before logging
def sanitise_for_logging(data: dict) -> dict:
    """Remove sensitive fields before logging."""
    sensitive_keys = {"password", "token", "secret", "api_key", "credit_card"}
    return {
        k: "***REDACTED***" if k.lower() in sensitive_keys else v
        for k, v in data.items()
    }

user_data = {
    "username": "alice",
    "password": "secret123",
    "api_key": "sk-abc123",
    "role": "admin",
}

logger.info(f"User data: {sanitise_for_logging(user_data)}")
# User data: {'username': 'alice', 'password': '***REDACTED***',
#              'api_key': '***REDACTED***', 'role': 'admin'}
```

---

#### Mini-project 1: Secure password manager

A local password manager that stores credentials safely.

```python
"""
password_vault.py — Secure local password manager.

Demonstrates:
- PBKDF2 key derivation
- secrets for salt generation
- Encrypted storage (using XOR for demo — use Fernet in production)
- Input validation
- Safe file handling
"""
import hashlib
import secrets
import hmac
import json
import os
from pathlib import Path
from getpass import getpass

class PasswordVault:
    """Simple encrypted password vault."""

    def __init__(self, vault_path: str = "vault.json"):
        self.vault_path = Path(vault_path)
        self.entries: dict[str, dict] = {}
        self.master_key: bytes = b""
        self._is_unlocked = False

    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derive an encryption key from the master password."""
        return hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=password.encode(),
            salt=salt,
            iterations=600_000,
        )

    def _xor_encrypt(self, data: bytes, key: bytes) -> bytes:
        """Simple XOR encryption (demo only — use Fernet in production)."""
        return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

    def create(self, master_password: str) -> None:
        """Create a new vault with a master password."""
        salt = secrets.token_bytes(16)
        key = self._derive_key(master_password, salt)
        verification = hashlib.sha256(key).hexdigest()

        vault_data = {
            "salt": salt.hex(),
            "verification": verification,
            "entries": {},
        }

        self.vault_path.write_text(json.dumps(vault_data, indent=2))
        self.master_key = key
        self._is_unlocked = True
        self.entries = {}
        print(f"  Vault created at {self.vault_path}")

    def unlock(self, master_password: str) -> bool:
        """Unlock an existing vault."""
        if not self.vault_path.exists():
            print("  No vault found. Create one first.")
            return False

        vault_data = json.loads(self.vault_path.read_text())
        salt = bytes.fromhex(vault_data["salt"])
        key = self._derive_key(master_password, salt)
        verification = hashlib.sha256(key).hexdigest()

        if not hmac.compare_digest(verification, vault_data["verification"]):
            print("  Wrong master password!")
            return False

        self.master_key = key
        self._is_unlocked = True

        # Decrypt entries
        self.entries = {}
        for name, encrypted_hex in vault_data.get("entries", {}).items():
            encrypted = bytes.fromhex(encrypted_hex)
            decrypted = self._xor_encrypt(encrypted, key)
            self.entries[name] = json.loads(decrypted.decode())

        print(f"  Vault unlocked. {len(self.entries)} entries loaded.")
        return True

    def _save(self) -> None:
        """Save vault to disk."""
        vault_data = json.loads(self.vault_path.read_text())
        encrypted_entries = {}
        for name, entry in self.entries.items():
            data = json.dumps(entry).encode()
            encrypted = self._xor_encrypt(data, self.master_key)
            encrypted_entries[name] = encrypted.hex()
        vault_data["entries"] = encrypted_entries
        self.vault_path.write_text(json.dumps(vault_data, indent=2))

    def add(self, name: str, username: str, password: str, url: str = "") -> None:
        """Add a credential entry."""
        if not self._is_unlocked:
            print("  Vault is locked!")
            return

        self.entries[name] = {
            "username": username,
            "password": password,
            "url": url,
        }
        self._save()
        print(f"  Added entry: {name}")

    def get(self, name: str) -> dict | None:
        """Retrieve a credential entry."""
        if not self._is_unlocked:
            print("  Vault is locked!")
            return None

        entry = self.entries.get(name)
        if entry:
            return entry
        print(f"  Entry '{name}' not found.")
        return None

    def list_entries(self) -> list[str]:
        """List all entry names (without revealing passwords)."""
        if not self._is_unlocked:
            print("  Vault is locked!")
            return []
        return list(self.entries.keys())

    def generate_password(self, length: int = 20) -> str:
        """Generate a secure random password."""
        import string
        alphabet = string.ascii_letters + string.digits + "!@#$%&*"
        password = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice("!@#$%&*"),
        ]
        password += [secrets.choice(alphabet) for _ in range(length - 4)]
        import random
        random.SystemRandom().shuffle(password)
        return "".join(password)


# --- Demo ---
def demo():
    vault = PasswordVault("demo_vault.json")

    # Create vault
    vault.create("my_master_password_123")

    # Add entries
    vault.add("github", "alice", vault.generate_password(), "https://github.com")
    vault.add("email", "alice@example.com", vault.generate_password(), "https://mail.example.com")
    vault.add("database", "admin", "db_password_456", "localhost:5432")

    # List entries
    print(f"\n  Entries: {vault.list_entries()}")

    # Retrieve
    entry = vault.get("github")
    if entry:
        print(f"\n  GitHub credentials:")
        print(f"    Username: {entry['username']}")
        print(f"    Password: {entry['password']}")
        print(f"    URL:      {entry['url']}")

    # Lock and re-unlock
    vault2 = PasswordVault("demo_vault.json")
    vault2.unlock("my_master_password_123")
    entry2 = vault2.get("github")
    print(f"\n  After re-unlock: {entry2['username']}")

    # Wrong password
    vault3 = PasswordVault("demo_vault.json")
    vault3.unlock("wrong_password")

    # Cleanup
    Path("demo_vault.json").unlink(missing_ok=True)

demo()
```

**What you practised:** PBKDF2 key derivation, `secrets` module, `hmac.compare_digest`, encrypted storage, input validation, safe file handling.

---

#### Mini-project 2: Security audit scanner

A tool that scans Python source files for common security issues.

```python
"""
security_scanner.py — Static security analysis for Python files.

Demonstrates:
- Regular expressions for pattern matching
- File system scanning with pathlib
- Rule-based analysis
- Reporting
"""
import re
from pathlib import Path
from dataclasses import dataclass

@dataclass
class SecurityIssue:
    file: str
    line_number: int
    line: str
    rule: str
    severity: str   # "HIGH", "MEDIUM", "LOW"
    description: str

# --- Security rules ---
RULES = [
    {
        "name": "HARDCODED_PASSWORD",
        "pattern": r'(?i)(password|passwd|secret|api_key|token)\s*=\s*["\'][^"\']+["\']',
        "severity": "HIGH",
        "description": "Possible hardcoded credential. Use environment variables instead.",
        "exclude_patterns": ["example", "test", "demo", "placeholder"],
    },
    {
        "name": "SHELL_INJECTION",
        "pattern": r'subprocess\.\w+\(.*shell\s*=\s*True',
        "severity": "HIGH",
        "description": "subprocess with shell=True is vulnerable to shell injection.",
    },
    {
        "name": "SQL_INJECTION",
        "pattern": r'execute\(\s*f["\']|execute\(.*%\s*\(|execute\(.*\.format\(',
        "severity": "HIGH",
        "description": "Possible SQL injection. Use parameterised queries (?) instead.",
    },
    {
        "name": "PICKLE_LOAD",
        "pattern": r'pickle\.loads?\(',
        "severity": "MEDIUM",
        "description": "pickle.load can execute arbitrary code. Don't use with untrusted data.",
    },
    {
        "name": "EVAL_EXEC",
        "pattern": r'\b(eval|exec)\s*\(',
        "severity": "HIGH",
        "description": "eval/exec can execute arbitrary code. Avoid with user input.",
    },
    {
        "name": "INSECURE_RANDOM",
        "pattern": r'\brandom\.(randint|choice|random|uniform)\b',
        "severity": "LOW",
        "description": "random module is not cryptographically secure. Use secrets for security.",
    },
    {
        "name": "ASSERT_SECURITY",
        "pattern": r'\bassert\b.*(?i)(auth|permission|admin|login|token)',
        "severity": "MEDIUM",
        "description": "assert is removed with -O flag. Don't use for security checks.",
    },
    {
        "name": "TEMP_FILE_UNSAFE",
        "pattern": r'open\(\s*["\']/tmp/',
        "severity": "MEDIUM",
        "description": "Hardcoded /tmp path. Use tempfile module for secure temp files.",
    },
    {
        "name": "DEBUG_MODE",
        "pattern": r'(?i)debug\s*=\s*True',
        "severity": "LOW",
        "description": "Debug mode enabled. Ensure this is disabled in production.",
    },
    {
        "name": "BINDING_ALL_INTERFACES",
        "pattern": r'(?:bind|host)\s*=?\s*["\']0\.0\.0\.0["\']',
        "severity": "MEDIUM",
        "description": "Binding to 0.0.0.0 exposes service to all network interfaces.",
    },
]

class SecurityScanner:
    """Scan Python files for common security issues."""

    def __init__(self):
        self.issues: list[SecurityIssue] = []

    def scan_file(self, filepath: Path) -> list[SecurityIssue]:
        """Scan a single Python file."""
        file_issues = []
        try:
            content = filepath.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            return file_issues

        lines = content.splitlines()
        for line_num, line in enumerate(lines, start=1):
            stripped = line.strip()

            # Skip comments
            if stripped.startswith("#"):
                continue

            for rule in RULES:
                if re.search(rule["pattern"], stripped):
                    # Check exclusions
                    exclude = rule.get("exclude_patterns", [])
                    if any(ex in stripped.lower() for ex in exclude):
                        continue

                    issue = SecurityIssue(
                        file=str(filepath),
                        line_number=line_num,
                        line=stripped[:100],
                        rule=rule["name"],
                        severity=rule["severity"],
                        description=rule["description"],
                    )
                    file_issues.append(issue)

        self.issues.extend(file_issues)
        return file_issues

    def scan_directory(self, directory: Path, exclude_dirs: set | None = None) -> list[SecurityIssue]:
        """Recursively scan all Python files in a directory."""
        exclude_dirs = exclude_dirs or {".git", "__pycache__", ".venv", "venv", "node_modules"}
        self.issues = []

        for py_file in directory.rglob("*.py"):
            # Skip excluded directories
            if any(excluded in py_file.parts for excluded in exclude_dirs):
                continue
            self.scan_file(py_file)

        return self.issues

    def report(self) -> str:
        """Generate a security report."""
        if not self.issues:
            return "No security issues found!"

        lines = []
        lines.append(f"\n{'='*70}")
        lines.append(f"SECURITY SCAN REPORT")
        lines.append(f"{'='*70}")

        # Summary
        high = sum(1 for i in self.issues if i.severity == "HIGH")
        medium = sum(1 for i in self.issues if i.severity == "MEDIUM")
        low = sum(1 for i in self.issues if i.severity == "LOW")
        lines.append(f"\n  Total issues: {len(self.issues)}")
        lines.append(f"  HIGH:   {high}")
        lines.append(f"  MEDIUM: {medium}")
        lines.append(f"  LOW:    {low}")

        # Details grouped by severity
        for severity in ["HIGH", "MEDIUM", "LOW"]:
            severity_issues = [i for i in self.issues if i.severity == severity]
            if not severity_issues:
                continue

            lines.append(f"\n--- {severity} ---")
            for issue in severity_issues:
                lines.append(f"\n  [{issue.rule}] {issue.file}:{issue.line_number}")
                lines.append(f"  Code: {issue.line}")
                lines.append(f"  Fix:  {issue.description}")

        return "\n".join(lines)


# --- Demo: Scan a sample file ---
def demo():
    # Create a sample file with issues
    sample = Path("sample_insecure.py")
    sample.write_text('''
import pickle
import subprocess
import random
import sqlite3

# Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"
DEBUG = True

def get_user(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return cursor.fetchone()

def run_command(user_input):
    subprocess.run(f"echo {user_input}", shell=True)

def load_data(raw_bytes):
    return pickle.loads(raw_bytes)

def generate_token():
    return random.randint(100000, 999999)

def check_admin(user):
    assert user.role == "admin", "Not an admin"

def calculate(expr):
    return eval(expr)
''')

    scanner = SecurityScanner()
    scanner.scan_file(sample)
    print(scanner.report())

    # Cleanup
    sample.unlink()

demo()
```

**What you practised:** Regex for pattern matching, `pathlib` for file scanning, `dataclass` for structured data, rule-based analysis, security awareness across multiple vulnerability categories.

---

## Recipes & Quick-Reference Cheatsheets

Practical code snippets you can copy and adapt for common tasks. Each recipe is self-contained — copy it straight into your project.

---

### File operations

**Read / write entire files:**

```python
from pathlib import Path

# Read entire text file
text = Path("file.txt").read_text(encoding="utf-8")

# Write text file
Path("output.txt").write_text("content here", encoding="utf-8")

# Read binary file
data = Path("image.png").read_bytes()

# Append to a file
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new log line\n")
```

**Process a file line by line (memory-efficient):**

```python
with open("big_file.txt", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        if "ERROR" in line:
            print(f"Line {line_number}: {line.strip()}")
```

**Recursively find files:**

```python
from pathlib import Path

# All Python files under current directory
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# All images (multiple extensions)
for img in Path("photos").rglob("*"):
    if img.suffix.lower() in {".jpg", ".png", ".gif"}:
        print(f"{img.name}: {img.stat().st_size:,} bytes")
```

**Copy, move, and delete:**

```python
import shutil
from pathlib import Path

shutil.copy2("src.txt", "dst.txt")           # copy with metadata
shutil.copytree("src_dir", "dst_dir")        # copy entire directory
shutil.move("old_name.txt", "new_name.txt")  # rename / move
Path("unwanted.txt").unlink(missing_ok=True)  # delete file
shutil.rmtree("old_directory")                # delete directory tree
```

**Temporary files (secure):**

```python
import tempfile

# Temporary file (auto-deleted when closed)
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    f.write('{"key": "value"}')
    temp_path = f.name
    print(f"Temp file: {temp_path}")

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp dir: {tmpdir}")
    # directory and contents are deleted when exiting the block
```

---

### Data formats

**JSON — read, write, pretty-print:**

```python
import json
from pathlib import Path

# Write
data = {"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}
Path("data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))

# Read
loaded = json.loads(Path("data.json").read_text())

# Pretty-print to console
print(json.dumps(loaded, indent=2))

# Custom serialisation (e.g., datetime)
from datetime import datetime

def default_serialiser(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Cannot serialise {type(obj)}")

json.dumps({"now": datetime.now()}, default=default_serialiser)
```

**CSV — read and write:**

```python
import csv
from pathlib import Path

# Write
rows = [["Name", "Age", "City"], ["Alice", 30, "London"], ["Bob", 25, "Paris"]]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

# Read as dicts
with open("people.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"  {row['Name']} is {row['Age']} from {row['City']}")
```

**SQLite — quick database:**

```python
import sqlite3

conn = sqlite3.connect("app.db")     # file-based; use ":memory:" for RAM
conn.row_factory = sqlite3.Row       # access columns by name
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done BOOLEAN DEFAULT 0
    )
""")

# Insert (ALWAYS use ? parameters — never f-strings)
cursor.execute("INSERT INTO tasks (title) VALUES (?)", ("Buy groceries",))

# Query
cursor.execute("SELECT * FROM tasks WHERE done = ?", (0,))
for row in cursor:
    print(f"  [{row['id']}] {row['title']} (done={row['done']})")

conn.commit()
conn.close()
```

**TOML (Python 3.11+):**

```python
import tomllib     # read-only, built in since 3.11

toml_str = '''
[project]
name = "my-app"
version = "1.0.0"

[project.dependencies]
requests = ">=2.28"
'''

config = tomllib.loads(toml_str)
print(config["project"]["name"])          # my-app
print(config["project"]["dependencies"])  # {'requests': '>=2.28'}
```

---

### String manipulation

**Common string operations:**

```python
text = "  Hello, World!  "

text.strip()                    # 'Hello, World!'
text.lower()                    # '  hello, world!  '
text.replace("World", "Python") # '  Hello, Python!  '
text.split(",")                 # ['  Hello', ' World!  ']
"_".join(["a", "b", "c"])       # 'a_b_c'

"hello".startswith("he")        # True
"hello".endswith("lo")          # True
"hello".center(20, "-")         # '-------hello--------'
"hello".zfill(10)               # '00000hello'

# f-string formatting
value = 1234.5678
f"{value:,.2f}"                 # '1,234.57'
f"{value:>12.2f}"               # '    1234.57' (right-align width 12)
f"{42:08b}"                     # '00101010' (binary, zero-padded)
f"{255:#06x}"                   # '0x00ff' (hex with prefix)
f"{'left':<10}|{'right':>10}"   # 'left      |     right'
```

**Regex quick reference:**

```python
import re

text = "Call 020-1234-5678 or email user@example.com today"

# search — first match
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
if match:
    print(f"Phone: {match.group()}")   # 020-1234-5678

# findall — all matches
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
print(f"Emails: {emails}")            # ['user@example.com']

# sub — replace
cleaned = re.sub(r"\d", "X", text)
print(cleaned)  # 'Call XXX-XXXX-XXXX or email user@example.com today'

# split — on pattern
parts = re.split(r"[,;\s]+", "a, b;  c  d")
print(parts)   # ['a', 'b', 'c', 'd']

# Compile for re-use
PHONE_RE = re.compile(r"\d{3}-\d{4}-\d{4}")
matches = PHONE_RE.findall(text)

# Named groups
pattern = r"(?P<area>\d{3})-(?P<number>\d{4}-\d{4})"
m = re.search(pattern, text)
if m:
    print(f"Area: {m.group('area')}, Number: {m.group('number')}")
```

---

### Date and time

```python
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo     # Python 3.9+

# Current date/time
now = datetime.now()
today = date.today()

# Formatting
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # 2026-02-16 14:30:00
print(now.strftime("%d/%m/%Y"))              # 16/02/2026
print(now.strftime("%A, %B %d"))             # Monday, February 16

# Parsing strings to datetime
dt = datetime.strptime("2026-03-15 10:30", "%Y-%m-%d %H:%M")

# Arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
diff = date(2026, 12, 25) - today
print(f"Days until Christmas: {diff.days}")

# Timezones
utc_now = datetime.now(ZoneInfo("UTC"))
london = utc_now.astimezone(ZoneInfo("Europe/London"))
tokyo = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
print(f"UTC:    {utc_now:%H:%M}")
print(f"London: {london:%H:%M}")
print(f"Tokyo:  {tokyo:%H:%M}")

# ISO format (recommended for data exchange)
iso_str = now.isoformat()
parsed_back = datetime.fromisoformat(iso_str)
```

---

### Command-line tools

**argparse — full CLI:**

```python
import argparse

def build_cli():
    parser = argparse.ArgumentParser(
        description="Process files in a directory",
        epilog="Example: python tool.py --input data/ --format json --verbose",
    )
    parser.add_argument("--input", "-i", required=True, help="Input directory")
    parser.add_argument("--output", "-o", default="output/", help="Output directory")
    parser.add_argument("--format", choices=["json", "csv", "txt"], default="json")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--count", type=int, default=10, help="Max items to process")
    return parser.parse_args()

# args = build_cli()
# print(f"Input: {args.input}, Format: {args.format}, Verbose: {args.verbose}")
```

**Subcommands (like `git commit`, `git push`):**

```python
import argparse

parser = argparse.ArgumentParser(prog="mytool")
subparsers = parser.add_subparsers(dest="command", required=True)

# 'init' subcommand
init_parser = subparsers.add_parser("init", help="Initialise a project")
init_parser.add_argument("name", help="Project name")

# 'build' subcommand
build_parser = subparsers.add_parser("build", help="Build the project")
build_parser.add_argument("--release", action="store_true")

# args = parser.parse_args()
# if args.command == "init":
#     print(f"Initialising {args.name}")
# elif args.command == "build":
#     print(f"Building ({'release' if args.release else 'debug'})")
```

---

### HTTP and networking

**Built-in `urllib` (no dependencies):**

```python
import urllib.request
import json

# GET request
with urllib.request.urlopen("https://api.github.com/zen") as response:
    print(response.read().decode())

# GET with JSON
with urllib.request.urlopen("https://api.github.com/users/octocat") as response:
    data = json.loads(response.read())
    print(f"Name: {data['name']}, Repos: {data['public_repos']}")

# POST request
import urllib.parse
data = urllib.parse.urlencode({"key": "value"}).encode()
req = urllib.request.Request("https://httpbin.org/post", data=data)
# with urllib.request.urlopen(req) as response:
#     print(response.read().decode())
```

**`requests` library (pip install requests):**

```python
import requests

# GET
resp = requests.get("https://api.github.com/users/octocat")
print(resp.status_code)    # 200
data = resp.json()

# POST with JSON
resp = requests.post("https://httpbin.org/post", json={"key": "value"})

# With headers and timeout
resp = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer token123"},
    timeout=10,
)

# Download a file
resp = requests.get("https://example.com/file.zip", stream=True)
with open("file.zip", "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        f.write(chunk)
```

---

### Collections cheatsheet

```python
from collections import Counter, defaultdict, deque, namedtuple, ChainMap

# Counter — count occurrences
words = "the cat sat on the mat the cat".split()
counts = Counter(words)
print(counts.most_common(3))   # [('the', 3), ('cat', 2), ('sat', 1)]

# defaultdict — auto-create missing keys
graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")
graph["B"].append("C")
print(dict(graph))   # {'A': ['B', 'C'], 'B': ['C']}

# deque — fast append/pop from both ends
dq = deque(maxlen=3)
dq.extend([1, 2, 3])
dq.append(4)        # [2, 3, 4] — oldest dropped
dq.appendleft(0)    # [0, 2, 3] — newest on right dropped

# namedtuple — lightweight class
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"({p.x}, {p.y})")   # (3, 4)

# ChainMap — layered dict lookup
defaults = {"color": "red", "size": 10}
overrides = {"color": "blue"}
config = ChainMap(overrides, defaults)
print(config["color"])   # blue (from overrides)
print(config["size"])    # 10 (from defaults)
```

---

### itertools cheatsheet

```python
import itertools

# chain — flatten iterables
list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]

# product — cartesian product
list(itertools.product("AB", "12"))
# [('A','1'), ('A','2'), ('B','1'), ('B','2')]

# combinations and permutations
list(itertools.combinations("ABC", 2))    # [('A','B'), ('A','C'), ('B','C')]
list(itertools.permutations("AB", 2))     # [('A','B'), ('B','A')]

# groupby (data must be sorted by key first!)
data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot"), ("veg", "pea")]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {[item[1] for item in group]}")
# fruit: ['apple', 'banana']
# veg: ['carrot', 'pea']

# batched (Python 3.12+)
# list(itertools.batched(range(10), 3))   # [[0,1,2], [3,4,5], [6,7,8], [9]]

# repeat, count, cycle
list(itertools.repeat("x", 3))           # ['x', 'x', 'x']
list(itertools.islice(itertools.count(10, 2), 5))  # [10, 12, 14, 16, 18]
list(itertools.islice(itertools.cycle("ABC"), 7))   # ['A','B','C','A','B','C','A']

# accumulate — running totals
list(itertools.accumulate([1, 2, 3, 4]))   # [1, 3, 6, 10]
```

---

### Comprehension patterns

```python
# List comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested (flatten)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]   # [1, 2, ..., 9]

# Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hey", "hello"]}

# Generator expression (lazy — doesn't build a list)
total = sum(x**2 for x in range(1_000_000))

# Walrus operator in comprehension (Python 3.8+)
import math
results = [
    (n, root)
    for n in range(100)
    if (root := math.sqrt(n)) == int(root)
]
# [(0, 0.0), (1, 1.0), (4, 2.0), (9, 3.0), (16, 4.0), ...]
```

---

### Decorator patterns

```python
import functools
import time

# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper

# Retry decorator with parameters
def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Cache with TTL
def cache_with_ttl(seconds=60):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if now - timestamp < seconds:
                    return result
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

# Usage:
@timer
def slow_function():
    time.sleep(0.5)
    return "done"

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "success"

@cache_with_ttl(seconds=30)
def expensive_lookup(key):
    time.sleep(1)
    return f"result for {key}"
```

---

### Logging setup recipe

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(
    log_file: str = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 5_000_000,
    backup_count: int = 3,
):
    """Production-ready logging setup."""
    # Format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setLevel(logging.DEBUG)   # file gets everything
    file_handler.setFormatter(formatter)

    # Root logger
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(console)
    root.addHandler(file_handler)

    return logging.getLogger(__name__)

# Usage:
# logger = setup_logging()
# logger.info("Application started")
# logger.warning("Disk space low")
# logger.error("Connection failed", exc_info=True)
```

---

### Environment and system

```python
import os
import sys
import platform

# Environment variables
os.environ.get("HOME", "unknown")
os.environ.get("PATH", "").split(os.pathsep)

# System info
print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Machine: {platform.machine()}")
print(f"CPU count: {os.cpu_count()}")
print(f"CWD: {os.getcwd()}")

# Run external commands
import subprocess
result = subprocess.run(
    ["python", "--version"],
    capture_output=True, text=True, check=True,
)
print(f"Output: {result.stdout.strip()}")
```

---

### Python type-hints cheatsheet

```python
from typing import Any

# Basic types
name: str = "Alice"
age: int = 30
score: float = 98.5
active: bool = True

# Collections (Python 3.9+ built-in generics)
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 100}
unique: set[int] = {1, 2, 3}
pair: tuple[str, int] = ("Alice", 30)

# Optional and Union (Python 3.10+ pipe syntax)
maybe_name: str | None = None
id_value: int | str = "abc"

# Callable
from collections.abc import Callable
handler: Callable[[str, int], bool] = lambda s, i: True

# TypedDict
from typing import TypedDict
class UserDict(TypedDict):
    name: str
    age: int
    email: str | None

# Function signatures
def greet(name: str, times: int = 1) -> str:
    return f"Hello {name}! " * times

def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

---

## What’s New in Python 3.14

Python 3.14 (expected final release: **October 2025**) introduces several notable changes. Below is a summary of confirmed and proposed features.

---

### Template strings (PEP 750)

Python 3.14 introduces **template strings** (t-strings), a new kind of string literal similar to f-strings but that produce a `Template` object instead of a `str`. This lets libraries intercept and process the template before rendering.

```python
# t-string — creates a Template object, not a string
name = "Alice"
template = t"Hello, {name}!"
# template is a Template object with .args and .strings

# Libraries can process templates for safe SQL, HTML, etc.
# This is a language-level feature for preventing injection attacks.
```

> **Why it matters:** Template strings let libraries like ORMs and HTML renderers process user values safely, preventing injection attacks at the language level rather than relying on developers to remember parameterised queries.

---

### Deferred evaluation of annotations (PEP 649)

Annotations are no longer evaluated eagerly at function/class definition time. Instead, they're stored in a compact form and only evaluated when accessed via `__annotations__` or `typing.get_type_hints()`.

```python
# This now works without quotes or __future__ annotations
class Tree:
    def __init__(self, left: Tree | None, right: Tree | None):
        self.left = left
        self.right = right
# Previously would raise NameError because Tree isn't fully defined yet
```

> **Why it matters:** Forward references and self-referencing types work naturally without `from __future__ import annotations` or string quotes.

---

### Improved error messages

Python continues to improve its error messages, building on the detailed tracebacks introduced in 3.11-3.13:

```python
# More helpful suggestions for common mistakes
# e.g., "Did you forget to return a value?"
# e.g., "Did you mean 'append'?" for misspelled attributes
```

---

### Performance improvements

- Continued work on the **adaptive specialising interpreter** (started in 3.11)
- Incremental GC improvements
- Faster `isinstance()` and `issubclass()` checks
- Experimental **free-threaded build** (`--disable-gil`) improvements from 3.13

---

### Deprecations and removals

- Several long-deprecated modules scheduled for removal in 3.14 (see PEP 594 — "dead batteries"):
  - `aifc`, `audioop`, `cgi`, `cgitb`, `chunk`, `crypt`, `imghdr`, `mailcap`, `msilib`, `nis`, `nntplib`, `ossaudiodev`, `pipes`, `sndhdr`, `spwd`, `sunau`, `telnetlib`, `uu`, `xdrlib`
- `wstr` members of the C API Unicode object are removed
- Various `asyncio` legacy APIs deprecated in 3.10-3.12 are now removed

> **Tip:** Run your code with `-W error::DeprecationWarning` to catch any deprecated features you're still using.

---

### How to try Python 3.14

```bash
# Install via pyenv (recommended)
pyenv install 3.14.0a5
pyenv local 3.14.0a5

# Or download from python.org/downloads/
# Or use Docker
docker run -it python:3.14-rc python
```

---

## Appendix: Resources & Further Reading

### Official resources

- **Python docs:** https://docs.python.org/3/
- **Python 3.14 What's New:** https://docs.python.org/3.14/whatsnew/3.14.html
- **PEP index:** https://peps.python.org/
- **Python Package Index:** https://pypi.org/
- **Python Glossary:** https://docs.python.org/3/glossary.html

### Learning resources

- **Real Python:** https://realpython.com/ — high-quality tutorials on every topic
- **Python Cookbook (O'Reilly):** recipes for advanced Python
- **Fluent Python (2nd ed):** deep dive into Python's data model
- **Effective Python (Brett Slatkin):** 90 specific ways to write better Python

### Tools

- **mypy:** https://mypy.readthedocs.io/ — static type checker
- **ruff:** https://docs.astral.sh/ruff/ — fast Python linter and formatter
- **pytest:** https://docs.pytest.org/ — testing framework
- **black:** https://black.readthedocs.io/ — opinionated code formatter

### Community

- **Python Discourse:** https://discuss.python.org/
- **r/Python:** https://reddit.com/r/Python
- **Python Discord:** https://pythondiscord.com/
- **Stack Overflow `[python]` tag:** https://stackoverflow.com/questions/tagged/python
