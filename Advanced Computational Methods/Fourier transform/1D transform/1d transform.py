"""
1D Fourier Transform
@author: Aldo Cervantes Marquez
ECG
https://www.kaggle.com/datasets/jiahuali/labledata

The 1D Fourier Transform script focuses on processing ECG (Electrocardiogram) signals. 
It includes functions for filtering signals using different types of filters like low-pass,
high-pass, band-pass, and band-stop. The script also visualizes the original and 
filtered signals in the frequency domain.
"""

import sounddevice as sd
import soundfile as sf
import pandas as pd
import numpy as np
import scipy
from scipy.fft import fft
from scipy.signal import butter  # Uncomment if you have problems
import matplotlib.pyplot as plt

def filters(y, t_f, freq, T):
    
    order = 10  # Filter order
    w0 = 2 * np.pi / T
    length = y.shape
    div = int(length[0] / 2)
    yfft = scipy.fft.fft(y) / length
    aux = yfft
    yfft = np.concatenate((aux[div:-1, ], aux[0:div, ]))
    if length[0] % 2 == 0:
        wn = w0 * np.arange(-div, div - 1, 1)
    else:
        wn = w0 * np.arange(-div, div, 1)
    plt.figure()
    plt.stem(wn, abs(yfft))
    plt.title('Original Amplitude Spectrum')
    plt.xlabel('W')
    plt.ylabel('|A|')
    
    if t_f == 'lp':
        # Low-pass filter
        b, a = scipy.signal.butter(order, freq, btype='lowpass', analog=False)
        ft = scipy.signal.lfilter(b, a, y)
        length = ft.shape
        div = int(length[0] / 2)
        yfft = scipy.fft.fft(ft) / length
        aux = yfft
        yfft = np.concatenate((aux[div:-1, ], aux[0:div, ]))
        if length[0] % 2 == 0:
            wn = w0 * np.arange(-div, div - 1, 1)
        else:
            wn = w0 * np.arange(-div, div, 1)
        plt.figure()
        plt.stem(wn, abs(yfft))
        plt.title('Low-pass Filtered Amplitude Spectrum')
        plt.xlabel('W')
        plt.ylabel('|A|') 
        
    elif t_f == 'hp':
        # High-pass filter
        b, a = scipy.signal.butter(order, freq, btype='highpass', analog=False)
        ft = scipy.signal.lfilter(b, a, y)
        length = ft.shape
        div = int(length[0] / 2)
        yfft = scipy.fft.fft(ft) / length
        aux = yfft
        yfft = np.concatenate((aux[div:-1, ], aux[0:div, ]))
        if length[0] % 2 == 0:
            wn = w0 * np.arange(-div, div - 1, 1)
        else:
            wn = w0 * np.arange(-div, div, 1)
        plt.figure()
        plt.stem(wn, abs(yfft))
        plt.title('High-pass Filtered Amplitude Spectrum')
        plt.xlabel('W')
        plt.ylabel('|A|') 
    elif t_f == 'bp':
        # Band-pass filter
        b, a = scipy.signal.butter(order, freq, btype='bandpass', analog=False)
        ft = scipy.signal.lfilter(b, a, y)
        length = ft.shape
        div = int(length[0] / 2)
        yfft = scipy.fft.fft(ft) / length
        aux = yfft
        yfft = np.concatenate((aux[div:-1, ], aux[0:div, ]))
        if length[0] % 2 == 0:
            wn = w0 * np.arange(-div, div - 1, 1)
        else:
            wn = w0 * np.arange(-div, div, 1)
        plt.figure()
        plt.stem(wn, abs(yfft))
        plt.title('Band-pass Filtered Amplitude Spectrum')
        plt.xlabel('W')
        plt.ylabel('|A|')
    elif t_f == 'bs':
        # Band-stop filter
        b, a = scipy.signal.butter(order, freq, btype='bandstop', analog=False)
        ft = scipy.signal.lfilter(b, a, y)
        length = ft.shape
        div = int(length[0] / 2)
        yfft = scipy.fft.fft(ft) / length
        aux = yfft
        yfft = np.concatenate((aux[div:-1, ], aux[0:div, ]))
        if length[0] % 2 == 0:
            wn = w0 * np.arange(-div, div - 1, 1)
        else:
            wn = w0 * np.arange(-div, div, 1)
        plt.figure()
        plt.stem(wn, abs(yfft))
        plt.title('Band-stop Filtered Amplitude Spectrum')
        plt.xlabel('W')
        plt.ylabel('|A|')
    return ft

## ECG data acquisition
M = pd.read_csv('labelData.csv')
ecg = M.to_numpy()
ecg = ecg[:, 100]  # from 0 to 255
t = ecg.size
fs = t
x = np.linspace(0, 20, t)
plt.figure()
plt.plot(x, ecg)
plt.title('Original Signal')
plt.ylabel('A')
plt.xlabel('t')
plt.grid()
plt.show()
y = ecg

# Usage of the filters
av = filters(y, 'bs', [0.1, 0.2], 1/fs)  # Function parameters
plt.figure()
plt.plot(y)
plt.plot(av)
plt.legend(['Original Signal', 'Filtered Signal'])
plt.title('Filtered Signal')
plt.ylabel('A')
plt.xlabel('t')
plt.grid()
plt.show()

"""
sd.play(data * 0.5, fs)

status = sd.wait()

sd.play(av * 0.5, fs)
status = sd.wait()
"""
