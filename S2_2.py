import subprocess

video = input("Introduce the directory of the video you want to cut: \n ")
time_sel = input("How many seconds do you want from the video: ")
sec  = "00:00:" + time_sel
subprocess.call(['ffmpeg','-ss', '00:00:00', '-i', video, '-to', sec , '-c:a',
                 'copy', 'cut_video_S2.mp4'])

#To obtain the mp3 audio of the video
subprocess.call(["ffmpeg", "-i", "cut_video_S2.mp4", "-acodec", "mp3", "audio_mp3.mp3"])

#To obtain the aac audio of the video
subprocess.call(["ffmpeg", "-i", "cut_video_S2.mp4", "-acodec", "aac", "audio_aac.aac"])

#Package them into a mp4
subprocess.call(["ffmpeg", "-i", "cut_video_S2.mp4", "-i", "audio_mp3.mp3", "-i",
                 "audio_aac.aac", "-map", "0", "-map", "1", "-map", "2",
                 "S2_2_mp4_video.mp4"])

