import uiScriptLocale

window = {
	"name" : "QuestionDialog",

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : 280,
	"height" : 75,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 280,
			"height" : 75,

			"children" :
			(
				{
					"name" : "message",
					"type" : "text",

					"x" : 0,
					"y" : 25,

					"text" : uiScriptLocale.LOGIN_CONNECTING,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "countdown_message",
					"type" : "text",

					"x" : 0,
					"y" : 50,

					"text" : uiScriptLocale.MESSAGE,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
			),

		},
	),
}
