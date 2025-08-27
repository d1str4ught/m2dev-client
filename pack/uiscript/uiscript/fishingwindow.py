FISHING_PATH = "d:/ymir work/ui/game/fishing/"

window = {
	"name" : "FishingWindow",
	"style" : ("movable", "float",),

	"x" : 100,
	"y" : 100,

	"width" : 150,
	"height" : 195,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,
			"width" : 150,
			"height" : 195,
			"title" : "≥¨Ω√",

			"children" :
			(

				{
					"name" : "FishingBox1",
					"type" : "box",

					"x" : 9,
					"y" : 31,
					"width" : 131,
					"height" : 131,

					"color" : 0xFF6C6359,
				},

				{
					"name" : "FishingBox2",
					"type" : "box",

					"x" : 10,
					"y" : 32,
					"width" : 129,
					"height" : 129,

					"color" : 0xFF35302D,
				},

				{
					"name" : "Water",
					"type" : "ani_image",

					"x" : 0,
					"y" : 33,
					"width" : 128,
					"height" : 128,
					"horizontal_align" : "center",

					"delay" : 7,

					"images" :
					(
						FISHING_PATH + "water/00.dds",
						FISHING_PATH + "water/01.dds",
						FISHING_PATH + "water/02.dds",
						FISHING_PATH + "water/03.dds",
						FISHING_PATH + "water/04.dds",
						FISHING_PATH + "water/05.dds",
						FISHING_PATH + "water/06.dds",
					),

					"children" :
					(

						{
							"name" : "FishName",
							"type" : "text",

							"x" : 10,
							"y" : 10,

							"text" : "π∞∞Ì±‚ ¿Ã∏ß",
						},

						{
							"name" : "Float_Wait",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,
							"width" : 32,
							"height" : 128,
							"horizontal_align" : "center",

							"delay" : 5,

							"images" :
							(
								FISHING_PATH + "float_wait/fh_wait00.tga",
								FISHING_PATH + "float_wait/fh_wait01.tga",
								FISHING_PATH + "float_wait/fh_wait02.tga",
								FISHING_PATH + "float_wait/fh_wait03.tga",
								FISHING_PATH + "float_wait/fh_wait04.tga",
								FISHING_PATH + "float_wait/fh_wait05.tga",
								FISHING_PATH + "float_wait/fh_wait06.tga",
								FISHING_PATH + "float_wait/fh_wait07.tga",
								FISHING_PATH + "float_wait/fh_wait08.tga",
								FISHING_PATH + "float_wait/fh_wait09.tga",
								FISHING_PATH + "float_wait/fh_wait10.tga",
							),
						},

						{
							"name" : "Float_Throw",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,
							"width" : 128,
							"height" : 128,
							"horizontal_align" : "center",

							"delay" : 5,

							"images" :
							(
								FISHING_PATH + "float_throw/fh_fall00.tga",
								FISHING_PATH + "float_throw/fh_fall01.tga",
								FISHING_PATH + "float_throw/fh_fall02.tga",
								FISHING_PATH + "float_throw/fh_fall03.tga",
								FISHING_PATH + "float_throw/fh_fall04.tga",
								FISHING_PATH + "float_throw/fh_fall05.tga",
								FISHING_PATH + "float_throw/fh_fall06.tga",
								FISHING_PATH + "float_throw/fh_fall07.tga",
								FISHING_PATH + "float_throw/fh_fall08.tga",
								FISHING_PATH + "float_throw/fh_fall09.tga",
								FISHING_PATH + "float_throw/fh_fall10.tga",
								FISHING_PATH + "float_throw/fh_fall11.tga",
								FISHING_PATH + "float_throw/fh_fall12.tga",
								FISHING_PATH + "float_throw/fh_fall13.tga",
							),
						},

						{
							"name" : "Float_React",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,
							"width" : 64,
							"height" : 128,
							"horizontal_align" : "center",

							"delay" : 5,

							"images" :
							(
								FISHING_PATH + "float_react/fh_bite00.tga",
								FISHING_PATH + "float_react/fh_bite01.tga",
								FISHING_PATH + "float_react/fh_bite02.tga",
								FISHING_PATH + "float_react/fh_bite03.tga",
								FISHING_PATH + "float_react/fh_bite04.tga",
								FISHING_PATH + "float_react/fh_bite05.tga",
								FISHING_PATH + "float_react/fh_bite06.tga",
								FISHING_PATH + "float_react/fh_bite07.tga",
								FISHING_PATH + "float_react/fh_bite08.tga",
								FISHING_PATH + "float_react/fh_bite09.tga",
								FISHING_PATH + "float_react/fh_bite10.tga",
								FISHING_PATH + "float_react/fh_bite11.tga",
								FISHING_PATH + "float_react/fh_bite12.tga",
								FISHING_PATH + "float_react/fh_bite13.tga",
							),
						},

						{
							"name" : "Float_Catch",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,
							"width" : 128,
							"height" : 128,
							"horizontal_align" : "center",

							"delay" : 5,

							"images" :
							(
								FISHING_PATH + "float_catch/fh_catch00.tga",
								FISHING_PATH + "float_catch/fh_catch01.tga",
								FISHING_PATH + "float_catch/fh_catch02.tga",
								FISHING_PATH + "float_catch/fh_catch03.tga",
								FISHING_PATH + "float_catch/fh_catch04.tga",
								FISHING_PATH + "float_catch/fh_catch05.tga",
								FISHING_PATH + "float_catch/fh_catch06.tga",
								FISHING_PATH + "float_catch/fh_catch07.tga",
								FISHING_PATH + "float_catch/fh_catch08.tga",
								FISHING_PATH + "float_catch/fh_catch09.tga",
								FISHING_PATH + "float_catch/fh_catch10.tga",
								FISHING_PATH + "float_catch/fh_catch11.tga",
							),
						},

					),

				},

				{
					"name" : "FishingButton",
					"type" : "button",

					"x" : 0,
					"y" : 30,

					"text" : "≥¨Ω√",
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",
				},

			),
		},
	),
}