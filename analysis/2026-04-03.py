import numpy as np
import scipy.interpolate as spl
import matplotlib.pyplot as plt


signal, time = np.loadtxt("../readings/sensor1-idle_4.txt", delimiter=",", unpack=True)
time = (time - time[0]) / 1000

plt.clf()
plt.cla()
plt.close()
plt.xlabel("ADC Output")
plt.ylabel("Number of readings")
plt.hist(signal, bins=100)
plt.savefig("../obsidian/graphite-sensor/figures/sensor1-idle-hist_dc.png")
# plt.show()

average = np.mean(signal)
print(np.std(signal))
print(np.mean(signal))
print(np.mean(signal) / np.std(signal))

fft_vals = np.fft.rfft(signal - average)
fft_freqs = np.fft.rfftfreq(len(signal), time[1] - time[0])

plt.clf()
plt.cla()
plt.close()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.plot(
    fft_freqs,
    np.abs(fft_vals) ** 2,
)
plt.savefig("../obsidian/graphite-sensor/figures/dc-power-spectrum.png")
# plt.show()


signal, time = np.loadtxt(
    "../readings/sensor1-outward-90_1.txt", delimiter=",", unpack=True
)
time = (time - time[0]) / 1000
spline = spl.make_smoothing_spline(time, signal, lam=5)

plt.clf()
plt.cla()
plt.close()
plt.xlabel("ADC Output")
plt.ylabel("Time (ms)")
plt.plot(time, signal)
plt.plot(time, spline(time))
plt.savefig("../obsidian/graphite-sensor/figures/sensor1-outwardbend-timeseries.png")
# plt.show()


fft_vals = np.fft.rfft(signal - spline(time))
fft_freqs = np.fft.rfftfreq(len(signal), time[1] - time[0])

plt.clf()
plt.cla()
plt.close()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.plot(
    fft_freqs,
    np.abs(fft_vals) ** 2,
)
plt.savefig("../obsidian/graphite-sensor/figures/outwardbend-power-spectrum.png")
# plt.show()
