import uiScriptLocale

BUTTON_START_X_POS = -60
BUTTON_X_STEP = 30

window = {
	"name" : "MessengerWindow",

	"x" : SCREEN_WIDTH - 200,
	"y" : SCREEN_HEIGHT - 400 - 50,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 300,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 300,
			"title" : uiScriptLocale.MESSENGER_TITLE,
		},

		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 27,
			"y" : 40,
			"size" : 100,
			"horizontal_align" : "right",
		},

		{
			"name" : "AddFriendButton",
			"type" : "button",

			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*0,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_ADD_FRIEND,
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_04.sub",
		},
		{
			"name" : "WhisperButton",
			"type" : "button",

			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*1,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_WHISPER,
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/game/windows/messenger_whisper_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_whisper_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_whisper_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_whisper_04.sub",
		},
		{
			"name" : "MobileButton",
			"type" : "button",

			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*2,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_MOBILE,
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/game/windows/messenger_mobile_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_mobile_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_mobile_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_mobile_04.sub",
		},
		{
			"name" : "RemoveButton",
			"type" : "button",

			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*3,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_DELETE_FRIEND,
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/game/windows/messenger_delete_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_delete_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_delete_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_delete_04.sub",
		},
		{
			"name" : "GuildButton",
			"type" : "button",

			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*4,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_OPEN_GUILD,
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/game/windows/messenger_guild_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_guild_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_guild_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_guild_04.sub",
		},

	), ## end of main window
}
