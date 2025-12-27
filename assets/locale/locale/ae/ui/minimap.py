ROOT = "d:/ymir work/ui/minimap/"
MOVE_X = 10

window = {
	"name" : "MiniMap",

	"x" : SCREEN_WIDTH - 136 - MOVE_X,
	"y" : 0,

	"width" : 136 + MOVE_X,
	"height" : 137,

	"children" :
	[
		## OpenWindow
		{
			"name" : "OpenWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 136 + MOVE_X,
			"height" : 137,

			"children" :
			[
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : 0 + MOVE_X,
					"y" : 0,
					"image" : ROOT + "minimap.sub",
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

					"x" : 6 + MOVE_X,
					"y" : 6,

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
			],
		},
		{
			"name" : "CloseWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 132 + MOVE_X,
			"height" : 48,

			"children" :
			[
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
			],
		},
	],
}
window["children"][0]["children"] = window["children"][0]["children"] + [
				## BattleButton
				{
					"name" : "BattleButton",
					"type" : "button",

					"x" : 6 + MOVE_X,
					"y" : 105,

					"default_image" : ROOT + "battle_open_default.tga",
					"over_image" : ROOT + "battle_open_over.tga",
					"down_image" : ROOT + "battle_open_down.tga",
				},]


window["children"][0]["children"] = window["children"][0]["children"] + [
				## Party Match
				{
					"name" : "PartyMatchButton",
					"type" : "button",

					"x" : -10 + MOVE_X,
					"y" : 85,

					"default_image" : ROOT + "party_match/0.sub",
					"over_image" : ROOT + "party_match/0.sub",
					"down_image" : ROOT + "party_match/0.sub",
				},
				{
					"name" : "PartyMatchEffect",
					"type" : "ani_image",
					
					"x" : 17 + MOVE_X,
					"y" : 85,
					
					"delay" : 6,

					"images" :
					(
						ROOT + "party_match/0.sub",
						ROOT + "party_match/1.sub",
						ROOT + "party_match/2.sub",
						ROOT + "party_match/3.sub",
						ROOT + "party_match/4.sub",
						ROOT + "party_match/5.sub",
						ROOT + "party_match/6.sub",
						ROOT + "party_match/7.sub",
						ROOT + "party_match/7.sub",
						ROOT + "party_match/6.sub",
						ROOT + "party_match/5.sub",
						ROOT + "party_match/4.sub",
						ROOT + "party_match/3.sub",
						ROOT + "party_match/2.sub",
						ROOT + "party_match/1.sub",
						ROOT + "party_match/0.sub",
					),
				},]

window["children"][0]["children"] = window["children"][0]["children"] + [
			## GuildDragonlairFirstGuildText
			{
				"name" : "GuildDragonlairFirstGuildText",
				"type" : "text",
				
				"text_horizontal_align" : "center",

				"outline" : 1,

				"x" : 60 + MOVE_X,
				"y" : 160,

				"text" : "1st",
			},
			## GuildDragonlairFirstGuildSecond
			{
				"name" : "GuildDragonlairFirstGuildSecond",
				"type" : "text",
				
				"text_horizontal_align" : "center",

				"outline" : 1,

				"x" : 100 + MOVE_X,
				"y" : 160,

				"text" : "None",
			},]


window["children"][0]["children"][5]["x"] = 0
window["children"][0]["children"][5]["y"] = 57

window["children"][0]["children"] = window["children"][0]["children"] + [
				## MailBox
				{
					"name" : "MailBoxButton",
					"type" : "button",

					"x" : 126,
					"y" : 30,

					"default_image" : "d:/ymir work/ui/game/mailbox/post_minimap.sub",
					"over_image" : "d:/ymir work/ui/game/mailbox/post_minimap.sub",
					"down_image" : "d:/ymir work/ui/game/mailbox/post_minimap.sub",
				},
				{
					"name" : "MailBoxEffect",
					"type" : "ani_image",
					
					"x" : 126,
					"y" : 30,
					
					"delay" : 6,

					"images" :
					(
						"d:/ymir work/ui/game/mailbox/minimap_flash/2.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/3.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/4.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/5.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/4.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/3.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/2.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/1.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/1.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/1.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/1.sub",
						"d:/ymir work/ui/game/mailbox/minimap_flash/1.sub",
					),
				},]
				
window["children"][0]["children"] = window["children"][0]["children"] + [
				## InGameEventButton
				{
					"name" : "InGameEventButton",
					"type" : "button",

					"x" : 2,
					"y" : 28,

					"default_image" : "d:/ymir work/ui/minimap/E_open_default.tga",
					"over_image" : "d:/ymir work/ui/minimap/E_open_over.tga",
					"down_image" : "d:/ymir work/ui/minimap/E_open_down.tga",
				},]
					

window["children"][0]["children"] = window["children"][0]["children"] + [
			{
				"name" : "ClientTimerText",
				"type" : "text",
				
				"text_horizontal_align" : "center",

				"outline" : 1,

				"x" : 80 + MOVE_X,
				"y" : 160,
			},]
				