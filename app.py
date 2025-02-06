from flask import Flask, request, render_template, redirect, url_for
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Inisialisasi Flask
app = Flask(__name__)

# Path untuk folder upload
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
model = load_model('16_cnn_model.h5')

# Label kelas
class_names = ['Layak (0 - 5 bulan)', 'Layak (5 - 12 bulan)', 'Layak (12 - 18 bulan)', 'Rawan (18 - 24 bulan)', 'Tak Layak (lebih dari 24 bulan)']

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk upload dan prediksi
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Simpan file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Preprocessing gambar
        img = load_img(filepath, target_size=(128, 128))  
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediksi
        predictions = model.predict(img_array)
        class_idx = np.argmax(predictions)
        result = class_names[class_idx]

        return render_template('index.html', result=result, image_url=filepath)

if __name__ == '__main__':
    app.run(debug=True)
