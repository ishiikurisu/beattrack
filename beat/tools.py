import wave
import numpy
import matplotlib.pyplot
import scipy.io.wavfile
import scipy.signal

def load(filename):
    fs, wave = scipy.io.wavfile.read(filename)
    return fs/100, scipy.signal.resample(wave, numpy.floor(len(wave)/100))


def plot(fs, song):
    time = numpy.arange(0, len(song)/fs, 1/fs)
    matplotlib.pyplot.plot(time, song)
    matplotlib.pyplot.show()

def envelope(song):
    return numpy.absolute(scipy.signal.hilbert(song))
