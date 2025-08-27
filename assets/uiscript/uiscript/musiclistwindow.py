import uiScriptLocale

window = {
	"name" : "MusicListWindow",

	"x" : SCREEN_WIDTH - 170,
	"y" : SCREEN_HEIGHT - 400 - 50,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 300,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 300,
			"title" : uiScriptLocale.MUSICLIST_TITLE,
		},

		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 27,
			"y" : 40,
			"size" : 220,
			"horizontal_align" : "right",
		},

		{
			"name" : "ok",
			"type" : "button",

			"x" : 15,
			"y" : 265,

			"width" : 61,
			"height" : 21,

			"text" : uiScriptLocale.OK,

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "cancel",
			"type" : "button",

			"x" : 60,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : uiScriptLocale.CANCEL,

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

		{
			"name" : "refresh",
			"type" : "button",

			"x" : 115,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : uiScriptLocale.MARKLIST_REFRESH,

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
	)
}
