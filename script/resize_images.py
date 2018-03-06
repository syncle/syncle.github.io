import cv2
import os
import numpy as np

# reference: https://stackoverflow.com/questions/44720580/resize-image-canvas-to-maintain-square-aspect-ratio-in-python-opencv
def resizeAndPad(img, size, padColor=1):
	h, w = img.shape[:2]
	sh, sw = size

	# interpolation method
	if h > sh or w > sw: # shrinking image
		interp = cv2.INTER_AREA
	else: # stretching image
		interp = cv2.INTER_CUBIC

	# aspect ratio of image
	aspect = w/h

	# compute scaling and pad sizing
	if aspect > 1: # horizontal image
		new_w = sw
		new_h = np.round(new_w/aspect).astype(int)
		pad_vert = (sh-new_h)/2
		pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
		pad_left, pad_right = 0, 0
	elif aspect < 1: # vertical image
		new_h = sh
		new_w = np.round(new_h*aspect).astype(int)
		pad_horz = (sw-new_w)/2
		pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
		pad_top, pad_bot = 0, 0
	else: # square image
		new_h, new_w = sh, sw
		pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

	# set pad color
	if len(img.shape) is 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
		padColor = [padColor]*3

	# scale and pad
	scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
	if pad_top < 0 or pad_bot < 0 or pad_left < 0 or pad_right < 0:
		scaled_img = scaled_img[-pad_top:new_h+pad_bot, -pad_left:new_w+pad_right,:]
	else:
		scaled_img = cv2.copyMakeBorder(
				scaled_img, pad_top, pad_bot, pad_left, pad_right,
				borderType=cv2.BORDER_CONSTANT, value=padColor)

	return scaled_img

if __name__ == "__main__":
	for file in os.listdir("../publications/data/"):
		if file.endswith(".png") or file.endswith(".jpg"):
			file_path = os.path.join("../publications/data/", file)
			file_name = os.path.basename(file)
			img = cv2.imread(file_path)
			img_scale = resizeAndPad(img, [200,500], padColor=1)
			# os.remove(file_path)
			cv2.imwrite("../publications/data/" + file_name + '_crop.jpg', img_scale)
