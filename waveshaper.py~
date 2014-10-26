import numpy as np

sr = 44100

def maketones(hd, dur, fund):
    t = np.arange(sr*dur)/float(sr)
    
    hdhat = hd/np.linalg.norm(hd)
    signal = np.zeros(sr*dur)

    for i in range(len(hd)):
        signal = signal + hdhat[i]*np.sin(2*np.pi*(i+1)*fund*t)
        
    return signal
