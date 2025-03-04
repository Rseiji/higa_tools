"""Utilities for data validation."""

from itertools import chain, combinations
import pandas as pd

def validate_df_by_default(df: pd.DataFrame) -> pd.DataFrame:
    """Run some default validations on a pd.DataFrame.

    Parameters
    ----------
    df: pd.DataFrame
        A pandas DataFrame to validate
    """
    validations_frame = {}
    for validation in [
        lambda df: {"rowsize": df.shape[0],},
        _profile_duplicated_columns,
        _profile_columns_maxmin,
        _profile_none_count,
        _profile_string_columns_with_limit,
    ]:
        validations_frame.update(validation(df))
    return pd.DataFrame.from_dict(validations_frame, orient='index')


def _profile_duplicated_columns(df):
    # Generate all combinations of lengths 1 to the length of the list
    columns_combinations = [
        list(combinations(df.columns, i)) for i in range(1, len(df.columns) + 1)
    ]
    columns_combinations = [list(x) for x in chain(*columns_combinations)]
    combinations_with_duplicates = []

    for columns_combination in columns_combinations:
        if df[columns_combination].duplicated().any():
            combinations_with_duplicates.append([columns_combination])
    return {"columns_subsets_with_duplicates": combinations_with_duplicates}


def _profile_string_columns_with_limit(df, limit_records=10):
    output = {}
    for column in df.columns:
        if pd.api.types.is_string_dtype(df[column]):
            output.update(
                {
                    f"{column}_col_str_values": df[column].unique(),
                }
            )
    return output


def _profile_columns_maxmin(df):
    output = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            output.update(
                {
                    f"{column}_col_max": df[column].max(),
                    f"{column}_col_min": df[column].min(),
                }
            )
    return output


def _profile_none_count(df):
    output = {}
    for column in df.columns:
        output.update(
            {
                f"{column}_col_nan_count": df[column].isna().sum(),
            }
        )
    return output
