import app

OPTION_SHADOW = "SHADOW"

CODEPAGE = str(app.GetDefaultCodePage())

#CUBE_TITLE = "Cube Window"

def LoadLocaleFile(srcFileName, localeDict):
	localeDict["CUBE_INFO_TITLE"] = "Recipe"
	localeDict["CUBE_REQUIRE_MATERIAL"] = "Requirements"
	localeDict["CUBE_REQUIRE_MATERIAL_OR"] = "or"
	
	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadUIScriptLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		tokens = line[:-1].split("\t")
		
		if len(tokens) >= 2:
			localeDict[tokens[0]] = tokens[1]			
			
		else:
			print len(tokens), lines.index(line), line


LOCALE_UISCRIPT_PATH = "locale/ui/"
LOGIN_PATH = "locale/ui/login/"
EMPIRE_PATH = "locale/ui/empire/"
GUILD_PATH = "locale/ui/guild/"
SELECT_PATH = "locale/ui/select/"
WINDOWS_PATH = "locale/ui/windows/"
MAPNAME_PATH = "locale/ui/mapname/"

JOBDESC_WARRIOR_PATH = "locale/language/%s/jobdesc_warrior.txt" % app.GetLocaleName()
JOBDESC_ASSASSIN_PATH = "locale/language/%s/jobdesc_assassin.txt" % app.GetLocaleName()
JOBDESC_SURA_PATH = "locale/language/%s/jobdesc_sura.txt" % app.GetLocaleName()
JOBDESC_SHAMAN_PATH = "locale/language/%s/jobdesc_shaman.txt" % app.GetLocaleName()

EMPIREDESC_A = "locale/language/%s/empiredesc_a.txt" % app.GetLocaleName()
EMPIREDESC_B = "locale/language/%s/empiredesc_b.txt" % app.GetLocaleName()
EMPIREDESC_C = "locale/language/%s/empiredesc_c.txt" % app.GetLocaleName()

LOCALE_INTERFACE_FILE_NAME = "locale/language/%s/locale_interface.txt" % app.GetLocaleName()

LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, locals())

