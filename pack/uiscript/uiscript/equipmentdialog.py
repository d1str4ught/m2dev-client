import uiScriptLocale

window = {
	"name" : "EquipmentDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 180,
	"height" : 230,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 180,
			"height" : 230,

			"title" : "Character Name",

			"children" :
			(
				{
					"name":"EquipmentBaseImage",
					"type":"image",
					"style" : ("attach",),

					"x" : 0,
					"y" : 9,
					"horizontal_align" : "center",
					"vertical_align" : "center",

					"image" : "d:/ymir work/ui/equipment_bg_without_ring.tga",

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 150,
							"height" : 182,

							"slot" : (
										{"index":0, "x":39, "y":37, "width":32, "height":64},
										{"index":1, "x":39, "y":2, "width":32, "height":32},
										{"index":2, "x":39, "y":145, "width":32, "height":32},
										{"index":3, "x":75, "y":67, "width":32, "height":32},
										{"index":4, "x":3, "y":3, "width":32, "height":96},
										{"index":5, "x":114, "y":67, "width":32, "height":32},
										{"index":6, "x":114, "y":35, "width":32, "height":32},
										{"index":7, "x":2, "y":145, "width":32, "height":32},
										{"index":8, "x":75, "y":145, "width":32, "height":32},
										{"index":9, "x":114, "y":2, "width":32, "height":32},
										{"index":10, "x":75, "y":35, "width":32, "height":32},
										## 새 반지1
										##{"index":21, "x":2, "y":106, "width":32, "height":32},
										## 새 반지2
										##{"index":22, "x":75, "y":106, "width":32, "height":32},
										## 새 벨트
										{"index":23, "x":39, "y":106, "width":32, "height":32},
									),
						},

					),

				},
			),
		},
	),
}
