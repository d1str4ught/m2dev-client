import uiScriptLocale

RESOURCE_NAME_POS = 132

window = {
	"name" : "GuildWindow_BaseInfoPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		## Name
		{
			"name" : "BaseName",
			"type" : "text",
			"x" : 90,
			"y" : 10,
			"text" : uiScriptLocale.GUILD_BASENAME,
		},
		{
			"name" : "BaseNameSlot",
			"type" : "slotbar",
			"x" : 180,
			"y" : 3,
			"width" : 105,
			"height" : 24,
			"text" : uiScriptLocale.GUILD_BASENAME,
			"children" :
			(
				{
					"name" : "BaseNameValue",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"text" : uiScriptLocale.GUILD_BASENAME,
					"fontsize" : "LARGE",
					"all_align" : "center",
				},
			),
		},

		## Resource Information
		{
			"name" : "HorizontalBar1",
			"type" : "horizontalbar",
			"x" : 0,
			"y" : 32,
			"width" : 337,
			"horizontal_align" : "center",
			"children" :
			(

				{
					"name" : "ResourceInformationName",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"text" : uiScriptLocale.GUILD_RESOURCE_INFO,
					"all_align" : "center",
				},

				{
					"name" : "ResourceSlot1", "type" : "slotbar", "x" : 5 + 31*0, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName1", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_WATER_STONE, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue1", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},
				{
					"name" : "ResourceSlot2", "type" : "slotbar", "x" : 5 + 31*1, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName2", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_METIN_STONE, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue2", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},
				{
					"name" : "ResourceSlot3", "type" : "slotbar", "x" : 5 + 31*2, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName3", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_WATER, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue3", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},
				{
					"name" : "ResourceSlot4", "type" : "slotbar", "x" : 5 + 31*3, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName4", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_CRYSTAL, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue4", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},
				{
					"name" : "ResourceSlot5", "type" : "slotbar", "x" : 5 + 31*4, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName5", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_MINENAL, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue5", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},
				{
					"name" : "ResourceSlot6", "type" : "slotbar", "x" : 5 + 31*5, "y" : 38, "width" : 27, "height" : 18,
					"children" :
					(
						{ "name" : "ResourceName6", "type" : "text", "x" : 0, "y" : -16, "text" : uiScriptLocale.GUILD_GEM, "horizontal_align" : "center", "text_horizontal_align" : "center", },
						{ "name" : "ResourceValue6", "type" : "text", "x" : 0, "y" : 0, "text" : "999", "all_align" : "center", },
					),
				},

				{
					"name" : "ResourceBasket", "type" : "bar", "x" : 195, "y" : 21, "width" : 142, "height" : 39,
					"children" :
					(
						{
							"name" : "ResourceBasketDescription1", "type" : "text", "x" : 0, "y" : 5, "text" : uiScriptLocale.GUILD_DROP_RESOURCE1, "horizontal_align" : "center", "text_horizontal_align" : "center",
						},
						{
							"name" : "ResourceBasketDescription2", "type" : "text", "x" : 0, "y" : 21, "text" : uiScriptLocale.GUILD_DROP_RESOURCE2, "horizontal_align" : "center", "text_horizontal_align" : "center",
						},
					),
				},

			),
		},

		## Resource Information
		{
			"name" : "HorizontalBar1",
			"type" : "horizontalbar",
			"x" : 0,
			"y" : 95,
			"width" : 337,
			"horizontal_align" : "center",
			"children" :
			(

				{
					"name" : "ResourceInformationName",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"text" : uiScriptLocale.GUILD_BUILDING_INFO,
					"all_align" : "center",
				},

				## BuildingName
				{
					"name" : "BuildingName", "type" : "text", "x" : 16, "y" : 20, "text" : uiScriptLocale.GUILD_BUILDING_NAME,
				},
				## Grade
				{
					"name" : "Grade", "type" : "text", "x" : 89, "y" : 20, "text" : uiScriptLocale.GUILD_BUILDING_GRADE,
				},

				## Resources
				{ "name" : "ResourceName1", "type" : "text", "x" : RESOURCE_NAME_POS + 29*0, "y" : 20, "text" : uiScriptLocale.GUILD_WATER_STONE, "text_horizontal_align" : "center", },
				{ "name" : "ResourceName2", "type" : "text", "x" : RESOURCE_NAME_POS + 29*1, "y" : 20, "text" : uiScriptLocale.GUILD_METIN_STONE, "text_horizontal_align" : "center", },
				{ "name" : "ResourceName3", "type" : "text", "x" : RESOURCE_NAME_POS + 29*2, "y" : 20, "text" : uiScriptLocale.GUILD_WATER, "text_horizontal_align" : "center", },
				{ "name" : "ResourceName4", "type" : "text", "x" : RESOURCE_NAME_POS + 29*3, "y" : 20, "text" : uiScriptLocale.GUILD_CRYSTAL, "text_horizontal_align" : "center", },
				{ "name" : "ResourceName5", "type" : "text", "x" : RESOURCE_NAME_POS + 29*4, "y" : 20, "text" : uiScriptLocale.GUILD_MINENAL, "text_horizontal_align" : "center", },
				{ "name" : "ResourceName6", "type" : "text", "x" : RESOURCE_NAME_POS + 29*5, "y" : 20, "text" : uiScriptLocale.GUILD_GEM, "text_horizontal_align" : "center", },

				## Power
				{
					"name" : "Power", "type" : "text", "x" : 303, "y" : 20, "text" : uiScriptLocale.GUILD_BUILDING_OPERATE,
				},

			),
		},

		## Buttons
		{
			"name" : "RefreshButton",
			"type" : "button",
			"x" : 337,
			"y" : 5,
			"default_image" : "d:/ymir work/ui/game/guild/Refresh_Button_01.sub",
			"over_image" : "d:/ymir work/ui/game/guild/Refresh_Button_02.sub",
			"down_image" : "d:/ymir work/ui/game/guild/Refresh_Button_03.sub",
			"tooltip_text" : uiScriptLocale.GUILD_BUILDING_REFRESH,
		},

	),
}
