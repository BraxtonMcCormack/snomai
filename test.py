"""
C:/Users/captl/Desktop/snomai/result/output.mp4
C:/Users/captl/Desktop/snomai/watermark/watermark.png
"""
# import moviepy.editor as mp

# video = mp.VideoFileClip("C:/Users/captl/Desktop/snomai/result/output.mp4")

# logo = (mp.ImageClip("C:/Users/captl/Desktop/snomai/watermark/watermark.png")
#           .set_duration(video.duration)
#           .resize(height=30) # if you need to resize...
#           .margin(right=5, bottom=8, opacity=3) # (optional) logo-border padding
#           .set_pos(("right","bottom")))

# final = mp.CompositeVideoClip([video, logo])
# final.write_videofile("test.mp4")

import moviepy.editor

video = moviepy.editor.VideoFileClip("C:/Users/captl/Desktop/snomai/result/output.mp4")

logo = (moviepy.editor.ImageClip("C:/Users/captl/Desktop/snomai/watermark/watermark.png")
          .set_duration(video.duration)
          .resize(height=30) # if you need to resize...
          .margin(right=5, bottom=8, opacity=3) # (optional) logo-border padding
          .set_pos(("right","bottom")))

final = moviepy.editor.CompositeVideoClip([video, logo])
final.write_videofile("test.mp4")