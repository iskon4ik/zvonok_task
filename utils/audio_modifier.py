import numpy as np
from pydub import AudioSegment
from pydub.utils import mediainfo
import pyrubberband as pyrb
import soundfile as sf


class AudioModifier:

    def __init__(self, input_path, speed_coef, volume_coef, output_path):
        assert speed_coef > 0
        self.input_path = input_path
        self.speed_coef = speed_coef
        self.volume_coef = volume_coef
        self.output_path = output_path

    def read_audio(self):
        data = AudioSegment.from_wav(self.input_path)
        info = mediainfo(self.input_path)
        samplerate = int(info['sample_rate'])
        return data, samplerate

    def change_volume(self, data):
        return data + self.volume_coef

    def change_speed(self, data, samplerate):
        np_array = np.array(data.get_array_of_samples())
        return pyrb.time_stretch(np_array, samplerate, self.speed_coef)

    def save_audio(self, data, samplerate):
        sf.write(self.output_path, data, samplerate, format='wav')

    def modify_audio(self):
        data, samplerate = self.read_audio()
        new_data = self.change_volume(data)
        new_data = self.change_speed(new_data, samplerate)
        self.save_audio(new_data, samplerate)

