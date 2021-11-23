from videoprops import get_video_properties
from videoprops import get_audio_properties

video = input("Introduce video's directory: \n")
props_video = get_video_properties(video) #Obtaining video info
props_audio = get_audio_properties(video) #Obtaining audio info

video_prop = props_video['codec_name']
audio_prop = props_audio['codec_name']

#If to categorize boradcasting
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