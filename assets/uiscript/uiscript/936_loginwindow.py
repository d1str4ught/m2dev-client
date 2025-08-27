import uiScriptLocale

LOCALE_PATH = "d:/ymir work/ui/intro/"+uiScriptLocale.CODEPAGE+"_login/"

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(

		## Board
		{
			"name" : "BackGround",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 42,

			"image" : "d:/ymir work/ui/intro/pattern/background_pattern.tga",

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 128) / 128.0, float(SCREEN_HEIGHT - 128 - 42*2) / 128.0),
		},

		## Alpha
		{
			"name" : "Alpha",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/intro/login/background_alpha.sub",

			"x_scale" : float(SCREEN_WIDTH) / 128.0,
			"y_scale" : float(SCREEN_HEIGHT) / 96.0,
		},

		## Top & Bottom Line
		{
			"name" : "Top_Line",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/intro/pattern/line_pattern.tga",

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 50) / 50.0, 0.0),
		},
		{
			"name" : "Bottom_Line",
			"type" : "expanded_image",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 42,

			"image" : "d:/ymir work/ui/intro/pattern/line_pattern.tga",

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 50) / 50.0, 0.0),
		},

		## BackGround
		{
			"name" : "BackGround",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 800.0,
			"y_scale" : float(SCREEN_HEIGHT) / 600.0,
			"mode" : "MODULATE",

			"image" : "d:/ymir work/ui/intro/pattern/intro_background.dds",
		},

		## Metin2 Logo
		{
			"name" : "Metin2_Logo",
			"type" : "expanded_image",

			"x" : float(SCREEN_WIDTH) / 800.0 * 20,
			"y" : float(SCREEN_HEIGHT) / 600.0 * 10,
			"x_scale" : float(SCREEN_WIDTH) / 800.0,
			"y_scale" : float(SCREEN_HEIGHT) / 600.0,

			"image" : "d:/ymir work/ui/intro/936_login/logo.sub",
		},

		## Copyright
		{
			"name" : "Copyright",
			"type" : "image",

			"x" : SCREEN_WIDTH/2 - 378/2,
			"y" : SCREEN_HEIGHT - 33,

			"image" : "d:/ymir work/ui/intro/login/copyright.sub",
		},

		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : SCREEN_WIDTH - 275,
			"y" : SCREEN_HEIGHT - 195,
			"width" : 208,
			"height" : 30,

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 10,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 155,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_BUTTON,
				},
			),
		},

		## Alert
		{
			"name" : "AlertBoard",
			"type" : "thinboard",

			"x" : 67,
			"y" : SCREEN_HEIGHT - 169,
			"width" : 228,
			"height" : 111,

			"children" :
			(
				{
					"name" : "936_AlertImage",
					"type" : "image",

					"x" : 0,
					"y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",

					"image" : "d:/ymir work/ui/intro/936_login/alert.sub",
				},
			),
		},

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : SCREEN_WIDTH - 275,
			"y" : SCREEN_HEIGHT - 155,

			"image" : LOCALE_PATH+"loginwindow.sub",

			"children" :
			(
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 77,
					"y" : 16,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Password_EditLine",
					"type" : "editline",

					"x" : 77,
					"y" : 43,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 15,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_CONNECT,
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 105,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_EXIT,
				},
			),
		},

		## ServerBoard
		{
			"name" : "ServerBoard",
			"type" : "thinboard",

			"x" : 0,
			"y" : 308,
			"width" : 375,
			"height" : 220,
			"horizontal_align" : "center",

			"children" :
			(

				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : uiScriptLocale.LOGIN_SELECT_TITLE,
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 354,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 355,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "VerticalLine1",
					"type" : "line",

					"x" : 246,
					"y" : 38,
					"width" : 0,
					"height" : 175,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 247,
					"y" : 38,
					"width" : 0,
					"height" : 175,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox",

					"x" : 10,
					"y" : 40,
					"width" : 232,
					"height" : 171,

					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 255,
					"y" : 40,
					"width" : 109,
					"height" : 171,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 267,
					"y" : 170,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 267,
					"y" : 192,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},

			),

		},

		## SettlementBoard
		{
			"name" : "RegionBoard",
			"type" : "thinboard",

			"x" : 0,
			"y" : 308,
			"width" : 375,
			"height" : 220,
			"horizontal_align" : "center",

			"children" :
			(

				## Title
				{
					"name" : "RegionTitle",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : uiScriptLocale.LOGIN_REGION_TITLE,
				},

				## Horizontal
				{
					"name" : "RegionHorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 354,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "RegionHorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 355,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "RegionVerticalLine1",
					"type" : "line",

					"x" : 246,
					"y" : 38,
					"width" : 0,
					"height" : 175,
					"color" : 0xff777777,
				},
				{
					"name" : "RegionVerticalLine2",
					"type" : "line",

					"x" : 247,
					"y" : 38,
					"width" : 0,
					"height" : 175,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "RegionGroupList",
					"type" : "listbox",

					"x" : 10,
					"y" : 40,
					"width" : 232,
					"height" : 171,

					"item_align" : 0,
				},
				{
					"name" : "ServerListOnRegionBoard",
					"type" : "listbox",

					"x" : 255,
					"y" : 40,
					"width" : 109,
					"height" : 171,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "RegionSelectButton",
					"type" : "button",

					"x" : 267,
					"y" : 170,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "RegionExitButton",
					"type" : "button",

					"x" : 267,
					"y" : 192,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},

			),

		},

	),
}
