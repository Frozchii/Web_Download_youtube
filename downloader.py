from pytubefix import YouTube
import subprocess
import os

def download_video(url , pilih):
    ytVideo = YouTube(url)
    

    if pilih == "mp4" :
        videoStream = ytVideo.streams.filter( res="720p" , progressive=False).first()
        audioStream = ytVideo.streams.filter(only_audio=True).first()

        print("download video.............................")
        videoPath= videoStream.download(filename="tempVideo.mp4")
        print("download audio.............................")
        audioPath= audioStream.download(filename="tempaudio.mp4")
        typeFile =".mp4"

        print("combining the video........................")
        subprocess.run(["ffmpeg", "-i", videoPath, "-i", audioPath, "-c", "copy", "output.mp4"])
        os.remove(videoPath)
        os.remove(audioPath)

        filePath = "output.mp4"

      
    elif pilih == "mp3":
        typeFile = ".mp3"
        AudioStream = ytVideo.streams.filter(only_audio=True).first()
        audioPath = AudioStream.download(filename="tempaudio.m4a")
        subprocess.run(["ffmpeg", "-i", audioPath, "-vn", "-acodec", "libmp3lame", "-q:a", "2", "output.mp3"])
        os.remove(audioPath)
        
        filePath = "output.mp3"


    else :
        print("format tidak mendukung")
        return


    # f
    return {
        "title" : ytVideo.title ,
        "file_Path" : filePath,
        "typeFile" : typeFile
    }


# download_video("https://www.youtube.com/watch?v=RVSjASRcYaE" , "mp3")