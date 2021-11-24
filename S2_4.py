import subprocess

video = input("Introduce the video's directory: \n")
print("Now I will download the subtitles\n")
subprocess.call(["wget", "https://github.com/moust/MediaPlayer/blob/master/demo/subtitles.srt"])

subprocess.call(["ffmpeg", "-i", video, "-vf", "subtitles=subtitles.srt","-c:v",
                 "libx264", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "output.mp4"])

