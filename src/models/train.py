from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Dense,
    Flatten,
    Dropout,
)
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.utils import to_categorical
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1) / 255.0
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)
x_train /= 255
x_test /= 255

cnn_model = Sequential(
    [
        Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(256, activation="relu"),
        Dropout(0.5),
        Dense(10, activation="softmax"),
    ]
)

cnn_model.compile(
    optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
)
cnn_model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
cnn_model.save("cnn_model.h5")

mlp_model = Sequential(
    [
        InputLayer(input_shape=(28 * 28,)),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax"),
    ]
)

x_train_flat = x_train.reshape(-1, 28 * 28)
x_test_flat = x_test.reshape(-1, 28 * 28)

mlp_model.compile(
    optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
)

mlp_model.fit(x_train_flat, y_train, epochs=5, validation_data=(x_test_flat, y_test))
mlp_model.save("mlp_model.h5")
