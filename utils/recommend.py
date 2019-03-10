import pandas as pd
import numpy as np

from clarifai.rest import ClarifaiApp

from utils.get_top_k import get_top_k
from utils.get_pearson import pearson
from utils.get_new_pic_matrix import build_new_pic_matrix

def recommend(image_url):
    """
    :return:
    """
    all_tags = []
    all_tags_filename = "database_200.txt"
    df_matrix_filename = "df_matrix_200.csv"

    # Create clarifai model instance
    app = ClarifaiApp(api_key='1fc0e40ef28b4e3085522ee5857b1aee')
    model = app.public_models.general_model

    with open(all_tags_filename, "r") as file:
        all_tags = eval(file.readline())
    print("new built all_tags[] length is:", len(all_tags))

    M = pd.read_csv(df_matrix_filename)
    M.drop(["Unnamed: 0"], axis=1, inplace=True)

    m = build_new_pic_matrix(image_url, model, all_tags)

    topK = get_top_k(M, m, 8)

    return [(*key,)[0] for key in topK]









