import json
import whisper


class AudioTranscriber:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.model = whisper.load_model('base')

    def is_russian(self):
        audio = whisper.load_audio(self.input_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        _, probs = self.model.detect_language(mel)
        return probs['ru'] > probs['en']

    def get_speech(self):
        options = dict(beam_size=5, best_of=5)
        if self.is_russian():
            options['language'] = 'Russian'
        transcribe_options = dict(task="transcribe", **options)

        return self.model.transcribe(self.input_path, **transcribe_options)['text']

    def save_result(self, speech):
        result = {
            'input_path': self.input_path,
            'speech': speech
        }
        with open(self.output_path, "w") as outfile:
            json.dump(result, outfile)

    def recognize(self):
        speech = self.get_speech()
        print(speech)
        self.save_result(speech)