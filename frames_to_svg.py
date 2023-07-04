import os
import cv2
from PIL import Image
from svg.path import parse_path
lst = os.listdir('path_to_jpg_frames')
files_len = len(lst)
objects = []
for i in range(0,files_len):
	jpg_path = f'{"path_to_jpg_frames"}{i}{".jpg"}'
	im_gray = cv2.imread(jpg_path, cv2.IMREAD_GRAYSCALE)
	(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	thresh = 127
	im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
	cv2.imwrite('path_to_png', im_bw)
	img = Image.open("path_to_png")
	img.save('path_to_bmp')
	os.system(f'{"potrace path_to_bmp --svg -o path_to_svg"}{i}{".svg"}')
	print("frame №",i," converted!")