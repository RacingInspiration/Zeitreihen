import numpy as np
import plotly.graph_objects as go
from tensorflow import keras
from keras import layers

# Generiere die Cosinus-Funktion
x = np.linspace(0, 10 * 2 * np.pi, 1000)  # 10 Perioden
y = np.cos(x)  # Cosinus-Funktion

# Parameter für Sequenzlänge und Vorhersage
sequence_length = 50  # Anzahl der Punkte pro Input-Sequenz
prediction_horizon = 200  # 11. und 12. Periode (~200 Punkte)

# Eingabedaten (X) und Zielwerte (y)
X = []
y_target = []
for i in range(len(y) - sequence_length - prediction_horizon):
    X.append(y[i:i + sequence_length])
    y_target.append(y[i + sequence_length:i + sequence_length + prediction_horizon])

X = np.array(X)
y_target = np.array(y_target)

# Reshape für das CNN
X = X[..., np.newaxis]  # (samples, sequence_length, 1)

# Train-Test-Split
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y_target[:train_size], y_target[train_size:]

# Baue das CNN-Modell
model = keras.Sequential([
    keras.Input(shape=(sequence_length, 1)),
    layers.Conv1D(64, kernel_size=3, activation="relu"),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(128, kernel_size=3, activation="relu"),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(prediction_horizon)  # Vorhersage der nächsten Punkte
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.summary()

# Trainiere das Modell
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32, verbose=0)

# Teste das Modell
test_input = y[-sequence_length:]  # Letzte Sequenz der Cosinus-Funktion
test_input = test_input.reshape(1, sequence_length, 1)  # Reshape für das Modell
predicted = model.predict(test_input)[0]  # Vorhersage

# Bereite x-Werte für die Vorhersage vor
predicted_x = np.linspace(x[-1], x[-1] + 2 * 2 * np.pi, prediction_horizon)  # 11. und 12. Periode

# Erstelle die Plotly-Figur
fig = go.Figure()

# Ursprüngliche Funktion (10 Perioden)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Gegebene Funktion'))

# Vorhersage durch das CNN (11. und 12. Periode)
fig.add_trace(go.Scatter(x=predicted_x, y=predicted, mode='lines', name='Vorhersage (CNN)', line=dict(dash='dash')))

# Details und Anzeige
fig.update_layout(
    title="Cosinus-Funktion und Vorhersage mit CNN",
    xaxis_title="x",
    yaxis_title="y",
    legend=dict(x=0.01, y=0.99),
    template="plotly_white"
)

fig.show()
