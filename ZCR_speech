import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load the audio file
audio_file = "file path of Sampleaudio.wav"  # Replace with your file path
y, sr = librosa.load(audio_file, sr=None)

# Frame length and hop length (adjustable)
frame_length = 2048  # Number of samples per frame
hop_length = 512     # Number of samples between frames

# Calculate Zero Crossing Rate (ZCR)
zcr = librosa.feature.zero_crossing_rate(y, frame_length=frame_length, hop_length=hop_length)

# Time for each frame
frames = range(zcr.shape[1])
t = librosa.frames_to_time(frames, sr=sr, hop_length=hop_length)
total_zc = int(np.sum(zcr) * len(y) / hop_length)
# Plot the original waveform
plt.figure(figsize=(14, 6))
plt.plot(np.linspace(0, len(y)/sr, len(y)), y, label="Waveform")
plt.title("Speech Audio with Zero Crossings Highlighted")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot Zero Crossing Rate (ZCR)
plt.figure(figsize=(14, 6))
plt.plot(t, zcr[0], color='r', label="Zero Crossing Rate")
plt.title("Zero Crossing Rate Over Time")
plt.xlabel("Time (s)")
plt.ylabel("ZCR")
plt.legend()
plt.grid()
plt.show()

# Print Average ZCR for reference
average_zcr = np.mean(zcr)
print(f"Total Zero Crossing:", total_zc)
print(f"Average Zero Crossing Rate: {average_zcr:.4f} crossings per frame")
