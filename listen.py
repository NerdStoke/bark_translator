import array
import pyaudio
#import struct
import numpy as np
import time

mic = pyaudio.PyAudio()


CHUNK=512
#CHUNK=8192
FORMAT=pyaudio.paInt32
DEVICE=0
RATE=int(mic.get_device_info_by_index(DEVICE)['defaultSampleRate'])


mic_kwargs = {
    'input_device_index': DEVICE,
    'format': FORMAT,
    'channels': 1,
    'rate': RATE,
    'input': True,
    'output': True,
    'frames_per_buffer': CHUNK}


stream = mic.open(**mic_kwargs)


while True:
    data = array.array('h')
    #for i in range(0,int(RATE / CHUNK * RECORD SECONDS))
    #data.fromstring(stream.read(CHUNK, exception_on_overflow = False))
    data = stream.read(CHUNK, exception_on_overflow = False)
    data = np.frombuffer(data, np.int32)
    y = np.fft.fft(np.array(data, dtype='i'))
    #print(y)
    spec_x = np.fft.fftfreq(CHUNK, d = 1.0 / RATE)
    spec_y = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in y]
    print(spec_y[0])
    #print(len(spec_y))
    #time.sleep(0.1)
