import uiScriptLocale

window = {
	"name" : "DragonSoulRefineWindow",

	## ¿ëÈ¥¼® Ã¢ ¹Ù·Î ¿ÞÂÊ
	"x" : SCREEN_WIDTH - 176 - 287 - 10 - 287,
	"y" : SCREEN_HEIGHT - 37 - 505,

	"style" : ("movable", "float",),

	"width" : 287,
	"height" : 232,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 287,
			"height" : 232,

			"children" :
			(
				## Base BackGroud Image
				{
					"name" : "DragonSoulRefineWindowBaseImage",
					"type" : "expanded_image",
					"x" : 0,
					"y" : 0,

					"image" : "d:/ymir work/ui/dragonsoul/dragon_soul_refine_bg.tga",
				},

				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 5,
					"y" : 7,

					"width" : 275,
					"color" : "yellow",

					"children" :
					(
						{ 
							"name":"TitleName", 
							"type":"text", 
							"x":140, 
							"y":5, 
							"text":uiScriptLocale.DRAGONSOUL_REFINE_WINDOW_TITLE, 
							"text_horizontal_align":"center" 
						},
					),
				},
				
				## Refine Slot
				{
					"name" : "RefineSlot",
					"type" : "grid_table",

					"image" : "d:/ymir work/ui/dragonsoul/cap.tga", 

					"x" : 15,
					"y" : 39,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 3,
					"x_step" : 32,
					"y_step" : 32,
				},

				## Result Slot
				{
					"name" : "ResultSlot",
					"type" : "grid_table",

					"x" : 207,
					"y" : 39,

					"start_index" : 0,
					"x_count" : 2,
					"y_count" : 3,
					"x_step" : 32,
					"y_step" : 32,
				},
				
				## Grade Button
				{
					"name" : "GradeButton",
					"type" : "toggle_button",

					"x" : 36,
					"y" : 148,

					"default_image" : "d:/ymir work/ui/dragonsoul/button_01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/button_02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/button_03.tga",

					"children" :
					(
						{
							"name" : "GradeSlotTitle",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : uiScriptLocale.GRADE_SELECT,
							"color" : 0xFFF1E6C0,
						},
					),
				},

				## Step Button
				{
					"name" : "StepButton",
					"type" : "toggle_button",

					"x" : 118,
					"y" : 148,

					"default_image" : "d:/ymir work/ui/dragonsoul/button_01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/button_02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/button_03.tga",

					"children" :
					(
						{
							"name" : "StepSlotTitle",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : uiScriptLocale.STEP_SELECT,
							"color" : 0xFFF1E6C0,
						},
					),
				},

				## Refine Button
				{
					"name" : "StrengthButton",
					"type" : "toggle_button",

					"x" : 198,
					"y" : 148,

					"default_image" : "d:/ymir work/ui/dragonsoul/button_01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/button_02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/button_03.tga",

					"children" :
					(
						{
							"name" : "RefineSlotTitle",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : uiScriptLocale.STRENGTH_SELECT,
							"color" : 0xFFF1E6C0,
						},
					),
				},

				## Money Print
				{
					"name":"Money_Slot",
					"type" : "text",

					"x":35,
					"y":180,

					"horizontal_align" : "right",
					"text_horizontal_align" : "right",

					"text" : "123456789",
				},

				## Do Refine Button
				{
					"name" : "DoRefineButton",
					"type" : "button",

					"x" : 188,
					"y" : 200,

					"default_image" : "d:/ymir work/ui/dragonsoul/l_button01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/l_button02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/l_button03.tga",

					"children" :
					(
						{ 
							"name" : "DoRefineButtonTitle", 
							"type" : "text", 
							"x" : 0, 
							"y" : 0, 
							"text" : uiScriptLocale.DO_REFINE, 
							"all_align" : "center",
						},
					),
				},
			),
		},
	),
}

