from flask import Flask, render_template, request, send_from_directory
import os
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model
model = load_model('models/model.h5')
CLASS_LABELS = ['glioma', 'meningioma', 'notumor', 'pituitary']

def predict_tumor(image_path):
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Model prediction
    avg_pred = model.predict(img_array, verbose=0)[0]
    pred_idx = np.argmax(avg_pred)
    
    return {
        'prediction': CLASS_LABELS[pred_idx],
        'confidence': float(avg_pred[pred_idx]),
        'probabilities': {c: float(avg_pred[i]) for i, c in enumerate(CLASS_LABELS)}
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            result = predict_tumor(filepath)
            return render_template('index.html', 
                                result=result,
                                file_path=f'/uploads/{filename}')
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
