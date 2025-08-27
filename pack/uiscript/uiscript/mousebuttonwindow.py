import uiScriptLocale

ROOT = "d:/ymir work/ui/game/taskbar/"

window = {
	"name" : "ButtonWindow",

	"x" : 0,
	"y" : 0,

	"width" : 32,
	"height" : 32 * 3,

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
			"name" : "button_auto_attack",
			"type" : "button",

			"x" : 0,
			"y" : 32,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_AUTO_ATTACK,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : ROOT + "Mouse_Button_Auto_Attack_01.sub",
			"over_image" : ROOT + "Mouse_Button_Auto_Attack_02.sub",
			"down_image" : ROOT + "Mouse_Button_Auto_Attack_03.sub",
		},
		{
			"name" : "button_camera",
			"type" : "button",

			"x" : 0,
			"y" : 64,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_CAMERA,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : ROOT + "Mouse_Button_Camera_01.sub",
			"over_image" : ROOT + "Mouse_Button_Camera_02.sub",
			"down_image" : ROOT + "Mouse_Button_Camera_03.sub",
		},
	),
}