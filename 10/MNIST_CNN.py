# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:01:57 2021
MNIST Datensatz - Erkennung von Ziffern mit CNN
Verwenden Keras als Bibliotek
@author: torsten.schmidt
"""
# Importiere die notwendigen Bibliotheken
import numpy as np
import tensorflow
from keras import layers
import matplotlib.pyplot as plt

# Definiere die Modell Parameter
num_classes = 10
imput_shape = (28, 28, 1)
batch_size = 128
epochs = 2

# Lade Datensatz direkt geteilt als Trainings- und Testdaten
(X_train, y_train), (X_test, y_test) = tensorflow.keras.datasets.mnist.load_data()

# Skaliere die Bilder zum Intervall [0,1]
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# Erweitere die Dimension der Inputdaten um 1 dim am Ende des jetzigen Feldes
X_train = np.expand_dims(X_train,-1)
X_test = np.expand_dims(X_test,-1)

# Wandle die y-Werte in Klassen um
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes)
y_test = tensorflow.keras.utils.to_categorical(y_test, num_classes)

# Baue das CNN modell auf
model = tensorflow.keras.Sequential(
[
tensorflow.keras.Input(shape = imput_shape),
layers.Conv2D(32, kernel_size = (3,3), activation ="relu"),
layers.MaxPooling2D(pool_size=(2,2)),
layers.Conv2D(64, kernel_size=(3,3), activation = "relu"),
layers.MaxPooling2D(pool_size=(2,2)),
layers.Flatten(),
layers.Dropout(0.5),
layers.Dense(num_classes,activation = "softmax"),
]
)
model.summary()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fitte das Modell
model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, validation_split = 0.1)

# Evaluation und Anwendung des Modells
score = model.evaluate(X_test, y_test, verbose = 0)

print("Test Genauigkeit", score[1])

# Ziffer eines bestimmten Bildes auslesen
plt.imshow(X_test[300])
plt.show()
X = np.expand_dims(X_test[300], 0)
y_vec = model.predict(X)
print(y_vec)
y = np.argmax(model.predict(X), axis=-1)
print('Die Ziffer wurde als: ',y,' erkannt!')