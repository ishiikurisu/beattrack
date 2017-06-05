import os
import re
import beat

if __name__ == '__main__':
    wave_files = map(lambda f: os.path.join('data', f),
                     filter(lambda f: re.search(r'\.wav', f),
                            [f for f in os.listdir('data')
                               if os.path.isfile(os.path.join('data', f))]))
    for wave_file in wave_files:
        print(wave_file)
        # TODO Load file
        fs, song = beat.load(wave_file)
        # TODO Plot song
        beat.plot(fs, song)
        # TODO Discover song tempo
