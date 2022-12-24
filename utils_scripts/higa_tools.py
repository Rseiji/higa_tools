import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import supervenn

from IPython.display import display_html
from itertools import chain,cycle


class GeneralUtils():
    @staticmethod
    def get_psycopg2_conn():
        pass

    @staticmethod
    def get_table():
        pass
        
    @staticmethod
    def execute_statement():
        pass

    @staticmethod
    def copy_to_db():
        pass

    @staticmethod
    def get_supervenn(sets: dict, rotate_col_annotations=False,
                      figsize=(20, 8)):
        """
        Generate a supervenn plot.

        Some default configurations defined by us. This way, we do not have
        to configure them each time we want to use.
        
        Notes
        -----
        Supervenn is a library developed by
        ``https://github.com/gecko984/supervenn``
        """
        plt.figure(figsize=figsize)
        supervenn(
            sets.values(),
            sets.keys(),
            side_plots=False,
            widths_minmax_ratio=0.05,
            rotate_col_annotations=rotate_col_annotations
        )

    @staticmethod
    def get_general_insigths(df, cols_to_unique=[], cols_to_nunique=[],
                             cols_to_maxmin=[]):
        print(f'\033[1mShape\033[0m: {df.shape}')
        if cols_to_unique:
            for col in cols_to_unique:
                print(f'\033[1m{col} unique values\033[0m: {df[col].unique()}')
        if cols_to_nunique:
            for col in cols_to_nunique:
                print(f'\033[1m{col} nunique values\033[0m: {df[col].nunique()}')
        if cols_to_maxmin:
            for col in cols_to_maxmin:
                print(f'\033[1m{col} max\033[0m': {df[col].max()})
                print(f'\033[1m{col} min\033[0m': {df[col].min()})

    @staticmethod
    def display_ax1(*args,titles=cycle([''])):
        """Display pandas dataframes side by side, like axis=1, as
        output

        Notes
        -----
        Source: https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
        """
        html_str=''
        for df, title in zip(args, chain(titles,cycle(['</br>'])) ):
            html_str+='<th style="text-align:center"><td style="vertical-align:top">'
            html_str+=f'<h2>{title}</h2>'
            html_str+=df.to_html().replace('table','table style="display:inline"')
            html_str+='</td></th>'
        display_html(html_str,raw=True)

    @staticmethod
    def bold(string: str):
        return '\033[1m' + string + '\033[0m'

    @staticmethod
    def underline(string: str):
        return  '\033[4m' + string + '\033[0m'

    @staticmethod
    def underline(string: str):
        return  '\x1B[3m' + string + '\x1B[0m'

    @staticmethod
    def red(string: str):
        return  '\033[91m' + string + '\033[0m'

    @staticmethod
    def green(string: str):
        return  '\033[92m' + string + '\033[0m'

    @staticmethod
    def blue(string: str):
        return  '\033[93m' + string + '\033[0m'

    @staticmethod
    def blue(string: str):
        return  '\033[94m' + string + '\033[0m'

