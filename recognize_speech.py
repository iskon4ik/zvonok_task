import argparse

from utils.audio_transcriber import AudioTranscriber

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, help='Path to input audio file.')
    parser.add_argument('--output_path', type=str, help='Path to output JSON file.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    audio_transcriber = AudioTranscriber(args.input_path, args.output_path)
    audio_transcriber.recognize()

if __name__ == "__main__":
    main()