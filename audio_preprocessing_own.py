import math
import librosa
import os
from sklearn.preprocessing import StandardScaler
import argparse
from pydub import AudioSegment

def audio_preprocessing_end(args):
    winlen = 0.02
    hoplen = 0.01
    n_mfcc = 19
    output_dir = args.output_dir
    for audio_file in os.listdir(args.input_dir):
        audio_file = audio_file

        original, sr = librosa.load(args.input_dir + audio_file)

        mel_spectrum = librosa.feature.melspectrogram(y=original, sr=sr, n_fft=int(sr * winlen), hop_length=int(sr * hoplen))

        mfcc_features = librosa.feature.mfcc(S=librosa.power_to_db(mel_spectrum), n_mfcc=n_mfcc)

        ss = StandardScaler()

        trans_mfcc_features = ss.fit_transform(mfcc_features.T).T

        bounds = librosa.segment.agglomerative(trans_mfcc_features, 2)

        bound_times = librosa.frames_to_time(bounds)

        boundary = math.floor(bounds[1] * hoplen)-2

        boundary_ms = boundary * 1000

        audio_last_music_removed = AudioSegment.from_wav(args.input_dir + audio_file)[0:boundary_ms]

        audio_last_music_removed.export(out_f=f'{output_dir}/{audio_file}',format='wav')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir",type=str,help=" Directory path containing wav audios")
    parser.add_argument("--output_dir", type=str, help=" Output directory path")
    args = parser.parse_args()
    audio_preprocessing_end(args)