import numpy as np
import os
import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

model = tf.keras.models.load_model("dogbreed.h5")

class_names = ['beagle','basset','bulldog','boxer','chihuahua',
               'doberman','german_shepherd','golden_retriever',
               'labrador','pug']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/output', methods=['POST'])
def output():
    if 'file' not in request.files:
        return "No file uploaded"

    f = request.files['file']
    filepath = os.path.join("uploads", f.filename)
    f.save(filepath)

    img = load_img(filepath, target_size=(224,224))
    img_array = img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    pred_class = class_names[np.argmax(prediction)]

    return render_template("output.html", prediction=pred_class)

if __name__ == "__main__":
    app.run(debug=True)