import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np

mic = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
DEVICE=0
RATE=int(mic.get_device_info_by_index(DEVICE)['defaultSampleRate'])
CHUNK = int(RATE/20)
stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)


fig, ax = plt.subplots(figsize=(14,6))
x = np.arange(0, 2 * CHUNK, 2)
ax.set_ylim(-CHUNK, CHUNK)
ax.set_xlim(0, CHUNK) #make sure our x axis matched our chunk size
line, = ax.plot(x, np.random.rand(CHUNK))


while True:
    data = stream.read(CHUNK)
    data = np.frombuffer(data, np.int16)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)