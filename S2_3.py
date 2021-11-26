from videoprops import get_video_properties
from videoprops import get_audio_properties
import subprocess

video = input("Introduce video's directory: \n")
props_video = get_video_properties(video) #Obtaining video info
props_audio = get_audio_properties(video) #Obtaining audio info of first track

video_prop = props_video['codec_name']
audio_prop = props_audio['codec_name']

#Obtaining a video with just the second audio track
subprocess.call(["ffmpeg", "-i", video, "-map", "0", "-map", "-0:a:0", "-c",
                 "copy", "container_no_audio_1.mp4"])

props_audio_2 = get_audio_properties("container_no_audio_1.mp4")
audio_prop_2 = props_audio_2['codec_name']

#If to categorize boradcasting
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

print("Thanks to: ", props_audio_2['codec_name'], " it could belong to:")
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

#Seeing more video properties
print(f'''
Codec: {props_video['codec_name']}
Resolution: {props_video['width']}×{props_video['height']}
Aspect ratio: {props_video['display_aspect_ratio']}
Frame rate: {props_video['avg_frame_rate']}
''')

#Seeing more audio properties
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