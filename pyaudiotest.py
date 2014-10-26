import numpy as np
import math
import pyaudio
import time
import waveshaper

#t = np.arange(44100)/44100.


#tone = np.array([np.sin(440*2*np.pi*t),np.sin(880*2*np.pi*t)])
#tone = np.transpose(tone)


hd = 1/np.pi *np.array([ 0.+0.2j       ,  0.-0.25j      ,  0.+0.33333333j,  0.-0.5j       ,
        0.+1.j        ,  0.+0.j        ,  0.-1.j        ,  0.+0.5j       ,
        0.-0.33333333j,  0.+0.25j      ,  0.-0.2j       ])

tone2 = waveshaper.makeCtones(hd, 1, 440)
tone2 = np.array([tone2,tone2])
#LOUD LOUD LOUD!!!
tone2 = 0.05*np.transpose(tone2)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32, channels=2, rate=44100, output=1)

for i in range(0,9):
    stream.write(tone2.astype(np.float32).tostring())
    time.sleep(0.1)

p.terminate()

