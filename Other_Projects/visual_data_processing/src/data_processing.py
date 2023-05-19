from collections import Counter
from datetime import datetime
import os
from pathlib import Path

import numpy as np
from PIL import Image


def load_float_csv(path: Path, delimiter: str = ',') -> np.ndarray:
    with open(path, 'r') as f:
        rows = [list(map(float, line.strip().split(delimiter))) for line in f.readlines()]

    return np.array(rows)


def save_float_csv(data: np.ndarray, path: Path = None, delimiter: str = ',') -> None:
    path = path or Path(f"../data_output/{datetime.now().timestamp()}.data")

    if not os.path.exists(path.parent):
        os.makedirs(path.parent, exist_ok=True)

    with open(path, "w") as f:
        f.writelines(delimiter.join(row.astype(str)) + '\n' for row in data)


def filter_highpass(data: np.ndarray, threshold: float = None) -> np.ndarray:
    threshold = threshold or Counter(data.flatten()).most_common(1)[0][0] * 1.3
    return np.where(data >= threshold, data, 0)


def normalize(data: np.ndarray) -> np.ndarray:
    max_val = data.max()
    min_val = data.min()

    return (data - min_val) / (max_val - min_val)


def data_to_rgba(data: np.ndarray, alpha: int = 192) -> np.ndarray:
    gray_data = 255 * data
    rgb_data = np.repeat(gray_data[:, :, np.newaxis], 3, axis=2)
    alpha_data = np.full(data.shape, alpha)
    rgba_data = np.dstack((rgb_data, alpha_data))

    return rgba_data.astype(np.uint8)

def scale_rgba(rgba_data: np.ndarray, r: float = 1, g: float = 1, b: float = 1, a: float = 1) -> np.ndarray:
    return (rgba_data * [r, g, b, a]).astype(np.uint8)


def merge_data(data_1: np.ndarray, data_2: np.ndarray, data_1_indices: tuple[int, int, int, int],
               data_2_indices: tuple[int, int, int, int]) -> np.ndarray:
    d1_sr, d1_sc, d1_er, d1_ec = data_1_indices
    d2_sr, d2_sc, d2_er, d2_ec = data_2_indices

    return data_1[d1_sr:d1_er, d1_sc:d1_ec] - data_2[d2_sr:d2_er, d2_sc:d2_ec]


if __name__ == "__main__":
    pass
