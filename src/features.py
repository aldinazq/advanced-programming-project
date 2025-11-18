from __future__ import annotations

import numpy as np
import pandas as pd


def basic_cleaning(df: pd.DataFrame, target_column: str | None = None) -> pd.DataFrame:
    """
    I apply a few very simple cleaning steps to my raw dataframe.
    I want this function to stay general, so I only use information
    that I explicitly receive as arguments.
    """
    # I work on a copy so I do not accidentally modify the original dataframe in place
    cleaned = df.copy()

    # If I was given a target column and it exists, I drop rows where the target is missing
    if target_column is not None and target_column in cleaned.columns:
        cleaned = cleaned.dropna(subset=[target_column])

    # I remove exact duplicate rows, if any
    cleaned = cleaned.drop_duplicates()

    return cleaned


def add_simple_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    I create a few simple derived features that I may later use in my models.
    I only add a feature if the columns I need are present, so this stays general
    across different datasets.
    """
    # I start from a copy of the cleaned dataframe
    features = df.copy()

    # If I have fatalities, I add a log-transformed version to reduce the impact of extremes
    if "fatalities" in features.columns:
        features["log_fatalities"] = (features["fatalities"] + 1).apply(np.log)

    # If I have total_affected and population, I create a per-1000 indicator
    if {"total_affected", "population"}.issubset(features.columns):
        features["affected_per_1000"] = (
            1000 * features["total_affected"] / features["population"]
        )

    return features


def make_feature_table(df: pd.DataFrame, target_column: str | None = None) -> pd.DataFrame:
    """
    I take a raw dataframe and turn it into a cleaned and enriched feature table.
    I keep this function general by letting the caller decide what the target column is,
    or by leaving it unspecified.
    """
    # First I run a basic cleaning pass (optionally using the target column)
    cleaned = basic_cleaning(df, target_column=target_column)

    # Then I add simple derived features on top of the cleaned data
    features = add_simple_features(cleaned)

    # I return the final feature table
    return features
