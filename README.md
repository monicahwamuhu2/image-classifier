Image Classification Web App

This project is a web-based image classification application built using Flask, TensorFlow, and a pre-trained model on the CIFAR dataset. Users can upload images to the web app, and it predicts the class of the uploaded image. This app is a great example of deploying a machine learning model for real-time predictions in a simple web interface.

Features

Image Upload: Users can upload images to be classified.
Predictions: The model provides predictions on uploaded images with a list of possible classes (top 3) and a confidence score.
Feedback Form: Users can submit feedback on the predictions to help improve the model in future updates.

![Screenshot (138)](https://github.com/user-attachments/assets/e928afd4-747f-4ab9-acc8-c44875eeacad)

![Screenshot (137)](https://github.com/user-attachments/assets/caf09134-cd9c-4865-a609-6cfde863933a)

Project Structure
app.py: The main Flask application file, which handles routes, image processing, and prediction.
templates/: HTML templates for rendering pages.
index.html: Homepage for uploading images.
result.html: Displays the predicted class of the uploaded image and allows feedback.
static/: Directory for static assets, including the model file CIFAR.h5, images, and styles.
venv/: Virtual environment for managing dependencies (not necessary to include in GitHub).
Installation and Setup
Prerequisites
Python 3.6+
Flask (for web app development)
TensorFlow (for loading the model and making predictions)
Pillow (for image processing)
Step 1: Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/monicahwamuhu2/image-classifier.git
cd image-classifier
Step 2: Create and Activate a Virtual Environment (Recommended)
Set up a virtual environment to manage dependencies.

bash
Copy code
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Step 3: Install Required Packages
Install the dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
If requirements.txt is not available, install the following dependencies manually:

bash
Copy code
pip install Flask TensorFlow Pillow
Step 4: Add the Model
Ensure the CIFAR model file (CIFAR.h5) is located in the static directory. This model should be trained on the CIFAR-10 dataset, which classifies images into 10 categories (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).

Step 5: Run the Application
Run the Flask application using:

bash
Copy code
python app.py
After running this command, you should see output indicating that the app is running. Visit http://127.0.0.1:5000 in your web browser to view the app.

Step 6: Upload an Image
On the homepage, upload an image for classification.
The app will display the predicted class along with the top 3 predictions and confidence scores.
If the prediction is incorrect, you can submit feedback with the correct class to help improve the model.
