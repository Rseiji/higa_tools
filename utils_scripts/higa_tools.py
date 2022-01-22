import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import supervenn


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
        Generates a supervenn plot, with some default configurations
        defined by us. This way, we do not have to configure them
        each time we want to use
        
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

