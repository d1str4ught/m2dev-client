import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.SELECT_PATH

BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (215) / 600

PLUS_BUTTON_WIDTH = 20
TEMPORARY_HEIGHT =  5

window = {
	"name" : "CreateCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGroundPattern",
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

			"image" : "d:/ymir work/ui/intro/select/background_alpha.sub",

			"x_scale" : float(SCREEN_WIDTH) / 100.0,
			"y_scale" : float(SCREEN_HEIGHT) / 69.0,
			"x_origin" : 0.0,
			"y_origin" : 0.0,
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

		## Buttons
		{
			"name" : "left_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (440) / 800,
			"y" : SCREEN_HEIGHT * (510) / 600,

			"default_image" : "d:/ymir work/ui/intro/select/left_button_01.sub",
			"over_image" : "d:/ymir work/ui/intro/select/left_button_02.sub",
			"down_image" : "d:/ymir work/ui/intro/select/left_button_03.sub",
		},
		{
			"name" : "right_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (570) / 800,
			"y" : SCREEN_HEIGHT * (510) / 600,

			"default_image" : "d:/ymir work/ui/intro/select/right_button_01.sub",
			"over_image" : "d:/ymir work/ui/intro/select/right_button_02.sub",
			"down_image" : "d:/ymir work/ui/intro/select/right_button_03.sub",
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
			"height" : 300 + TEMPORARY_HEIGHT,

			"children" :
			(
				{
					"name" : "text_board",
					"type" : "bar",

					"x" : 8,
					"y" : 10,

					"width" : 189,
					"height" : 122,

					"children" :
					(
						{
							"name" : "prev_button",
							"type" : "button",

							"x" : 95,
							"y" : 95,

							"text" : uiScriptLocale.CREATE_PREV,

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "next_button",
							"type" : "button",

							"x" : 140,
							"y" : 95,

							"text" : uiScriptLocale.CREATE_NEXT,

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "right_line",
							"type" : "line",

							"x" : 189-1,
							"y" : -1,

							"width" : 0,
							"height" : 122,

							"color" : 0xffAAA6A1,
						},
						{
							"name" : "bottom_line",
							"type" : "line",

							"x" : 0,
							"y" : 122-1,

							"width" : 189,
							"height" : 0,

							"color" : 0xffAAA6A1,
						},
						{
							"name" : "left_line",
							"type" : "line",

							"x" : 0,
							"y" : 0,

							"width" : 0,
							"height" : 122-1,

							"color" : 0xff2A2521,
						},
						{
							"name" : "top_line",
							"type" : "line",

							"x" : 0,
							"y" : 0,

							"width" : 189,
							"height" : 0,

							"color" : 0xff2A2521,
						},
					),
				},
				{
					"name" : "hth",
					"type" : "text",

					"x" : 15,
					"y" : 138,

					"text" : uiScriptLocale.CREATE_HP,

					"children" :
					(
						{
							"name" : "hth_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "red",
						},
						{
							"name" : "hth_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "hth_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "int",
					"type" : "text",

					"x" : 15,
					"y" : 157,

					"text" : uiScriptLocale.CREATE_SP,

					"children" :
					(
						{
							"name" : "int_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "pink",
						},
						{
							"name" : "int_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "int_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "str",
					"type" : "text",

					"x" : 15,
					"y" : 176,

					"text" : uiScriptLocale.CREATE_ATT_GRADE,

					"children" :
					(
						{
							"name" : "str_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "purple",
						},
						{
							"name" : "str_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "str_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "dex",
					"type" : "text",

					"x" : 15,
					"y" : 195,

					"text" : uiScriptLocale.CREATE_DEX_GRADE,

					"children" :
					(
						{
							"name" : "dex_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "blue",
						},
						{
							"name" : "dex_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "dex_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},

				{
					"name" : "hth_button",
					"type" : "button",

					"x" : 184,
					"y" : 139,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "int_button",
					"type" : "button",

					"x" : 184,
					"y" : 158,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "str_button",
					"type" : "button",

					"x" : 184,
					"y" : 177,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "dex_button",
					"type" : "button",

					"x" : 184,
					"y" : 196,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},

				{
					"name" : "character_name",
					"type" : "text",

					"x" : 43,
					"y" : 217 + TEMPORARY_HEIGHT,

					"text" : uiScriptLocale.CREATE_NAME,

					"text_horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "character_name_slot",
							"type" : "image",

							"x" : 40 - 1,
							"y" : -2,

							"image" : "d:/ymir work/ui/public/parameter_slot_04.sub",
						},
						{
							"name" : "character_name_value",
							"type" : "editline",

							"x" : 40 - 1 + 3,
							"y" : 0,

							"input_limit" : 12,

							"width" : 90,
							"height" : 20,
						},
					),
				},

				{
					"name" : "character_name",
					"type" : "text",

					"x" : 43,
					"y" : 241 + TEMPORARY_HEIGHT,

					"text" : uiScriptLocale.CREATE_SHAPE,

					"text_horizontal_align" : "center",
				},
				{
					"name" : "shape_button_01",
					"type" : "radio_button",

					"x" : 79,
					"y" : 239 + TEMPORARY_HEIGHT,

					"text" : "1",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "shape_button_02",
					"type" : "radio_button",

					"x" : 139,
					"y" : 239 + TEMPORARY_HEIGHT,

					"text" : "2",

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "create_button",
					"type" : "button",

					"x" : 11,
					"y" : 265 + TEMPORARY_HEIGHT,

					"text" : uiScriptLocale.CREATE_CREATE,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 109,
					"y" : 265 + TEMPORARY_HEIGHT,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
			),
		},
	),
}
