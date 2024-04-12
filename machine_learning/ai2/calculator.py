from pathlib import Path

import numpy
import numpy as np
from tensorflow.keras.saving import load_model

MODEL_DIR = Path("./models/")
MODEL = "m4th_v6.keras"

OPERATOR_TO_ONE_HOT = {op_char: one_hot for op_char, one_hot in zip("+-*/", np.eye(4))}

def main():
    model = load_model(MODEL_DIR / MODEL)
    model.summary()

    while True:
        try:

            num1, op_char, num2 = input("Enter simple expression: ").split()
            queries = numpy.array(((float(num1), float(num2), *OPERATOR_TO_ONE_HOT[op_char]),))
        except ValueError:
            continue

        print(f"query: {queries[0]}")
        prediction = model.predict(queries, verbose=0)
        print(prediction[0, 0])


if __name__ == '__main__':
    main()
