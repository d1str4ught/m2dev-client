from FindFilesByExt import FindFilesByExt

for name in FindFilesByExt(".msa", "."):
	lines = open(name).read().splitlines()

	out = open(name, "w")
	for line in lines:
		if "ymir work" in line.lower():
			line = line.lower()
			line = line.replace("\\", "/")
			line = line.replace("d:/ymir work/pc/", "d:/ymir work/pc2/")
			line = line.replace("motionfilename", "MotionFileName")
			line = line.replace("effectfilename", "EffectFileName")
			print line
			out.write("%s\n" % line)
		else:
			out.write("%s\n" % line)
	


