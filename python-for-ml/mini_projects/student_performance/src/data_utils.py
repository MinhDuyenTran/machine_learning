from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "student_id",
    "gender",
    "major",
    "study_hours",
    "attendance_rate",
    "assignment_score",
    "midterm_score",
    "final_score",
}


SCORE_COLUMNS = [
    "assignment_score",
    "midterm_score",
    "final_score",
]


def load_student_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(
            f"Data file not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            f"{sorted(missing_columns)}"
        )

    return df


def validate_student_data(df: pd.DataFrame,) -> dict[str, object]:
    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        return {
            "is_valid": False,
            "missing_columns": sorted(missing_columns),
        }

    missing_values = df.isna().sum().to_dict()

    invalid_scores = {
        column: int(
            (
                df[column].notna()
                & ~df[column].between(0, 10)
            ).sum()
        )
        for column in SCORE_COLUMNS
    }

    invalid_study_hours = int(
        (
            df["study_hours"].notna()
            & (df["study_hours"] < 0)
        ).sum()
    )

    invalid_attendance = int(
        (
            df["attendance_rate"].notna()
            & ~df["attendance_rate"].between(0, 100)
        ).sum()
    )

    report = {
        "is_valid": (
            sum(missing_values.values()) == 0
            and int(df.duplicated().sum()) == 0
            and int(df["student_id"].duplicated().sum()) == 0
            and invalid_study_hours == 0
            and invalid_attendance == 0
            and sum(invalid_scores.values()) == 0
        ),
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_columns": [],
        "missing_values": missing_values,
        "exact_duplicates": int(
            df.duplicated().sum()
        ),
        "duplicate_student_ids": int(
            df["student_id"].duplicated().sum()
        ),
        "invalid_study_hours": invalid_study_hours,
        "invalid_attendance": invalid_attendance,
        "invalid_scores": invalid_scores,
    }

    return report