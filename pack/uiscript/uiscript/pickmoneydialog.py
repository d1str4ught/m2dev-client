import uiScriptLocale

window = {
	"name" : "PickMoneyDialog",

	"x" : 100,
	"y" : 100,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 90,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 90,
			"title" : uiScriptLocale.PICK_MONEY_TITLE,

			"children" :
			(

				## Money Slot
				{
					"name" : "money_slot",
					"type" : "image",

					"x" : 20,
					"y" : 34,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_02.sub",

					"children" :
					(
						{
							"name" : "money_value",
							"type" : "editline",

							"x" : 3,
							"y" : 2,

							"width" : 60,
							"height" : 18,

							"input_limit" : 6,
							"only_number" : 1,

							"text" : "1",
						},
						{
							"name" : "max_value",
							"type" : "text",

							"x" : 63,
							"y" : 3,

							"text" : "/ 999999",
						},
					),
				},

				## Button
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : 170/2 - 61 - 5,
					"y" : 58,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 170/2 + 5,
					"y" : 58,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}