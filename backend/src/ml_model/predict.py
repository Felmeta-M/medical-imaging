import os
import io
from PIL import Image
import numpy as np
import datetime
import base64
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image

# Load the model
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FILE_NAME = "alexnet.h5"
MODEL_PATH = os.path.join(BASE_DIR, FILE_NAME)

# Custom model loading function
def load_model_custom(model_path):
    model = tf.keras.models.load_model(model_path, compile=False)
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['acc']
    )
    return model

model = load_model_custom(MODEL_PATH)

# Classes
class_names = ['normal', 'tuberculosis']

def transform_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((227, 227))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array = img_array / 255.0  # Normalize the image array
    return img_array

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def get_prediction(image_bytes):
    img = transform_image(image_bytes=image_bytes)
    predictions = model.predict(img)
    img_out = sigmoid(predictions)
    predicted_idx = np.argmax(img_out[0])
    confidence = round(img_out[0][predicted_idx] * 100, 2)
    return class_names[predicted_idx], confidence

def get_result(image_file, is_api=False):
    start_time = datetime.datetime.now()
    image_bytes = image_file.file.read()
    class_name, confidence = get_prediction(image_bytes)
    if not is_api:
        encoded_string = base64.b64encode(image_bytes)
        bs64 = encoded_string.decode('utf-8')
        image_data = f'data:image/png;base64,{bs64}'
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    result = {
        "inference_time": execution_time,
        "predictions": {
            "class_name": class_name,
            "confidence": confidence
        }
    }
    if not is_api:
        result["image_data"] = image_data
    return result
