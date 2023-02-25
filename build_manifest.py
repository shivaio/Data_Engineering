import argparse
import os
import json
import librosa


def make_manifest(args):

    output_dir = args.output_dir

    transcript_dir = args.transcript_dir

    with open(f"{output_dir}/train_manifest.json", 'w') as fp:
        for audio_idx,audio_file in enumerate(os.listdir(args.audio_dir)):

            audio_file_path = args.audio_dir + audio_file

            audio_lecture_number = int(audio_file.split(".")[0][8:])

            duration = librosa.core.get_duration(filename=audio_file_path)

            text_file_name = "lec" + str(audio_lecture_number) + ".txt"

            transcript_path = f"{transcript_dir}/{text_file_name}"

            transcript = open(transcript_path).read().replace("\n","")

            metadata = {
                "audio_filepath": audio_file_path,
                "duration": duration,
                "text": transcript
                    }
            json.dump(metadata, fp)
            fp.write('\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_dir", type=str, help="Path of preprocessed audio directory")
    parser.add_argument("--transcript_dir", type=str, help="Path of corrected transcript directory")
    parser.add_argument("--output_dir", type=str, help="output directory for the manifest file")
    args = parser.parse_args()
    make_manifest(args)