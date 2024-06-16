# -*- coding: utf-8 -*-
"""
2D FFT for images
Aldo Cervantes Marquez

https://stackoverflow.com/questions/59921561/gaussian-notch-filter-in-python

The 2D Fourier Transform script is designed for image processing, 
specifically using FFT (Fast Fourier Transform) for images.
It provides functions for filtering images in the frequency domain, including 
visualizations of the original and filtered images' spectra and phases.
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def filters(img, t_f, freq):
    if img.ndim == 3: # Ensure the number of channels
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ax, ay = img.shape
    fftg = np.fft.fft2(img)
    amp_spectrum = np.abs(np.fft.fftshift(fftg))
    phase_spectrum = np.angle(np.fft.fftshift(fftg))
    plt.figure()
    plt.imshow(100*np.log(1+amp_spectrum))
    plt.title('Original Image Amplitude Spectrum')
    plt.show()
    plt.figure()
    plt.imshow(phase_spectrum)
    plt.title('Original Image Phase Spectrum')
    plt.show()
    
    cx = int(ax/2)
    cy = int(ay/2)
    if t_f == 'lp':
        size = freq
        mask1 = np.zeros(img.shape)
        mask1[cx-size:cx+size, cy-size:cy+size] = 1
        filtered_amp = amp_spectrum * mask1
        filtered_phase = phase_spectrum * mask1
    elif t_f == 'hp':
        size = freq
        mask1 = np.zeros(img.shape)
        mask1[cx-size:cx+size, cy-size:cy+size] = 1
        mask2 = 1 - mask1
        filtered_amp = amp_spectrum * mask2
        filtered_phase = phase_spectrum * mask2
    elif t_f == 'bp':
        b_sup = freq[-1]
        b_inf = freq[0]
        mask3 = np.zeros(img.shape)
        mask3[cx-b_sup:cx+b_sup, cy-b_sup:cy+b_sup] = 1
        mask3[cx-b_inf:cx+b_inf, cy-b_inf:cy+b_inf] = 0
        filtered_amp = amp_spectrum * mask3
        filtered_phase = phase_spectrum * mask3
    elif t_f == 'bs':
        b_sup = freq[-1]
        b_inf = freq[0]
        mask3 = np.zeros(img.shape)
        mask3[cx-b_sup:cx+b_sup, cy-b_sup:cy+b_sup] = 1
        mask3[cx-b_inf:cx+b_inf, cy-b_inf:cy+b_inf] = 0
        mask4 = 1 - mask3
        filtered_amp = amp_spectrum * mask4
        filtered_phase = phase_spectrum * mask4
    else:
        return 'Error'
    plt.figure()
    plt.imshow(100*np.log(filtered_amp+1))
    plt.title('Filtered Image Magnitude Spectrum')
    plt.show()
    plt.figure()
    plt.imshow(filtered_phase)
    plt.title('Filtered Image Phase Spectrum')
    plt.show()
    # Image reconstruction
    filtered_image = filtered_amp * np.exp(1j*filtered_phase)
    filtered_image = np.fft.ifft2(filtered_image)
    # Image limits
    cmin = np.min(np.min(np.abs(filtered_image)))
    cmax = np.max(np.max(np.abs(filtered_image)))
    plt.figure()
    plt.imshow(np.abs(filtered_image), cmap='gray')
    plt.title('Filtered Image')
    plt.show()
    return filtered_image

# Load images and display them in grayscale

# Image 1
ima = cv2.imread('Casa1.jpeg')
if ima.ndim == 3:
    ima = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image 1', ima)
# 2D Fourier Transform
ffta = np.fft.fft2(ima)
# Magnitude and phase
fftam = np.abs(np.fft.fftshift(ffta))
fftang = np.angle(np.fft.fftshift(ffta))
plt.figure()
plt.imshow(100*np.log(1+fftam))
plt.title('Image 1 Magnitude Spectrum')
plt.show()
plt.figure()
plt.imshow(fftang)
plt.title('Image 1 Phase Spectrum')
plt.show()

# Image 2
imb = cv2.imread('aishwayra.jpeg')
imb = cv2.cvtColor(imb, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image 2', imb)
fftb = np.fft.fft2(imb)
# Magnitude and phase
fftbm = np.abs(np.fft.fftshift(fftb))
fftbng = np.angle(np.fft.fftshift(fftb))
plt.figure()
plt.imshow(100*np.log(1+fftbm))
plt.title('Image 2 Magnitude Spectrum')
plt.show()
plt.figure()
plt.imshow(fftbng)
plt.title('Image 2 Phase Spectrum')
plt.show()

# Image 3
imc = cv2.imread('img ruido periodico.jpeg')
imc = cv2.cvtColor(imc, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image 3 Original', imc)
fftc = np.fft.fft2(imc)
# Magnitude and phase
fftcm = np.abs(np.fft.fftshift(fftc))
fftcng = np.angle(np.fft.fftshift(fftc))
plt.figure()
plt.imshow(100*np.log(1+fftcm))
plt.title('Image 3 Magnitude Spectrum')
plt.show()
plt.figure()
plt.imshow(fftcng)
plt.title('Image 3 Phase Spectrum')
plt.show()

# Filtered image = filters(filters(imc, 'bs', [55,62]), 'bs', [110,130])
filtered_image = filters(imc, 'bs', [52,67])

cv2.waitKey(0)
cv2.destroyAllWindows()
