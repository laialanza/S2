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
            "Introduce the directory of the video you want to see motion vectors: \n ")

        subprocess.call(["ffmpeg", "-flags2", "export_mvs", "-i", video, "-vf",
                         "codecview=mv=pf+bf+bb", "motion_vectors.mp4"])
    # Ex 2
    elif answer == 2:
        video = input(
            "Introduce the directory of the video you want to cut: \n ")
        subprocess.call(
            ['ffmpeg', '-ss', '00:00:00', '-i', video, '-to', '00:01:00',
             '-c', 'copy', '1min.mp4'])

        # Export the 1 min audio as MP3 stereo audio track
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'mp3', 'bbbMP3.mp3'])

        # Export BBB(1min) audio in AAC w/ lower bitrate
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'aac', "-b:a", "70k",
             'bbbAAC.aac'])

        # Create container
        subprocess.call(
            ['ffmpeg', '-i', '1min.mp4', '-i', 'bbbMP3.mp3', '-i', 'bbbAAC.aac',
             "-c:v", "copy", "-c:a", "copy", "-c:a", "copy", '-map', '0:v',
             '-map', '1:a','-map', '2:a', 'container.mp4'])
    # Ex 3
    elif answer == 3:
        video = input("Introduce video's directory: \n")
        props_video = get_video_properties(video)  # Obtaining video info
        props_audio = get_audio_properties(
            video)  # Obtaining audio info of first track

        video_prop = props_video['codec_name']
        audio_prop = props_audio['codec_name']

        # Obtaining a video with just the second audio track
        subprocess.call(
            ["ffmpeg", "-i", video, "-map", "0", "-map", "-0:a:0", "-c",
             "copy", "container_no_audio_1.mp4"])

        props_audio_2 = get_audio_properties("container_no_audio_1.mp4")
        audio_prop_2 = props_audio_2['codec_name']

        # If to categorize boradcasting
        print("Thanks to: ", props_audio['codec_name'], " it could belong to:")
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
            print("It does not belong to any broadcast")

        print("Thanks to: ", props_audio_2['codec_name'],
              " it could belong to:")
        if video_prop == "h264" and audio_prop_2 == "ac3":
            print("It could belong to DVB, ATSC and DTMB")
        elif video_prop == "mpeg2" and audio_prop_2 == "ac3":
            print("It could belong to DVB, ATSC and DTMB")
        elif video_prop == "avs" and audio_prop_2 == "ac3":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop_2 == "ac3":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop_2 == "aac":
            print("It could belong to DVB, ISDB and DTMB")
        elif video_prop == "mpeg2" and audio_prop_2 == "aac":
            print("It could belong to DVB, ISDB and DTMB")
        elif video_prop == "avs" and audio_prop_2 == "aac":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop_2 == "aac":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop_2 == "mp3":
            print("It could belong to DVB and DTMB")
        elif video_prop == "mpeg2" and audio_prop_2 == "mp3":
            print("It could belong to DVB and DTMB")
        elif video_prop == "avs" and audio_prop_2 == "mp3":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop_2 == "mp3":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop_2 == "mp2":
            print("It could belong DTMB")
        elif video_prop == "mpeg2" and audio_prop_2 == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "avs" and audio_prop_2 == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop_2 == "mp2":
            print("It could belong to DTMB")
        elif video_prop == "h264" and audio_prop_2 == "dra":
            print("It could belong DTMB")
        elif video_prop == "mpeg2" and audio_prop_2 == "dra":
            print("It could belong to DTMB")
        elif video_prop == "avs" and audio_prop_2 == "dra":
            print("It could belong to DTMB")
        elif video_prop == "avs+" and audio_prop_2 == "dra":
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

        print(f'''
        Codec: {props_audio_2['codec_name']}
        Channels: {props_audio_2['channels']}
        Sample rate: {props_audio_2['sample_rate']}
        ''')
    # Ex 4
    elif answer == 4:
        video = input("Introduce the video's directory: \n")
        print("Now I will download the subtitles\n")
        subprocess.call(["wget",
                         "https://www.opensubtitles.com/download/A9CAE7B67F3C8248E6608E410ADAA5F87049E943A891C12175B300B2331FABCC5F5E1968C6EC0A72FC6F911941272ECDBDF7631237C2B8B36F020030428382E2284054D9A2421ED7D20BB95FB2C398BCF8E4A0ADF87E19BA110A0454F8FA7142EB29780E1BF1926510916E0A2635F40911DFF04C6A5DFF1A129BE7CBEB64E675554FBEA7ED52DA1079113F22AACD5615F744A64CE97E8F7254A8DC91D2B172D63BE259124C3D807A8AA73C3FBDCD9E8B7F390D838947872CF42533E7D465F411DB44B9B7244BE40E5B0647899953244EAD2ACF862B202395F4A55EE90173F8D7D5919B76FD7CB6847B91271B2BAA82F7ED6A1A35A55118CD4A4FC64F278DEFF00DA6B2C45350082ADB874E272C907480E634D2315375F193/subfile/Game.of.Thrones.The.Story.So.Far.2017.HDTV.x264-PLUTONiUM.srt"])

        subprocess.call(["ffmpeg", "-i", video, "-vf",
                         "subtitles=Game.of.Thrones.The.Story.So.Far.2017.HDTV.x264-PLUTONiUM.srt",
                         "-c:v",
                         "libx264", "-crf", "20", "-c:a", "aac", "-b:a", "192k",
                         "output.mp4"])


    # To exit
    elif answer == 5:
        answer = False
    # Wrong command
    else:
        print("Write a valid command")