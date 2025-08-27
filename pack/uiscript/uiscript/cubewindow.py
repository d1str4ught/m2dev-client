import localeInfo
import uiScriptLocale

LOCALE_PATH = uiScriptLocale.WINDOWS_PATH
ICON_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"

window = {
	"name" : "CubeWindow",

#	"x" : 430,
#	"y" : 130,
	"x" : SCREEN_WIDTH - 176 - 200 - 80,
	"y" : SCREEN_HEIGHT - 37 - 563,


	"style" : ("movable", "float",),

	"width" : 285,
	"height" : 521,

	"children" :
	(
		{
			"name" : "board",
			"type" : "expanded_image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width"		: 285,
			"height"	: 521,

			"image"		: uiScriptLocale.LOCALE_UISCRIPT_PATH + "new_cube_bg.tga",

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 5,
					"y" : 5,

					"width" : 273,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.CUBE_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Cube Slot
				{
					"name" : "CubeSlot",
					"type" : "grid_table",

					"x" : 14,
					"y" : 364,

					"start_index" : 0,
					"x_count" : 8,
					"y_count" : 3,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				## Print
				{
					"name" : "NeedMoney",
					"type" : "text",

					"x" : 20,
					"y" : 468,

					"width" : 200,

					"horizontal_align" : "right",
					"text_horizontal_align" : "right",

					"text" : localeInfo.NumberToMoneyString(0),
				},

				{
					"name" : "contentScrollbar",
					"type" : "thin_scrollbar",

					"x" : 253,
					"y" : 38,

					"size" : 315,
				},

				# Cube Result List. 1 ~ 3
				{
					"name" : "result1board",
					"type" : "window",
					
					"x" : 25,
					"y" : 41,
					
					"width" : 216,
					"height" : 64,

					"children" : 
					(
						{
							"name" : "result1", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 0,
							"y" : 0,
						},
						{
							"name" : "material11", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 57,
							"y" : 0,
						},
						{
							"name" : "material12", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 90,
							"y" : 0,
						},
						{
							"name" : "material13", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 123, 
							"y" : 0,
						},
						{
							"name" : "material14", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 156, 
							"y" : 0,
						},
						{
							"name" : "material15", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 189, 
							"y" : 0,
						},
					),

				},
				{
					"name" : "result2board",
					"type" : "window",
					
					"x" : 25,
					"y" : 147,
					
					"width" : 216,
					"height" : 64,

					"children" : 
					(
						{
							"name" : "result2", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 0,
							"y" : 0,
						},
						{
							"name" : "material21", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 57,
							"y" : 0,
						},
						{
							"name" : "material22", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 90,
							"y" : 0,
						},
						{
							"name" : "material23", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 123, 
							"y" : 0,
						},
						{
							"name" : "material24", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 156, 
							"y" : 0,
						},
						{
							"name" : "material25", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 189, 
							"y" : 0,
						},
					),
				},
				{
					"name" : "result3board",
					"type" : "window",
					
					"x" : 25,
					"y" : 253,
					
					"width" : 216,
					"height" : 64,

					"children" : 
					(
						{
							"name" : "result3", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 0,
							"y" : 0,
						},
						{
							"name" : "material31", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 57,
							"y" : 0,
						},
						{
							"name" : "material32", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 90,
							"y" : 0,
						},
						{
							"name" : "material33", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 123, 
							"y" : 0,
						},
						{
							"name" : "material34", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 156, 
							"y" : 0,
						},
						{
							"name" : "material35", 
							"type" : "grid_table",
							"start_index" : 0,
						
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"x" : 189, 
							"y" : 0,
						},
					),
				},


				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : 148,
					"y" : 32,
					"vertical_align" : "bottom",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 211,
					"y" : 32,
					"vertical_align" : "bottom",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				
			),
		},
	),
}
