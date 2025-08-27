import app
import ui
import uiScriptLocale
import localeInfo

LOCALE_PATH = uiScriptLocale.MAPNAME_PATH

class MapNameShower(ui.ExpandedImageBox):

	MAP_NAME_IMAGE =	{}

	STATE_HIDE = 0
	STATE_FADE_IN = 1
	STATE_SHOW = 2
	STATE_FADE_OUT = 3

	def __init__(self):
		if localeInfo.IsARABIC():
			self.MAP_NAME_IMAGE =	{
							"metin2_map_a1"  : LOCALE_PATH+"a1.tga",
							"map_a2"         : LOCALE_PATH+"a2.tga",
							"season2/metin2_map_a2_1": LOCALE_PATH+"a2_2.tga",
							"metin2_map_a3"  : LOCALE_PATH+"a3.tga",
							"metin2_map_b1"  : LOCALE_PATH+"b1.tga",
							"map_b2"         : LOCALE_PATH+"b2.tga",
							"metin2_map_b3"  : LOCALE_PATH+"b3.tga",
							"metin2_map_c1"  : LOCALE_PATH+"c1.tga",
							"map_c2"         : LOCALE_PATH+"c2.tga",
							"metin2_map_c3"  : LOCALE_PATH+"c3.tga",
							"metin2_map_deviltower1" : LOCALE_PATH+"devil1_title.tga",
							"metin2_map_n_desert_01" : LOCALE_PATH+"desert1.tga",
							"season2/metin2_map_n_desert_02": LOCALE_PATH+"desert2.tga",
							"metin2_map_n_flame_01" : LOCALE_PATH+"frame1.tga",
							"season2/metin2_map_n_flame_02": LOCALE_PATH+"frame2.tga",
							"metin2_map_milgyo" : LOCALE_PATH+"milgyo.tga",
							"season2/metin2_map_milgyo_a": LOCALE_PATH+"milgyo2.TGA",
							"metin2_map_monkeydungeon" : LOCALE_PATH+"monkey1.tga",
							"metin2_map_monkeydungeon_02" : LOCALE_PATH+"monkey2.tga",
							"metin2_map_monkeydungeon_03" : LOCALE_PATH+"monkey3.tga",
							"metin2_map_guild_01" : LOCALE_PATH+"guild1.tga",
							"metin2_map_guild_02" : LOCALE_PATH+"guild2.tga",
							"metin2_map_guild_03" : LOCALE_PATH+"guild3.tga",
							"season2/metin2_map_skipia_dungeon_01": LOCALE_PATH+"skipia.tga",
							"season2/metin2_map_skipia_dungeon_02": LOCALE_PATH+"skipia.tga",
							"map_n_snowm_01" : LOCALE_PATH+"snow1.tga",
							"season2/map_n_snowm_02": LOCALE_PATH+"snow2.tga",
							"metin2_map_spiderdungeon" : LOCALE_PATH+"spider1.tga",
							"metin2_map_trent" : LOCALE_PATH+"trent.tga",
							"metin2_map_trent02" : LOCALE_PATH+"trent02.tga",
							"season2/metin2_map_trent_a": LOCALE_PATH+"trent_a.tga",
							"season2/metin2_map_trent02_a": LOCALE_PATH+"trent02_a.tga",
							"metin2_map_dd"	:	LOCALE_PATH+"devil_basement.tga",
							"metin2_map_devilsCatacomb"	:	LOCALE_PATH+"devil_basement.tga",
							"metin2_map_dd"	:	LOCALE_PATH+"devil_basement.tga",
							"season1/metin2_map_WL_01" :	LOCALE_PATH+"wl.tga",
							"season1/metin2_map_nusluck01":	LOCALE_PATH+"nusluck.tga",	
						}
		else:
			self.MAP_NAME_IMAGE =	{
							"metin2_map_a1"  : LOCALE_PATH+"a1.tga",
							"map_a2"         : LOCALE_PATH+"a2.tga",
							"metin2_map_a3"  : LOCALE_PATH+"a3.tga",
							"metin2_map_b1"  : LOCALE_PATH+"b1.tga",
							"map_b2"         : LOCALE_PATH+"b2.tga",
							"metin2_map_b3"  : LOCALE_PATH+"b3.tga",
							"metin2_map_c1"  : LOCALE_PATH+"c1.tga",
							"map_c2"         : LOCALE_PATH+"c2.tga",
							"metin2_map_c3"  : LOCALE_PATH+"c3.tga",
							"map_n_snowm_01" : LOCALE_PATH+"snow1.tga",
							"metin2_map_deviltower1" : LOCALE_PATH+"devil1_title.tga",
							"metin2_map_n_flame_01" : LOCALE_PATH+"frame1.tga",
							"metin2_map_n_desert_01" : LOCALE_PATH+"desert1.tga",
							"metin2_map_milgyo" : LOCALE_PATH+"milgyo.tga",
							"metin2_map_monkeydungeon" : LOCALE_PATH+"monkey1.tga",
							"metin2_map_monkeydungeon_02" : LOCALE_PATH+"monkey2.tga",
							"metin2_map_monkeydungeon_03" : LOCALE_PATH+"monkey3.tga",
							"metin2_map_guild_01" : LOCALE_PATH+"guild1.tga",
							"metin2_map_guild_02" : LOCALE_PATH+"guild2.tga",
							"metin2_map_guild_03" : LOCALE_PATH+"guild3.tga",
							"metin2_map_trent" : LOCALE_PATH+"trent.tga",
							"metin2_map_trent02" : LOCALE_PATH+"trent02.tga",
							"season2/map_n_snowm_02": LOCALE_PATH+"snow2.tga",
							"season2/metin2_map_a2_1": LOCALE_PATH+"a2_2.tga",
							"season2/metin2_map_n_desert_02": LOCALE_PATH+"desert2.tga",
							"season2/metin2_map_n_flame_02": LOCALE_PATH+"frame2.tga",
							"season2/metin2_map_milgyo_a": LOCALE_PATH+"milgyo2.TGA",
							"season2/metin2_map_trent_a": LOCALE_PATH+"trent_a.tga",
							"season2/metin2_map_trent02_a": LOCALE_PATH+"trent02_a.tga",
							"season2/metin2_map_skipia_dungeon_01": LOCALE_PATH+"skipia.tga",
							"season2/metin2_map_skipia_dungeon_02": LOCALE_PATH+"skipia.tga",
							"metin2_map_devilsCatacomb"	:	LOCALE_PATH+"devil_basement.tga",
							"metin2_guild_village_01"	:	LOCALE_PATH+"a4.tga",
							"metin2_guild_village_02"	:	LOCALE_PATH+"b4.tga",
							"metin2_guild_village_03"	:	LOCALE_PATH+"c4.tga",
							"metin2_map_BayBlackSand"	:	LOCALE_PATH+"bay.tga",
							"metin2_map_Mt_Thunder"		:	LOCALE_PATH+"thunder.tga",
							"metin2_map_dawnmistwood"	:	LOCALE_PATH+"dawn.tga",
							"Metin2_map_CapeDragonHead"	:	LOCALE_PATH+"cape.tga",
							"metin2_map_spiderdungeon"	:	LOCALE_PATH+"spider1.tga",
							"metin2_map_spiderdungeon_02"	:	LOCALE_PATH+"spider1.tga",
							"metin2_map_spiderdungeon_03"		:	LOCALE_PATH+"spider1.tga",
						}

		ui.ExpandedImageBox.__init__(self, "TOP_MOST")
		self.AddFlag("not_pick")
		self.__Initialize()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def __Initialize(self):
		self.floorImage = None
		self.objectiveImage = None
		self.fadeStartTime = 0
		self.state = self.STATE_HIDE
		self.curAlpha = 0.0
		self.SetAlpha(0.0)
		self.SetWindowHorizontalAlignCenter()
		self.SetPosition(0, 80)
		self.Hide()

	def __GetDevilTowerFloor(self, x, y):
		if x > 10000 and y > 58000 and x < 25000 and y < 72000:
			return 1
		elif x > 10000 and y > 35000 and x < 25000 and y < 50000:
			return 2
		elif x > 10000 and y > 10000 and x < 25000 and y < 25000:
			return 3
		elif x > 35000 and y > 61000 and x < 43500 and y < 70500:
			return 4
		elif x > 35000 and y > 38000 and x < 43500 and y < 48000:
			return 5
		elif x > 14000 and y > 14000 and x < 43500 and y < 24500:
			return 6
		elif x > 56000 and y > 60000 and x < 68000 and y < 73000:
			return 7
		elif x > 56000 and y > 38000 and x < 68000 and y < 49000:
			return 8
		elif x > 56000 and y > 13000 and x < 68000 and y < 23000:
			return 9	 
		return 0
	def __GetDevilBase(self, x, y):
		if x > 3000 and y > 4500 and x < 45000 and y < 45000:
			return 1
		elif x > 54000 and y > 3900 and x < 100000 and y < 46200:
			return 2
		elif x > 104800 and y > 3500 and x < 145500 and y < 45800:
			return 3
		elif x > 3100 and y > 54100 and x < 56400 and y < 105800:
			return 4
		elif x > 65000 and y > 54000 and x < 105000 and y < 95500:
			return 5
		elif x > 117500 and y > 57600 and x < 142000 and y < 81000:
			return 6
		elif x > 5000 and y > 104900 and x < 15000 and y < 122000:
			return 7
		return	0
	def ShowMapName(self, mapName, x, y):
		if not self.MAP_NAME_IMAGE.has_key(mapName):
			print " [ERROR] - There is no map name image", mapName
			return

		try:
			self.LoadImage(self.MAP_NAME_IMAGE[mapName])
		except RuntimeError:
			return

		self.__Initialize()

		if mapName == "metin2_map_deviltower1":
			self.SetPosition(-60, 80)

			self.floorImage = ui.ExpandedImageBox()
			self.floorImage.AddFlag("not_pick")
			self.floorImage.SetWindowHorizontalAlignCenter()
			self.floorImage.SetPosition(100, 80)
			self.floorImage.SetAlpha(0.0)
			self.floorImage.Show()
			# 맵이름 (ex: 아귀동굴) 이미지 로딩 & 표시			
			try:
				floor = self.__GetDevilTowerFloor(x, y)
				print x, y, floor
				self.floorImage.LoadImage(LOCALE_PATH+"devil1_%df.tga" % floor)
			except RuntimeError:
				self.SetPosition(0, 80)
				self.floorImage.Hide()
				self.floorImage = None
							
			if localeInfo.IsYMIR() or localeInfo.IsWE_KOREA():	
				self.objectiveImage = ui.ExpandedImageBox()
				self.objectiveImage.AddFlag("not_pick")
				self.objectiveImage.SetWindowHorizontalAlignCenter()
				self.objectiveImage.SetPosition(0, 200)
				self.objectiveImage.SetAlpha(0.0)
				self.objectiveImage.Show()
			
				# 층별 목표 이미지 로딩 & 표시
				# 던전은 현재 몇층인지 알아오는 부분 때문에 하드코딩을 피하기가 힘들다...
				try:
					floor = self.__GetDevilTowerFloor(x, y)
					print x, y, floor
					self.objectiveImage.LoadImage(LOCALE_PATH + mapName + "/obj_%02df.tga" % floor)
				except RuntimeError:
					self.SetPosition(0, 80)
					self.objectiveImage.Hide()
					self.objectiveImage = None
				
		if mapName == "metin2_map_devilsCatacomb":
			self.SetPosition(-75, 80)

			self.floorImage = ui.ExpandedImageBox()
			self.floorImage.AddFlag("not_pick")
			self.floorImage.SetWindowHorizontalAlignCenter()
			self.floorImage.SetPosition(100, 80)
			self.floorImage.SetAlpha(0.0)
			self.floorImage.Show()

			# 맵이름 (ex: 아귀동굴) 이미지 로딩 & 표시
			try:
				floor = self.__GetDevilBase(x, y)
				print x, y, floor
				self.floorImage.LoadImage(LOCALE_PATH+"devil1_%df.tga" % floor)
			except RuntimeError:
				self.SetPosition(0, 80)
				self.floorImage.Hide()
				self.floorImage = None
			if localeInfo.IsYMIR() or localeInfo.IsWE_KOREA():	
				self.objectiveImage = ui.ExpandedImageBox()
				self.objectiveImage.AddFlag("not_pick")
				self.objectiveImage.SetWindowHorizontalAlignCenter()
				self.objectiveImage.SetPosition(0, 200)
				self.objectiveImage.SetAlpha(0.0)
				self.objectiveImage.Show()
				

				# 층별 목표 이미지 로딩 & 표시
				# 던전은 현재 몇층인지 알아오는 부분 때문에 하드코딩을 피하기가 힘들다...
				try:
					floor = self.__GetDevilBase(x, y)
					print x, y, floor
					self.objectiveImage.LoadImage(LOCALE_PATH + mapName + "/obj_%02df.tga" % floor)
				except RuntimeError:
					self.SetPosition(0, 80)
					self.objectiveImage.Hide()
					self.objectiveImage = None
								
		self.state = self.STATE_FADE_IN
		self.fadeStartTime = app.GetTime() + 1.0
		self.Show()

	def Update(self):

		self.SetAlpha(self.curAlpha)
		if self.floorImage:
			self.floorImage.SetAlpha(self.curAlpha)

		if self.objectiveImage:
			self.objectiveImage.SetAlpha(self.curAlpha)

		if self.STATE_FADE_IN == self.state:
			if app.GetTime() > self.fadeStartTime:
				self.curAlpha += 0.05

				if self.curAlpha > 0.9:
					self.state = self.STATE_SHOW
					self.fadeStartTime = app.GetTime() + 5.0

		elif self.STATE_SHOW == self.state:
			if app.GetTime() > self.fadeStartTime:
				self.state = self.STATE_FADE_OUT

		elif self.STATE_FADE_OUT == self.state:
			self.curAlpha -= 0.05

			if self.curAlpha < 0.0001:
				self.Hide()
				if self.floorImage:
					self.floorImage.Hide()
					self.floorImage = None
					
				if self.objectiveImage:
					self.objectiveImage.Hide()
					self.objectiveImage = None					
				return
