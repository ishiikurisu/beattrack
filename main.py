import wave
import os
import re

if __name__ == '__main__':
    wave_files = map(lambda f: os.path.join('data', f),
                     filter(lambda f: re.search(r'\.wav', f),
                            [f for f in os.listdir('data') if os.path.isfile(os.path.join('data', f))]))
    for wave_file in wave_files:
        print(wave_file)
        # TODO Discover song tempo
        
