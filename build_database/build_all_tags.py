from clarifai.rest import ClarifaiApp
import pandas as pd
import numpy as np

# Global Variables
# 10: ten folder
total_photos_num_10 = 10
image_folder_path_10 = "../static/images/ten/"
all_tags_filename_10 = "../database_10.txt"

# 200: two hundred folder
total_photos_num_200 = 200
image_folder_path_200 = "../static/images/two_hundred/"
all_tags_filename_200 = "../database_200.txt"

all_tags = []

# Create clarifai model instance
app = ClarifaiApp(api_key='1fc0e40ef28b4e3085522ee5857b1aee')
model = app.public_models.general_model

def read_all_tags_and_save_as_local_file(total_photos_num, image_folder_path, model, all_tags_filename):
    """
    iterate image folder, read image one by one and build all_tags[]
    :param image_folder_path: folder path for images
    :param model: Clarifai model instance
    :return: void
    """
    for i in range(total_photos_num):
        print("Indexing photo number: # ", i)
        filename = image_folder_path + str(i) + '.jpg'
        response = model.predict_by_filename(filename=filename)
        concepts = response['outputs'][0]['data']['concepts']
        for concept in concepts:
            if concept['name'] not in all_tags:
                all_tags.append(concept['name'])
    # return all_tags
    # Save all_tags to local file
    print("new built all_tags[] length is:", len(all_tags))
    with open(all_tags_filename, "w") as file:
        file.write(str(all_tags))

read_all_tags_and_save_as_local_file(total_photos_num=total_photos_num_200, image_folder_path=image_folder_path_200, model=model, all_tags_filename=all_tags_filename_200)













