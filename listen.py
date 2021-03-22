import array
import pyaudio
#import struct
import numpy as np
import time
import pickle

mic = pyaudio.PyAudio()

BG_CALC_RATE=10
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

spec_x = np.fft.fftfreq(CHUNK, d=(1.0/RATE))
half_way = int(len(spec_x)/2)

iter = 1
sub_array = np.empty((0,CHUNK),int)
background = None

while True:
    if iter % BG_CALC_RATE == 0:
        print(iter)
        print('-----')
        background = np.median(sub_array, axis=0)
        #print(len(background))
        #print(background[0])
        #print(np.shape(background))
        #print(np.shape(background[0]))
        sub_array = np.empty((0,CHUNK),int)
    data = array.array('h')
    #for i in range(0,int(RATE / CHUNK * RECORD SECONDS))
    #data.fromstring(stream.read(CHUNK, exception_on_overflow = False))
    data = stream.read(CHUNK, exception_on_overflow = False)
    data = np.frombuffer(data, np.int32)
    y = np.fft.fft(np.array(data, dtype='i'))
    #print(y)
    spec_y = np.array([[np.sqrt(c.real ** 2 + c.imag ** 2) for c in y]])
    sub_array = np.append(sub_array,spec_y,axis=0)
    #print(sub_array)
    if background is not None:
        #print(spec_y[0]-background)
        with open('data.pkl', 'wb') as fp:
            pickle.dump(spec_y[0]-background,fp)
        #print(spec_y[0][-1],background[-1])
    #print(len(spec_y))
    #time.sleep(0.1)

    iter+=1
