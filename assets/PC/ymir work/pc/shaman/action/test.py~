import glob
for name in glob.glob("*.msa"):
	old_lines = open(name).readlines()
	new_lines = []

	for line in old_lines:
		if "wedding" in line:
			new_lines.append(line.replace("wedding", "action"))
		else:
			new_lines.append(line)

	if old_lines != new_lines:
		print name
		open(name, "w").writelines(new_lines)
