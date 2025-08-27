METIN2THEMA = "M2BG.mp3"

loginMusic="login_window.mp3"
createMusic="characterselect.mp3"
selectMusic="characterselect.mp3"
fieldMusic=METIN2THEMA

def SaveLastPlayFieldMusic():
	global fieldMusic

	try:
		lastPlayFile=open("BGM/lastplay.inf", "w")
	except IOError:
		return

	lastPlayFile.write(fieldMusic)


def LoadLastPlayFieldMusic():
	global fieldMusic

	try:
		lastPlayFile=open("BGM/lastplay.inf", "r")
	except IOError:
		return

	fieldMusic=lastPlayFile.read()


