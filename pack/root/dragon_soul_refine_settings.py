import item

# default_grade_need_count = [3, 3, 3, 3]
default_grade_need_count = [15, 10, 5, 3]
default_grade_fee = [30000, 50000, 70000, 100000]
default_step_need_count = [4, 3, 2, 1]
default_step_fee = [20000, 30000, 40000, 50000]

strength_fee = {
	item.MATERIAL_DS_REFINE_NORMAL : 10000,
	item.MATERIAL_DS_REFINE_BLESSED : 20000,
	item.MATERIAL_DS_REFINE_HOLLY : 30000,
}

# 강화가 어느 단계 까지 가능 한지
# table(GRADE, STEP) = max strength.
default_strength_max_table = [
	[2, 2, 3, 3, 4],
	[3, 3, 3, 4, 4],
	[4, 4, 4, 4, 4],
	[4, 4, 4, 4, 5],
	[4, 4, 4, 5, 6],
]

# 일단 기획적으로는 strength 강화의 경우, 강화석에 의해 fee가 셋팅되기 때문에,
# dragon_soul_refine_info에 넣지 않았다.
# (강화석만 넣어도 얼마 필요한지 보일 수 있도록 하기 위해)
# 다만 서버에서는 용혼석 타입 별로 강화석 fee를 셋팅할 수 있도록 해놨기 때문에,
# 만일 용혼석 별로 강화석 fee를 다르게 하고 싶다면,
# 클라 코드를 수정해야할 것이다.
default_refine_info = {
	"grade_need_count" : default_grade_need_count,
	"grade_fee" : default_grade_fee,
	"step_need_count" : default_step_need_count,
	"step_fee" : default_step_fee,
	"strength_max_table" : default_strength_max_table,
}

dragon_soul_refine_info = {
	11 : default_refine_info,
	12 : default_refine_info,
	13 : default_refine_info,
	14 : default_refine_info,
	15 : default_refine_info,
	16 : default_refine_info,
}

