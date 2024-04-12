import pickle
from pathlib import Path

import numpy as np

DATA_DIR = Path("./data/")

OPERATORS = [
    (np.add, (1, 0, 0, 0)),
    (np.subtract, (0, 1, 0, 0)),
    (np.multiply, (0, 0, 1, 0)),
    (np.true_divide, (0, 0, 0, 1))
]

VALUES = np.linspace(-100, 100, 1001)
value1, value2 = np.meshgrid(VALUES, VALUES)

mask = value2 != 0
value1 = value1[mask]
value2 = value2[mask]

data = np.concatenate(
    [
        np.stack(
            (
                value1.ravel(),
                value2.ravel(),
                *(np.full_like(value1, e).ravel() for e in encoding),
                operation(value1, value2)
            ),
            axis=1
        )
        for operation, encoding in OPERATORS
    ]
)

print("Saving . . .")
print(data)

if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA_DIR / "1k1k4.pkl", "wb") as f:
    pickle.dump(data, f)
