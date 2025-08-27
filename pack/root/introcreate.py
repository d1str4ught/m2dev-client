import chr
import grp
import app
import net
import snd
import wndMgr
import event
import systemSetting
import localeInfo

import ui
import networkModule
import math
import snd
import musicInfo
import playerSettingModule
import uiScriptLocale
import uiToolTip

LOCALE_PATH = "uiscript/"+uiScriptLocale.CODEPAGE+"_"

MAN			= 0
WOMAN		= 1
SHAPE0		= 0
SHAPE1		= 1
PAGE_COUNT	= 2
SLOT_COUNT	= 4
BASE_CHR_ID	= 3

class CreateCharacterWindow(ui.Window):

	SLOT_ROTATION = [135.0, 225.0, 315.0, 45.0]
	

	CREATE_STAT_POINT = 0

	STAT_CON = 0
	STAT_INT = 1
	STAT_STR = 2
	STAT_DEX = 3

	STAT_DESCRIPTION =	{
							STAT_CON : localeInfo.STAT_TOOLTIP_CON,
							STAT_INT : localeInfo.STAT_TOOLTIP_INT,
							STAT_STR : localeInfo.STAT_TOOLTIP_STR,
							STAT_DEX : localeInfo.STAT_TOOLTIP_DEX,
						}

	START_STAT =	(  ## CON INT STR DEX
						[ 4, 3, 6, 3, ], ## Warrior
						[ 3, 3, 4, 6, ], ## Assassin
						[ 3, 5, 5, 3, ], ## Sura
						[ 4, 6, 3, 3, ], ## Shaman
						[ 4, 3, 6, 3, ], ## Warrior
						[ 3, 3, 4, 6, ], ## Assassin
						[ 3, 5, 5, 3, ], ## Sura
						[ 4, 6, 3, 3, ], ## Shaman
					)

	DESCRIPTION_FILE_NAME =	(
		uiScriptLocale.JOBDESC_WARRIOR_PATH,
		uiScriptLocale.JOBDESC_ASSASSIN_PATH,
		uiScriptLocale.JOBDESC_SURA_PATH,
		uiScriptLocale.JOBDESC_SHAMAN_PATH,
	)

	class DescriptionBox(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)
			self.descIndex = 0
		def __del__(self):
			ui.Window.__del__(self)
		def SetIndex(self, index):
			self.descIndex = index
		def OnRender(self):
			event.RenderEventSet(self.descIndex)

	class CharacterRenderer(ui.Window):
		def OnRender(self):
			grp.ClearDepthBuffer()
			grp.SetGameRenderState()
			grp.PushState()
			grp.SetOmniLight()

			screenWidth = wndMgr.GetScreenWidth()
			screenHeight = wndMgr.GetScreenHeight()
			newScreenWidth = float(screenWidth - 270)
			newScreenHeight = float(screenHeight)

			grp.SetViewport(270.0/screenWidth, 0.0, newScreenWidth/screenWidth, newScreenHeight/screenHeight)

			app.SetCenterPosition(0.0, 0.0, 0.0)
			app.SetCamera(1550.0, 15.0, 180.0, 95.0)
			grp.SetPerspective(10.0, newScreenWidth/newScreenHeight, 1000.0, 3000.0)

			(x, y) = app.GetCursorPosition()
			grp.SetCursorPosition(x, y)

			chr.Deform()
			chr.Render()

			grp.RestoreViewport()
			grp.PopState()
			grp.SetInterfaceRenderState()

	def __init__(self, stream):
		print "NEW CREATE WINDOW ----------------------------------------------------------------------------"
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_CREATE, self)

		self.stream=stream

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE CREATE WINDOW"

		net.SetPhaseWindow(net.PHASE_WINDOW_CREATE, 0)
		ui.Window.__del__(self)

	def Open(self):
		print "OPEN CREATE WINDOW ----------------------------------------------------------------------------"

		playerSettingModule.LoadGameData("INIT")

		self.reservingRaceIndex = -1
		self.reservingShapeIndex = -1
		self.reservingStartTime = 0
		self.stat = [0, 0, 0, 0]
	
		self.gender = 0
		self.slot = -1
		self.shapeList = [
			[0, 0, 0, 0],
			[0, 0, 0, 0]]

		self.descIndex = 0

		try:
			dlgBoard = ui.ScriptWindow()
			pythonScriptLoader = ui.PythonScriptLoader()
			pythonScriptLoader.LoadScriptFile(dlgBoard, uiScriptLocale.LOCALE_UISCRIPT_PATH + "createcharacterwindow.py")

		except:
			import exception
			exception.Abort("CreateCharacterWindow.Open.LoadObject")

		try:
			getChild = dlgBoard.GetChild

			self.NameList = []
			self.NameList.append(getChild("name_warrior"))
			self.NameList.append(getChild("name_assassin"))
			self.NameList.append(getChild("name_sura"))
			self.NameList.append(getChild("name_shaman"))

			self.GaugeList = []
			self.GaugeList.append(getChild("hth_gauge"))
			self.GaugeList.append(getChild("int_gauge"))
			self.GaugeList.append(getChild("str_gauge"))
			self.GaugeList.append(getChild("dex_gauge"))

			self.btnCreate = getChild("create_button")
			self.btnCancel = getChild("cancel_button")
			self.btnPrev = getChild("prev_button")
			self.btnNext = getChild("next_button")
			self.btnLeft = getChild("left_button")
			self.btnRight = getChild("right_button")
			self.textBoard = getChild("text_board")

			self.genderButtonList = []
			self.genderButtonList.append(getChild("gender_button_01"))
			self.genderButtonList.append(getChild("gender_button_02"))

			self.shapeButtonList = []
			self.shapeButtonList.append(getChild("shape_button_01"))
			self.shapeButtonList.append(getChild("shape_button_02"))

			self.editCharacterName = getChild("character_name_value")

			self.statValue = []
			self.statValue.append(getChild("hth_value"))
			self.statValue.append(getChild("int_value"))
			self.statValue.append(getChild("str_value"))
			self.statValue.append(getChild("dex_value"))

			getChild("hth_button").ShowToolTip = lambda arg=self.STAT_CON: self.OverInStatButton(arg)
			getChild("hth_button").HideToolTip = lambda arg=self.STAT_CON: self.OverOutStatButton()
			getChild("int_button").ShowToolTip = lambda arg=self.STAT_INT: self.OverInStatButton(arg)
			getChild("int_button").HideToolTip = lambda arg=self.STAT_INT: self.OverOutStatButton()
			getChild("str_button").ShowToolTip = lambda arg=self.STAT_STR: self.OverInStatButton(arg)
			getChild("str_button").HideToolTip = lambda arg=self.STAT_STR: self.OverOutStatButton()
			getChild("dex_button").ShowToolTip = lambda arg=self.STAT_DEX: self.OverInStatButton(arg)
			getChild("dex_button").HideToolTip = lambda arg=self.STAT_DEX: self.OverOutStatButton()

			getChild("hth_button").Hide()
			getChild("int_button").Hide()
			getChild("str_button").Hide()
			getChild("dex_button").Hide()

			self.backGround = getChild("BackGround")

		except:
			import exception
			exception.Abort("CreateCharacterWindow.Open.BindObject")

		self.btnCreate.SetEvent(ui.__mem_func__(self.CreateCharacter))
		self.btnCancel.SetEvent(ui.__mem_func__(self.CancelCreate))
		self.btnPrev.SetEvent(ui.__mem_func__(self.PrevDescriptionPage))
		self.btnNext.SetEvent(ui.__mem_func__(self.NextDescriptionPage))
		self.btnLeft.SetEvent(ui.__mem_func__(self.__DecreaseSlotIndex))
		self.btnRight.SetEvent(ui.__mem_func__(self.__IncreaseSlotIndex))

		self.genderButtonList[0].SetEvent(ui.__mem_func__(self.__SelectGender), MAN)
		self.genderButtonList[1].SetEvent(ui.__mem_func__(self.__SelectGender), WOMAN)

		self.shapeButtonList[0].SetEvent(ui.__mem_func__(self.__SelectShape), SHAPE0)
		self.shapeButtonList[1].SetEvent(ui.__mem_func__(self.__SelectShape), SHAPE1)
		self.editCharacterName.SetReturnEvent(ui.__mem_func__(self.CreateCharacter))
		self.editCharacterName.SetEscapeEvent(ui.__mem_func__(self.CancelCreate))
		self.dlgBoard = dlgBoard

		self.curRotation	= [] + self.SLOT_ROTATION
		self.destRotation	= [] + self.SLOT_ROTATION
		self.curNameAlpha	= [0.0, 0.0, 0.0, 0.0, 0.0]
		self.destNameAlpha	= [0.0, 0.0, 0.0, 0.0, 0.0]
		self.curGauge		= [0.0, 0.0, 0.0, 0.0]
		self.destGauge		= [0.0, 0.0, 0.0, 0.0]

		self.descriptionBox = self.DescriptionBox()
		self.descriptionBox.Show()

		self.chrRenderer = self.CharacterRenderer()
		self.chrRenderer.SetParent(self.backGround)
		self.chrRenderer.Show()

		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.ClearToolTip()

		self.editCharacterName.SetText("")

		self.EnableWindow()
		self.__SelectSlot(0)

		app.SetCamera(500.0, 10.0, 180.0, 95.0)

		self.__MakeCharacter(0, 0, playerSettingModule.RACE_WARRIOR_M)
		self.__MakeCharacter(0, 1, playerSettingModule.RACE_ASSASSIN_M)
		self.__MakeCharacter(0, 2, playerSettingModule.RACE_SURA_M)
		self.__MakeCharacter(0, 3, playerSettingModule.RACE_SHAMAN_M)

		self.__MakeCharacter(1, 0, playerSettingModule.RACE_WARRIOR_W)
		self.__MakeCharacter(1, 1, playerSettingModule.RACE_ASSASSIN_W)
		self.__MakeCharacter(1, 2, playerSettingModule.RACE_SURA_W)
		self.__MakeCharacter(1, 3, playerSettingModule.RACE_SHAMAN_W)

		self.__SelectGender(app.GetRandom(MAN, WOMAN))
		self.__SelectShape(0)
		self.__SelectSlot(app.GetRandom(0, 3))

		self.dlgBoard.Show()
		self.Show()

		if musicInfo.createMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.createMusic)

		app.ShowCursor()

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE CREATE WINDOW"

		self.editCharacterName.Enable()
		self.dlgBoard.ClearDictionary()
		self.stream=0
		self.shapeButtonList = []
		self.genderButtonList = []
		self.btnCreate = 0
		self.btnCancel = 0
		self.btnPrev = 0
		self.btnNext = 0
		self.btnLeft = 0
		self.btnRight = 0
		self.textBoard = 0
		self.editCharacterName = 0
		self.backGround = None

		if musicInfo.createMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.createMusic)

		for id in xrange(BASE_CHR_ID + SLOT_COUNT * PAGE_COUNT):
			chr.DeleteInstance(id)

		self.dlgBoard.Hide()
		self.Hide()

		app.HideCursor()
		event.Destroy()

	def EnableWindow(self):
		self.reservingRaceIndex = -1
		self.reservingShapeIndex = -1
		self.btnCreate.Enable()
		self.btnCancel.Enable()
		self.btnPrev.Enable()
		self.btnNext.Enable()
		self.btnLeft.Enable()
		self.btnRight.Enable()

		self.editCharacterName.SetFocus()
		self.editCharacterName.Enable()

		for page in xrange(PAGE_COUNT):
			for slot in xrange(SLOT_COUNT):
				chr_id = self.__GetSlotChrID(page, slot)
				chr.SelectInstance(chr_id)
				chr.BlendLoopMotion(chr.MOTION_INTRO_WAIT, 0.1)

	def DisableWindow(self):
		self.btnCreate.Disable()
		self.btnCancel.Disable()
		self.btnPrev.Disable()
		self.btnNext.Disable()
		self.btnLeft.Disable()
		self.btnRight.Disable()
		self.editCharacterName.Disable()

		self.btnCreate.SetUp()

	## Manage Character
	def __GetSlotChrID(self, page, slot):
		return BASE_CHR_ID + page * SLOT_COUNT + slot

	def __MakeCharacter(self, page, slot, race):

		chr_id = self.__GetSlotChrID(page, slot)

		chr.CreateInstance(chr_id)
		chr.SelectInstance(chr_id)
		chr.SetVirtualID(chr_id)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.SetHair(0)

		chr.Refresh()
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

		chr.SetRotation(0.0)
		chr.Hide()

	def __SelectGender(self, gender):		
		for button in self.genderButtonList:
			button.SetUp()

		self.genderButtonList[gender].Down()

		self.gender = gender

		if gender == MAN:
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(0, i))
				chr.Show()
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(1, i))
				chr.Hide()
		else:
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(0, i))
				chr.Hide()
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(1, i))
				chr.Show()			

	def __SelectShape(self, shape):
		self.shapeList[self.gender][self.slot] = shape

		for button in self.shapeButtonList:
			button.SetUp()

		self.shapeButtonList[shape].Down()

		chr_id = self.__GetSlotChrID(self.gender, self.slot)		
		chr.SelectInstance(chr_id)		
		chr.ChangeShape(shape)		
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

	def GetSlotIndex(self):
		return self.slot

	def RefreshStat(self):
		statSummary = self.stat[0] + self.stat[1] + self.stat[2] + self.stat[3]
		self.destGauge =	(
								float(self.stat[0])/float(statSummary),
								float(self.stat[1])/float(statSummary),
								float(self.stat[2])/float(statSummary),
								float(self.stat[3])/float(statSummary),
							)

		for i in xrange(4):
			self.statValue[i].SetText(str(self.stat[i]))

	def __SelectSlot(self, slot):

		if slot < 0:
			return

		if slot >= SLOT_COUNT:
			return		

		if self.slot == slot:
			return

		self.slot = slot
		self.ResetStat()

		for i in xrange(SLOT_COUNT):
			self.destNameAlpha[i] = 0.0

		self.destNameAlpha[slot] = 1.0

		for i in xrange(SLOT_COUNT):
			self.destRotation[(i+self.slot)%SLOT_COUNT] = self.SLOT_ROTATION[i]

		if self.IsShow():
			snd.PlaySound("sound/ui/click.wav")

		event.ClearEventSet(self.descIndex)
		self.descIndex = event.RegisterEventSet(self.DESCRIPTION_FILE_NAME[self.slot])
		
		if localeInfo.IsARABIC(): 
			event.SetEventSetWidth(self.descIndex, 170)

		chr_id = self.__GetSlotChrID(self.gender, slot)
		if chr.HasInstance(chr_id):
			chr.SelectInstance(chr_id)
			self.__SelectShape(self.shapeList[self.gender][slot])

	def CreateCharacter(self):

		if -1 != self.reservingRaceIndex:
			return

		textName = self.editCharacterName.GetText()
		if False == self.__CheckCreateCharacter(textName):
			return

		if musicInfo.selectMusic != "":
			snd.FadeLimitOutMusic("BGM/"+musicInfo.selectMusic, systemSetting.GetMusicVolume()*0.05)

		self.DisableWindow()

		
		chr_id = self.__GetSlotChrID(self.gender, self.slot)

		chr.SelectInstance(chr_id)

		self.reservingRaceIndex = chr.GetRace()

		self.reservingShapeIndex = self.shapeList[self.gender][self.slot]
		self.reservingStartTime = app.GetTime()

		for eachSlot in xrange(SLOT_COUNT):

			sel_id = self.__GetSlotChrID(self.gender, eachSlot)

			chr.SelectInstance(sel_id)

			if eachSlot == self.slot:
				chr.PushOnceMotion(chr.MOTION_INTRO_SELECTED)
			else:
				chr.PushOnceMotion(chr.MOTION_INTRO_NOT_SELECTED)

	def CancelCreate(self):
		self.stream.SetSelectCharacterPhase()

	def __DecreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() - 1 + SLOT_COUNT) % SLOT_COUNT
		self.__SelectSlot(slotIndex)

	def __IncreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() + 1) % SLOT_COUNT
		self.__SelectSlot(slotIndex)

	def PrevDescriptionPage(self):
		if True == event.IsWait(self.descIndex):
			if event.GetVisibleStartLine(self.descIndex)-5 >= 0:
				event.SetVisibleStartLine(self.descIndex, event.GetVisibleStartLine(self.descIndex)-5)
				event.Skip(self.descIndex)
		else:
			event.Skip(self.descIndex)

	def NextDescriptionPage(self):
		if True == event.IsWait(self.descIndex):
			event.SetVisibleStartLine(self.descIndex, event.GetVisibleStartLine(self.descIndex)+5)
			event.Skip(self.descIndex)
		else:
			event.Skip(self.descIndex)

	def __CheckCreateCharacter(self, name):
		if len(name) == 0:
			self.PopupMessage(localeInfo.CREATE_INPUT_NAME, self.EnableWindow)
			return False

		if name.find(localeInfo.CREATE_GM_NAME)!=-1:
			self.PopupMessage(localeInfo.CREATE_ERROR_GM_NAME, self.EnableWindow)
			return False

		if net.IsInsultIn(name):
			self.PopupMessage(localeInfo.CREATE_ERROR_INSULT_NAME, self.EnableWindow)
			return False

		return True		

	def ResetStat(self):
		for i in xrange(4):
			self.stat[i] = self.START_STAT[self.slot][i]
		self.lastStatPoint = self.CREATE_STAT_POINT
		self.RefreshStat()

	## Event
	def OnCreateSuccess(self):
		self.stream.SetSelectCharacterPhase()

	def OnCreateFailure(self, type):
		if 1 == type:
			self.PopupMessage(localeInfo.CREATE_EXIST_SAME_NAME, self.EnableWindow)
		else:
			self.PopupMessage(localeInfo.CREATE_FAILURE, self.EnableWindow)

	def OnKeyDown(self, key):

		if key == 2:
			self.__SelectSlot(0)
		if key == 3:
			self.__SelectSlot(1)
		if key == 4:
			self.__SelectSlot(2)
		if key == 5:
			self.__SelectSlot(3)

		if 203 == key:
			self.__DecreaseSlotIndex()
		if 205 == key:
			self.__IncreaseSlotIndex()

		if 59 == key:
			self.__SelectGender(MAN_PAGE)
		if 60 == key:
			self.__SelectGender(WOMAN_PAGE)

		return True

	def OnUpdate(self):
		chr.Update()

		(xposEventSet, yposEventSet) = self.textBoard.GetGlobalPosition()
		event.UpdateEventSet(self.descIndex, xposEventSet+7, -(yposEventSet+7))
		self.descriptionBox.SetIndex(self.descIndex)

		for i in xrange(4):
			self.curNameAlpha[i] += (self.destNameAlpha[i] - self.curNameAlpha[i]) / 10.0
			self.NameList[i].SetAlpha(self.curNameAlpha[i])

		for i in xrange(4):
			self.curGauge[i] += (self.destGauge[i] - self.curGauge[i]) / 10.0
			if abs(self.curGauge[i] - self.destGauge[i]) < 0.005:
				self.curGauge[i] = self.destGauge[i]
			self.GaugeList[i].SetPercentage(self.curGauge[i], 1.0)

		for page in xrange(PAGE_COUNT):
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(page, i))

				distance = 50.0
				rotRadian = self.curRotation[i] * (math.pi*2) / 360.0
				x = distance*math.sin(rotRadian) + distance*math.cos(rotRadian)
				y = distance*math.cos(rotRadian) - distance*math.sin(rotRadian)
				chr.SetPixelPosition(int(x), int(y), 30)

				if abs(self.destRotation[i] - self.curRotation[i]) < 1.0:
					self.curRotation[i] = self.destRotation[i]

				dir = app.GetRotatingDirection(self.destRotation[i], self.curRotation[i])
				rot = app.GetDegreeDifference(self.destRotation[i], self.curRotation[i])

				if app.DEGREE_DIRECTION_RIGHT == dir:
					self.curRotation[i] += rot / 10.0
				elif app.DEGREE_DIRECTION_LEFT == dir:
					self.curRotation[i] -= rot / 10.0

				self.curRotation[i] = (self.curRotation[i] + 360.0) % 360.0

		###########################################################
		if -1 != self.reservingRaceIndex:
			if app.GetTime() - self.reservingStartTime >= 1.5:

				chrSlot=self.stream.GetCharacterSlot()
				textName = self.editCharacterName.GetText()
				raceIndex = self.reservingRaceIndex
				shapeIndex = self.reservingShapeIndex

				startStat = self.START_STAT[self.reservingRaceIndex]
				statCon = self.stat[0] - startStat[0]
				statInt = self.stat[1] - startStat[1]
				statStr = self.stat[2] - startStat[2]
				statDex = self.stat[3] - startStat[3]

				net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, statCon, statInt, statStr, statDex)

				self.reservingRaceIndex = -1

		###########################################################	

	def EmptyFunc(self):
		pass

	def PopupMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		self.CancelCreate()
		return True

	def OverInStatButton(self, stat):
		if not self.STAT_DESCRIPTION.has_key(stat):
			return

		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(self.STAT_DESCRIPTION[stat])
		self.toolTip.Show()

	def OverOutStatButton(self):
		self.toolTip.Hide()

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import networkModule

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	mainStream = networkModule.MainStream()
	mainStream.Create()	

	test = CreateCharacterWindow(mainStream)
	test.Open()

	app.Loop()
