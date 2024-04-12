from pathlib import Path
import pickle

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import BatchNormalization, Conv2D, Dense, LSTM, Reshape, Dropout, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential, load_model

DATA_DIR = Path("./data/data2.pkl")


def load_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    if not path.exists():
        raise Exception(f"Path {path} does not exist")

    with open(path, "rb") as f:
        return pickle.load(f)


def build_model(input_shape, output_nodes):
    model = Sequential([
        Reshape((input_shape[0], input_shape[1], 1), input_shape=input_shape),
        Conv2D(32, (7, 5), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((7, 1)),

        Conv2D(64, (5, 3), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((5, 1)),

        Conv2D(128, (3, 1), activation="relu"),
        BatchNormalization(),
        MaxPooling2D((3, 1)),
        #
        # Reshape((97, -1)),
        # LSTM(256, return_sequences=True),
        # LSTM(128),
        #

        Flatten(),

        Dense(128, activation="relu"),
        Dense(64, activation="relu"),
        Dense(32, activation="relu"),

        Dense(output_nodes, activation='linear')
    ])

    model.compile(optimizer="adam", loss="msle")

    return model


def main():
    spectrograms, annotations = load_data(DATA_DIR)
    spectrograms = spectrograms.transpose(0, 2, 1)

    model = build_model(spectrograms.shape[1:], annotations.shape[1])
    model.summary()

    x_train, x_test, y_train, y_test = train_test_split(spectrograms, annotations, test_size=0.2, random_state=1)

    model.fit(
        x_train,
        y_train,
        epochs=100,
        batch_size=64,
        validation_data=(x_test, y_test),
        verbose=1,
        callbacks=[EarlyStopping(patience=3, restore_best_weights=True)]
    )

    model.save("rekordbox.keras")

    predictions = model.predict(x_test[:5])

    for i in range(len(predictions)):
        print(f"Sample {i + 1} - Actual: {y_test[i] * 240}, Predicted: {predictions[i] * 240}")

    print("#" * 32)

    predictions = model.predict(x_train[:5])

    for i in range(len(predictions)):
        print(f"Sample {i + 1} - Actual: {y_train[i] * 240}, Predicted: {predictions[i] * 240}")


if __name__ == '__main__':
    main()
