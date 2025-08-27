import uiScriptLocale

HELP_STICK_IMAGE_FILE_NAME = "d:/ymir work/ui/pattern/help_stick.tga"

START_HEIGHT = 50
HEIGHT_STEP = 20

window = {
	"name" : "HelpWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Float Text
		{
			"name" : "help_01", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*0) / 600,
			"text" : uiScriptLocale.HELP_MOVE_KEY,
		},
		{
			"name" : "help_02", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*1) / 600,
			"text" : uiScriptLocale.HELP_CONTROL_CAMERA_BY_RIGHTBUTTON,
		},
		{
			"name" : "help_02", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*2) / 600,
			"text" : uiScriptLocale.HELP_CONTROL_CAMERA_BY_MIDDLEBUTTON,
		},
		{
			"name" : "help_03", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*3) / 600,
			"text" : uiScriptLocale.HELP_SHOW_ALL_NAME,
		},
		{
			"name" : "help_04", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*4) / 600,
			"text" : uiScriptLocale.HELP_OPEN_CHAT,
		},
		{
			"name" : "help_05", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*5) / 600,
			"text" : uiScriptLocale.HELP_OPEN_WHISPER,
		},
		{
			"name" : "help_06", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*6) / 600,
			"text" : uiScriptLocale.HELP_ATTACK_KEY,
		},
		{
			"name" : "help_07", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*7) / 600,
			"text" : uiScriptLocale.HELP_OPEN_CHARACTER,
		},
		{
			"name" : "help_08", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*8) / 600,
			"text" : uiScriptLocale.HELP_OPEN_SKILL,
		},
		{
			"name" : "help_09", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*9) / 600,
			"text" : uiScriptLocale.HELP_OPEN_QUEST,
		},
		{
			"name" : "help_10", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*10) / 600,
			"text" : uiScriptLocale.HELP_OPEN_INVENTORY,
		},
		{
			"name" : "help_11", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*11) / 600,
			"text" : uiScriptLocale.HELP_OPEN_LOG,
		},
		{
			"name" : "help_12", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*12) / 600,
			"text" : uiScriptLocale.HELP_OPEN_ZONEMAP,
		},
		{
			"name" : "help_13", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*13) / 600,
			"text" : uiScriptLocale.HELP_OPEN_MINIMAP,
		},
		{
			"name" : "help_14", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*14) / 600,
			"text" : uiScriptLocale.HELP_CHANGE_PK_MODE,
		},
		{
			"name" : "help_15", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*15) / 600,
			"text" : uiScriptLocale.HELP_PICK_ITEM,
		},
		{
			"name" : "help_16", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*16) / 600,
			"text" : uiScriptLocale.HELP_SCREEN_CAPTURE,
		},
		{
			"name" : "help_17", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*17) / 600,
			"text" : uiScriptLocale.HELP_GUILD_WINDOW,
		},
		{
			"name" : "help_18", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*18) / 600,
			"text" : uiScriptLocale.HELP_MESSENGER_WINDOW,
		},
		{
			"name" : "help_19", "type" : "text", "outline" : 1,
			"x" : SCREEN_WIDTH * 150 / 800, "y" : SCREEN_HEIGHT * (START_HEIGHT+HEIGHT_STEP*19) / 600,
			"text" : uiScriptLocale.HELP_HELP,
		},

		## TaskBar
		{
			"name" : "taskbar_help_stick_01", "type" : "expanded_image",
			"x" : 22, "y" : SCREEN_HEIGHT - 120,
			"rect" : (0.0, 0.0, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_01", "type" : "text",
					"x" : -20, "y" : -20,
					"text" : uiScriptLocale.HELP_FURY,
				},
			),
		},
		{
			"name" : "taskbar_help_stick_02", "type" : "expanded_image",
			"x" : 80, "y" : SCREEN_HEIGHT - 122,
			"rect" : (0.0, -0.3, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_02", "type" : "text",
					"x" : 4, "y" : 12,
					"text" : uiScriptLocale.HELP_HP,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_03", "type" : "expanded_image",
			"x" : 120, "y" : SCREEN_HEIGHT - 107,
			"rect" : (0.0, -0.4, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_03", "type" : "text",
					"x" : 4, "y" : 23,
					"text" : uiScriptLocale.HELP_SP,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_04", "type" : "expanded_image",
			"x" : 206, "y" : SCREEN_HEIGHT - 116,
			"rect" : (0.0, -0.7, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_04", "type" : "text",
					"x" : 4, "y" : 51,
					"text" : uiScriptLocale.HELP_EXP,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_05", "type" : "expanded_image",
			"x" : SCREEN_WIDTH/2 - 128 + 12, "y" : SCREEN_HEIGHT - 116,
			"rect" : (0.0, -0.5, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_05", "type" : "text",
					"x" : 4, "y" : 32,
					"text" : uiScriptLocale.HELP_MOUSE_LEFT,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_06", "type" : "expanded_image",
			"x" : SCREEN_WIDTH/2 + 128 + 66 + 12, "y" : SCREEN_HEIGHT - 116,
			"rect" : (0.0, -0.5, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_06", "type" : "text",
					"x" : 4, "y" : 32,
					"text" : uiScriptLocale.HELP_MOUSE_RIGHT,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_07", "type" : "expanded_image",
			"x" : SCREEN_WIDTH * (400 - 4) / 800, "y" : SCREEN_HEIGHT - 116,
			"rect" : (0.0, -0.7, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_07", "type" : "text",
					"x" : 4, "y" : 51,
					"text" : uiScriptLocale.HELP_QUICKSLOT,
					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "taskbar_help_stick_08", "type" : "expanded_image",
			"x" : SCREEN_WIDTH - 77 - 4, "y" : SCREEN_HEIGHT - 116,
			"rect" : (0.0, -0.28, 0.0, 0.0),
			"image" : HELP_STICK_IMAGE_FILE_NAME,

			"children" :
			(
				{
					"name" : "taskbar_help_08a", "type" : "text",
					"x" : 4, "y" : -20,
					"text" : uiScriptLocale.HELP_SYSTEM_BUTTON,
					"text_horizontal_align" : "center",
				},
				{
					"name" : "taskbar_help_08b", "type" : "text",
					"x" : 4, "y" : -5,
					"text" : uiScriptLocale.HELP_CHARACTER_BUTTON1,
					"text_horizontal_align" : "center",
				},
				{
					"name" : "taskbar_help_08c", "type" : "text",
					"x" : 4, "y" : 10,
					"text" : uiScriptLocale.HELP_CHARACTER_BUTTON2,
					"text_horizontal_align" : "center",
				},
			),
		},

		## Button
		{
			"name" : "close_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (55) / 800,
			"y" : SCREEN_HEIGHT * (55) / 600,

			"text" : uiScriptLocale.CLOSE,

			"default_image" : "d:/ymir work/ui/public/xlarge_thin_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/xlarge_thin_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/xlarge_thin_button_03.sub",
		},
	),
}
