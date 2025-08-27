import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "RestartDialog",
	"style" : ("float",),

	"x" : 50,
	"y" : 50,

	"width" : 200,
	"height" : 88,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 88,

			"r" : 0.3333,
			"g" : 0.2941,
			"b" : 0.2588,
			"a" : 1.0,

			"children" :
			(
				{
					"name" : "restart_here_button",
					"type" : "button",

					"x" : 10,
					"y" : 17,

					"text" : uiScriptLocale.RESTART_HERE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "restart_town_button",
					"type" : "button",

					"x" : 10,
					"y" : 47,

					"text" : uiScriptLocale.RESTART_TOWN,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
			),
		},
	),
}
