import os
import pandas as pd

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

def load_M_matrix():
    df_matrix_filename = "df_matrix_200.csv"
    df_matrix_filename_path = os.path.join(APP_STATIC, df_matrix_filename)
    M = pd.read_csv(df_matrix_filename_path)
    M.drop(["Unnamed: 0"], axis=1, inplace=True)
    return M
