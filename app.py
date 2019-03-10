# Import dependencies
from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import pandas as pd
import io
from PIL import Image

from clarifai.rest import ClarifaiApp

from utils.get_top_k import get_top_k
from utils.get_pearson import pearson
from utils.get_new_pic_matrix import build_new_pic_matrix
from load_all_tags import load_all_tags
from load_M_matrix import load_M_matrix

# Create instance of Flask App
app = Flask(__name__)

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

def load_global_model():
    global model
    global all_tags
    global M
    app = ClarifaiApp(api_key='1fc0e40ef28b4e3085522ee5857b1aee')
    model = app.public_models.general_model
    all_tags = load_all_tags()
    M = load_M_matrix()


print("* Loading model and global vars...")
load_global_model()

# Route to Home page _GET
@app.route("/")
def home():
    return render_template("index.html")

# Route to Demo page _GET
@app.route("/demo")
def demo():
    return render_template("demo.html")

# Upload image API _POST
@app.route("/predict", methods=["POST"])
def predict():
    imageURL = request.get_json(force=True)
    image_url = imageURL['image_url']

    m = build_new_pic_matrix(image_url, model, all_tags)
    topK = get_top_k(M, m, 8)
    predictedResultArray = [(*key,)[0] for key in topK]

    response = {
        'prediction': predictedResultArray
    }
    return jsonify(response)

# Running app server
if(__name__ == '__main__'):
    app.run(debug=True)