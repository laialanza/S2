import subprocess
video = input("Introduce the directory of the video you want to cut: \n ")
subprocess.call(
            ['ffmpeg', '-ss', '00:00:00', '-i', video, '-to', '00:01:00',
             '-c', 'copy', '1min.mp4'])

# Export the 1 min audio as MP3 stereo audio track
subprocess.call(['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'mp3', 'bbbMP3.mp3'])

# Export BBB(1min) audio in AAC w/ lower bitrate
subprocess.call(['ffmpeg', '-i', '1min.mp4', '-vn', '-acodec', 'aac', "-b:a", "70k", 'bbbAAC.aac'])

# Create container
subprocess.call(['ffmpeg', '-i', '1min.mp4', '-i', 'bbbMP3.mp3', '-i', 'bbbAAC.aac',
                 "-c:v", "copy", "-c:a", "copy", "-c:a", "copy", '-map', '0:v', '-map', '1:a',
                 '-map', '2:a', 'container.mp4'])