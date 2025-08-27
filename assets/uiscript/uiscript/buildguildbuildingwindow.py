import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_02.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"

TEMP_X = 110

window = {
	"name" : "BuildGuildBuildingWindow",
	"style" : ("movable", "float",),

	"x" : 10,
	"y" : SCREEN_HEIGHT - 240 - 50,

	"width" : 355+TEMP_X,
	"height" : 240,

	"children" :
	(

		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 355+TEMP_X,
			"height" : 240,

			"title" : uiScriptLocale.GUILD_BUILDING_TITLE,

			"children" :
			(

				{
					"name" : "BuildingCategoryTitle",
					"type" : "text",

					"x" : 15 + 50,
					"y" : 33,
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.GUILD_BUILDING_CATEGORY_TITLE,
				},
				{
					"name" : "BuildingCategoryBar",
					"type" : "slotbar",

					"x" : 15,
					"y" : 50,

					"width" : 100,
					"height" : 80,

					"children" :
					(
						{
							"name" : "CategoryList",
							"type" : "listbox",

							"x" : 0,
							"y" : 1,

							"width" : 100,
							"height" : 80,
						},
					),
				},

				{
					"name" : "BuildingPriceTitle",
					"type" : "text", "x" : 30, "y" : 143, "text" : uiScriptLocale.GUILD_BUILDING_PRICE,
					"text_horizontal_align" : "center",
					"children" :
					(
						{
							"name":"BuildingPriceSlot",
							"type":"slotbar", "x":25, "y":-4, "width":60, "height":17,
							"children" :
							(
								{ "name" : "BuildingPriceValue", "type" : "text", "x" : 0, "y" : 1, "all_align" : "center", "text" : "50000000", },
							),
						},
					),
				},

				{
					"name" : "BuildingMaterialStoneTitle",
					"type" : "text", "x" : 30, "y" : 163, "text" : uiScriptLocale.GUILD_BUILDING_STONE,
					"text_horizontal_align" : "center",
					"children" :
					(
						{
							"name":"BuildingMaterialStoneSlot",
							"type":"slotbar", "x":25, "y":-4, "width":60, "height":17,
							"children" :
							(
								{ "name" : "BuildingMaterialStoneValue", "type" : "text", "x" : 0, "y" : 1, "all_align" : "center", "text" : "50000000", },
							),
						},
					),
				},

				{
					"name" : "BuildingMaterialLogTitle",
					"type" : "text", "x" : 30, "y" : 183, "text" : uiScriptLocale.GUILD_BUILDING_LOG,
					"text_horizontal_align" : "center",
					"children" :
					(
						{
							"name":"BuildingMaterialLogSlot",
							"type":"slotbar", "x":25, "y":-4, "width":60, "height":17,
							"children" :
							(
								{ "name" : "BuildingMaterialLogValue", "type" : "text", "x" : 0, "y" : 1, "all_align" : "center", "text" : "50000000", },
							),
						},
					),
				},

				{
					"name" : "BuildingMaterialPlywoodTitle",
					"type" : "text", "x" : 30, "y" : 203, "text" : uiScriptLocale.GUILD_BUILDING_PLY,
					"text_horizontal_align" : "center",
					"children" :
					(
						{
							"name":"BuildingMaterialPlywoodSlot",
							"type":"slotbar", "x":25, "y":-4, "width":60, "height":17,
							"children" :
							(
								{ "name" : "BuildingMaterialPlywoodValue", "type" : "text", "x" : 0, "y" : 1, "all_align" : "center", "text" : "50000000", },
							),
						},
					),
				},

				{
					"name" : "temp_window",
					"type" : "window",
					"style" : ("not_pick",),

					"x" : TEMP_X,
					"y" : 0,
					"width" : 355,
					"height" : 240,

					"children" :
					(

						### START_TEMP
						{
							"name" : "BuildingListTitle",
							"type" : "text",

							"x" : 15 + 60,
							"y" : 33,
							"text_horizontal_align" : "center",

							"text" : uiScriptLocale.GUILD_BUILDING_LIST_TITLE,
						},

						{
							"name" : "BuildingListBar",
							"type" : "slotbar",

							"x" : 15,
							"y" : 50,

							"width" : 120,
							"height" : 172,

							"children" :
							(
								{
									"name" : "BuildingList",
									"type" : "listbox",

									"x" : 0,
									"y" : 1,

									"width" : 105,
									"height" : 172,
								},
								{
									"name" : "ListScrollBar",
									"type" : "scrollbar",

									"x" : 15,
									"y" : 2,
									"size" : 172-2,
									"horizontal_align" : "right",
								},
							),
						},

						{
							"name" : "BuildingPositionTitle",
							"type" : "text",

							"x" : 250,
							"y" : 33,
							"text_horizontal_align" : "center",

							"text" : uiScriptLocale.GUILD_BUILDING_POSITION,
						},
						{
							"name" : "PositionButton",
							"type" : "radio_button", "x" : 280, "y" : 50, "text" : uiScriptLocale.GUILD_BUILDING_CHANGE,
							"default_image" : ROOT_PATH + "Big_Button_01.sub",
							"over_image" : ROOT_PATH + "Big_Button_02.sub",
							"down_image" : ROOT_PATH + "Big_Button_03.sub",
						},
						{
							"name" : "BuildingPositionXTitle",
							"type" : "text", "x" : 150, "y" : 53, "text" : "X",
							"text_horizontal_align" : "center",
							"children" :
							(
								{
									"name":"BuildingPositionXSlot",
									"type":"image", "x":23, "y":-3, "image":MIDDLE_VALUE_FILE,
									"children" :
									(
										{ "name" : "BuildingPositionXValue", "type" : "text", "x" : 0, "y" : 0, "all_align" : "center", "text" : "999", },
									),
								},
							),
						},
						{
							"name" : "BuildingPositionY",
							"type" : "text", "x" : 150, "y" : 73, "text" : "Y",
							"text_horizontal_align" : "center",
							"children" :
							(
								{
									"name":"BuildingPositionYSlot",
									"type":"image", "x":23, "y":-3, "image":MIDDLE_VALUE_FILE,
									"children" :
									(
										{ "name" : "BuildingPositionYValue", "type" : "text", "x" : 0, "y" : 0, "all_align" : "center", "text" : "999", },
									),
								},
							),
						},

						{
							"name" : "BuildingRotationTitle",
							"type" : "text",

							"x" : 250,
							"y" : 95,
							"text_horizontal_align" : "center",

							"text" : uiScriptLocale.GUILD_BUILDING_DIRECTION,
						},
						{
							"name" : "BuildingRotationXTitle",
							"type" : "text", "x" : 150, "y" : 115, "text" : "X",
							"text_horizontal_align" : "center",
						},
						{
							"name" : "BuildingRotationX",
							"type" : "sliderbar",
							"x" : 158, "y" : 115,
						},
						{
							"name" : "BuildingRotationYTitle",
							"type" : "text", "x" : 150, "y" : 135, "text" : "Y",
							"text_horizontal_align" : "center",
						},
						{
							"name" : "BuildingRotationY",
							"type" : "sliderbar",
							"x" : 158, "y" : 135,
						},
						{
							"name" : "BuildingRotationZTitle",
							"type" : "text", "x" : 150, "y" : 155, "text" : "Z",
							"text_horizontal_align" : "center",
						},
						{
							"name" : "BuildingRotationZ",
							"type" : "sliderbar",
							"x" : 158, "y" : 155,
						},

						{
							"name" : "PreviewButton",
							"type" : "toggle_button",

							"x" : 200,
							"y" : 60,
							"vertical_align" : "bottom",

							"text" : uiScriptLocale.GUILD_BUILDING_PREVIEW,

							"default_image" : ROOT_PATH + "Large_Button_01.sub",
							"over_image" : ROOT_PATH + "Large_Button_02.sub",
							"down_image" : ROOT_PATH + "Large_Button_03.sub",
						},

						{
							"name" : "AcceptButton",
							"type" : "button",

							"x" : 200,
							"y" : 35,

							"text" : uiScriptLocale.ACCEPT,
							"vertical_align" : "bottom",

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "CancelButton",
							"type" : "button",

							"x" : 245,
							"y" : 35,

							"text" : uiScriptLocale.CANCEL,
							"vertical_align" : "bottom",

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						### END_TEMP

					),

				},

			),
		},

	),
}
