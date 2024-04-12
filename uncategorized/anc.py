# FAILURE

import numpy as np

import pyaudio

RATE = 44_100
CHANNELS = 2
FORMAT = pyaudio.paInt16
INPUT = True
OUTPUT = True
INPUT_DEVICE_INDEX = None
OUTPUT_DEVICE_INDEX = None
FRAMES_PER_BUFFER = 128


def callback(input_data, _, __, ___):
    data = np.invert(np.frombuffer(input_data, np.int16)).tobytes()
    return data, pyaudio.paContinue


py_audio = pyaudio.PyAudio()

stream = py_audio.open(rate=RATE,
                       channels=CHANNELS,
                       format=FORMAT,
                       input=INPUT,
                       output=OUTPUT,
                       input_device_index=INPUT_DEVICE_INDEX,
                       output_device_index=OUTPUT_DEVICE_INDEX,
                       frames_per_buffer=FRAMES_PER_BUFFER,
                       stream_callback=callback)

input("Press enter to stop.")

stream.stop_stream()
stream.close()
py_audio.terminate()