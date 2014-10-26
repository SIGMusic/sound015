import numpy as np

sr = 44100

def getSampleRate():
    return sr

def maketones(hd, dur, fund):
    t = np.arange(sr*dur)/float(sr)
    
    hdhat = hd/np.linalg.norm(hd)
    signal = np.zeros(sr*dur)

    for i in range(len(hd)):
        signal = signal + hdhat[i]*np.sin(2*np.pi*(i+1)*fund*t)
        
    return signal

def makeCtones(hdc, dur, fund):

    #complex fourier series coefficients so we don't
    #have to do 2 seperate hd vectors for sine and cos

    ncoef = (len(hdc)-1)/2
    
    t = np.arange(sr*dur)/float(sr)
    
    signal = np.zeros(sr*dur)
    
    for i in range(len(hdc)):
        signal = signal + hdc[i]*np.exp(1j*2*np.pi*(i-ncoef)*fund*t)
    
    signal = signal.real

    return signal
