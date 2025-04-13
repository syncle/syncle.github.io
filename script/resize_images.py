import cv2
import os
import numpy as np

def resize_and_pad(img, size, padColor=255):
	h, w = img.shape[:2]
	sh, sw = size

	# interpolation method
	if h > sh or w > sw: # shrinking image
		interp = cv2.INTER_AREA
	else: # stretching image
		interp = cv2.INTER_LANCZOS4

	# compute scaling
	if w > sw and h > sh:
		if w/sw > h/sh:
			s = w/sw
			new_h = np.round(h/s).astype(int)
			scaled_img = cv2.resize(img, (sw, new_h), interpolation=interp)
		else:
			s = h/sh
			new_w = np.round(w/s).astype(int)
			scaled_img = cv2.resize(img, (new_w, sh), interpolation=interp)
	elif w > sw:
		s = w/sw
		new_h = np.round(h/s).astype(int)
		scaled_img = cv2.resize(img, (sw, new_h), interpolation=interp)
	elif h > sh:
		s = h/sh
		new_w = np.round(w/s).astype(int)
		scaled_img = cv2.resize(img, (new_w, sh), interpolation=interp)
	else:
		scaled_img = img

	# padding
	h, w = scaled_img.shape[:2]
	aspect = w/h
	aspect_desired = sw/sh
	if aspect >= aspect_desired:
		#print("image is wider than desired shape. Adding vertical padding")
		new_w = w
		new_h = np.round(new_w/aspect_desired).astype(int)
		pad_vert = (new_h-h)/2
		pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
		pad_left, pad_right = 0, 0
	elif aspect < aspect_desired:
		#print("image is taller than desired shape. Adding horizontal padding")
		new_h = h
		new_w = np.round(new_h*aspect_desired).astype(int)
		pad_horz = (new_w-w)/2
		pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
		pad_top, pad_bot = 0, 0

	# set pad color
	if len(img.shape) == 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
		padColor = [padColor]*3

	if pad_top < 0 or pad_bot < 0 or pad_left < 0 or pad_right < 0:
		scaled_img = scaled_img[-pad_top:new_h+pad_bot, -pad_left:new_w+pad_right,:]
	else:
		scaled_img = cv2.copyMakeBorder(
				scaled_img, pad_top, pad_bot, pad_left, pad_right,
				borderType=cv2.BORDER_CONSTANT, value=padColor)

	return scaled_img

# reference: https://stackoverflow.com/questions/44720580/resize-image-canvas-to-maintain-square-aspect-ratio-in-python-opencv
def resize_and_crop(img, size, padColor=255):
	# import pdb; pdb.set_trace()
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
	if len(img.shape) == 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
		padColor = [padColor]*3

	# scale and pad
	#print("orig size : %d, %d" % (w, h))
	#print("new size : %d, %d" % (new_w, new_h))
	scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
	if pad_top < 0 or pad_bot < 0 or pad_left < 0 or pad_right < 0:
		scaled_img = scaled_img[-pad_top:new_h+pad_bot, -pad_left:new_w+pad_right,:]
	else:
		scaled_img = cv2.copyMakeBorder(
				scaled_img, pad_top, pad_bot, pad_left, pad_right,
				borderType=cv2.BORDER_CONSTANT, value=padColor)

	return scaled_img

def run_folder(source_folder, target_folder, imgsize):
	for file in os.listdir(source_folder):
		if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
			file_path = os.path.join(source_folder, file)
			file_name = os.path.splitext(os.path.basename(file))[0]
			#print("processing %s" % file_name)
			img = cv2.imread(file_path)
			img_scale = resize_and_pad(img, imgsize, padColor=255)
			# os.remove(file_path)
			cv2.imwrite(target_folder + file_name + '.jpg', img_scale)

if __name__ == "__main__":
	run_folder("../publications/data/raw_images/", "../publications/data/", [400,750])
	run_folder("../source/lab_pics/raw_images/", "../source/lab_pics/", [2000,3600])