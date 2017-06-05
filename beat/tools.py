import wave
import numpy
import matplotlib.pyplot
import scipy.io.wavfile

def load(filename):
    fs, wave = scipy.io.wavfile.read(filename)
    return fs, wave


def plot(fs, song):
    time = numpy.arange(0, len(song)/fs, 1/fs)
    matplotlib.pyplot.plot(time, song)
    matplotlib.pyplot.show()
