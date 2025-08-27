import uiScriptLocale

window = {
	"name" : "InputDialog_WithDescription",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 106,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 106,

			"title" : "",

			"children" :
			(

				## Text
				{
					"name" : "Description",
					"type" : "text",
					"text" : "",
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"x" : 0,
					"y" : 34,
				},

				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 0,
					"y" : 51,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},

				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 74,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 74,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

			),
		},
	),
}