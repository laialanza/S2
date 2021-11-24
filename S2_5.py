import subprocess
from videoprops import get_video_properties
from videoprops import get_audio_properties

answer=True
while answer:
    print("""
        1.Show the macroblocks and the motion vectors. 
        2. You’re going to create a script in order to create a new BBB container:
            ·Cut BBB into 1 minute only video.
            ·Export BBB(1min) audio as MP3 stereo track.
            ·Export BBB(1min) audio in AAC w/ lower bitrate
        Now package everything in a .mp4 with FFMPEG!!
        3.Create a script which reads the tracks from an MP4 container, and it’s able to say:
            ·Which broadcasting standard would fit
            ·ERROR in case it doesn’t fit any
            ·Any more “pijada” you could think (be creative!)
        4.Create a script which will download subtitles, integrate them and output a video
        with printed subtitles (this means, it will form part of the video track)
        5.Exit
        """)
    answer = input("What would you like to do? \n")
    # Ex 1
    if answer == 1:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")

        subprocess.call(["ffmpeg", "-flags2", "export_mvs", "-i", video, "-vf",
                         "codecview=mv=pf+bf+bb", "motion_vectors.mp4"])
    # Ex 2
    elif answer == 2:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")
        time_sel = input("How many seconds do you want from the video: ")
        sec = "00:00:" + time_sel
        subprocess.call(
            ['ffmpeg', '-ss', '00:00:00', '-i', video, '-to', sec, '-c:a',
             'copy', 'cut_video_S2.mp4'])

        # To obtain the mp3 audio of the video
        subprocess.call(["ffmpeg", "-i", "cut_video_S2.mp4", "-acodec", "mp3",
                         "audio_mp3.mp3"])

        # To obtain the aac audio of the video
        subprocess.call(["ffmpeg", "-i", "cut_video_S2.mp4", "-acodec", "aac",
                         "audio_aac.aac"])

        # Package them into a mp4
        subprocess.call(
            ["ffmpeg", "-i", "cut_video_S2.mp4", "-i", "audio_mp3.mp3", "-i",
             "audio_aac.aac", "-map", "0", "-map", "1", "-map", "2",
             "S2_2_mp4_video.mp4"])
    # Ex 3
    elif answer == 3:
        video = input("Introduce video's directory: \n")
        props_video = get_video_properties(video)  # Obtaining video info
        props_audio = get_audio_properties(video)  # Obtaining audio info

        video_prop = props_video['codec_name']
        audio_prop = props_audio['codec_name']

        # If to categorize boradcasting
        if video_prop == "h264" and audio_prop == "ac3":
            print("It could belong to DVB, ATSC and DTMB")
        elif video_prop == "mpeg2" and audio_prop == "ac3":
            print("It could belong to DVB, ATSC and DTMB")
        elif video_prop == "avs" and audio_prop == "ac3":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop == "ac3":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop == "aac":
            print("It could belong to DVB, ISDB and DTMB")
        elif video_prop == "mpeg2" and audio_prop == "aac":
            print("It could belong to DVB, ISDB and DTMB")
        elif video_prop == "avs" and audio_prop == "aac":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop == "aac":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop == "mp3":
            print("It could belong to DVB and DTMB")
        elif video_prop == "mpeg2" and audio_prop == "mp3":
            print("It could belong to DVB and DTMB")
        elif video_prop == "avs" and audio_prop == "mp3":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop == "mp3":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop == "mp2":
            print("It could belong DTMB")
        elif video_prop == "mpeg2" and audio_prop == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "avs" and audio_prop == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop == "dra":
            print("It could belong DTMB")
        elif video_prop == "mpeg2" and audio_prop == "dra":
            print("It could belong to DTMB")
        elif video_prop == "avs" and audio_prop == "dra":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop == "dra":
            print("It could belong to DTMB")
        else:
            print("It does not belong to any broadcasting")

        # Seeing more video properties
        print(f'''
            Codec: {props_video['codec_name']}
            Resolution: {props_video['width']}×{props_video['height']}
            Aspect ratio: {props_video['display_aspect_ratio']}
            Frame rate: {props_video['avg_frame_rate']}
            ''')

        # Seeing more audio properties
        print(f'''
            Codec: {props_audio['codec_name']}
            Channels: {props_audio['channels']}
            Sample rate: {props_audio['sample_rate']}
            ''')

    # Ex 4
    elif answer == 4:
        video = input("Introduce the video's directory: \n")
        print("Now I will download the subtitles\n")
        subprocess.call(["wget",
                         "https://github.com/moust/MediaPlayer/blob/master/demo/subtitles.srt"])

        subprocess.call(
            ["ffmpeg", "-i", video, "-vf", "subtitles=subtitles.srt", "-c:v",
             "libx264", "-crf", "20", "-c:a", "aac", "-b:a", "192k",
             "output.mp4"])

    # To exit
    elif answer == 5:
        answer = False
    # Wrong command
    else:
        print("Write a valid command")