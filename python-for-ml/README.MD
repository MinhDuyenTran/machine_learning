# Python for Machine Learning

## Learning Outcomes

By completing this roadmap, you will be able to perform the following tasks independently and confidently:

- [ ] **Python Core:** Proficiently use `list`, `dict`, `set`, `tuple`, and List/Dict Comprehensions.
- [ ] **Clean Code & Modularization:** Package data processing logic into resuable function/modules with type hints and docstrings.
- [ ] **Basic OOP:** Read and write simple classes aligned with the Scikit-Learn API paradigm(`fit`, `tranform`, `fit_transform`).
- [ ] **Numpy\*:** mulyi-dimesional arrays(`ndarray`), apply vectorization, broadcasting, and matrix operations without relying on `for` loops.
- [ ] **Matplotlib & Visualization:** Create line plots, bar charts, histograms, and scatter plots.
- [ ] **Jupyter Notebooks:** Structure readable notebooks, manage execution flow properly, and ehxplain findings using Markdown.
- [ ] **End-to-End Mini-Project:** Complete a small data analysis project from scratch.

## Reponsitory Structure

```text
python-for-ml/
├── notebooks/         # Jupyter Notebooks for lessons & EDA drafts
├── exercises/         # Weekly practical exercises
├── mini_projects/student_performance/  # End-to-end data analysis project
|   ├── data/
|   │   ├── raw/
|   │   └── processed/
|   ├── notebooks/
|   │   └── student_performance_analysis.ipynb
|   ├── reports/
|   │   └── figures/
|   ├── src/
|   │   └── data_utils.py
|   └── README.md    
├── data/              # Raw and processed datasets (.csv, .json)
├── README.md          # Roadmap documentation
└── requirements.txt   # Required Python packages
```

## Week Roadmap

### Week 0: Setup & Entry Assessment
Core Topics:
- Install Python & VS Code
- Set up a virtual environment
- Install core tools: `jupyter`, `numpy `, `pandas`, `matplotlib`.

### Week 1: Python Core for Data Processing
- Filter, transform, and aggregate data structures without needing to look up syntax for loops, conditions, or comprehensions.
- Core Topics:
   - [ ] Primitive Data Types: `int`, `float`, `str`, `bool`, `None` & Type Casting.
   - [ ] Control Flow: `if/elif/else`, `for`, `while`, `range()`, `enumerate()`, `zip()`.
   - [ ] Collections: `list`, `tuple`, `dict`, `set`  (Mutability, Indexing, Slicing).
   - [ ] Comprehensions: List and Dict comprehensions.

### Week 2: Functions, Modules & Error Handling
- Write reusable, testable code, implement type hints, and handle exceptions cleanly.
- Core Topics:
   - [ ] Paramenters & Arguments: Default paramenters, positional vs. keyword arguments.
   - [ ] Basic Type Hints & Docstrings (Google/NumPy style).
   - [ ] File I/O: Reading and writing files using context managers(`with`).
   - [ ] Exception Handling: `try...except...else...finally, raise ValueError, assert`.

### Week 3: Object-Oriented Programming for Machine Learning APIs
- Goal:Understand the class-based APIs used by Scikit-Learn and other Machine Learning libraries.
- Core Topics:
   - [ ] Classes and objects.
   - [ ] `__init__` and `self`.
   - [ ] Instance attributes and instance methods.
   - [ ] Class attributes at a basic level.
   - [ ] Basic inheritance and `super()`.
   - [ ] Composition.
   - [ ] `__repr__`.
   - [ ] `@property` at a recognition level.
   - [ ] Naming conventions involving `_` and `__`.
   - [ ] Difference between hyperparameters and learned attributes.
   - [ ] Why `fit()` must be called before `transform()` or `predict()`.

### Week 4: NumPy — Vectorized Computation and Matrices
- Goal: Replace element-by-element Python loops with efficient array and matrix operations.
- Core Topics:
   - [ ] Create `ndarray` objects.
   - [ ] Understand `shape`, `ndim`, `size`, and `dtype`.
   - [ ] Index and slice one-dimensional and multidimensional arrays.
   - [ ] Use Boolean masks.
   - [ ] Reshape and transpose arrays.
   - [ ] Understand broadcasting.
   - [ ] Use vectorized arithmetic.
   - [ ] Aggregate with `sum`, `mean`, `min`, `max`, and `std`.
   - [ ] Understand `axis=0` and `axis=1`.
   - [ ] Use `np.where()`, `np.concatenate()`, `np.vstack()`, `np.hstack()`, and `np.c_`.
   - [ ] Compute dot products and matrix multiplication with `@`.
   - [ ] Understand copies versus views.
   - [ ] Detect and handle `NaN`.
   - [ ] Use `np.random.default_rng()` for reproducible random data.

### Week 5: pandas — Data Manipulation and Analysis
- Goal: Load, inspect, clean, transform, aggregate, merge, and export tabular data.
- Core Topics:
   - [ ] `Series` and `DataFrame`.
   - [ ] `pd.read_csv()` and `DataFrame.to_csv()`.
   - [ ] `head()`, `tail()`, `shape`, `columns`, and `dtypes`.
   - [ ] `info()` and `describe()`.
   - [ ] Column and row selection.
   - [ ] `loc` and `iloc`.
   - [ ] Boolean filtering.
   - [ ] Sorting with `sort_values()`.
   - [ ] Missing values with `isna()`, `dropna()`, and `fillna()`.
   - [ ] Duplicate detection and removal.
   - [ ] `value_counts()`.
   - [ ] `groupby()` and `agg()`.
   - [ ] Creating new columns.
   - [ ] Prefer vectorized operations over `apply()` when possible.
   - [ ] Merging and joining DataFrames.
   - [ ] Categorical data.
   - [ ] `drop()`, `copy()`, `rename()`, `reset_index()`, `corr()`, and `pd.cut()`.
   - [ ] Convert between pandas and NumPy with `to_numpy()` and `pd.DataFrame()`.

### Week 6: Matplotlib, Jupyter, and Mini-Project Preparation
- Matplotlib Core Topics:
   - [ ] Line plots with plt.plot().
   - [ ] Bar charts with plt.bar() or pandas plotting.
   - [ ] Histograms with plt.hist().
   - [ ] Scatter plots with plt.scatter().
   - [ ] Figure size.
   - [ ] Titles and axis labels.
   - [ ] Legends.
   - [ ] Grid lines where useful.
   - [ ] plt.tight_layout().
   - [ ] Save figures with plt.savefig().
- Jupyter Core Topics:
   - [ ] Code cells and Markdown cells.
   - [ ] Run cells with Shift + Enter.
   - [ ] Understand the notebook kernel.
   - [ ] Restart the kernel.
   - [ ] Run all cells from top to bottom.
   - [ ] Avoid hidden state and out-of-order dependencies.
   - [ ] Explain code, results, and limitations in Markdown.
   - [ ] Use project-relative paths with pathlib.