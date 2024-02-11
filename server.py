from flask import Flask, render_template, request, jsonify, send_file
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

model = load_model('my_model.h5')
class_names = ['Bayterek', 'Chair', 'Table']

def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(io.BytesIO(file.read()))
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_class_index = np.argmax(prediction)
            predicted_class_name = class_names[predicted_class_index]
            return jsonify({'prediction': predicted_class_name})
    return render_template('index.html')

@app.route('/index.js')
def js_file():
    return render_template('index.js')

@app.route('/model.json')
def send_model_json():
    return send_file('model.json')

@app.route('/group1-shard1of3.bin')
def group1_shard1of3_bin():
    return send_file('group1-shard1of3.bin')

@app.route('/group1-shard2of3.bin')
def group1_shard3of3_bin():
    return send_file('group1-shard2of3.bin')

@app.route('/group1-shard3of3.bin')
def group1_shard2of3_bin():
    return send_file('group1-shard3of3.bin')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(io.BytesIO(file.read()))
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_class_index = np.argmax(prediction)
            predicted_class_name = class_names[predicted_class_index]
            return jsonify({'prediction': predicted_class_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
