from __future__ import annotations

import pandas as pd

from src.config import get_paths, ensure_directories


def load_raw_disaster_data(filename: str = "disasters.csv") -> pd.DataFrame:
    """
    I load the raw disaster CSV file from the data/raw folder.

    Parameters
    ----------
    filename : str
        I expect this to be the name of the CSV file located in data/raw.

    Returns
    -------
    pd.DataFrame
        I return the loaded dataset as a pandas DataFrame.
    """
    # I get the standard project paths (data, results, etc.)
    paths = get_paths()

    # I make sure the expected folders (data/raw, results/...) exist
    ensure_directories(paths)

    # I build the full path to the CSV file I want to load
    csv_path = paths.data_raw / filename

    # If the file is missing, I stop early with a clear error message
    if not csv_path.exists():
        raise FileNotFoundError(
            f"I expected the file {csv_path} to exist.\n"
            "I need you to place your raw CSV file in the 'data/raw' folder, "
            "or pass a different filename to load_raw_disaster_data()."
        )

    # I read the CSV into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # I return the dataframe so that other parts of my project can use it
    return df


def preview_dataframe(df: pd.DataFrame, n_rows: int = 5) -> None:
    """
    I print a small, human-readable summary of a dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        This is the dataframe I want to summarise.
    n_rows : int
        This is the number of rows I want to show from the top.
    """
    print("\n--- Data preview ---")
    print(f"I see a dataframe with {df.shape[0]} rows and {df.shape[1]} columns.")
    print("Columns:", list(df.columns))
    print("\nHere are the first rows:")
    print(df.head(n_rows))

