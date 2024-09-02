


"""
Audio Graph

import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load the audio file
y, sr = librosa.load('audio_file.wav')

# Compute the Root Mean Square (RMS) for loudness
rms = librosa.feature.rms(y=y)[0]

# Create a time axis
frames = range(len(rms))
t = librosa.frames_to_time(frames, sr=sr)

# Plot the RMS energy over time
plt.figure(figsize=(10, 6))
plt.plot(t, rms, label='Loudness (RMS)')
plt.xlabel('Time (s)')
plt.ylabel('Loudness')
plt.title('Loudness Over Time')
plt.legend()
plt.show()

OR


def time_volume_2d(audio_file):
    Plots the time and volume of an audio file in 2D.

    Args:
        audio_file (string): Path to the audio file.
  

    y, sr = librosa.load(audio_file)

    volume = librosa.feature.rms(y=y)
    time = librosa.times_like(volume)

    plt.plot(time, volume[0])
    plt.show()

"""

