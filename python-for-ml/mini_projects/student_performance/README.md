# STUDENT PERFORMANCE ANALYSIS

## Project Goal

Analyze a student-performance dataset and produce a reproducible notebook that loads, validates, cleans, explores, visualizes, and summarizes the data.

## Suggested columns:

student_id
gender
major
study_hours
attendance_rate
assignment_score
midterm_score
final_score

## Required Project Structure

```
mini_projects/student_performance/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── student_performance_analysis.ipynb
├── reports/
│   └── figures/
├── src/
│   └── data_utils.py
└── README.md
```

## 1. Problem Statement
- Write a short introduction explaining:
    - What the dataset represents.
    - Which questions you want to answer.
    - Which columns are inputs and which are outcomes.
    - What limitations you expect.

## 2. Load the Data
- Requirements:
    - Read the CSV with pandas.
    - Display the first five rows.
    - Report shape, columns, and data types.
    - Store the data path using pathlib.

## 3. Validate and Clean the Data
- Check:
    - Missing values.
    - Duplicates.
    - Invalid IDs.
    - Scores outside the valid range.
    - Attendance values outside the expected range.
    - Inconsistent category spelling and whitespace.
    - Numeric columns loaded as text.
    - Document every decision. Do not silently remove data.

## 4. Feature Engineering
Create at least these features:

```python
df["average_score"] = (
    df["assignment_score"] * 0.2
    + df["midterm_score"] * 0.3
    + df["final_score"] * 0.5
)

df["passed"] = df["average_score"] >= 5.0

Create a study-level category:

df["study_level"] = pd.cut(
    df["study_hours"],
    bins=[0, 5, 10, 20, float("inf")],
    labels=["Low", "Moderate", "High", "Very high"],
    include_lowest=True,
)
```
Add at least one original feature of your own and justify why it may be useful.

## 5. Analysis Questions
- Answer at least:
    - What is the overall average score?
    - What percentage of students passed?
    - Which major has the highest mean score?
    - Which major has the lowest pass rate?
    - Is study time associated with final performance?
    - Is attendance associated with performance?
    - Which students appear to be outliers?
    - Do any groups have noticeably different score distributions?

## 6. Required Visualizations
- Create at least five figures:
    - Histogram of average scores.
    - Bar chart of mean score by major.
    - Scatter plot of study hours versus average score.
    - Scatter plot of attendance versus average score.
    - Bar chart of pass and fail counts or rates.
    - Every figure must include:
    - Clear title.
    - Axis labels.
    - Appropriate units.
    - A one- or two-sentence interpretation below the chart.
    - Save important figures in reports/figures/.

## 7. Functions and Code Quality
- Implement at least three reusable functions, such as:
```
load_student_data()
validate_student_data()
clean_student_data()
calculate_summary()
create_score_features()
```

- Requirements:
    - Type hints.
    - Docstrings.
    - Input validation.
    - Clear variable names.
    - No repeated code blocks.
    - No unnecessary global variables.

## 8. Conclusions
- Write:
    - At least five findings in Vietnamese.
    - At least three findings in simple English.
    - At least five data limitations.
    - At least three additional features that would improve the analysis.
    - A clear statement explaining that correlation does not prove causation.

## 9. Reproducibility Test
- Before finishing:
    - Save the notebook.
    - Restart the kernel.
    - Run all cells from top to bottom.
    - Confirm no errors occur.
    - Confirm generated files use relative paths.
    - Export the cleaned dataset.
    - Update the README with execution instructions.

