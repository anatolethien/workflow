import sqlite3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def select_table(
    table_name: str,
) -> pd.DataFrame:
    """Fetch a specified SQLite3 table from `data/db.sqlite3` and return it as a
    DataFrame.

    Parameters
    ----------
    table_name : str
        The name of the SQLite table to select from.

    Returns
    ----------
    pd.DataFrame
        A DataFrame containing the specified table.
    """
    conn = sqlite3.connect("data/db.sqlite3")
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(
        sql=query,
        con=conn,
    )
    conn.close()
    return df


def insert_table(
    df: pd.DataFrame,
    table_name: str,
):
    """Insert a DataFrame into a SQLite3 database at `data/db.sqlite3`.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be inserted into the SQLite database.
    table_name : str
        The name of the SQLite table to insert the DataFrame into. If the table
        exists, it will be replaced.

    Returns
    -------
    None
        This function does not return a value.
    """
    conn = sqlite3.connect("data/db.sqlite3")
    df.to_sql(
        name=table_name,
        con=conn,
        index=True,
        if_exists="replace",
    )
    conn.close()


def remove_outliers(
    ser: pd.Series,
    z: float = 2.0,
) -> pd.Series:
    """Remove outliers from a Series based on a z-score threshold.

    Parameters
    ----------
    ser : pd.Series
        The Series from which to remove outliers.
    z : float, optional
        The z-score used as a threshold for identifying outliers. Default value
        is 2.

    Returns
    -------
    pd.Series
        A new Series with outliers removed.

    Notes
    -----
    In a normal distribution:
    - 68% of data has its z-score lower or equal to 1.
    - 95% of data has its z-score lower or equal to 2.
    - 99.7% of data has its z-score lower or equal to 3.
    """
    mask = np.abs((ser - np.mean(ser)) / np.std(ser)) < z
    return ser[mask]


def fill_outliers(
    ser: pd.Series,
    z: float = 2.0,
    method: str = "mean",
) -> pd.Series:
    """Replace outliers in a Series with a specified value calculated from the
    non-outlier values.

    Parameters
    ----------
    ser : pd.Series
        The Series containing the outliers to be replaced.
    z : float, optional
        The z-score used as a threshold for identifying outliers. Default value
        is 2.
    method : str, optional
        The method to use for calculating the replacement value. Valid options
        include `mean` and `median`. Default value is `mean`.

    Returns
    -------
    pd.Series
        A new Series with outliers replaced by the specified method.

    Notes
    -----
    In a normal distribution:
    - 68% of data has its z-score lower or equal to 1.
    - 95% of data has its z-score lower or equal to 2.
    - 99.7% of data has its z-score lower or equal to 3.
    """
    mask = np.abs((ser - np.mean(ser)) / np.std(ser)) < z
    match method:
        case "mean" | "avg":
            ser[~mask] = np.mean(ser[mask])
        case "median":
            ser[~mask] = np.median(ser[mask])
    return ser


def correlation_matrix(
    df: pd.DataFrame,
    abs: bool = True,
):
    """Plot the correlation matrix for all numerical columns in the DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data for which to compute the correlation
        matrix.
    abs : bool, optional
        The correlation values will be displayed as absolute values if True.

    Returns
    -------
    None
        This function does not return a value.
    """
    m = df.select_dtypes(include=np.number).corr()
    plt.figure(figsize=(10, 8))
    plt.title("Correlation Matrix", fontfamily="monospace", fontsize=16)
    sns.heatmap(
        data=m.abs() if abs else m,
        annot=True,
        annot_kws={"fontfamily": "monospace", "fontsize": 8},
        vmax=1.0,
        vmin=0.0 if abs else -1.0,
        linewidths=0.5
    )
    plt.show()
