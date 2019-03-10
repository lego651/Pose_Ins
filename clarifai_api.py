import pandas as pd
import numpy as np

from clarifai.rest import ClarifaiApp

from utils.get_top_k import get_top_k
from utils.get_pearson import pearson

# Global Variables
# 10: ten folder
all_tags_filename_10 = "database_10.txt"
df_matrix_filename_10 = "df_matrix_10.csv"

# 200: two hundred folder
all_tags_filename_200 = "database_200.txt"
df_matrix_filename_200 = "df_matrix_200.csv"

# Set current Vars
all_tags = []
image_url = "https://i.ibb.co/30zgK2H/1-beach-miami-south-beach.jpg"
# image_url = "https://i.ibb.co/47hbcJb/2-rose-garden.jpg"
# image_url = "https://i.ibb.co/C1LsDG7/3-green-park.jpg"
# image_url = "https://i.ibb.co/9sL96dj/4-city-street.jpg"
# image_url = "https://i.ibb.co/HCqd9FB/5-indoor-coffee-shop.jpg"
# image_url = "https://i.ibb.co/yyWPd3m/6-Ins-wall.jpg"

# Create clarifai model instance
app = ClarifaiApp(api_key='1fc0e40ef28b4e3085522ee5857b1aee')
model = app.public_models.general_model


###
#   Step1: get all_tags[]: all_tags
#   If there is no database_10.txt, just run /build_database/build_all_tags.py first
###
with open(all_tags_filename_200, "r") as file:
    all_tags = eval(file.readline())
print("new built all_tags[] length is:", len(all_tags))


###
#   Step2: get df_matrix: M
#   If there is no df_matrix_10.csv, just run /build_database/build_all_tags.py first
###
M = pd.read_csv(df_matrix_filename_200)
M.drop(["Unnamed: 0"], axis = 1, inplace = True)


###
#   Step3: return a img_series based on a new image url
###
def build_new_pic_matrix(image_url, model, all_tags):
    m = pd.DataFrame(0, index=all_tags, columns=list('n'))
    response = model.predict_by_url(image_url)
    concepts = response['outputs'][0]['data']['concepts']
    for concept in concepts:
        tag_name = concept['name']
        if(tag_name not in all_tags):
            continue
        else:
            val = concept['value']
            m.loc[tag_name, 'n'] = val
    return m


# Get new image df_matrix based on its image_url
m = build_new_pic_matrix(image_url, model, all_tags)
# m.index = M.index # We do this step already in get_top_k.py function

topK = get_top_k(M, m, 10)
print(topK)











