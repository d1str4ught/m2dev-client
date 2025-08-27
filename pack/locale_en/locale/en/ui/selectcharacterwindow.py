import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.SELECT_PATH

BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (220) / 600

BOARD_ITEM_ADD_POSITION = -40

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/en/ui/select.sub",
		},
		## Name
		{
			"name" : "name_warrior",
			"type" : "image",

			"x" : BOARD_X - 27,
			"y" : BOARD_Y - 174 + 25,

			"image" : LOCALE_PATH+"name_warrior.sub",
		},
		{
			"name" : "name_assassin",
			"type" : "image",

			"x" : BOARD_X - 27,
			"y" : BOARD_Y - 174 + 25,

			"image" : LOCALE_PATH+"name_assassin.sub",
		},
		{
			"name" : "name_sura",
			"type" : "image",

			"x" : BOARD_X - 27,
			"y" : BOARD_Y - 174 + 25,

			"image" : LOCALE_PATH+"name_sura.sub",
		},
		{
			"name" : "name_shaman",
			"type" : "image",

			"x" : BOARD_X - 27,
			"y" : BOARD_Y - 174 + 25,

			"image" : LOCALE_PATH+"name_shaman.sub",
		},


		## Character Board
		{
			"name" : "character_board",
			"type" : "thinboard",

			"x" : BOARD_X,
			"y" : BOARD_Y,

			"width" : 208,
			"height" : 363 + BOARD_ITEM_ADD_POSITION,

			"children" :
			(

				## Empire Flag
				{
					"name" : "EmpireFlag_A",
					"type" : "expanded_image",

					"x" : 21,
					"y" : 12,
					"x_scale" : 0.5,
					"y_scale" : 0.5,

					"image" : "d:/ymir work/ui/intro/empire/empireflag_a.sub"
				},
				{
					"name" : "EmpireFlag_B",
					"type" : "expanded_image",

					"x" : 21,
					"y" : 12,
					"x_scale" : 0.5,
					"y_scale" : 0.5,

					"image" : "d:/ymir work/ui/intro/empire/empireflag_b.sub"
				},
				{
					"name" : "EmpireFlag_C",
					"type" : "expanded_image",

					"x" : 21,
					"y" : 12,
					"x_scale" : 0.5,
					"y_scale" : 0.5,

					"image" : "d:/ymir work/ui/intro/empire/empireflag_c.sub"
				},

				{
					"name" : "EmpireNameSlot",
					"type" : "image",

					"x" : 100,
					"y" : 12,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",

					"children" :
					(
						{
							"name" : "EmpireName",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"text" : uiScriptLocale.SELECT_EMPIRE_NAME,

							"all_align" : "center",
						},
					),
				},

				{
					"name" : "GuildNameSlot",
					"type" : "image",

					"x" : 100,
					"y" : 33,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",

					"children" :
					(
						{
							"name" : "GuildName",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"text" : uiScriptLocale.SELECT_NO_GUILD,

							"all_align" : "center",
						},
					),
				},

				{
					"name" : "character_name",
					"type" : "text",

					"x" : 17,
					"y" : 124 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_NAME,

					"children" :
					(
						{
							"name" : "character_name_slot",
							"type" : "image",

							"x" : 43,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
						},
						{
							"name" : "character_name_value",
							"type" : "text",

							"x" : 43 + 130/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_level",
					"type" : "text",

					"x" : 17,
					"y" : 50 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_LEVEL,

					"children" :
					(
						{
							"name" : "character_level_slot",
							"type" : "image",

							"x" : 43,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
						},
						{
							"name" : "character_level_value",
							"type" : "text",

							"x" : 43 + 130/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_play_time",
					"type" : "text",

					"x" : 17,
					"y" : 76 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_PLAYTIME,

					"children" :
					(
						{
							"name" : "character_play_time_slot",
							"type" : "image",

							"x" : 83,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_03.sub",
						},
						{
							"name" : "character_play_time_value",
							"type" : "text",

							"x" : 83 + 91/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_hth",
					"type" : "text",

					"x" : 17,
					"y" : 102 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_HP,

					"children" :
					(
						{
							"name" : "gauge_hth",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100,
							"color" : "red",
						},
						{
							"name" : "character_hth_slot",
							"type" : "image",

							"x" : 134,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						},
						{
							"name" : "character_hth_value",
							"type" : "text",

							"x" : 134 + 39/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_int",
					"type" : "text",

					"x" : 17,
					"y" : 128 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_SP,

					"children" :
					(
						{
							"name" : "gauge_int",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100,
							"color" : "pink",
						},
						{
							"name" : "character_int_slot",
							"type" : "image",

							"x" : 134,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						},
						{
							"name" : "character_int_value",
							"type" : "text",

							"x" : 134 + 39/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_str",
					"type" : "text",

					"x" : 17,
					"y" : 154 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_ATT_GRADE,

					"children" :
					(
						{
							"name" : "gauge_str",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100,
							"color" : "purple",
						},
						{
							"name" : "character_str_slot",
							"type" : "image",

							"x" : 134,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						},
						{
							"name" : "character_str_value",
							"type" : "text",

							"x" : 134 + 39/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_dex",
					"type" : "text",

					"x" : 17,
					"y" : 180 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_DEX_GRADE,

					"children" :
					(
						{
							"name" : "gauge_dex",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100,
							"color" : "blue",
						},
						{
							"name" : "character_dex_slot",
							"type" : "image",

							"x" : 134,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						},
						{
							"name" : "character_dex_value",
							"type" : "text",

							"x" : 134 + 39/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},

				## Buttons
				{
					"name" : "start_button",
					"type" : "button",

					"x" : 14,
					"y" : 210 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_SELECT,
					"text_height" : 6,

					"default_image" : ROOT_PATH + "XLarge_Button_01.sub",
					"over_image" : ROOT_PATH + "XLarge_Button_02.sub",
					"down_image" : ROOT_PATH + "XLarge_Button_03.sub",
				},
				{
					"name" : "create_button",
					"type" : "button",

					"x" : 14,
					"y" : 210 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_CREATE,
					"text_height" : 6,

					"default_image" : ROOT_PATH + "XLarge_Button_01.sub",
					"over_image" : ROOT_PATH + "XLarge_Button_02.sub",
					"down_image" : ROOT_PATH + "XLarge_Button_03.sub",
				},
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 105,
					"y" : 245 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_EXIT,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "delete_button",
					"type" : "button",

					"x" : 14,
					"y" : 245 + 100 - 21 + BOARD_ITEM_ADD_POSITION,

					"text" : uiScriptLocale.SELECT_DELETE,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
			),
		},

		## Buttons
		{
			"name" : "left_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (450 - 22*3) / 800,
			"y" : SCREEN_HEIGHT * (505) / 600,

			"default_image" : "d:/ymir work/ui/intro/select/dragon_left_button_01.sub",
			"over_image" : "d:/ymir work/ui/intro/select/dragon_left_button_02.sub",
			"down_image" : "d:/ymir work/ui/intro/select/dragon_left_button_03.sub",
		},
		{
			"name" : "right_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (580 - 22) / 800,
			"y" : SCREEN_HEIGHT * (505) / 600,

			"default_image" : "d:/ymir work/ui/intro/select/dragon_right_button_01.sub",
			"over_image" : "d:/ymir work/ui/intro/select/dragon_right_button_02.sub",
			"down_image" : "d:/ymir work/ui/intro/select/dragon_right_button_03.sub",
		},

	),
}
