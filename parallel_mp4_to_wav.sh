#!/usr/bin/bash

input_dir=$(pwd)
output_dir=$(pwd)
number_processes=3

USAGE="$0 [--input_dir in] [--output_dir out] [--number_processes num]"

while [ $# -gt 0 ]; do
    case "$1" in
    (--input_dir) input_dir=$2; shift;;
    (--output_dir) output_dir=$2; shift;;
    (--number_processes) number_processes=$2; shift;;
    (--help) echo $USAGE; exit 0;;
    (--) shift; break;;
    (*)  break;;
    esac
    shift
done

mkdir $output_dir

mp4_to_wav()
{

	ffmpeg -i $file_path -ac 1 -ar 16000 -f wav $output_dir/$file.wav

}



for file_path in $input_dir/*.mp4; do

	file_name=$(basename $file_path)
	
	file=${file_name%.mp4}
	
	mp4_to_wav $file &
	
	if [[ $(jobs -r -p | wc -l) -ge $number_processes ]]; then wait -n; fi
	
done

wait


