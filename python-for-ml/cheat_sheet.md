# PYTHON FOR DATA SCIENCE & MACHINE LEARNING

> A six-week foundation roadmap, reference sheet, and practice checklist for learning the Python skills required to study Machine Learning with NumPy, pandas, Matplotlib, Jupyter, and Scikit-Learn.

## How to Use This Document

This file is not only a syntax reference. Each week contains:

1. **Learning objectives** — what you should understand.
2. **Core knowledge** — concepts and syntax to review.
3. **Practical examples** — small, runnable code samples.
4. **Common mistakes** — errors to recognize and avoid.
5. **Exercises** — tasks to complete without copying a solution.
6. **Exit criteria** — evidence that you are ready to continue.
7. **English vocabulary** — technical terms to review.

Use the following learning cycle in every session:

1. **Recall:** write what you remember before opening the notes.
2. **Learn:** study one small group of concepts.
3. **Type:** type code manually instead of copying it.
4. **Predict:** predict the output, type, and shape before running.
5. **Modify:** change the input or requirement.
6. **Explain:** describe why the code works in simple English.

---

# WEEK 0: ENVIRONMENT, JUPYTER & WORKSPACE

## Learning Objectives

By the end of this week, you should be able to:

- Create and activate an isolated Python environment.
- Install and verify the required libraries.
- Start Jupyter Notebook or JupyterLab.
- Create a clean project structure.
- Save package dependencies.
- Use basic Git commands to track your work.
- Restart a notebook kernel and run all cells successfully.

## 1. Create a Project Directory

```bash
mkdir python-for-ml
cd python-for-ml
```

Recommended structure:

```text
python-for-ml/
├── data/
├── exercises/
├── mini_projects/
├── notebooks/
├── src/
├── .gitignore
├── README.md
└── requirements.txt
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# macOS or Linux
source .venv/bin/activate
```

Deactivate it:

```bash
deactivate
```

## 3. Install Required Packages

```bash
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas matplotlib scipy scikit-learn
```

Verify the installation:

```bash
python -c "import numpy, pandas, matplotlib, scipy, sklearn; print('Installation OK')"
```

Save dependencies:

```bash
python -m pip freeze > requirements.txt
```

Install dependencies later:

```bash
python -m pip install -r requirements.txt
```

## 4. Jupyter Notebook Essentials

Start Jupyter:

```bash
jupyter notebook
```

Important notebook concepts:

- A **Code cell** contains executable Python.
- A **Markdown cell** contains headings, explanations, formulas, and conclusions.
- `Shift + Enter` runs the current cell and moves to the next cell.
- A **kernel** is the Python process that stores variables and runs code.
- Cell execution order matters because the kernel keeps state.
- Before submitting work, use **Restart Kernel and Run All Cells**.
- A notebook is reproducible only when it runs from top to bottom without hidden state.

Recommended notebook structure:

```markdown
# Topic or Project Name

## 1. Objectives

## 2. Imports and Configuration

## 3. Load Data

## 4. Explore Data

## 5. Process Data

## 6. Results

## 7. Conclusions

## 8. Questions and Limitations
```

## 5. Basic Git Workflow

```bash
git init
git status
git add .
git commit -m "Initialize Python for ML roadmap"
```

A minimal `.gitignore`:

```text
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
```

## Common Mistakes

- Installing packages outside the activated virtual environment.
- Running `pip` from a different Python installation.
- Executing notebook cells out of order.
- Storing large datasets or virtual environments in Git.
- Forgetting to restart the kernel before checking reproducibility.

## Exercises

1. Create the recommended directory structure.
2. Create and activate `.venv`.
3. Install all required packages.
4. Create `notebooks/00_environment_check.ipynb`.
5. Import NumPy, pandas, Matplotlib, and Scikit-Learn.
6. Print each library version.
7. Restart the kernel and run the notebook from top to bottom.
8. Commit the project to Git.

## Exit Criteria

You are ready for Week 1 when:

- Your virtual environment activates correctly.
- All required libraries import without errors.
- Your notebook runs from the first cell to the last cell after a kernel restart.
- Your repository contains a clear folder structure and an initial Git commit.

## English Vocabulary

| Term         | Simple definition                                              |
| ------------ | -------------------------------------------------------------- |
| environment  | an isolated place containing a Python interpreter and packages |
| dependency   | a package required by a project                                |
| kernel       | the process that executes notebook code                        |
| cell         | one executable or text block in a notebook                     |
| reproducible | able to produce the same result when run again                 |
| repository   | a project tracked by Git                                       |

---

# WEEK 1: PYTHON CORE FOR DATA PROCESSING

## Learning Objectives

By the end of this week, you should be able to:

- Use Python scalar types and convert between types.
- Write conditions and loops correctly.
- Choose between list, tuple, dictionary, and set.
- Use indexing, slicing, unpacking, and comprehensions.
- Process collections using `range()`, `enumerate()`, and `zip()`.
- Explain mutability and object identity.

## 1. Common Built-in Scalar Types

| Type       | Purpose            | Example              |
| ---------- | ------------------ | -------------------- |
| `int`      | whole numbers      | `42`                 |
| `float`    | decimal numbers    | `3.14`               |
| `str`      | text               | `"Machine Learning"` |
| `bool`     | logical values     | `True`, `False`      |
| `NoneType` | absence of a value | `None`               |

`None` is the single value of type `NoneType`.

```python
value = None
print(type(value))  # <class 'NoneType'>
```

## 2. Type Casting

```python
age_text = "20"
age = int(age_text)
score = float("8.5")
message = str(42)
is_valid = bool(1)
```

Be careful:

```python
bool("")       # False
bool("False")  # True because the string is not empty
bool(0)        # False
bool([])       # False
```

## 3. Mutability and Immutability

- **Immutable:** `int`, `float`, `str`, `bool`, `tuple`, `frozenset`.
- **Mutable:** `list`, `dict`, `set`.

```python
numbers = [1, 2, 3]
alias = numbers
alias.append(4)

print(numbers)  # [1, 2, 3, 4]
```

To create an independent list:

```python
copy_of_numbers = numbers.copy()
```

## 4. Operators

### Arithmetic Operators

```python
+  -  *  /  //  %  **
```

```python
7 / 2   # 3.5
7 // 2  # 3
7 % 2   # 1
2 ** 3  # 8
```

### Comparison Operators

```python
==  !=  <  <=  >  >=
```

### Logical Operators

```python
and  or  not
```

### Membership Operators

```python
in  not in
```

### Identity Operators

```python
is  is not
```

Use `==` to compare values and `is` to compare object identity.

```python
value = None
if value is None:
    print("No value")
```

Do not use `is` to compare normal numbers or strings.

## 5. Conditional Statements

```python
score = 8.2

if score >= 8.0:
    grade = "Excellent"
elif score >= 6.5:
    grade = "Good"
elif score >= 5.0:
    grade = "Average"
else:
    grade = "Fail"
```

Python treats empty collections, zero, `None`, and empty strings as false-like values.

```python
items = []

if not items:
    print("The list is empty")
```

## 6. Loops

### `for` Loop

A `for` loop iterates over an iterable.

```python
for value in [10, 20, 30]:
    print(value)
```

### `while` Loop

A `while` loop repeats while its condition remains `True`.

```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

### Loop Control

```python
break     # exit the loop
continue  # skip to the next iteration
```

## 7. Loop Helper Functions

```python
for index in range(0, 10, 2):
    print(index)
```

```python
names = ["An", "Binh", "Chi"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

```python
names = ["An", "Binh", "Chi"]
scores = [8.5, 6.0, 9.0]

for name, score in zip(names, scores):
    print(name, score)
```

## 8. Core Data Structures

| Structure |         Syntax | Characteristics                                  | Typical Uses                         |
| --------- | -------------: | ------------------------------------------------ | ------------------------------------ |
| `list`    |        `[...]` | ordered, mutable, duplicates allowed             | dynamic sequences                    |
| `tuple`   |        `(...)` | ordered, immutable, duplicates allowed           | fixed records                        |
| `dict`    | `{key: value}` | insertion-ordered, unique hashable keys          | structured records and lookup tables |
| `set`     |        `{...}` | unique hashable elements, no positional indexing | deduplication and set operations     |

### List

```python
scores = [7.5, 8.0, 9.0]
scores.append(8.5)
scores.extend([6.5, 7.0])
scores.remove(7.5)
```

### Tuple

```python
point = (10, 20)
x, y = point
```

### Dictionary

```python
student = {
    "name": "An",
    "score": 8.5,
    "passed": True,
}

student["major"] = "Software Engineering"
score = student.get("score", 0.0)
```

Useful methods:

```python
student.keys()
student.values()
student.items()
```

### Set

```python
values = {1, 2, 2, 3}
print(values)  # {1, 2, 3}
```

Set operations:

```python
a | b  # union
a & b  # intersection
a - b  # difference
a ^ b  # symmetric difference
```

## 9. Indexing and Slicing

```python
values = [10, 20, 30, 40, 50]

values[0]       # 10
values[-1]      # 50
values[1:4]     # [20, 30, 40]
values[:3]      # [10, 20, 30]
values[::2]     # [10, 30, 50]
values[::-1]    # reversed copy
```

The stop position is excluded.

## 10. Unpacking

```python
first, second = (10, 20)
first, *middle, last = [1, 2, 3, 4, 5]
```

## 11. Comprehensions

### List Comprehension

```python
squares = [number ** 2 for number in range(10)]
even_squares = [number ** 2 for number in range(10) if number % 2 == 0]
```

### Dictionary Comprehension

```python
word_lengths = {word: len(word) for word in ["model", "data", "feature"]}
```

### Set Comprehension

```python
unique_lengths = {len(word) for word in ["cat", "dog", "python"]}
```

Use a normal loop instead of a comprehension when the logic becomes difficult to read.

## 12. Useful Built-in Functions

```python
len()
sum()
min()
max()
sorted()
round()
any()
all()
```

```python
scores = [8.0, 6.5, 9.0]

all(score >= 5 for score in scores)  # True
any(score >= 9 for score in scores)  # True
```

## Practical Example: Clean and Summarize Names

```python
raw_names = ["  Alice", "BOB ", "", " alice ", None, "Charlie"]

cleaned_names = {
    name.strip().lower()
    for name in raw_names
    if isinstance(name, str) and name.strip()
}

result = sorted(cleaned_names)
print(result)  # ['alice', 'bob', 'charlie']
```

## Common Mistakes

- Writing `while condition is False` instead of understanding that `while` repeats while the condition is `True`.
- Using `is` instead of `==` for value comparison.
- Modifying a list while iterating over it.
- Forgetting that slicing excludes the stop index.
- Assuming a set preserves positional order or supports indexing.
- Creating aliases accidentally instead of independent copies.
- Writing overly complex one-line comprehensions.

## Exercises

### Exercise 1: Frequency Table

```python
values = [12, 7, 9, 12, 15, 7, 21, 9, 12]
```

Create:

```python
{
    12: 3,
    7: 2,
    9: 2,
    15: 1,
    21: 1,
}
```

Do not use an external library.

### Exercise 2: Student Records

```python
names = ["An", "Binh", "Chi"]
scores = [8.5, 6.0, 9.0]
```

Create:

```python
[
    {"name": "An", "score": 8.5},
    {"name": "Binh", "score": 6.0},
    {"name": "Chi", "score": 9.0},
]
```

### Exercise 3: Diagnostic Challenge

Given:

```python
scores = [7.5, 8.0, 5.5, 9.0, 6.5, 8.5, 4.0]
```

Write a program that:

- Calculates the mean.
- Finds the minimum and maximum.
- Counts scores greater than or equal to 8.
- Collects failing scores below 5.
- Assigns `Excellent`, `Good`, `Average`, or `Fail` to every score.

## Exit Criteria

You are ready for Week 2 when you can:

- Solve collection filtering and transformation tasks without looking up `for`, `if`, `dict`, or comprehension syntax.
- Explain the difference between equality and identity.
- Choose an appropriate core data structure for a given problem.
- Predict whether an operation mutates the original object.

## English Vocabulary

| Term       | Simple definition                          |
| ---------- | ------------------------------------------ |
| statement  | an instruction executed by Python          |
| expression | code that produces a value                 |
| assignment | storing a value in a variable              |
| iterable   | an object that can be looped over          |
| mutable    | changeable in place                        |
| immutable  | not changeable in place                    |
| membership | whether a value exists inside a collection |
| identity   | whether two names refer to the same object |

---

# WEEK 2: FUNCTIONS, MODULES & ERROR HANDLING

## Learning Objectives

By the end of this week, you should be able to:

- Design small functions with clear inputs and outputs.
- Use positional, keyword, and default arguments.
- Write type hints and useful docstrings.
- Organize code into modules.
- Read and write files safely.
- Validate inputs and raise meaningful exceptions.
- Read a traceback and identify the line causing an error.

## 1. Function Declaration and Return Values

```python
def square(number: float) -> float:
    return number ** 2
```

A function returns `None` when no `return` value is provided.

```python
def display_message(message: str) -> None:
    print(message)
```

## 2. Parameters and Arguments

```python
def calculate_total(price: float, quantity: int = 1) -> float:
    return price * quantity

calculate_total(10.0)
calculate_total(10.0, 3)
calculate_total(price=10.0, quantity=3)
```

- **Parameter:** a name in the function definition.
- **Argument:** a value supplied when calling the function.
- Non-default parameters must appear before default parameters.

## 3. Avoid Mutable Default Arguments

Do not write:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Use `None` instead:

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

## 4. Type Hints

```python
def calculate_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

Type hints improve readability and tool support, but Python does not enforce them automatically at runtime.

Common forms:

```python
list[int]
dict[str, float]
tuple[int, int]
str | None
```

## 5. Docstrings

```python
def calculate_mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list.

    Args:
        values: Numeric values to summarize.

    Returns:
        The arithmetic mean.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

## 6. Variable Scope: LEGB

Python resolves names in this order:

1. **Local:** current function.
2. **Enclosing:** outer nested function.
3. **Global:** module level.
4. **Built-in:** Python-provided names such as `len` and `sum`.

Avoid overwriting built-in names:

```python
# Avoid
list = [1, 2, 3]
sum = 10
```

## 7. Pure Functions and Side Effects

A pure function:

- Depends only on its inputs.
- Returns a value.
- Does not unexpectedly modify external state.

```python
def normalized_copy(values: list[float]) -> list[float]:
    maximum = max(values)
    return [value / maximum for value in values]
```

A side effect includes changing a global variable, modifying an input object, writing a file, or printing output.

## 8. Modules and Imports

Create `statistics_utils.py`:

```python
def calculate_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

Import it:

```python
import statistics_utils

result = statistics_utils.calculate_mean([1.0, 2.0, 3.0])
```

Other import forms:

```python
import numpy as np
from pathlib import Path
from statistics_utils import calculate_mean
```

Prefer explicit imports and avoid:

```python
from module import *
```

## 9. File Paths with `pathlib`

```python
from pathlib import Path

project_root = Path.cwd()
data_path = project_root / "data" / "scores.txt"
```

## 10. File Input and Output

```python
from pathlib import Path

path = Path("data") / "scores.txt"

with path.open("r", encoding="utf-8") as file:
    content = file.read()
```

Write a file:

```python
with path.open("w", encoding="utf-8") as file:
    file.write("8.5\n7.0\n9.0\n")
```

Common modes:

| Mode | Meaning                              |
| ---- | ------------------------------------ |
| `r`  | read; fail if file does not exist    |
| `w`  | write; create or replace file        |
| `a`  | append to the end of a file          |
| `x`  | create a new file; fail if it exists |
| `b`  | binary mode                          |

## 11. Exceptions

```python
def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("denominator must not be zero")

    return numerator / denominator
```

Handling exceptions:

```python
try:
    result = safe_divide(10, 0)
except ValueError as error:
    print(f"Invalid input: {error}")
else:
    print(result)
finally:
    print("Finished")
```

Catch specific exceptions instead of using a broad `except:` block.

## 12. Assertions

Assertions verify internal assumptions during development.

```python
score = 8.5
assert 0 <= score <= 10, "score must be between 0 and 10"
```

Do not use `assert` to validate untrusted user input in production code because assertions can be disabled.

## 13. Reading a Traceback

Common exceptions:

| Exception             | Typical cause                                     |
| --------------------- | ------------------------------------------------- |
| `SyntaxError`         | invalid Python syntax                             |
| `NameError`           | undefined variable                                |
| `TypeError`           | operation applied to an incompatible type         |
| `ValueError`          | valid type but invalid value                      |
| `IndexError`          | invalid sequence index                            |
| `KeyError`            | missing dictionary key                            |
| `AttributeError`      | object does not have the requested attribute      |
| `FileNotFoundError`   | requested file does not exist                     |
| `ModuleNotFoundError` | module is unavailable or environment is incorrect |

Debugging process:

1. Read the final line of the traceback.
2. Identify the exception type and message.
3. Find the first relevant line from your own code.
4. Inspect values, types, and shapes.
5. Reduce the problem to the smallest reproducible example.

## 14. Lightweight Testing

```python
def calculate_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)


assert calculate_mean([1.0, 2.0, 3.0]) == 2.0
assert calculate_mean([5.0]) == 5.0
```

Floating-point comparisons should allow tolerance:

```python
import math

assert math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)
```

## Practical Example: Statistics Module

```python
from math import sqrt


def calculate_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)


def calculate_variance(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")

    mean = calculate_mean(values)
    return sum((value - mean) ** 2 for value in values) / len(values)


def calculate_standard_deviation(values: list[float]) -> float:
    return sqrt(calculate_variance(values))
```

## Common Mistakes

- Writing one function that performs many unrelated tasks.
- Forgetting to return a value.
- Using mutable default arguments.
- Catching every exception and hiding the real error.
- Mixing input/output, calculations, and formatting in the same function.
- Overwriting built-in names such as `list`, `dict`, `sum`, or `max`.
- Using relative file paths without knowing the current working directory.

## Exercises

Create `src/statistics_utils.py` with:

```text
calculate_mean()
calculate_median()
calculate_variance()
calculate_standard_deviation()
normalize_values()
find_outliers()
```

Requirements:

- Use type hints.
- Write docstrings.
- Validate empty input.
- Do not use NumPy.
- Add at least three test cases for every function.
- Import and use the module from a notebook.

## Exit Criteria

You are ready for Week 3 when you can:

- Split a long script into small, reusable functions.
- Explain each function's input, output, and failure cases.
- Organize functions in a module and import them.
- Read a traceback and fix common errors without guessing randomly.

## English Vocabulary

| Term         | Simple definition                            |
| ------------ | -------------------------------------------- |
| function     | a reusable block of code                     |
| parameter    | a name in a function definition              |
| argument     | a value supplied to a function call          |
| return value | the result produced by a function            |
| scope        | the region where a name is available         |
| exception    | an object representing a runtime error       |
| raise        | intentionally create an exception            |
| handle       | catch and respond to an exception            |
| side effect  | a change outside a function's returned value |

---

# WEEK 3: OOP JUST ENOUGH FOR MACHINE LEARNING

## Learning Objectives

By the end of this week, you should be able to:

- Explain the difference between a class and an object.
- Define instance attributes and methods.
- Understand `__init__`, `self`, `__repr__`, inheritance, and composition.
- Read Scikit-Learn-style estimator code.
- Explain hyperparameters versus learned attributes.
- Implement a small transformer with `fit()`, `transform()`, and `fit_transform()`.

## 1. Classes and Objects

- A **class** is a blueprint describing data and behavior.
- An **object** or **instance** is a concrete value created from a class.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

`LinearRegression` is a class. `model` is an instance.

## 2. Constructor and `self`

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
```

- `__init__` initializes a new instance.
- `self` refers to the current instance.

## 3. Instance Attributes and Methods

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def has_passed(self) -> bool:
        return self.score >= 5.0
```

## 4. Class Attributes

```python
class Student:
    pass_score = 5.0

    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
```

A class attribute is shared unless an instance overrides it.

## 5. Object Representation

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, score={self.score})"
```

## 6. Properties

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self._score = score

    @property
    def score(self) -> float:
        return self._score
```

Properties allow controlled attribute access. Do not add them unless they improve the API or validation.

## 7. Basic Inheritance

```python
class BaseTransformer:
    def fit(self, X, y=None):
        return self


class IdentityTransformer(BaseTransformer):
    def transform(self, X):
        return X
```

Inheritance represents an **is-a** relationship. Prefer composition when objects simply work together.

## 8. Composition

```python
class Pipeline:
    def __init__(self, scaler, model):
        self.scaler = scaler
        self.model = model
```

A pipeline **has a** scaler and **has a** model.

## 9. Underscore Conventions

| Form                 | Meaning                                                   |
| -------------------- | --------------------------------------------------------- |
| `_internal`          | internal-use convention; not enforced privacy             |
| `learned_attribute_` | Scikit-Learn convention for values learned during `fit()` |
| `__name`             | name mangling inside a class                              |
| `__init__`           | special or “dunder” method                                |

Examples of Scikit-Learn learned attributes:

```python
model.coef_
model.intercept_
encoder.categories_
imputer.statistics_
```

## 10. Reading a Machine Learning Class

Ask these questions:

1. What hyperparameters are passed to `__init__`?
2. What values are learned and stored during `fit()`?
3. Which methods mutate internal state?
4. Which methods return transformed data or predictions?
5. What input shape does each method expect?
6. What happens if `transform()` or `predict()` is called before `fit()`?

## 11. Scikit-Learn-Style API

- `fit(X, y=None)` learns information from training data.
- `transform(X)` applies a learned transformation.
- `fit_transform(X, y=None)` fits and transforms.
- `predict(X)` produces predictions.
- `score(X, y)` returns a model-dependent performance measure.

Calling `fit()` only on training data helps prevent data leakage. Learned statistics from validation or test data must not influence training.

## Practical Example: Custom Standard Scaler

```python
import numpy as np


class CustomStandardScaler:
    """A small StandardScaler-like transformer for two-dimensional data."""

    def __init__(self, with_mean: bool = True):
        self.with_mean = with_mean
        self.mean_: np.ndarray | None = None
        self.scale_: np.ndarray | None = None

    def fit(self, X, y=None):
        """Learn column means and standard deviations from X."""
        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a two-dimensional array")

        if X.shape[0] == 0:
            raise ValueError("X must contain at least one row")

        if self.with_mean:
            self.mean_ = X.mean(axis=0)
        else:
            self.mean_ = np.zeros(X.shape[1], dtype=float)

        self.scale_ = X.std(axis=0)
        self.scale_ = np.where(self.scale_ == 0, 1.0, self.scale_)
        return self

    def transform(self, X):
        """Standardize X using statistics learned during fit."""
        if self.mean_ is None or self.scale_ is None:
            raise RuntimeError("Call fit() before transform()")

        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a two-dimensional array")

        if X.shape[1] != self.mean_.shape[0]:
            raise ValueError("X has a different number of features")

        return (X - self.mean_) / self.scale_

    def fit_transform(self, X, y=None):
        """Fit the scaler and transform X in one step."""
        return self.fit(X, y).transform(X)

    def __repr__(self) -> str:
        return f"CustomStandardScaler(with_mean={self.with_mean})"
```

Usage:

```python
X_train = [
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0],
]

scaler = CustomStandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_new_scaled = scaler.transform([[4.0, 40.0]])
```

## Common Mistakes

- Treating class attributes and instance attributes as the same thing.
- Forgetting `self` in instance methods.
- Storing learned information before calling `fit()`.
- Recomputing statistics inside `transform()` and causing leakage.
- Dividing by zero when a feature has zero variance.
- Using inheritance when simple composition would be clearer.
- Making every attribute “private” without a practical reason.

## Exercises

### Exercise 1: Student Dataset Class

Create a `StudentDataset` class with:

```text
add_record()
summary()
filter_by_score()
get_average_score()
__len__()
__repr__()
```

### Exercise 2: Min-Max Scaler

Create a `CustomMinMaxScaler` with:

```text
fit()
transform()
fit_transform()
```

It must:

- Work with 2D numeric data.
- Store `min_` and `range_` learned during fitting.
- Handle constant columns safely.
- Reject mismatched feature counts.

## Exit Criteria

You are ready for Week 4 when you can:

- Read a class and identify its state and behavior.
- Explain why `fit()` must precede `transform()` or `predict()`.
- Distinguish hyperparameters from learned parameters.
- Implement and test a small stateful transformer.

## English Vocabulary

| Term        | Simple definition                         |
| ----------- | ----------------------------------------- |
| class       | a blueprint for objects                   |
| instance    | one object created from a class           |
| attribute   | data stored on an object                  |
| method      | a function attached to a class            |
| constructor | the initialization method of a new object |
| inheritance | reusing behavior from a parent class      |
| composition | building an object from other objects     |
| state       | values currently stored inside an object  |
| fitted      | having learned parameters from data       |

---

# WEEK 4: NUMPY — VECTORIZED COMPUTATION & MATRICES

## Learning Objectives

By the end of this week, you should be able to:

- Create and inspect NumPy arrays.
- Interpret shape as `(samples, features)`.
- Index, slice, reshape, and transpose arrays.
- Use boolean masks and vectorized operations.
- Aggregate values along the correct axis.
- Explain broadcasting.
- Perform matrix multiplication.
- Handle missing values and random generation.
- Convert between NumPy arrays and pandas objects.

## 1. Creating Arrays

```python
import numpy as np

vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
identity = np.eye(3)
sequence = np.arange(0, 10, 2)
evenly_spaced = np.linspace(0, 1, 5)
```

## 2. Important Array Attributes

```python
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

X.shape  # (2, 3)
X.ndim   # 2
X.size   # 6
X.dtype  # usually float64
```

For Machine Learning:

```python
X.shape == (n_samples, n_features)
y.shape == (n_samples,)
```

- Rows normally represent samples or instances.
- Columns normally represent features.

## 3. Data Types and Conversion

```python
values = np.array([1, 2, 3], dtype=float)
integers = values.astype(int)
```

A NumPy array normally stores one data type across all elements.

## 4. Indexing and Slicing

```python
X[0, 1]      # one value
X[0]         # first row
X[:, 1]      # second column as a 1D array
X[:, 1:2]    # second column as a 2D array
X[:2, :2]    # first two rows and columns
```

Shape difference:

```python
X[:, 1].shape    # (2,)
X[:, 1:2].shape  # (2, 1)
```

## 5. Boolean Masking

```python
values = np.array([2, -1, 5, -3, 8])
positive_values = values[values > 0]
```

Multiple conditions require parentheses:

```python
selected = values[(values >= 0) & (values <= 5)]
```

Use `&`, `|`, and `~` for array masks, not `and`, `or`, and `not`.

## 6. `np.where()`

```python
scores = np.array([4.0, 6.5, 8.0])
labels = np.where(scores >= 5.0, "pass", "fail")
```

Replace values conditionally:

```python
clipped_scores = np.where(scores < 5.0, 5.0, scores)
```

## 7. Reshaping and Transposing

```python
values = np.arange(12)
X = values.reshape(3, 4)
column_vector = values.reshape(-1, 1)
transposed = X.T
```

`-1` asks NumPy to infer the dimension.

## 8. Vectorized Operations

```python
values = np.array([1.0, 2.0, 3.0])

values + 10
values * 2
values ** 2
np.sqrt(values)
np.exp(values)
np.log(values)
```

Prefer vectorized operations over Python loops for numerical arrays.

## 9. Broadcasting

Broadcasting allows operations between compatible shapes.

```python
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

column_means = X.mean(axis=0)
centered = X - column_means
```

Shapes:

```text
X:            (2, 3)
column_means:    (3,)
result:       (2, 3)
```

Two dimensions are compatible when they are equal or one of them is `1`, comparing from the final dimension backward.

## 10. Aggregation and Axes

```python
X.sum()
X.mean()
X.min()
X.max()
X.std()
```

```python
X.mean(axis=0)  # one result per column; collapses rows
X.mean(axis=1)  # one result per row; collapses columns
```

Use `keepdims=True` when a retained 2D shape is helpful:

```python
column_means = X.mean(axis=0, keepdims=True)
```

## 11. Combining Arrays

```python
a = np.array([[1], [2]])
b = np.array([[3], [4]])

np.concatenate([a, b], axis=1)
np.hstack([a, b])
np.vstack([a.T, b.T])
np.c_[a, b]
```

`np.c_` is commonly used to combine columns in compact examples.

## 12. Unique Values and Counts

```python
labels = np.array(["cat", "dog", "cat", "bird"])
unique_labels, counts = np.unique(labels, return_counts=True)
```

## 13. Linear Algebra

### Dot Product and Matrix Multiplication

```python
X = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])

weights = np.array([0.5, 1.5])
predictions = X @ weights
```

For a linear model:

```text
y = Xw + b
```

### Useful Functions

```python
np.linalg.norm()
np.linalg.solve()
np.linalg.inv()  # use carefully; solving directly is usually preferable
```

## 14. Copies and Views

A basic slice often shares memory with the original array.

```python
values = np.array([1, 2, 3, 4])
view = values[1:3]
view[0] = 99

print(values)  # [1, 99, 3, 4]
```

Create an independent copy:

```python
independent = values[1:3].copy()
```

## 15. Missing Values

```python
values = np.array([1.0, np.nan, 3.0])

np.isnan(values)
np.nanmean(values)
np.nansum(values)
np.nanmedian(values)
```

## 16. Random Number Generation

Recommended modern API:

```python
rng = np.random.default_rng(42)

uniform_values = rng.uniform(0, 1, size=5)
normal_values = rng.normal(0, 1, size=5)
random_integers = rng.integers(0, 10, size=5)
permutation = rng.permutation(10)
```

Legacy code often uses:

```python
np.random.seed(42)
np.random.rand(5)
np.random.randn(5)
```

You should recognize the legacy form when reading older notebooks, but prefer `default_rng()` in new code.

## 17. NumPy and pandas Conversion

```python
array = dataframe.to_numpy()
series_array = dataframe["score"].to_numpy()
```

```python
import pandas as pd

frame = pd.DataFrame(array, columns=["feature_1", "feature_2"])
```

## Practical Examples

```python
import numpy as np

# Vectorized scaling
values = np.array([1.0, 2.0, 3.0, 4.0])
scaled_values = values * 2.5

# Aggregation by axis
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

column_means = matrix.mean(axis=0)
row_sums = matrix.sum(axis=1)

# Missing values and boolean masking
X = np.array([1.0, np.nan, 3.0, 8.0])
X_clean = X[~np.isnan(X)]

# Linear prediction
features = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
weights = np.array([0.5, 1.5])
predictions = features @ weights
```

## Common Mistakes

- Confusing `(n,)` with `(n, 1)`.
- Using `and` or `or` on NumPy arrays.
- Aggregating along the wrong axis.
- Assuming every slice is an independent copy.
- Mixing incompatible shapes and not checking broadcasting.
- Using loops where a vectorized operation is clearer.
- Forgetting that integer arrays cannot store `NaN` without conversion to floating-point.
- Comparing floating-point values using exact equality.

## Exercises

Given:

```python
scores = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 9.5, 8.5],
    [4.0, 6.0, 5.0],
])
```

Complete these tasks without loops for the main calculations:

1. Calculate the mean score for each student.
2. Calculate the mean score for each subject.
3. Find the student with the highest mean.
4. Standardize every column.
5. Select students whose scores are all at least 5.
6. Replace every score below 5 with 5.
7. Add a fourth column containing each student's overall mean.
8. Explain the shape after every operation.

## Exit Criteria

You are ready for Week 5 when you can:

- Interpret a 2D array as samples and features.
- Predict output shapes before running code.
- Use vectorized expressions instead of element-by-element loops.
- Select the correct axis for row-wise or column-wise calculations.
- Explain when broadcasting will or will not work.

## English Vocabulary

| Term       | Simple definition                                              |
| ---------- | -------------------------------------------------------------- |
| array      | values arranged in one or more dimensions                      |
| dimension  | one axis of an array                                           |
| shape      | the size of every dimension                                    |
| axis       | a direction along which an operation is performed              |
| vectorized | performed on an entire array rather than one element at a time |
| broadcast  | expand compatible shapes during computation                    |
| aggregate  | combine many values into a summary                             |
| transpose  | exchange rows and columns                                      |
| mask       | a Boolean array used for selection                             |

---

# WEEK 5: PANDAS — DATA MANIPULATION & ANALYSIS

## Learning Objectives

By the end of this week, you should be able to:

- Load and inspect an unfamiliar CSV file.
- Select rows and columns correctly with `loc` and `iloc`.
- Detect and handle missing values and duplicates.
- Convert data types and clean text columns.
- Create new features with vectorized operations.
- Group, aggregate, merge, and reshape data.
- Calculate correlations and create categories.
- Convert between DataFrames and NumPy arrays.
- Export a cleaned dataset.

## 1. Series and DataFrame

- A **Series** is a one-dimensional labeled array.
- A **DataFrame** is a two-dimensional labeled table whose columns may have different data types.

```python
import pandas as pd

series = pd.Series([10, 20, 30], name="score")

frame = pd.DataFrame({
    "name": ["An", "Binh", "Chi"],
    "score": [8.5, 6.0, 9.0],
})
```

## 2. Load and Save Data

```python
df = pd.read_csv("data/students.csv")
df.to_csv("data/students_clean.csv", index=False)
```

Useful `read_csv()` arguments:

```python
pd.read_csv(
    "data.csv",
    usecols=["name", "score"],
    dtype={"name": "string"},
    na_values=["", "NA", "unknown"],
)
```

## 3. Initial Inspection Checklist

```python
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())
print(df.describe(include="all"))
print(df.isna().sum())
print(df.duplicated().sum())
print(df.nunique())
```

Interpretation:

- `shape` gives `(rows, columns)`.
- `info()` shows column types and non-null counts.
- `describe()` summarizes numerical columns by default.
- `value_counts()` is useful for categorical columns.

## 4. Column Selection

```python
scores = df["score"]
subset = df[["name", "score"]]
```

Selecting one column returns a Series. Selecting a list of columns returns a DataFrame.

## 5. `loc` and `iloc`

```python
selected = df.loc[df["score"] >= 8.0, ["name", "score"]]
```

```python
first_rows = df.iloc[:5, :3]
```

- `loc` is label-based.
- `iloc` is integer-position-based.

## 6. Boolean Filtering

```python
high_scores = df[df["score"] >= 8.0]
```

Multiple conditions:

```python
selected = df[
    (df["score"] >= 8.0)
    & (df["attendance_rate"] >= 0.8)
]
```

Use parentheses around every condition.

Useful methods:

```python
df["major"].isin(["AI", "Software Engineering"])
df["score"].between(5.0, 10.0)
```

## 7. Copying Data Safely

```python
working_df = df.copy()
```

Create an explicit copy before experimentation when you want to preserve the original DataFrame.

## 8. Drop, Rename, and Reset Index

```python
df = df.drop(columns=["unused_column"])
```

```python
df = df.rename(columns={"Final Score": "final_score"})
```

```python
df = df.reset_index(drop=True)
```

## 9. Missing Values

Detect missing values:

```python
df.isna()
df.isna().sum()
```

Remove missing rows:

```python
df = df.dropna(subset=["score"])
```

Fill missing values:

```python
median_score = df["score"].median()
df["score"] = df["score"].fillna(median_score)
df["major"] = df["major"].fillna("Unknown")
```

Do not compute imputation statistics from validation or test data in a Machine Learning workflow.

## 10. Duplicate Values

```python
df.duplicated()
df.duplicated(subset=["student_id"])
df = df.drop_duplicates()
```

Before removing duplicates, decide whether they are accidental duplicates or valid repeated events.

## 11. Data Type Conversion

```python
df["student_id"] = df["student_id"].astype("string")
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["major"] = df["major"].astype("category")
```

## 12. Cleaning Text Columns

```python
df["name"] = df["name"].astype("string").str.strip().str.title()
df["major"] = df["major"].astype("string").str.strip().str.lower()
```

Useful string methods:

```python
.str.lower()
.str.upper()
.str.strip()
.str.replace()
.str.contains()
```

## 13. Sorting and Counts

```python
df = df.sort_values(by="score", ascending=False)
major_counts = df["major"].value_counts(dropna=False)
proportions = df["major"].value_counts(normalize=True)
```

## 14. Feature Creation

Prefer vectorized operations:

```python
df["average_score"] = (
    df["assignment_score"] * 0.2
    + df["midterm_score"] * 0.3
    + df["final_score"] * 0.5
)

df["passed"] = df["average_score"] >= 5.0
```

Conditional feature:

```python
df["score_level"] = pd.cut(
    df["average_score"],
    bins=[0, 5, 6.5, 8, 10],
    labels=["Fail", "Average", "Good", "Excellent"],
    include_lowest=True,
)
```

## 15. `apply()` Versus Vectorization

`apply()` can run a custom Python function, but vectorized pandas or NumPy operations are usually clearer and faster when available.

Prefer:

```python
df["tax"] = df["sales"] * 0.1
```

Use `apply()` only when a suitable vectorized method does not exist:

```python
def classify_score(score: float) -> str:
    if score >= 8.0:
        return "high"
    if score >= 5.0:
        return "medium"
    return "low"


df["score_group"] = df["score"].apply(classify_score)
```

## 16. Grouping and Aggregation

```python
summary = df.groupby("major", observed=False).agg(
    student_count=("student_id", "count"),
    mean_score=("average_score", "mean"),
    pass_rate=("passed", "mean"),
)
```

Other operations:

```python
df.groupby("major")["score"].mean()
df.groupby(["major", "gender"])["score"].agg(["count", "mean", "median"])
```

## 17. Merge and Join

```python
students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["An", "Binh", "Chi"],
})

scores = pd.DataFrame({
    "student_id": [1, 2, 4],
    "score": [8.5, 7.0, 9.0],
})

merged = students.merge(scores, on="student_id", how="left", validate="one_to_one")
```

Join types:

| Join    | Result                                        |
| ------- | --------------------------------------------- |
| `inner` | keys appearing in both tables                 |
| `left`  | every left-table row plus matching right data |
| `right` | every right-table row plus matching left data |
| `outer` | all keys from both tables                     |

## 18. Reshaping

Pivot table:

```python
pivot = pd.pivot_table(
    df,
    index="major",
    columns="gender",
    values="average_score",
    aggfunc="mean",
)
```

Long format:

```python
long_df = df.melt(
    id_vars=["student_id"],
    value_vars=["midterm_score", "final_score"],
    var_name="exam",
    value_name="score",
)
```

## 19. Correlation

```python
numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()
```

Correlation measures linear association and does not prove causation.

## 20. Sampling

```python
sample = df.sample(n=100, random_state=42)
fraction = df.sample(frac=0.1, random_state=42)
```

## 21. NumPy Conversion

```python
X = df[["study_hours", "attendance_rate"]].to_numpy()
y = df["average_score"].to_numpy()
```

## Practical Example

```python
import numpy as np
import pandas as pd


df = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105],
    "category": ["Tech", "Tech", "Furniture", "Furniture", np.nan],
    "sales": [250.0, 150.0, np.nan, 300.0, 450.0],
})

# Clean data
df["category"] = (
    df["category"]
    .fillna("Unassigned")
    .astype("category")
)

df["sales"] = df["sales"].fillna(df["sales"].median())

# Vectorized feature creation
df["tax"] = df["sales"] * 0.1

# Filter
high_sales = df.loc[
    df["sales"] > 200,
    ["customer_id", "category", "sales"],
]

# Aggregate
summary = df.groupby("category", observed=False).agg(
    total_sales=("sales", "sum"),
    average_sales=("sales", "mean"),
    customer_count=("customer_id", "count"),
)
```

## Common Mistakes

- Confusing a Series with a one-column DataFrame.
- Forgetting parentheses around multiple Boolean conditions.
- Modifying a filtered view and triggering `SettingWithCopyWarning`.
- Filling missing values without understanding why they are missing.
- Using `apply()` for work that could be vectorized.
- Merging on the wrong key and silently duplicating rows.
- Computing preprocessing statistics from the full dataset before splitting.
- Treating correlation as proof of causation.
- Using `inplace=True` everywhere and making transformations harder to reason about.

## Exercises

Use an unfamiliar CSV dataset and answer:

1. How many rows and columns are present?
2. What is the type of every column?
3. Which columns contain missing values?
4. How many duplicates exist?
5. What are the most frequent categorical values?
6. What is the mean, median, minimum, and maximum of each numerical column?
7. Which group has the highest mean target value?
8. Which columns appear strongly correlated?
9. Which new features might be useful?
10. Can the cleaned data be exported and loaded again correctly?

Required operations:

```text
head
info
describe
isna
duplicated
loc
iloc
groupby
agg
merge
corr
cut
copy
drop
rename
```

## Exit Criteria

You are ready for Week 6 when you can receive an unfamiliar CSV and, within approximately 45 minutes:

- Inspect its structure.
- Identify missing values and duplicates.
- Clean obvious quality issues.
- Create useful derived features.
- Summarize numerical and categorical columns.
- Aggregate by groups.
- Export a clean result.

## English Vocabulary

| Term          | Simple definition                                       |
| ------------- | ------------------------------------------------------- |
| row           | one record in a table                                   |
| column        | one variable or field in a table                        |
| missing value | an unavailable or unknown value                         |
| duplicate     | a repeated record                                       |
| filter        | keep rows that satisfy a condition                      |
| aggregate     | summarize multiple records                              |
| merge         | combine tables using matching keys                      |
| feature       | an input variable used by a model                       |
| distribution  | how values are spread across possible ranges            |
| correlation   | the strength of a linear relationship between variables |

---

# WEEK 6: MATPLOTLIB & JUPYTER

## Learning Objectives

By the end of this week, you should be able to:

- Choose an appropriate basic chart for a question.
- Create line, bar, histogram, and scatter plots.
- Add clear labels, titles, legends, and annotations.
- Use Matplotlib's figure and axes objects.
- Save figures for reports.
- Organize a complete data-analysis notebook.
- Prepare a reproducible notebook structure for the final mini-project.

## 1. Import Matplotlib

```python
import matplotlib.pyplot as plt
```

In modern Jupyter environments, plots usually display automatically. Calling `plt.show()` is still explicit and useful.

## 2. Four Core Chart Types

### Line Plot

Use for ordered or continuous sequences such as time or training loss.

```python
epochs = [1, 2, 3, 4, 5]
loss = [1.2, 0.9, 0.7, 0.6, 0.55]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(epochs, loss, marker="o", label="Training loss")
ax.set_title("Training Loss by Epoch")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
```

### Bar Chart

Use to compare categories.

```python
majors = ["AI", "Software", "Data Science"]
mean_scores = [8.1, 7.6, 8.4]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(majors, mean_scores)
ax.set_title("Mean Score by Major")
ax.set_xlabel("Major")
ax.set_ylabel("Mean score")
plt.show()
```

### Histogram

Use to inspect a numerical distribution.

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["average_score"].dropna(), bins=10, edgecolor="black")
ax.set_title("Distribution of Average Scores")
ax.set_xlabel("Average score")
ax.set_ylabel("Number of students")
plt.show()
```

### Scatter Plot

Use to investigate the relationship between two numerical variables.

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["study_hours"], df["average_score"], alpha=0.6)
ax.set_title("Study Hours vs. Average Score")
ax.set_xlabel("Study hours")
ax.set_ylabel("Average score")
plt.show()
```

## 3. Figure and Axes API

Recommended pattern:

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y)
ax.set_title("Title")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.show()
```

- `fig` represents the complete figure.
- `ax` represents one plotting area.

The object-oriented API is easier to manage in larger notebooks than relying only on global `plt` calls.

## 4. Multiple Plots

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df["average_score"].dropna(), bins=10)
axes[0].set_title("Score Distribution")

axes[1].scatter(df["study_hours"], df["average_score"], alpha=0.6)
axes[1].set_title("Study Hours vs. Score")

fig.tight_layout()
plt.show()
```

Use multiple subplots only when the charts should be compared directly. Separate figures are often easier to read.

## 5. Labels, Legends, and Annotation

```python
ax.set_title("Clear and Specific Title")
ax.set_xlabel("Input Variable")
ax.set_ylabel("Target Variable")
ax.legend()
ax.grid(True, alpha=0.3)
```

Annotation:

```python
ax.annotate(
    "Possible outlier",
    xy=(20, 95),
    xytext=(15, 90),
    arrowprops={"arrowstyle": "->"},
)
```

## 6. Saving a Figure

```python
fig.savefig(
    "reports/study_hours_vs_score.png",
    dpi=300,
    bbox_inches="tight",
)
```

Save before closing the figure.

## 7. pandas Plotting

pandas provides convenient plotting methods backed by Matplotlib.

```python
df["average_score"].hist(bins=10)
```

```python
df.plot(
    kind="scatter",
    x="study_hours",
    y="average_score",
    alpha=0.5,
)
```

Use pandas plotting for quick exploration and Matplotlib axes for finer control.

## 8. Visualization Checklist

Before accepting a chart, ask:

- Does the chart answer a specific question?
- Is the chart type appropriate?
- Are the title and axis labels clear?
- Are units shown where necessary?
- Are categories sorted meaningfully?
- Are missing values handled?
- Is the scale misleading?
- Are there too many labels or visual elements?
- Can a reader understand the chart without reading the code?

## 9. Jupyter Notebook Quality Checklist

A strong notebook should:

- Start with objectives and dataset description.
- Use Markdown cells to explain reasoning.
- Keep imports near the beginning.
- Avoid duplicate code.
- Store repeated operations in functions.
- Show key intermediate results, not every temporary variable.
- Include conclusions and limitations.
- Run from top to bottom after a kernel restart.
- Avoid absolute paths specific to one computer.

## Common Mistakes

- Drawing a chart without a clear analytical question.
- Using a line chart for unordered categories.
- Omitting axis labels or units.
- Plotting raw data without handling missing values.
- Creating many decorative elements that obscure the result.
- Relying on notebook state created by cells executed out of order.
- Saving a figure after it has been cleared or closed.
- Interpreting visual association as proof of causation.

---

# MINI-PROJECT HANDOFF

The detailed mini-project specification is stored outside this cheat sheet:

```text
mini_projects/student_performance/README.md
```

This cheat sheet only defines the prerequisite skills and completion standard. Complete the project after finishing Weeks 0–6.

## Project Completion Standard

The project is complete when you can:

- Load, validate, clean, and analyze an unfamiliar CSV dataset.
- Use Python functions, NumPy, pandas, and Matplotlib together.
- Create reusable code instead of repeating notebook cells.
- Explain findings, limitations, and assumptions.
- Restart the Jupyter kernel and run the notebook from top to bottom without errors.

See `mini_projects/student_performance/README.md` for the dataset schema, required analyses, visualizations, folder structure, and grading checklist.

---

# FINAL GRADUATION ASSESSMENT

You have completed the Python foundation when you can finish the following task in approximately three hours without following a step-by-step tutorial:

1. Receive an unfamiliar CSV file.
2. Create a clean notebook and project structure.
3. Load and inspect the data.
4. Handle missing values and duplicates appropriately.
5. Convert incorrect data types.
6. Create at least two useful features.
7. Use NumPy for a numerical transformation.
8. Group and aggregate results with pandas.
9. Draw at least three appropriate charts.
10. Write at least three reusable functions.
11. Explain five findings and three limitations.
12. Restart the kernel and run every cell without error.

## Self-Assessment Template

```markdown
## Self-Assessment

### What I can do without notes

-

### What I still need to look up

-

### Errors I encountered

-

### Concepts I cannot yet explain clearly

-

### My next practice task

-
```

---

# CORE ENGLISH GLOSSARY

| Term          | Simple English definition                                               | Vietnamese meaning          |
| ------------- | ----------------------------------------------------------------------- | --------------------------- |
| data type     | a category describing what a value represents                           | kiểu dữ liệu                |
| variable      | a name that refers to a value                                           | biến                        |
| collection    | an object containing multiple values                                    | cấu trúc chứa nhiều giá trị |
| iterable      | an object that can be processed in a loop                               | đối tượng có thể duyệt      |
| function      | reusable code with inputs and outputs                                   | hàm                         |
| argument      | a value supplied to a function                                          | đối số                      |
| parameter     | a named input in a function definition                                  | tham số                     |
| exception     | a runtime error object                                                  | ngoại lệ                    |
| array         | values arranged in dimensions                                           | mảng                        |
| shape         | the size of each array dimension                                        | kích thước các chiều        |
| axis          | a direction of an array operation                                       | trục                        |
| vectorized    | applied to an entire array at once                                      | được vector hóa             |
| DataFrame     | a labeled two-dimensional table                                         | bảng dữ liệu hai chiều      |
| missing value | an unavailable data value                                               | giá trị thiếu               |
| feature       | an input variable used by a model                                       | đặc trưng đầu vào           |
| target        | the value a model tries to predict                                      | biến mục tiêu               |
| distribution  | how values are spread                                                   | phân phối                   |
| correlation   | linear association between variables                                    | tương quan                  |
| fit           | learn parameters from data                                              | huấn luyện/khớp             |
| transform     | apply a learned data conversion                                         | biến đổi dữ liệu            |
| predict       | produce an estimated output                                             | dự đoán                     |
| data leakage  | unintended use of unavailable or evaluation information during training | rò rỉ dữ liệu               |
| reproducible  | able to run again with the same procedure and result                    | có thể tái lập              |

---

# RECOMMENDED COMPLETION CHECKLIST

```text
[ ] Week 0 environment notebook runs successfully
[ ] Week 1 diagnostic challenge completed
[ ] Week 2 statistics module implemented and tested
[ ] Week 3 custom transformer implemented
[ ] Week 4 NumPy matrix exercises completed without loops
[ ] Week 5 unfamiliar CSV analysis completed
[ ] Week 6 mini-project completed
[ ] Notebook restarts and runs from top to bottom
[ ] README contains setup and execution instructions
[ ] English glossary reviewed with spaced repetition
[ ] Final graduation assessment completed
```
