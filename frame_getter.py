import cv2
vidcap = cv2.VideoCapture('path_to_videos')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("path_to_frames" % count, image)    
  success,image = vidcap.read()
  count += 1
