import uiScriptLocale

BOARD_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_06.sub"

window = {
	"name" : "GuildWindow_BoardPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		## ID
		{
			"name" : "IndexID", "type" : "text", "x" : 42, "y" : 8, "text" : uiScriptLocale.GUILD_BOARD_ID,
		},
		## Messages
		{
			"name" : "IndexMessages", "type" : "text", "x" : 212, "y" : 8, "text" : uiScriptLocale.GUILD_BOARD_TEXT,
		},

		## Refresh Button
		{
			"name" : "RefreshButton",
			"type" : "button",
			"x" : 337,
			"y" : 5,
			"default_image" : "d:/ymir work/ui/game/guild/Refresh_Button_01.sub",
			"over_image" : "d:/ymir work/ui/game/guild/Refresh_Button_02.sub",
			"down_image" : "d:/ymir work/ui/game/guild/Refresh_Button_03.sub",
			"tooltip_text" : uiScriptLocale.GUILD_BOARD_REFRESH,
		},

		## Post Comment Button
		{
			"name" : "PostCommentButton",
			"type" : "button",
			"x" : 337,
			"y" : 273,
			"default_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_01.sub",
			"over_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_02.sub",
			"down_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_03.sub",
			"tooltip_text" : uiScriptLocale.GUILD_GRADE_WRITE,
		},

		## EditLine
		{
			"name" : "CommentSlot",
			"type" : "slotbar",
			"x" : 15,
			"y" : 272,
			"width" : 315,
			"height" : 18,

			"children" :
			(
				{
					"name" : "CommentValue",
					"type" : "editline",
					"x" : 2,
					"y" : 3,
					"width" : 317,
					"height" : 15,
					"input_limit" : 49,
					"text" : "",
				},
			),
		},

	),
}
