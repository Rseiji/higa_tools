import multiprocessing
from itertools import chain, cycle
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display_html
from supervenn import supervenn


def bold(string: str):
    return "\033[1m" + string + "\033[0m"


def underline(string: str):
    return "\033[4m" + string + "\033[0m"


def red(string: str):
    return "\033[91m" + string + "\033[0m"


def green(string: str):
    return "\033[92m" + string + "\033[0m"


def blue(string: str):
    return "\033[93m" + string + "\033[0m"


def get_supervenn(
    sets: dict[str, Any], rotate_col_annotations=False, figsize=(20, 8)
) -> None:
    """Generate a supervenn plot.

    Parameters
    ----------
    sets : dict[str, Any]
        A dictionary of sets to compare using the supervenn plot.
    rotate_col_annotations : bool, optional
    figsize : tuple, optional

    Notes
    -----
    Supervenn is a library developed by ``https://github.com/gecko984/supervenn``.
    """
    plt.figure(figsize=figsize)
    supervenn(
        list(sets.values()),
        list(sets.keys()),
        side_plots=False,
        widths_minmax_ratio=0.05,
        rotate_col_annotations=rotate_col_annotations,
    )


def display_ax1(*dfs: pd.DataFrame, titles=()) -> None:
    """Display two dataframes side by side.

    Parameters
    ----------
    dfs : pd.DataFrame
        Tables to display.
    titles : tuple, optional
        Titles for the tables.
    """
    html_str = ''
    for i, df in enumerate(dfs):
        title = titles[i] if i < len(titles) else ''
        html_str += '<div style="display:inline-block; margin-right:20px;">'
        html_str += f'<h3>{title}</h3>'
        html_str += df.to_html()
        html_str += '</div>'
    display_html(html_str, raw=True)


def sort_df_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Sort by all columns in df order, ascending True."""
    return df[sorted(df.columns.tolist())]


def serie_parallel(func, arg_tuples, mode="series", n_jobs=-1):
    """Execute a given function in series or parallel mode and return the results.

    Parameters
    ----------
    func : callable
        The function to be executed.
    arg_tuples : list[tuple]
        The group of argument tuples to be passed to the function.
    mode : str, optional
        The execution mode. Can be 'series' (default) or 'parallel'.
    n_jobs : int, optional
        The number of cores to use for parallel execution. Default is -1,
        which uses all available cores. Set to 1 or 0 to execute in series mode.

    Returns
    -------
    list[Any]
        The list of results from the function execution.
    """
    results = []
    if mode == "series" or n_jobs in (0, 1):
        for args in arg_tuples:
            result = func(*args)
            results.append(result)
    elif mode == "parallel":
        with multiprocessing.Pool(processes=n_jobs) as pool:
            parallel_results = pool.starmap(func, arg_tuples)
        results.extend(parallel_results)
    else:
        raise ValueError("Invalid mode. Mode must be 'series' or 'parallel'.")
    return results
