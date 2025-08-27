from devil import *
from struct import *
from ilu import *
import ctypes
nvDXTsave = ctypes.cdll.nvdxt.nvDXTsave

import glob
import os

for srcFileName in glob.glob("*.tga"):
	srcHead, srcExt = os.path.splitext(srcFileName)
	print srcHead, srcExt

	src = ilGenImage()
	ilBindImage(src)
	ilLoad(IL_TYPE_UNKNOWN, srcFileName)
	ilConvertImage(IL_BGRA, IL_UNSIGNED_BYTE)
	w = ilGetInteger(IL_IMAGE_WIDTH)
	h = ilGetInteger(IL_IMAGE_HEIGHT)
	d = ilGetData()

	print w, h
	dst = ilGenImage()
	ilBindImage(dst)
	ilTexImage(128, 128, 1, 4, IL_BGRA, IL_UNSIGNED_BYTE, pack("l", 0) * 128 * 128)
	ilSetPixels(0, 128-h, 0, w, h, 1, IL_BGRA, IL_UNSIGNED_BYTE, d)
	iluFlipImage()

	d = ilGetData()
	w = ilGetInteger(IL_IMAGE_WIDTH)
	h = ilGetInteger(IL_IMAGE_HEIGHT)
	pitch = w * 4

	ddsFileName = "%s.dds" % (srcHead)
	if not nvDXTsave(d, w, h, pitch, ddsFileName):
		print "nvdxt.Save(%s) - ERROR" % (ddsFileName)

	lineList = (
		'title subImage',
		'version 2.0',
		'image "%s"' 	% (ddsFileName),
		'left %s' 	% (0),
		'top %s' 	% (0),
		'right %s' 	% (96),
		'bottom %s' 	% (96),
	)
	subFileName = "%s.sub" % (srcHead)
	subFile = file(subFileName, "w")
	subFile.write("\n".join(lineList))
