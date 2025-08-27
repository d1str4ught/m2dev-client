import os
import stat

def FindFilesByExt(ext, path):
	if path[-1] != os.sep:
		path += os.sep

	ext = ext.lower()

	retList = []
	for name in os.listdir(path):
		if stat.S_ISDIR(os.stat(path+name).st_mode):
			retList += FindFilesByExt(ext, path+name)
		else:
			if name[-len(ext):].lower() == ext:
				retList.append(path + name)

	return retList

if __name__ == "__main__":
	for path in FindFilesByExt(".msa", "."):
		print path
