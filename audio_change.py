import argparse

from utils.audio_modifier import AudioModifier


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, help='Path to input audio file.')
    parser.add_argument('--speed_coef', type=float, required=False, default=1.,
                        help='Coefficient for speed modification.')
    parser.add_argument('--volume_coef', type=float, required=False, default=0.,
                        help='Coefficient for volume modification.')
    parser.add_argument('--output_path', type=str, help='Path to output audio file.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    audio_modifier = AudioModifier(args.input_path, args.speed_coef, args.volume_coef, args.output_path)
    audio_modifier.modify_audio()

if __name__ == "__main__":
    main()