window = {
	"name" : "AuctionWindow_RegisterPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		{
			"name" : "ItemSlot",
			"type" : "slotbar",
			"x" : 0,
			"y" : 30,
			"width" : 97,
			"height" : 97,
			"horizontal_align" : "center",
			"text_horizontal_align" : "center",

			"children" :
			(
				{
					"name" : "TemporaryImage",
					"type" : "image",
					"x" : 0,
					"y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "d:/ymir work/ui/items/weapon/03100.sub",
				},
			),

		},

		{
			"name" : "ItemName",
			"type" : "text",
			"x" : 0,
			"y" : 150,
			"horizontal_align" : "center",
			"text_horizontal_align" : "center",
			"text" : "아이템을 이곳에 드래그하여 넣어주세요",
		},

		{
			"name" : "LowerSellingPriceName",
			"type" : "text",
			"x" : 70,
			"y" : 185,
			"text" : "매매 최저가",
		},
		{
			"name" : "LowerSellingPriceSlot",
			"type" : "image",
			"x" : 150,
			"y" : 185 - 3,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
			"children" :
			(
				{
					"name" : "LowerSellingPriceValue",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "123456789123456789",
				},
			),
		},

		{
			"name" : "AverageSellingPriceName",
			"type" : "text",
			"x" : 70,
			"y" : 205,
			"text" : "매매 평균가",
		},
		{
			"name" : "AverageSellingPriceSlot",
			"type" : "image",
			"x" : 150,
			"y" : 205 - 3,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
			"children" :
			(
				{
					"name" : "AverageSellingPriceValue",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"all_align" : "center",
					"text" : "123456789123456789",
				},
			),
		},

		{
			"name" : "InputPriceSlot",
			"type" : "image",
			"x" : 90,
			"y" : 250 - 3,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
			"children" :
			(
				{
					"name" : "InputPriceValue",
					"type" : "text",
					"x" : 0,
					"y" : 1,
					"all_align" : "center",
					"text" : "123456789123456789",
				},
			),
		},

		{
			"name" : "RegisterButton",
			"type" : "button",

			"x" : 230,
			"y" : 250 - 3,

			"text" : "등록",

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

	),
}
