import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/game/guild/"
LOCALE_PATH = uiScriptLocale.GUILD_PATH

window = {
	"name" : "GuildWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 376,
	"height" : 356,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 376,
			"height" : 356,

			"title" : uiScriptLocale.GUILD_NAME,

			"children" :
			(
				## Tab Area
				{
					"name" : "TabControl",
					"type" : "window",

					"x" : 0,
					"y" : 328,

					"width" : 376,
					"height" : 37,

					"children" :
					(
						## Tab
						{
							"name" : "Tab_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_1.sub",
						},
						{
							"name" : "Tab_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_2.sub",
						},
						{
							"name" : "Tab_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_3.sub",
						},
						{
							"name" : "Tab_04",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_4.sub",
						},
						{
							"name" : "Tab_05",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_5.sub",
						},
						{
							"name" : "Tab_06",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : LOCALE_PATH+"tab_6.sub",
						},
						## RadioButton
						{
							"name" : "Tab_Button_01",
							"type" : "radio_button",

							"x" : 6,
							"y" : 5,

							"width" : 53,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_02",
							"type" : "radio_button",

							"x" : 61,
							"y" : 5,

							"width" : 67,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_03",
							"type" : "radio_button",

							"x" : 130,
							"y" : 5,

							"width" : 60,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_04",
							"type" : "radio_button",

							"x" : 192,
							"y" : 5,

							"width" : 60,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_05",
							"type" : "radio_button",

							"x" : 254,
							"y" : 5,

							"width" : 60,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_06",
							"type" : "radio_button",

							"x" : 316,
							"y" : 5,

							"width" : 55,
							"height" : 27,
						},
					),
				},

			),
		},
	),
}
