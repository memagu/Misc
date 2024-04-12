from pathlib import Path
import pickle

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.models import Sequential

DATA_DIR = Path("./data/")
MODEL_DIR = Path("./models/")
RANDOM_SEED = 42


def load_data(path: Path) -> np.ndarray:
    if not path.exists():
        raise Exception(f"Path {path} does not exist")

    with open(path, "rb") as f:
        return pickle.load(f)


def build_model(input_shape: tuple[int, ...], output_neurons: int) -> Sequential:
    model = Sequential([
        InputLayer(input_shape=input_shape),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(8, activation="relu"),
        Dense(output_neurons, activation="linear")
    ])

    model.compile(optimizer="adam", loss="mse", metrics=["mae"])

    return model


def main():
    data = load_data(DATA_DIR / "4k4k4.pkl")
    inputs = data[:, :-1]
    outputs = data[:, -1]

    model = build_model((inputs.shape[-1],), 1)
    model.summary()

    x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=RANDOM_SEED)

    model.fit(
        x_train,
        y_train,
        epochs=100,
        batch_size=8192,
        validation_data=(x_test, y_test),
        verbose=1,
        callbacks=[EarlyStopping(patience=10, restore_best_weights=True)]
    )

    if not MODEL_DIR.exists():
        MODEL_DIR.mkdir(parents=True, exist_ok=True)

    model.save(MODEL_DIR / "m4th_v6.keras")


if __name__ == '__main__':
    main()
