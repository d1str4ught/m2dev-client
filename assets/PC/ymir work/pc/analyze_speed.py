import glob
import os
import stat

def GetSpeed(name):
	lines = open(name).readlines()

	inp = 0
	beg = 0
	end = 0
	for line in lines:
		if "DirectInput" in line:
			inp = float(line.strip().split()[1])
		if "AttackingStartTime" in line:
			beg = float(line.strip().split()[1])
		if "AttackingEndTime" in line:
			end = float(line.strip().split()[1])

	return inp, beg, end

def GetComboList(job):
	print job
	os.chdir(job)
	dirList = os.listdir(".")

	folders = [name for name in dirList if stat.S_ISDIR(os.stat(name).st_mode)]

	for folder in folders:
		os.chdir(folder)

		comboList = []
		for name in glob.glob("*.msa"):
			if "combo" in name:
				comboList.append("\t" + " ".join((name, "%.2f (%.2f-%.2f)" % (GetSpeed(name)))))

		if comboList:
			print folder
			print "\n".join(comboList)
		os.chdir("..")

	os.chdir("..")

GetComboList("warrior");
GetComboList("assassin");
GetComboList("sura");
GetComboList("shaman");
