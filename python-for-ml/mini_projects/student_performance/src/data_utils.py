from pathlib import Path

import numpy as np
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

NUMERIC_COLUMNS = [
    "study_hours",
    "attendance_rate",
    "assignment_score",
    "midterm_score",
    "final_score",
]

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

def clean_student_data(df: pd.DataFrame,) -> pd.DataFrame:


    cleaned_df = df.copy(deep=True)

    # Chuẩn hóa tên cột
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
    )

    # Chuẩn hóa student ID
    cleaned_df["student_id"] = (
        cleaned_df["student_id"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    # Chuẩn hóa categorical values
    cleaned_df["gender"] = (
        cleaned_df["gender"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    cleaned_df["major"] = (
        cleaned_df["major"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # Chuyển các cột số về numeric
    for column in NUMERIC_COLUMNS:
        cleaned_df[column] = pd.to_numeric(
            cleaned_df[column],
            errors="coerce",
        )

    # Xóa dòng trùng hoàn toàn
    cleaned_df = cleaned_df.drop_duplicates()

    # Xóa dòng không có ID hợp lệ
    cleaned_df = cleaned_df.dropna(
        subset=["student_id"]
    )

    cleaned_df = cleaned_df[
        cleaned_df["student_id"] != ""
    ]

    # Mỗi sinh viên chỉ giữ một bản ghi
    cleaned_df = cleaned_df.drop_duplicates(
        subset=["student_id"],
        keep="first",
    )

    # Giá trị ngoài phạm vi được đổi thành missing
    cleaned_df.loc[
        cleaned_df["study_hours"] < 0,
        "study_hours",
    ] = np.nan

    cleaned_df.loc[
        ~cleaned_df["attendance_rate"].between(
            0,
            100,
        ),
        "attendance_rate",
    ] = np.nan

    for column in SCORE_COLUMNS:
        cleaned_df.loc[
            ~cleaned_df[column].between(0, 10),
            column,
        ] = np.nan

    # Điền missing bằng median của từng cột
    for column in NUMERIC_COLUMNS:
        median_value = cleaned_df[column].median()

        if pd.isna(median_value):
            raise ValueError(
                f"Cannot calculate median for {column}."
            )

        cleaned_df[column] = (
            cleaned_df[column]
            .fillna(median_value)
        )

    return cleaned_df.reset_index(drop=True)