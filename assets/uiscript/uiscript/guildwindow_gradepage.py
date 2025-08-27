import uiScriptLocale

window = {
	"name" : "GuildWindow_BoardPage",

	"x" : 8,
	"y" : 30,

	"width" : 360,
	"height" : 298,

	"children" :
	(

		## GradeNumber
		{
			"name" : "GradeNumber", "type" : "text", "x" : 21, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_NUM,
		},
		## GradeName
		{
			"name" : "GradeName", "type" : "text", "x" : 76, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_RANK,
		},
		## InviteAuthority
		{
			"name" : "InviteAuthority", "type" : "text", "x" : 126, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_JOIN,
		},
		## DriveOutAuthority
		{
			"name" : "DriveOutAuthority", "type" : "text", "x" : 183, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_DELETE,
		},
		## NoticeAuthority
		{
			"name" : "NoticeAuthority", "type" : "text", "x" : 240, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_NOTICE,
		},
		## GeneralAuthority
		{
			"name" : "SkillAuthority", "type" : "text", "x" : 297, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_SKILL,
		},

	),
}
