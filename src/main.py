from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
cnn_model = load_model("models/cnn_model.h5")
mlp_model = load_model("models/mlp_model.h5")


def prepare_image(image, flatten=False):
    image = image.resize((28, 28))

    if image.mode != "L":
        image = image.convert("L")

    image = np.array(image)

    if flatten:
        image = image.reshape(1, -1)
    else:
        image = image.reshape(1, 28, 28, 1)

    return image


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    if file:
        image = Image.open(io.BytesIO(file.read()))
        cnn_image = prepare_image(image)
        mlp_image = prepare_image(image, flatten=True)
        cnn_prediction = cnn_model.predict(cnn_image).argmax(axis=-1)[0]
        mlp_prediction = mlp_model.predict(mlp_image).argmax(axis=-1)[0]
        return jsonify(
            {"cnn_digit": int(cnn_prediction), "mlp_digit": int(mlp_prediction)}
        )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
