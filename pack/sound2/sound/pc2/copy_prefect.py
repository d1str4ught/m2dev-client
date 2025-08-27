import os
import stat

def FindFilesByExt(path):
	if path[-1] != os.sep:
		path += os.sep

	retList = []
	for name in os.listdir(path):
		if stat.S_ISDIR(os.stat(path+name).st_mode):
			if name == ".svn":
				continue
			retList += FindFilesByExt(path+name)
		else:
			if "_3" in name.lower():
				retList.append(path + name)

	return retList

import shutil
for oldname in FindFilesByExt("."):
	newname = oldname.replace("_3", "_4")
	shutil.copyfile(oldname, newname)
	print oldname 
	print newname

