import uiScriptLocale

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
#Big-List
#SERVER_BOARD_HEIGHT = 180 + 390
#SERVER_LIST_HEIGHT = 171 + 350
#Small list like german
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180
SERVER_BOARD_WEIGHT = 375 
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
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/en/ui/serverlist.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/en/ui/login.sub",
		},

		## VirtualKeyboard
		{
			'name' : 'VirtualKeyboard',
			'type' : 'thinboard',
			'x' : (SCREEN_WIDTH - 564) / 2,
			'y' : SCREEN_HEIGHT - 300,
			'width' : 564,
			'height' : 254,
			'children' : 
			(
				{
					'name' : 'key_at',
					'type' : 'toggle_button',
					'x' : 40,
					'y' : 186,
					'default_image' : 'locale/en/ui/vkey/key_at.tga',
					'down_image' : 'locale/en/ui/vkey/key_at_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_at_over.tga',
				},
				{
					'name' : 'key_backspace',
					'type' : 'button',
					'x' : 498,
					'y' : 186,
					'default_image' : 'locale/en/ui/vkey/key_backspace.tga',
					'down_image' : 'locale/en/ui/vkey/key_backspace_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_backspace_over.tga',
				},
				{
					'name' : 'key_enter',
					'type' : 'button',
					'x' : 439,
					'y' : 186,
					'default_image' : 'locale/en/ui/vkey/key_enter.tga',
					'down_image' : 'locale/en/ui/vkey/key_enter_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_enter_over.tga',
				},
				{
					'name' : 'key_shift',
					'type' : 'toggle_button',
					'x' : 86,
					'y' : 186,
					'default_image' : 'locale/en/ui/vkey/key_shift.tga',
					'down_image' : 'locale/en/ui/vkey/key_shift_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_shift_over.tga',
				},
				{
					'name' : 'key_space',
					'type' : 'button',
					'x' : 145,
					'y' : 186,
					'default_image' : 'locale/en/ui/vkey/key_space.tga',
					'down_image' : 'locale/en/ui/vkey/key_space_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_space_over.tga',
				},
				{
					'name' : 'key_1',
					'type' : 'button',
					'x' : 40,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_2',
					'type' : 'button',
					'x' : 80,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_3',
					'type' : 'button',
					'x' : 120,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_4',
					'type' : 'button',
					'x' : 160,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_5',
					'type' : 'button',
					'x' : 200,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_6',
					'type' : 'button',
					'x' : 240,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_7',
					'type' : 'button',
					'x' : 280,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_8',
					'type' : 'button',
					'x' : 320,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_9',
					'type' : 'button',
					'x' : 360,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_10',
					'type' : 'button',
					'x' : 400,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_11',
					'type' : 'button',
					'x' : 440,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_12',
					'type' : 'button',
					'x' : 480,
					'y' : 24,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_13',
					'type' : 'button',
					'x' : 40,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_14',
					'type' : 'button',
					'x' : 80,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_15',
					'type' : 'button',
					'x' : 120,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_16',
					'type' : 'button',
					'x' : 160,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_17',
					'type' : 'button',
					'x' : 200,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_18',
					'type' : 'button',
					'x' : 240,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_19',
					'type' : 'button',
					'x' : 280,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_20',
					'type' : 'button',
					'x' : 320,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_21',
					'type' : 'button',
					'x' : 360,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_22',
					'type' : 'button',
					'x' : 400,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_23',
					'type' : 'button',
					'x' : 440,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_24',
					'type' : 'button',
					'x' : 480,
					'y' : 63,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_25',
					'type' : 'button',
					'x' : 60,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_26',
					'type' : 'button',
					'x' : 100,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_27',
					'type' : 'button',
					'x' : 140,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_28',
					'type' : 'button',
					'x' : 180,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_29',
					'type' : 'button',
					'x' : 220,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_30',
					'type' : 'button',
					'x' : 260,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_31',
					'type' : 'button',
					'x' : 300,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_32',
					'type' : 'button',
					'x' : 340,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_33',
					'type' : 'button',
					'x' : 380,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_34',
					'type' : 'button',
					'x' : 420,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_35',
					'type' : 'button',
					'x' : 460,
					'y' : 104,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_36',
					'type' : 'button',
					'x' : 60,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_37',
					'type' : 'button',
					'x' : 100,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_38',
					'type' : 'button',
					'x' : 140,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_39',
					'type' : 'button',
					'x' : 180,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_40',
					'type' : 'button',
					'x' : 220,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_41',
					'type' : 'button',
					'x' : 260,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_42',
					'type' : 'button',
					'x' : 300,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_43',
					'type' : 'button',
					'x' : 340,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_44',
					'type' : 'button',
					'x' : 380,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_45',
					'type' : 'button',
					'x' : 420,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_46',
					'type' : 'button',
					'x' : 460,
					'y' : 144,
					'default_image' : 'locale/en/ui/vkey/key_normal.tga',
					'down_image' : 'locale/en/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/en/ui/vkey/key_normal_over.tga',
				},
			)
		},

		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 208) / 2,
			"y" : (SCREEN_HEIGHT - 410 - 35),
			"width" : 208,
			"height" : 30,

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 15,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 150,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_BUTTON,
				},
			),
		},

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH - 208) / 2,
			"y" : (SCREEN_HEIGHT - 410),

			"image" : LOCALE_PATH + "loginwindow.sub",

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
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - 72,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,
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
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 247,
					"y" : 38,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",

					"x" : 10,
					"y" : 40,
					"width" : 232,
					"height" : SERVER_LIST_HEIGHT,
					"row_count" : 15,
					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 255,
					"y" : 40,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT + 22,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},

			),

		},

	),
}
