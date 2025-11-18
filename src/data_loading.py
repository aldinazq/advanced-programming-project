from __future__ import annotations

import pandas as pd

from src.config import get_paths, ensure_directories


def load_raw_disaster_data(filename: str = "disasters.csv") -> pd.DataFrame:
    """
    Load the raw disaster CSV file from the data/raw folder.

    Parameters
    ----------
    filename : str
        Name of the CSV file located in data/raw.

    Returns
    -------
    pd.DataFrame
        The loaded dataset as a pandas DataFrame.
    """
    # Get the standard project paths (data, results, etc.)
    paths = get_paths()

    # Make sure the expected folders (data/raw, results/...) exist
    ensure_directories(paths)

    # Build the full path to the CSV file
    csv_path = paths.data_raw / filename

    # If the file is missing, stop early with a clear error message
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Expected the file {csv_path} to exist.\n"
            "Place your raw CSV file in the 'data/raw' folder or pass a different "
            "filename to load_raw_disaster_data()."
        )

    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(csv_path)

    return df


def preview_dataframe(df: pd.DataFrame, n_rows: int = 5) -> None:
    """
    Print a small, human-readable summary of a dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to summarise.
    n_rows : int
        Number of rows to show from the top.
    """
    print("\n--- Data preview ---")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("Columns:", list(df.columns))
    print("\nFirst rows:")
    print(df.head(n_rows))
