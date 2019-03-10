from clarifai.rest import ClarifaiApp
import pandas as pd
import numpy as np

# Global Variables
# 10: ten folder
all_tags_filename_10 = "../database_10.txt"
total_photos_num_10 = 10
image_folder_path_10 = "../static/images/ten/"
df_matrix_filename_10 = "../df_matrix_10.csv"

# 200: two hundred folder
all_tags_filename_200 = "../database_200.txt"
total_photos_num_200 = 200
image_folder_path_200 = "../static/images/two_hundred/"
df_matrix_filename_200 = "../df_matrix_200.csv"

all_tags = []

# Create clarifai model instance
app = ClarifaiApp(api_key='1fc0e40ef28b4e3085522ee5857b1aee')
model = app.public_models.general_model

with open(all_tags_filename_200, "r") as file:
    all_tags = eval(file.readline())
print("new read all_tags[] length is:", len(all_tags))

def build_full_tags_matrix(total_photos_num, all_tags, image_folder_path, model, df_matrix_filename):
    """
    Build pd matrix based on 10 / 200 / 500 photos
    :param all_tags: array[], "database_10.txt" get from: read_all_tags_and_save_as_local_file
    :param model: Clarifai model instance
    :return: void
    """
    # M = pd.DataFrame(np.nan, index=all_tags, columns=list(range(total_photos_num)))
    M = pd.DataFrame(0, index=all_tags, columns=list(range(total_photos_num)))
    for i in range(total_photos_num):
        print("Indexing photo number: # ", i)
        filename = image_folder_path + str(i) + '.jpg'
        response = model.predict_by_filename(filename=filename)
        concepts = response['outputs'][0]['data']['concepts']
        for concept in concepts:
            index = concept['name']
            val = concept['value']
            M.loc[index, i] = val
    # pandas Matrix: First column has all_tags, each column represents a sample photo.
    print("new built matrix shape is:", M.shape)
    M.to_csv(df_matrix_filename)

build_full_tags_matrix(total_photos_num=total_photos_num_200, all_tags=all_tags, image_folder_path=image_folder_path_200,
                       model=model, df_matrix_filename=df_matrix_filename_200)

