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

# Maximum strength value for each grade and step of refinement
# table(GRADE, STEP) = max strength.
default_strength_max_table = [
	[2, 2, 3, 3, 4],
	[3, 3, 3, 4, 4],
	[4, 4, 4, 4, 4],
	[4, 4, 4, 4, 5],
	[4, 4, 4, 5, 6],
]

# For the current plan, strength enhancement is excluded, and enhancement fee is not determined yet,
# so it is not added to dragon_soul_refine_info.
# (Even if enhancement data exists, we want to be able to exclude it if needed)
# If you want to set different enhancement fees for different dragon soul types in other servers,
# and if you want different enhancement fees for each dragon soul type,
# you need to modify the client code.
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

