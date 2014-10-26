import numpy as np
import pyaudio
import time
import waveshaper

# make each synth an object and 
# then put them in an array
# and call them when you want

class dotsynth:
    """the synth"""
    
    
    def __init__(self, hd, dur, fund, pastream):
        
        self.hd = hd
        self.dur = dur
        self.fund = fund
        
        self.tone = waveshaper.makeCtones(hd, dur, fund)
        self.pastream = pastream
        

    def play(self):
        
        self.pastream.write(self.tone.astype(np.float32).tostring())

