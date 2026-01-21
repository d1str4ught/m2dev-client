METIN2THEMA = "M2BG.mp3"

loginMusic="login_window.mp3"
createMusic="characterselect.mp3"
selectMusic="characterselect.mp3"
fieldMusic=METIN2THEMA

def SaveLastPlayFieldMusic():
	global fieldMusic

	try:
		with open("BGM/lastplay.inf", "w") as lastPlayFile:
			lastPlayFile.write(fieldMusic)
	except IOError:
		return


def LoadLastPlayFieldMusic():
	global fieldMusic

	try:
		with open("BGM/lastplay.inf", "r") as lastPlayFile:
			fieldMusic=lastPlayFile.read()
	except IOError:
		return


