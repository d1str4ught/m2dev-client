import uiScriptLocale

ROOT = "d:/ymir work/ui/minimap/"
MOVE_X = 10

window = {
	"name" : "MiniMap",

	"x" : SCREEN_WIDTH - 136 - MOVE_X,
	"y" : 0,

	"width" : 136 + MOVE_X,
	"height" : 137,

	"children" :
	(
		## OpenWindow
		{
			"name" : "OpenWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 136 + MOVE_X,
			"height" : 137,

			"children" :
			(
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : 0 + MOVE_X,
					"y" : 0,
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "minimap/minimap.sub",
				},
				## MiniMapWindow
				{
					"name" : "MiniMapWindow",
					"type" : "window",

					"x" : 4 + MOVE_X,
					"y" : 5,

					"width" : 128,
					"height" : 128,
				},
				## ScaleUpButton
				{
					"name" : "ScaleUpButton",
					"type" : "button",

					"x" : 101 + MOVE_X,
					"y" : 116,

					"default_image" : ROOT + "minimap_scaleup_default.sub",
					"over_image" : ROOT + "minimap_scaleup_over.sub",
					"down_image" : ROOT + "minimap_scaleup_down.sub",
				},
				## ScaleDownButton
				{
					"name" : "ScaleDownButton",
					"type" : "button",

					"x" : 115 + MOVE_X,
					"y" : 103,

					"default_image" : ROOT + "minimap_scaledown_default.sub",
					"over_image" : ROOT + "minimap_scaledown_over.sub",
					"down_image" : ROOT + "minimap_scaledown_down.sub",
				},
				## MiniMapHideButton
				{
					"name" : "MiniMapHideButton",
					"type" : "button",

					"x" : 111 + MOVE_X,
					"y" : 6,

					"default_image" : ROOT + "minimap_close_default.sub",
					"over_image" : ROOT + "minimap_close_over.sub",
					"down_image" : ROOT + "minimap_close_down.sub",
				},
				## AtlasShowButton
				{
					"name" : "AtlasShowButton",
					"type" : "button",

					"x" : 12 + MOVE_X,
					"y" : 11,

					"default_image" : ROOT + "atlas_open_default.sub",
					"over_image" : ROOT + "atlas_open_over.sub",
					"down_image" : ROOT + "atlas_open_down.sub",
				},
				## ServerInfo
				{
					"name" : "ServerInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70 + MOVE_X,
					"y" : 140,

					"text" : "",
				},
				## PositionInfo
				{
					"name" : "PositionInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70 + MOVE_X,
					"y" : 160,

					"text" : "",
				},
				## ObserverCount
				{
					"name" : "ObserverCount",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70 + MOVE_X,
					"y" : 180,

					"text" : "",
				},
			),
		},
		{
			"name" : "CloseWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 132 + MOVE_X,
			"height" : 48,

			"children" :
			(
				## ShowButton
				{
					"name" : "MiniMapShowButton",
					"type" : "button",

					"x" : 100 + MOVE_X,
					"y" : 4,

					"default_image" : ROOT + "minimap_open_default.sub",
					"over_image" : ROOT + "minimap_open_default.sub",
					"down_image" : ROOT + "minimap_open_default.sub",
				},
			),
		},
	),
}
