from pathlib import Path
import pickle

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

DATA_DIR = Path("./data/")
MODEL_DIR = Path("./models/")
RANDOM_SEED = 42


def load_data(path: Path) -> np.ndarray:
    if not path.exists():
        raise Exception(f"Path {path} does not exist")

    with open(path, "rb") as f:
        return pickle.load(f)


def main():
    data = load_data(DATA_DIR / "2k2k4.pkl")
    inputs = data[:, :3]
    outputs = data[:, 3]

    model  = load_model
    x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2, random_state=RANDOM_SEED)


    predictions = model.predict(x_test[:5])

    for i in range(len(predictions)):
        print(f"Sample {i + 1} - Actual: {y_test[i] * 240}, Predicted: {predictions[i] * 240}")

    print("#" * 32)

    predictions = model.predict(x_train[:5])

    for i in range(len(predictions)):
        print(f"Sample {i + 1} - Actual: {y_train[i] * 240}, Predicted: {predictions[i] * 240}")


if __name__ == '__main__':
    main()