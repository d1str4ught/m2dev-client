import app
import constInfo
import dbg

APP_GET_LOCALE_PATH					= app.GetLocalePath()
APP_GET_LOCALE_PATH_COMMON			= app.GetLocalePathCommon()

APP_TITLE							= 'METIN2'

BLEND_POTION_NO_TIME				= 'BLEND_POTION_NO_TIME'
BLEND_POTION_NO_INFO				= 'BLEND_POTION_NO_INFO'

LOGIN_FAILURE_WRONG_SOCIALID 		= 'LOGIN_FAILURE_WRONG_SOCIALID'
LOGIN_FAILURE_SHUTDOWN_TIME 		= 'LOGIN_FAILURE_SHUTDOWN_TIME'

LOCALE_CHANGE_CONFIRM				= 'Change language to %s and reload the game?'

GUILD_MEMBER_COUNT_INFINITY 		= 'INFINITY'
GUILD_MARK_MIN_LEVEL				= '3'
GUILD_BUILDING_LIST_TXT				= '{:s}/GuildBuildingList.txt'.format(APP_GET_LOCALE_PATH)
FN_GM_MARK							= '{:s}/effect/gm.mse'.format(APP_GET_LOCALE_PATH_COMMON)

MAP_TREE2							= 'MAP_TREE2'

ERROR_MARK_UPLOAD_NEED_RECONNECT	= 'UploadMark: Reconnect to game'
ERROR_MARK_CHECK_NEED_RECONNECT		= 'CheckMark: Reconnect to game'

VIRTUAL_KEY_ALPHABET_LOWERS			= r"[1234567890]/qwertyuiop\=asdfghjkl;`'zxcvbnm.,"
VIRTUAL_KEY_ALPHABET_UPPERS			= r"{1234567890}?QWERTYUIOP|+ASDFGHJKL:~'ZXCVBNM<>"
VIRTUAL_KEY_SYMBOLS					= "!@#$%^&*()_+|{}:'<>?~"
VIRTUAL_KEY_NUMBERS					= "1234567890-=\[];',./`"
VIRTUAL_KEY_SYMBOLS_BR				= "!@#$%^&*()_+|{}:'<>?~aaaaeeeiioooouuc"

# Multi-language hot-reload support
def LoadLocaleData():
	"""
	Reload all game locale text strings from locale_game.txt

	Called by app.ReloadLocale() when the user changes language.
	Reloads locale_game.txt and updates all module-level locale strings.

	Returns:
		True on success, False on failure
	"""
	try:
		localePath = app.GetLocalePath()
		localeFilePath = "{:s}/locale_game.txt".format(localePath)

		# Reload locale_game.txt - this updates all global variables in this module
		LoadLocaleFile(localeFilePath, globals())

		return True
	except:
		# import dbg
		# dbg.TraceError("localeInfo.LoadLocaleData failed")
		return False

# Load locale_game.txt
def LoadLocaleFile(srcFileName, localeDict):
	def SNA(text):
		def f(x):
			return text
		return f

	def SA(text):
		def f(x):
			return text % x
		return f

	def SAN(text):
		def f(x):
			return text % x
		return f

	def SAA(text):
		def f(x):
			return text % x
		return f

	funcDict = {"SA": SA, "SNA": SNA, "SAA": SAA, "SAN": SAN}
	lineIndex = 1

	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		dbg.LogBox("LoadLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		if line.count("\t") == 0:
			continue

		try:
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				localeDict[tokens[0]] = tokens[1]
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					if type in funcDict:
						localeDict[tokens[0]] = funcDict[type](tokens[1])
					else:
						localeDict[tokens[0]] = tokens[1]
				else:
					localeDict[tokens[0]] = tokens[1]
			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			dbg.LogBox("%s: line(%d): %s" % (srcFileName, lineIndex, line), "Error")
			raise

LoadLocaleFile("{:s}/locale_game.txt".format(APP_GET_LOCALE_PATH), locals())

# Option pvp messages
OPTION_PVPMODE_MESSAGE_DICT = {
	0: PVP_MODE_NORMAL,
	1: PVP_MODE_REVENGE,
	2: PVP_MODE_KILL,
	3: PVP_MODE_PROTECT,
	4: PVP_MODE_GUILD,
}

# Whisper messages
WHISPER_ERROR = {
	1: CANNOT_WHISPER_NOT_LOGON,
	2: CANNOT_WHISPER_DEST_REFUSE,
	3: CANNOT_WHISPER_SELF_REFUSE,
}

# Exception of graphic device.
error = dict(
	CREATE_WINDOW = GAME_INIT_ERROR_MAIN_WINDOW,
	CREATE_CURSOR = GAME_INIT_ERROR_CURSOR,
	CREATE_NETWORK = GAME_INIT_ERROR_NETWORK,
	CREATE_ITEM_PROTO = GAME_INIT_ERROR_ITEM_PROTO,
	CREATE_MOB_PROTO = GAME_INIT_ERROR_MOB_PROTO,
	CREATE_NO_DIRECTX = GAME_INIT_ERROR_DIRECTX,
	CREATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_NOT_EXIST,
	CREATE_NO_APPROPRIATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_BAD_PERFORMANCE,
	CREATE_FORMAT = GAME_INIT_ERROR_GRAPHICS_NOT_SUPPORT_32BIT,
	NO_ERROR = str()
)

# Job information (none, skill_group1, skill_group2)
JOBINFO_TITLE = [
	[JOB_WARRIOR0, JOB_WARRIOR1, JOB_WARRIOR2,],
	[JOB_ASSASSIN0, JOB_ASSASSIN1, JOB_ASSASSIN2,],
	[JOB_SURA0, JOB_SURA1, JOB_SURA2,],
	[JOB_SHAMAN0, JOB_SHAMAN1, JOB_SHAMAN2,],
]

#if app.ENABLE_WOLFMAN_CHARACTER:
	#JOBINFO_TITLE += [[JOB_WOLFMAN0,JOB_WOLFMAN1,JOB_WOLFMAN2,],]

# Guild war description
GUILDWAR_NORMAL_DESCLIST = 					(GUILD_WAR_USE_NORMAL_MAP, GUILD_WAR_LIMIT_30MIN, GUILD_WAR_WIN_CHECK_SCORE)
# Guild war warp description
GUILDWAR_WARP_DESCLIST = 					(GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_WIPE_OUT_GUILD, GUILD_WAR_REWARD_POTION)
# Guild war flag description
GUILDWAR_CTF_DESCLIST = 					(GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_TAKE_AWAY_FLAG1, GUILD_WAR_WIN_TAKE_AWAY_FLAG2, GUILD_WAR_REWARD_POTION)

# Mode of pvp options
MODE_NAME_LIST = 							(PVP_OPTION_NORMAL, PVP_OPTION_REVENGE, PVP_OPTION_KILL, PVP_OPTION_PROTECT,)
# Title name of alignment
TITLE_NAME_LIST = 							(PVP_LEVEL0, PVP_LEVEL1, PVP_LEVEL2, PVP_LEVEL3, PVP_LEVEL4, PVP_LEVEL5, PVP_LEVEL6, PVP_LEVEL7, PVP_LEVEL8,)

# Horse levels
LEVEL_LIST = 								(str(), HORSE_LEVEL1, HORSE_LEVEL2, HORSE_LEVEL3)
# Horse health
HEALTH_LIST = 								(HORSE_HEALTH0, HORSE_HEALTH1, HORSE_HEALTH2, HORSE_HEALTH3)

# Use-skill messages
USE_SKILL_ERROR_TAIL_DICT = {	
	'IN_SAFE':								CANNOT_SKILL_SELF_IN_SAFE,
	'NEED_TARGET': 							CANNOT_SKILL_NEED_TARGET,
	'NEED_EMPTY_BOTTLE': 					CANNOT_SKILL_NEED_EMPTY_BOTTLE,
	'NEED_POISON_BOTTLE': 					CANNOT_SKILL_NEED_POISON_BOTTLE,
	'REMOVE_FISHING_ROD': 					CANNOT_SKILL_REMOVE_FISHING_ROD,
	'NOT_YET_LEARN': 						CANNOT_SKILL_NOT_YET_LEARN,
	'NOT_MATCHABLE_WEAPON':					CANNOT_SKILL_NOT_MATCHABLE_WEAPON,
	'WAIT_COOLTIME':						CANNOT_SKILL_WAIT_COOLTIME,
	'NOT_ENOUGH_HP':						CANNOT_SKILL_NOT_ENOUGH_HP,
	'NOT_ENOUGH_SP':						CANNOT_SKILL_NOT_ENOUGH_SP,
	'CANNOT_USE_SELF':						CANNOT_SKILL_USE_SELF,
	'ONLY_FOR_ALLIANCE': 					CANNOT_SKILL_ONLY_FOR_ALLIANCE,
	'CANNOT_ATTACK_ENEMY_IN_SAFE_AREA':		CANNOT_SKILL_DEST_IN_SAFE,
	'CANNOT_APPROACH':						CANNOT_SKILL_APPROACH,
	'CANNOT_ATTACK':						CANNOT_SKILL_ATTACK,
	'ONLY_FOR_CORPSE':						CANNOT_SKILL_ONLY_FOR_CORPSE,
	'EQUIP_FISHING_ROD':					CANNOT_SKILL_EQUIP_FISHING_ROD, 
	'NOT_HORSE_SKILL':						CANNOT_SKILL_NOT_HORSE_SKILL,
	'HAVE_TO_RIDE':							CANNOT_SKILL_HAVE_TO_RIDE,
}

# Notify messages
NOTIFY_MESSAGE = {
	'CANNOT_EQUIP_SHOP': 					CANNOT_EQUIP_IN_SHOP,
	'CANNOT_EQUIP_EXCHANGE': 				CANNOT_EQUIP_IN_EXCHANGE,
}

# Attack messages
ATTACK_ERROR_TAIL_DICT = {
	'IN_SAFE': 								CANNOT_ATTACK_SELF_IN_SAFE,
	'DEST_IN_SAFE': 						CANNOT_ATTACK_DEST_IN_SAFE,
}

# Shot messages
SHOT_ERROR_TAIL_DICT = {
	'EMPTY_ARROW': 							CANNOT_SHOOT_EMPTY_ARROW,
	'IN_SAFE':								CANNOT_SHOOT_SELF_IN_SAFE,
	'DEST_IN_SAFE':							CANNOT_SHOOT_DEST_IN_SAFE,
}

# Skill messages
USE_SKILL_ERROR_CHAT_DICT = {	
	'NEED_EMPTY_BOTTLE': 					SKILL_NEED_EMPTY_BOTTLE,
	'NEED_POISON_BOTTLE': 					SKILL_NEED_POISON_BOTTLE, 
	'ONLY_FOR_GUILD_WAR': 					SKILL_ONLY_FOR_GUILD_WAR,
}

# Shop/private-shop messages
SHOP_ERROR_DICT = {
	'NOT_ENOUGH_MONEY': 					SHOP_NOT_ENOUGH_MONEY,
	'SOLDOUT': 								SHOP_SOLDOUT,
	'INVENTORY_FULL': 						SHOP_INVENTORY_FULL,
	'INVALID_POS': 							SHOP_INVALID_POS,
	'NOT_ENOUGH_MONEY_EX': 					SHOP_NOT_ENOUGH_MONEY_EX,
}

# Character status description
STAT_MINUS_DESCRIPTION = {
	'HTH-': 								STAT_MINUS_CON,
	'INT-': 								STAT_MINUS_INT,
	'STR-': 								STAT_MINUS_STR,
	'DEX-': 								STAT_MINUS_DEX,
}

# Map names
MINIMAP_ZONE_NAME_DICT = {
	'metin2_map_a1': 						MAP_A1,
	'map_a2': 								MAP_A2,
	'metin2_map_a3': 						MAP_A3,
	'metin2_map_b1': 						MAP_B1,
	'map_b2': 								MAP_B2,
	'metin2_map_b3': 						MAP_B3,
	'metin2_map_c1': 						MAP_C1,
	'map_c2': 								MAP_C2,
	'metin2_map_c3': 						MAP_C3,
	'map_n_snowm_01': 						MAP_SNOW,
	'metin2_map_n_flame_01': 				MAP_FLAME,
	'metin2_map_n_desert_01': 				MAP_DESERT,
	'metin2_map_milgyo': 					MAP_TEMPLE,
	'metin2_map_spiderdungeon': 			MAP_SPIDER,
	'metin2_map_deviltower1': 				MAP_SKELTOWER,
	'metin2_map_guild_01': 					MAP_AG,
	'metin2_map_guild_02': 					MAP_BG,
	'metin2_map_guild_03': 					MAP_CG,
	'metin2_map_trent': 					MAP_TREE,
	'metin2_map_trent02': 					MAP_TREE2,
	'season1/metin2_map_WL_01': 			MAP_WL,
	'season1/metin2_map_nusluck01': 		MAP_NUSLUCK,
	'Metin2_map_CapeDragonHead': 			MAP_CAPE,
	'metin2_map_Mt_Thunder': 				MAP_THUNDER,
	'metin2_map_dawnmistwood': 				MAP_DAWN,
	'metin2_map_BayBlackSand': 				MAP_BAY,
}

# Path of quest icon file
def GetLetterImageName():
	return "season1/icon/scroll_close.tga"

def GetLetterOpenImageName():
	return "season1/icon/scroll_open.tga"

def GetLetterCloseImageName():
	return "season1/icon/scroll_close.tga"

# Sell item question
def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
	return DO_YOU_SELL_ITEM2 % (sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice)) if (sellItemCount > 1) else DO_YOU_SELL_ITEM1 % (sellItemName, NumberToMoneyString(sellItemPrice))

# Buy item question
def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice):
	return DO_YOU_BUY_ITEM2 % (buyItemName, buyItemCount, buyItemPrice) if (buyItemCount > 1) else DO_YOU_BUY_ITEM1 % (buyItemName, buyItemPrice)

# Notify when you can't attach a specific item.
def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName):
	return REFINE_FAILURE_CAN_NOT_ATTACH0 % (attachedItemName)

def REFINE_FAILURE_NO_SOCKET(attachedItemName):
	return REFINE_FAILURE_NO_SOCKET0 % (attachedItemName)

# Drop item question
def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName):
	return REFINE_FAILURE_NO_GOLD_SOCKET0 % (attachedItemName)

# Drop item question
def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount):
	return HOW_MANY_ITEM_DO_YOU_DROP2 % (dropItemName, dropItemCount) if (dropItemCount > 1) else HOW_MANY_ITEM_DO_YOU_DROP1 % (dropItemName)

# Fishing notify when looks like the fish is hooked.
def FISHING_NOTIFY(isFish, fishName):
	return FISHING_NOTIFY1 % (fishName) if isFish else FISHING_NOTIFY2 % (fishName)

# Fishing notify when you capture a fish.
def FISHING_SUCCESS(isFish, fishName):
	return FISHING_SUCCESS1 % (fishName) if isFish else FISHING_SUCCESS2 % (fishName)

# Convert a integer amount into a string and add . as separator for money.
def NumberToMoneyString(n):
	return '0 {:s}'.format(MONETARY_UNIT0) if (n <= 0) else '{:s} {:s}'.format('.'.join([(i - 3) < 0 and str(n)[:i] or str(n)[i - 3 : i] for i in range(len(str(n)) % 3, len(str(n)) + 1, 3) if i]), MONETARY_UNIT0)

# Convert a integer amount into a string and add . as separator for secondary coin.
def NumberToSecondaryCoinString(n):
	return '0 {:s}'.format(MONETARY_UNIT_JUN) if (n <= 0) else '{:s} {:s}'.format('.'.join([(i - 3) < 0 and str(n)[:i] or str(n)[i - 3: i] for i in range(len(str(n)) % 3, len(str(n)) + 1, 3) if i]), MONETARY_UNIT_JUN)

# Return the title of alignment by points.
def GetAlignmentTitleName(alignment):
	if alignment >= 12000:
		return TITLE_NAME_LIST[0]
	elif alignment >= 8000:
		return TITLE_NAME_LIST[1]
	elif alignment >= 4000:
		return TITLE_NAME_LIST[2]
	elif alignment >= 1000:
		return TITLE_NAME_LIST[3]
	elif alignment >= 0:
		return TITLE_NAME_LIST[4]
	elif alignment > -4000:
		return TITLE_NAME_LIST[5]
	elif alignment > -8000:
		return TITLE_NAME_LIST[6]
	elif alignment > -12000:
		return TITLE_NAME_LIST[7]

	return TITLE_NAME_LIST[8]

# Convert seconds to Days-Hours-Minutes
def SecondToDHM(time):
	if time < 60:
		return '0' + MINUTE

	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ''
	if day > 0:
		text += str(day) + DAY
		text += ' '

	if hour > 0:
		text += str(hour) + HOUR
		text += ' '

	if minute > 0:
		text += str(minute) + MINUTE
	return text

# Convert seconds to Hours-Minutes
def SecondToHM(time):
	if time < 60:
		return '0' + MINUTE

	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ''
	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += ' '

	if minute > 0:
		text += str(minute) + MINUTE
	return text
