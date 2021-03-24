# import wave
# import numpy as np
# import matplotlib.pyplot as plt

# signal_wave = wave.open('20210203-232549.wav', 'r')
# sample_rate = 16000
# sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)


# sig = sig[:]


# plt.figure(1)

# plot_a = plt.subplot(211)
# plot_a.plot(sig)
# plot_a.set_xlabel('sample rate * time')
# plot_a.set_ylabel('energy')

# plot_b = plt.subplot(212)
# plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, noverlap=900)
# plot_b.set_xlabel('Time')
# plot_b.set_ylabel('Frequency')

# plt.show()




# Load the required libraries:
#   * scipy
#   * numpy
#   * matplotlib
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

# Load the data and calculate the time of each sample
samplerate, data = wavfile.read('20210203-232549.wav')
print(samplerate)
times = np.arange(len(data))/float(samplerate)

# Make the plot
# You can tweak the figsize (width, height) in inches
plt.figure(figsize=(30, 4))
# plt.fill_between(times, data[:,0], data[:,1], color='k') 
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
# You can set the format by changing the extension
# like .pdf, .svg, .eps
plt.fill_between(times, data)
plt.savefig('plot.png', dpi=100)
plt.show()