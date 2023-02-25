import librosa
import os
import argparse
import soundfile as sf


def remove_silence_start_end(args):

    output_dir = args.output_dir

    for audio_file in os.listdir(args.input_dir):

        original_audio, sr = librosa.load(args.input_dir + audio_file,sr=None)

        trimmed_audio, index = librosa.effects.trim(original_audio)

        sf.write(f'{output_dir}/{audio_file}', trimmed_audio, 16000)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir",type=str, help="Path of input audio wavs directory")
    parser.add_argument("--output_dir",type=str, help="Path of output directory")
    args = parser.parse_args()
    remove_silence_start_end(args)