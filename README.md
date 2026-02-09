# Task: Development of an Application for Working with WAV Audio Files

## Setup:

`pip install -r requirements.txt`

## WARNING

The code was written on an M2 MacBook. Due to architectural differences, playback issues may occur. Specific package versions might not work on other systems.
As a fallback, I saved the script execution results from my machine in the `data/results` folder.

## Description:

Two functions are supported:

1. Audio file modification
2. Speech recognition

### Function 1: Audio File Modification

This function takes an audio file and allows you to change its speed and volume.
It uses the `audio_change.py` script, which accepts the following parameters:

* `input_path` – path to the original audio file
* `speed_coef` – speed coefficient; if `speed_coef = 2`, the new audio will play twice as fast. Default value is `1`.
* `volume_coef` – volume coefficient; if `volume_coef = 5`, the new audio will be 5 dB louder. Default value is `0`.
* `output_path` – path to save the modified audio file

Example:
`python audio_change.py --input_path data/345836__krzysiunet__im-not-speaking-english.wav --speed_coef 2 --volume_coef 10 --output_path data/results/speed_2_vol_10.wav`

### Function 2: Audio Transcription to Text

This function performs offline speech recognition. During the first run, the program will need to download the speech recognition model.
It uses the `recognize_speech.py` script, which accepts the following parameters:

* `input_path` – path to the original audio file
* `output_path` – path to save the JSON file with the results

Example:
`python recognize_speech.py --input_path data/607932__bogenseeberg__russian-names-poem.wav --output_path data/results/speech_rus.json`
