from pathlib import Path
import pickle
from xml.etree import ElementTree
from urllib.parse import unquote

import librosa
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

OUTPUT_PATH = Path("data/data.pkl")
DATA_DIR = Path("C:/Users/melke/Desktop/rekordboxml/temp")
AUDIO_DIR = DATA_DIR / "audio/"
XML_PATH = DATA_DIR / "nuav.xml"
PLAYLIST = "Nya House Quepoints"
SONG_DURATION_SECONDS = 480


def load_data(xml_path: Path, playlist: str) -> tuple[np.ndarray, np.ndarray]:
    xml = ElementTree.parse(str(xml_path))
    playlist = xml.find(f".//NODE[@Name='{playlist}']")

    spectrograms = []
    annotations = []

    for i, item in enumerate(playlist, 1):
        track_id = item.get("Key")
        track = xml.find(f".//TRACK[@TrackID='{track_id}']")
        location = Path(unquote(track.get("Location").removeprefix("file://localhost/")))
        duration_seconds = float(track.get("TotalTime"))
        print(f"{i}/{len(playlist)} ({i / len(playlist):.2%}) | {track.get('Name')}")

        if not location.exists():
            print(f"Missing file: {location}")
            continue

        marks = [
            float(mark.get("Start")) / duration_seconds
            for mark in sorted(track.findall("POSITION_MARK"), key=lambda m: m.get("Num"))
            if mark.get("Num") != "-1"
        ]

        if len(marks) != 4:
            continue

        try:
            audio, _ = librosa.load(location)

            playback_rate = librosa.get_duration(y=audio) / SONG_DURATION_SECONDS
            fixed_length_audio = librosa.effects.time_stretch(audio, rate=playback_rate)

            mfccs = librosa.feature.mfcc(y=fixed_length_audio, n_mfcc=13)
            print(mfccs.shape)
            mfccs_normalized = MinMaxScaler().fit_transform(mfccs.T).T

            librosa.display.specshow(mfccs_normalized)
            plt.colorbar()
            plt.show()

        except Exception as e:
            print(e)
            continue

        annotations.append(marks)
        spectrograms.append(mfccs_normalized)

    return np.array(spectrograms, dtype=np.float32), np.array(annotations, dtype=np.float32)


def main():
    data = load_data(XML_PATH, PLAYLIST)

    print(f"Saving data to: {OUTPUT_PATH}")
    with open(OUTPUT_PATH, "wb") as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    main()
