import numpy as np
import matplotlib.pyplot as plt


signal, time = np.loadtxt("../readings/sensor1-idle_2.txt", delimiter=",", unpack=True)
dc_signal, dc_time = np.loadtxt(
    "../readings/sensor1-idle_3.txt", delimiter=",", unpack=True
)
time = (time - time[0]) / 1000
dc_time = (dc_time - dc_time[0]) / 1000

plt.clf()
plt.cla()
plt.close()
plt.xlabel("ADC Output")
plt.ylabel("Number of readings")
plt.hist(signal, bins=100)
plt.savefig("./obsidian/graphite-sensor/figures/sensor1-idle-hist.png")
# plt.show()
print(np.std(signal))
print(np.mean(signal))
print(np.mean(signal) / np.std(signal))
average = np.mean(signal)
dc_average = np.mean(dc_signal)

fft_vals = np.fft.rfft(signal - average)
dc_fft_vals = np.fft.rfft(dc_signal - dc_average)
fft_freqs = np.fft.rfftfreq(len(signal), time[1] - time[0])
dc_fft_freqs = np.fft.rfftfreq(len(dc_signal), dc_time[1] - dc_time[0])

plt.clf()
plt.cla()
plt.close()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.plot(fft_freqs, np.abs(fft_vals) ** 2, label="Laptop plugged in")
plt.plot(dc_fft_freqs, np.abs(dc_fft_vals) ** 2, label="Laptop unplugged")
plt.legend()
plt.savefig("./obsidian/graphite-sensor/figures/laptop-groundloop-demo.png")
# plt.show()
