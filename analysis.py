import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("./readings/sensor1-idle.txt")

plt.hist(data)
# plt.show()

t = np.arange(0, 1.0, 1 / len(data))
fft_vals = np.fft.rfft(data)
fft_freqs = np.fft.rfftfreq(len(data), 1 / len(data))

plt.plot(fft_freqs[1:], fft_vals[1:])
plt.show()
