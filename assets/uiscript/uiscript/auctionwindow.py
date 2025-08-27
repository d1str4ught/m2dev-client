ROOT_PATH = "d:/ymir work/ui/game/guild/"

window = {
	"name" : "AuctionWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 376,
	"height" : 370,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 376,
			"height" : 370,

			"title" : "매매 등록",

			"children" :
			(
				## Tab Area
				{
					"name" : "TabControl",
					"type" : "window",

					"x" : 0,
					"y" : 37,
					"vertical_align" : "bottom",

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

							"image" : ROOT_PATH+"tab_1.sub",
						},
						{
							"name" : "Tab_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : ROOT_PATH+"tab_2.sub",
						},
						{
							"name" : "Tab_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 376,
							"height" : 37,

							"image" : ROOT_PATH+"tab_3.sub",
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
					),
				},

			),
		},
	),
}
