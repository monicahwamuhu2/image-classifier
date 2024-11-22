from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
model = load_model('static/CIFAR.h5')  # Load your trained model
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('static', filename)
        file.save(filepath)
        top_classes, predicted_class = predict(filepath)
        return render_template('result.html', image_path=filepath, prediction=top_classes, predicted_class=predicted_class)

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((32, 32))  # Resize to 32x32 pixels
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict(image_path):
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)[0]
    top_indices = prediction.argsort()[-3:][::-1]  # Get indices of top 3 predictions
    top_classes = [(class_names[i], prediction[i]) for i in top_indices]
    predicted_class = top_classes[0][0]  # Most likely class
    return top_classes, predicted_class

@app.route('/feedback', methods=['POST'])
def feedback():
    image_path = request.form['image_path']
    correct_class = request.form['correct_class']
    # Here you can save the feedback to a database or a file for future model improvement
    # For now, we'll just print it
    print(f"Image: {image_path}, Correct Class: {correct_class}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
