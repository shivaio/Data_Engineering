# Data_Engineering

## For Downloading videos and transcripts
1. Run web_scraping_nptel.py --url  < url >  --output_dir_video  < Directory path for storing videos > --output_dir_trans < Directory path for storing Transcripts >
2. Run web_scraping_nptel.py --help to see options

# Comments:
1. Paths can be relative or absolute
2. What i have done is insead of downloading videos from youtube using yt-dlp, i have directly downloaded mp4 videos from nptel archive using script
3. I have downloaded pdf transcripts from google drive links available on nptel archive using gdown package
4. My script only works if by default nptel url opens with course details tab( as their are some old course nptel url which does which doesnot open by default in course details page, i am working on it to make it robust)

## For Audio Preprocessing

## For mp4 to wav

1. Run parallel_mp4_to_wav.sh --input_dir < Directory containing all mp4 videos > --output_dir < Output Directory for storing all audio wavs> --number_processes < number >
2. Run parallel_mp4_to_wav --help to see options

## Comments
1. Output directory need not to exist, script will make the directory
2. I am directly converting mp4 to wav mono channel 16kHz using ffmpeg

## For removing music at the end and start

## Comments
1. For removing music at end first i started with extracting Mel frequency cepstral coefficients(MFCC) features by dividing audio wav into 20ms window and stride of 10ms,then i tried to agglomerative clustering until i get 2 classes one for music and one for speech.( code is audio_preprocessing_own.py)
2. audio_preprocessing_own.py works only removing audio at end(  audio_preprocessing_own.py --input_dir < > --output_dir < >
3. But i realized is that it works only when their is music at end, but their are many NPTEL videos which doesnot have music at end, they have music only at start of video.
4. After removing music at the end, saving those wavs, again i tried to do agglomerative clustering for finding music at start, sometimes it works and sometimes it doesnot.
5. Then again i tried clustering using Guassian mixture model(GMM) with 2 GMM components for removing music at start of audio,but gives good results when their is only music at start, and it doest not work when audio has music at the end.
6. I did small survey on NPTEL videos, how and where the music is present, their is some videos where music is present at start and at the end, and their are some videos where music is present only at the start and their are some videos of particular course where NO music is present at the start or end only silence is present.
7. And Interestingly music used also in the video is different for different for different production units.(say IIsc production team used a music for the video which is different from music of IIT Madras production unit.)
8. Then i read this research paper INA’S MIREX 2018 MUSIC AND SPEECH DETECTION SYSTEM which is CNN based approach, i have used that code(available as package) and did some post processing which gives very good results and it can seperate music present at the start and the end.
9. audio_preprocessing_fn.py will remove music present at start and the end.
10. audio_preprocessing_fn.py --input_dir < audio wavs directory > --output_dir < output directory >.
11. For audio_preprocessing_own.py and audio_preprocessing_fn.py paths can absolute or relative if relative say ./audio_wavs  add extra / at the end say ./audio_wavs/

## For Text Preprocessing

1. Run pdf_scrapper.py --input_dir < Directory of all pdfs > --output_dir < Output Directory  >.
2. Run pdf_scrapper.py --help to see options.
3. Run text_preprocessing.py --input_dir < Directory with txts files> --output_dir <Output Directory >.
4. For pdf_scrapper.py and text_preprocessing.py paths can absolute or relative if relative say ./pdfs_txt  add extra / at the end say ./pdfs_txt/

## Comments

1. Their are some text segments which are not spoken by speaker say course name, prof. name, refer slide time etc are present , they are also removed using text_preprocessing.py

## Making manifest file

1. Run build_manifest.py --audio_dir < preprocessed audio wavs > --transcript_dir < preprocessed txt files> --output_dir < directory for train_manifest.json file >.


## Final comments

1. Preprocessed audio wavs in audio_wav_music_removed, all are not uploaded beacause of size contrainst.
2. Preprocessed corrected txt in pdfs_text_corrected.
3. Final manifest file is train_manifest.json
4. Literally i was struggling a way to preprocess audio, but i have done something, it is really hectic here doing this assignment (but enjoyed alot) with doing, attending classes for 6 courses in this semester.i was not able to complete visualization part, i am working on it.






