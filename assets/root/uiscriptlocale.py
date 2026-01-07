import app

AUTOBAN_QUIZ_ANSWER = "ANSWER"
AUTOBAN_QUIZ_REFRESH = "REFRESH"
AUTOBAN_QUIZ_REST_TIME = "REST_TIME"

OPTION_SHADOW = "SHADOW"

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

name = app.GetLocalePath()
LOCALE_UISCRIPT_PATH = "%s/ui/" % (name)
LOGIN_PATH = "%s/ui/login/" % (name)
EMPIRE_PATH = "%s/ui/empire/" % (name)
GUILD_PATH = "%s/ui/guild/" % (name)
SELECT_PATH = "%s/ui/select/" % (name)
WINDOWS_PATH = "%s/ui/windows/" % (name)
MAPNAME_PATH = "%s/ui/mapname/" % (name)

JOBDESC_WARRIOR_PATH = "%s/jobdesc_warrior.txt" % (name)
JOBDESC_ASSASSIN_PATH = "%s/jobdesc_assassin.txt" % (name)
JOBDESC_SURA_PATH = "%s/jobdesc_sura.txt" % (name)
JOBDESC_SHAMAN_PATH = "%s/jobdesc_shaman.txt" % (name)

EMPIREDESC_A = "%s/empiredesc_a.txt" % (name)
EMPIREDESC_B = "%s/empiredesc_b.txt" % (name)
EMPIREDESC_C = "%s/empiredesc_c.txt" % (name)

LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)
LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, locals())

def LoadLocaleData():
	"""
	Reload all UI locale strings from locale_interface.txt

	Called by app.ReloadLocale() when the user changes language.
	Updates all locale-dependent paths and reloads locale_interface.txt.

	Returns:
		True on success, False on failure
	"""
	try:
		# Update all locale-dependent paths
		global name, LOCALE_UISCRIPT_PATH, LOGIN_PATH, EMPIRE_PATH, GUILD_PATH, SELECT_PATH, WINDOWS_PATH, MAPNAME_PATH
		global JOBDESC_WARRIOR_PATH, JOBDESC_ASSASSIN_PATH, JOBDESC_SURA_PATH, JOBDESC_SHAMAN_PATH
		global EMPIREDESC_A, EMPIREDESC_B, EMPIREDESC_C, LOCALE_INTERFACE_FILE_NAME

		name = app.GetLocalePath()
		LOCALE_UISCRIPT_PATH = "%s/ui/" % (name)
		LOGIN_PATH = "%s/ui/login/" % (name)
		EMPIRE_PATH = "%s/ui/empire/" % (name)
		GUILD_PATH = "%s/ui/guild/" % (name)
		SELECT_PATH = "%s/ui/select/" % (name)
		WINDOWS_PATH = "%s/ui/windows/" % (name)
		MAPNAME_PATH = "%s/ui/mapname/" % (name)

		JOBDESC_WARRIOR_PATH = "%s/jobdesc_warrior.txt" % (name)
		JOBDESC_ASSASSIN_PATH = "%s/jobdesc_assassin.txt" % (name)
		JOBDESC_SURA_PATH = "%s/jobdesc_sura.txt" % (name)
		JOBDESC_SHAMAN_PATH = "%s/jobdesc_shaman.txt" % (name)

		EMPIREDESC_A = "%s/empiredesc_a.txt" % (name)
		EMPIREDESC_B = "%s/empiredesc_b.txt" % (name)
		EMPIREDESC_C = "%s/empiredesc_c.txt" % (name)

		LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)

		# Reload locale_interface.txt - this updates all UI strings
		LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, globals())

		return True
	except:
		# import dbg
		# dbg.TraceError("uiScriptLocale.LoadLocaleData failed")
		return False