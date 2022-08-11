"""
snomai version 0.2.2
Created by: Braxton McCormack
"""
########################################imports 
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import time
import os
import random
from pytube import YouTube
########################################

########################################  
def cut_function(input,timestamps,padding = 0.1):
    temp = "C:/Users/captl/Desktop/snomai/temp/"
    for i in range(len(timestamps)):
        named_output = temp + str(i) + ".mp4"
        if (timestamps[i+1] != -1):
            ffmpeg_extract_subclip(input, timestamps[i]+padding, timestamps[i+1]-padding, targetname = named_output)
        else: break    
########################################  

########################################
def get_timestamp():
    print("Enter float value timestamps:")
    try:
        timestamps = []
        while True:
            timestamps.append(float(input()))    
    except:
        return(timestamps)
########################################    

########################################
def clip_pick():
    mylist = os.listdir("C:/Users/captl/Desktop/snomai/temp/")
    return mylist

########################################

########################################
def timestamp_text_to_list(timestamps):
    text_file = open(timestamps)
    data = text_file.read()
    text_file.close
    timestamplist = [float(x) for x in data.split(',')]
    return timestamplist

########################################

########################################
def clip_merge(filelist,output):
    cliplist = []
    for i in range(len(filelist)):
        cliplist.append(VideoFileClip("C:/Users/captl/Desktop/snomai/temp/" + filelist[i]))
    final = concatenate_videoclips(cliplist)
    final.write_videofile(output)
        
########################################

########################################
def watermark(output):
    video = VideoFileClip(output)

    logo = (ImageClip("C:/Users/captl/Desktop/snomai/watermark/watermark.png")
            .set_duration(video.duration)
            .resize(height=30) # if you need to resize...
            .margin(right=5, bottom=8, opacity=3) # (optional) logo-border padding
            .set_pos(("right","bottom")))

    final = CompositeVideoClip([video, logo])
    final.write_videofile("test.mp4")

########################################

########################################
def get_youtube(link, download_path = "C:/Users/captl/Desktop/snomai/resources/download.mp4"):
    yt = YouTube(link)
    try:
        yt.streams.filter(file_extension="mp4").get_by_resolution("1080p").download(download_path)
    except:
        yt.streams.filter(file_extension="mp4").get_highest_resolution().download(download_path)

########################################

########################################
def clip_delete(link, filelist):
    tempPath = "C:/Users/captl/Desktop/snomai/temp/"
    for i in range(len(filelist)):
        os.remove("C:/Users/captl/Desktop/snomai/temp/" + filelist[i])

########################################

########################################  
def main():
    downloadPath = "C:/Users/captl/Desktop/snomai/resources/"
    file = "C:/Users/captl/Desktop/snomai/resources/download.mp4"
    output = "C:/Users/captl/Desktop/snomai/result/output.mp4"
    timestamps = "C:\Users\captl\Desktop\snomai\timestamps\timestamps_1"

    # get_youtube("https://youtu.be/_i4R-wkblpQ", downloadPath)
    
    # timestamp_list = get_timestamp()
    timestamp_list = timestamp_text_to_list(timestamps)
    timestamp_list.append(float(-1))  

    # cut_function(file,timestamp_list)

    # cliplist = clip_pick()
    # random.shuffle(cliplist)
    # clip_merge(cliplist,output)

    watermark(output)
########################################  

########################################  
if __name__ == "__main__":
    main()
########################################  