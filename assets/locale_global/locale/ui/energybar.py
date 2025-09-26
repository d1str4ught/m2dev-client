import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0
window = {
	"name" : "EnergyBar",

	"x" : 0,
	"y" : SCREEN_HEIGHT - 55,

	"width" : 50,
	"height" : 10,

	"children" :
	(
		# ±â·Â
		{
			"name" : "EnergyGauge_Board",
			"type" : "image",

			"x" : 0,
			"y" : -10 + Y_ADD_POSITION,

			"image" : "D:/Ymir Work/UI/Pattern/EnergyGauge/energygauge_base.tga",

			"children" :
			(
				{
					"name" : "EnergyGauge_Empty",
					"type" : "expanded_image",

					"x" : 5,
					"y" : 8,

					"image" : "D:/Ymir Work/UI/Pattern/EnergyGauge/gauge_empty.tga",
				},
				{
					"name" : "EnergyGauge_Hungry",
					"type" : "expanded_image",

					"x" : 5,
					"y" : 8,

					"image" : "D:/Ymir Work/UI/Pattern/EnergyGauge/gauge_hungry.tga",
				},
				{
					"name" : "EnergyGauge_Full",
					"type" : "expanded_image",

					"x" : 5,
					"y" : 8,

					"image" : "D:/Ymir Work/UI/Pattern/EnergyGauge/gauge_full.tga",
				},
			),
		},
		{
			"name" : "EnergyGauge_ToolTip",

			"x" : 0,
			"y" : 0,
			
			"width"  : 50,
			"height" : 10,		
			"type" : "window",
		},		
	),
}

