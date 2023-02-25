import argparse
import math
import os
from inaSpeechSegmenter import Segmenter
from pydub import AudioSegment
import librosa

def audio_preprocessing_function(args):
    seg_object = Segmenter(vad_engine='sm', detect_gender=False)
    output_dir = args.output_dir

    for audio_file in os.listdir(args.input_dir):

        segment_list = seg_object(args.input_dir + audio_file)

        segment_length = len(segment_list)

        if (segment_list[0][0] == 'music') and (segment_list[segment_length-1][0] == 'music'):

            speech_init = math.floor(segment_list[1][1])

            speech_init_ms = speech_init*1000

            speech_final = math.floor(segment_list[segment_length-2][2])

            speech_final_ms = speech_final*1000

            music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[speech_init_ms:speech_final_ms+1]

            music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')

        if (segment_list[0][0] == 'music') and (segment_list[segment_length - 1][0] == 'noEnergy'):

            if segment_list[segment_length - 2][0] == 'music':

                speech_init = math.floor(segment_list[1][1])

                speech_init_ms = speech_init * 1000

                speech_final = math.floor(segment_list[segment_length - 3][2])

                speech_final_ms = speech_final * 1000

                music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[
                                      speech_init_ms:speech_final_ms + 1]

                music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')

            else:

                speech_init = math.floor(segment_list[1][1])

                speech_init_ms = speech_init * 1000

                speech_final = math.floor(segment_list[segment_length - 2][2])

                speech_final_ms = speech_final * 1000

                music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[
                                      speech_init_ms:speech_final_ms + 1]

                music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')

        if segment_list[0][0] == 'music' and segment_list[segment_length - 1][0] == 'speech':

            speech_init = math.floor(segment_list[1][1])

            speech_init_ms = speech_init * 1000

            speech_final = math.floor(segment_list[segment_length-1][2])

            speech_final_ms = speech_final * 1000

            music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[speech_init_ms:speech_final_ms + 1]

            music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')

        if segment_list[0][0] == 'speech' and segment_list[segment_length - 1][0] == 'music':

            speech_init = math.floor(segment_list[0][1])

            speech_init_ms = speech_init * 1000

            speech_final = math.floor(segment_list[segment_length-2][2])

            speech_final_ms = speech_final * 1000

            music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[speech_init_ms:speech_final_ms + 1]

            music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')

        if segment_list[0][0] == 'speech' and segment_list[segment_length - 1][0] == 'speech':

            speech_init = math.floor(segment_list[0][1])

            speech_init_ms = speech_init * 1000

            speech_final = math.floor(segment_list[segment_length - 1][2])

            speech_final_ms = speech_final * 1000

            music_removed_audio = AudioSegment.from_wav(args.input_dir + audio_file)[speech_init_ms:speech_final_ms + 1]

            music_removed_audio.export(out_f=f'{output_dir}/{audio_file}', format='wav')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="Path of input directory containing audio wavs")
    parser.add_argument("--output_dir", type=str, help="Path of output directory")
    args = parser.parse_args()
    audio_preprocessing_function(args)


