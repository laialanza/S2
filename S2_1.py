import subprocess
video = input("Introduce the directory of the video you want to cut: \n ")

subprocess.call(["ffmpeg", "-flags2", "export_mvs", "-i", video, "-vf",
                 "codecview=mv=pf+bf+bb", "motion_vectors.mp4"])
