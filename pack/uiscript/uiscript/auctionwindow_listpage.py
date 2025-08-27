SEARCHING_AREA_X_POS = 15
SEARCHING_AREA_Y_POS = 235

window = {
	"name" : "AuctionWindow_RegisterPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		{
			"name" : "NumberPrint",
			"type" : "text",
			"x" : 18,
			"y" : 7,
			"text" : "번호",
		},
		{
			"name" : "NamePrint",
			"type" : "text",
			"x" : 79,
			"y" : 7,
			"text" : "아이템 이름",
		},
		{
			"name" : "NamePrint",
			"type" : "text",
			"x" : 228,
			"y" : 7,
			"text" : "가격",
		},

		{
			"name" : "ItemSearchAreaBar",
			"type" : "horizontalbar",

			"x" : 0,
			"y" : 235,
			"width" : 330,
			"horizontal_align" : "center",
			"children" :
			(

				{
					"name" : "ItemSearchAreaBarPrint",
					"type" : "text",
					"x" : 0,
					"y" : 0,
					"text" : "아이템 검색하기",
					"all_align" : "center",
				},

			),
		},

		{
			"name" : "SearchingNamePrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 5,
			"y" : SEARCHING_AREA_Y_POS + 24,
			"text" : "아이템이름",
		},
		{
			"name" : "SearchingNameSlot",
			"type" : "image",
			"x" : SEARCHING_AREA_X_POS + 68,
			"y" : SEARCHING_AREA_Y_POS + 22,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",
		},

		{
			"name" : "SearchingIDPrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 5,
			"y" : SEARCHING_AREA_Y_POS + 44,
			"text" : "번호로찾기",
		},
		{
			"name" : "SearchingIDSlot",
			"type" : "image",
			"x" : SEARCHING_AREA_X_POS + 68,
			"y" : SEARCHING_AREA_Y_POS + 42,
			"image" : "d:/ymir work/ui/public/Parameter_Slot_04.sub",
		},

		{
			"name" : "SearchingIDPrint",
			"type" : "text",
			"x" : SEARCHING_AREA_X_POS + 205,
			"y" : SEARCHING_AREA_Y_POS + 24,
			"text" : "소켓여부",
		},

		{
			"name" : "SearchingButtonByName",
			"type" : "button",
			"x" : SEARCHING_AREA_X_POS + 295,
			"y" : SEARCHING_AREA_Y_POS + 20,
			"text" : "찾기",
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "SearchingButtonByID",
			"type" : "button",
			"x" : SEARCHING_AREA_X_POS + 295,
			"y" : SEARCHING_AREA_Y_POS + 40,
			"text" : "찾기",
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

	),
}
