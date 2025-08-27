import uiScriptLocale

ROOT = "d:/ymir work/ui/game/taskbar/"

window = {
	"name" : "RightButtonWindow",

	"x" : 0,
	"y" : 0,

	"width" : 32 * 2,
	"height" : 32,

	"children" :
	(
		{
			"name" : "button_move_and_attack",
			"type" : "button",

			"x" : 0,
			"y" : 0,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_ATTACK,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : ROOT + "Mouse_Button_Attack_01.sub",
			"over_image" : ROOT + "Mouse_Button_Attack_02.sub",
			"down_image" : ROOT + "Mouse_Button_Attack_03.sub",
		},
		{
			"name" : "button_camera",
			"type" : "button",

			"x" : 32,
			"y" : 0,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_CAMERA,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : ROOT + "Mouse_Button_Camera_01.sub",
			"over_image" : ROOT + "Mouse_Button_Camera_02.sub",
			"down_image" : ROOT + "Mouse_Button_Camera_03.sub",
		},
		{
			"name" : "button_skill",
			"type" : "button",

			"x" : 64,
			"y" : 0,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_SKILL,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : ROOT + "Mouse_Button_Skill_01.sub",
			"over_image" : ROOT + "Mouse_Button_Skill_02.sub",
			"down_image" : ROOT + "Mouse_Button_Skill_03.sub",
		},
	),
}