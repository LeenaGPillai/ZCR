import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency in Hz
f = 5      # Frequency of the sine wave in Hz
duration = 1  # Duration in seconds

# Generate time vector
t = np.linspace(0, duration, int(fs * duration))

# Generate sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Zero Crossing Detection
zero_crossings = np.where(np.diff(np.sign(sine_wave)))[0]
zcr = len(zero_crossings) / duration

print(f"Zero Crossing Rate (ZCR): {zcr:.2f} crossings per second")

# Plot the sine wave and zero crossings
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Sine Wave (5 Hz)")
plt.plot(t[zero_crossings], sine_wave[zero_crossings], 'ro', label="Zero Crossings")
plt.title("Sine Wave with Zero Crossings")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
