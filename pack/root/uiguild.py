import app
import ui
import guild
import net
import wndMgr
import grp
import grpText
import uiPickMoney
import localeInfo
import player
import skill
import mouseModule
import uiUploadMark
import uiCommon
import uiToolTip
import playerSettingModule
import constInfo
import background
import miniMap
import chr
import uiScriptLocale
from _weakref import proxy

DISABLE_GUILD_SKILL = False
DISABLE_DECLARE_WAR = False

def NumberToMoneyString(n):
	return localeInfo.NumberToMoneyString(n)

if (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/br"):
	def NumberToMoneyString(n):
		if n <= 0 :
			return "0"

		return "%s" % (','.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))

MATERIAL_STONE_INDEX = 0
MATERIAL_LOG_INDEX = 1
MATERIAL_PLYWOOD_INDEX = 2

MATERIAL_STONE_ID = 90010
MATERIAL_LOG_ID = 90011
MATERIAL_PLYWOOD_ID = 90012

BUILDING_DATA_LIST = []

def GetGVGKey(srcGuildID, dstGuildID):
	minID = min(srcGuildID, dstGuildID)
	maxID = max(srcGuildID, dstGuildID)
	return minID*1000 + maxID
def unsigned32(n):
	return n & 0xFFFFFFFFL
	
class DeclareGuildWarDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.type=0
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def __CreateDialog(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()

			if localeInfo.IsVIETNAM() :
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "declareguildwardialog.py")
			else:
				pyScrLoader.LoadScriptFile(self, "uiscript/declareguildwardialog.py")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")

			self.typeButtonList=[]
			self.typeButtonList.append(getObject("NormalButton"))
			self.typeButtonList.append(getObject("WarpButton"))
			self.typeButtonList.append(getObject("CTFButton"))

			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")

			gameType=getObject("GameType")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - BindObject")

		if constInfo.GUILD_WAR_TYPE_SELECT_ENABLE==0:
			gameType.Hide()

		self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonNormal)
		self.typeButtonList[1].SAFE_SetEvent(self.__OnClickTypeButtonWarp)
		self.typeButtonList[2].SAFE_SetEvent(self.__OnClickTypeButtonCTF)

		self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_NORMAL_TITLE, localeInfo.GUILDWAR_NORMAL_DESCLIST))
		self.typeButtonList[1].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_WARP_TITLE, localeInfo.GUILDWAR_WARP_DESCLIST))
		self.typeButtonList[2].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_CTF_TITLE, localeInfo.GUILDWAR_CTF_DESCLIST))

		self.__ClickRadioButton(self.typeButtonList, 0)

		self.SetAcceptEvent(ui.__mem_func__(self.__OnOK))
		self.SetCancelEvent(ui.__mem_func__(self.__OnCancel))

	def __OnOK(self):
		text = self.GetText()
		type = self.GetType()

		if ""==text:
			return

		net.SendChatPacket("/war %s %d" % (text, type))
		self.Close()

		return 1

	def __OnCancel(self):
		self.Close()
		return 1

	def __OnClickTypeButtonNormal(self):
		self.__ClickTypeRadioButton(0)

	def __OnClickTypeButtonWarp(self):
		self.__ClickTypeRadioButton(1)

	def __OnClickTypeButtonCTF(self):
		self.__ClickTypeRadioButton(2)

	def __ClickTypeRadioButton(self, type):
		self.__ClickRadioButton(self.typeButtonList, type)
		self.type=type

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.inputValue.SetMax(length)
		self.SetSlotWidth(width)
		self.SetBoardWidth(max(width + 50, 160))

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())

	def SetBoardWidth(self, width):
		self.board.SetSize(max(width + 50, 160), self.GetHeight())
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetType(self):
		return self.type

	def GetText(self):
		return self.inputValue.GetText()

	def __CreateGameTypeToolTip(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)
		toolTip.AppendSpace(5)

		for desc in descList:
			toolTip.AutoAppendTextLine(desc)

		toolTip.AlignHorizonalCenter()
		return toolTip


class AcceptGuildWarDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.type=0
		self.__CreateDialog()

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE AcceptGuildWarDialog"
		ui.ScriptWindow.__del__(self)

	def Open(self, guildName, warType):
		self.guildName=guildName
		self.warType=warType
		self.__ClickSelectedTypeRadioButton()
		self.inputValue.SetText(guildName)
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def GetGuildName(self):
		return self.guildName

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def __ClickSelectedTypeRadioButton(self):
		self.__ClickTypeRadioButton(self.warType)

	def __CreateDialog(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/acceptguildwardialog.py")
		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")

			self.typeButtonList=[]
			self.typeButtonList.append(getObject("NormalButton"))
			self.typeButtonList.append(getObject("WarpButton"))
			self.typeButtonList.append(getObject("CTFButton"))

			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")

			gameType=getObject("GameType")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - BindObject")

		if constInfo.GUILD_WAR_TYPE_SELECT_ENABLE==0:
			gameType.Hide()

		self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonNormal)
		self.typeButtonList[1].SAFE_SetEvent(self.__OnClickTypeButtonWarp)
		self.typeButtonList[2].SAFE_SetEvent(self.__OnClickTypeButtonCTF)

		self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_NORMAL_TITLE, localeInfo.GUILDWAR_NORMAL_DESCLIST))
		self.typeButtonList[1].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_WARP_TITLE, localeInfo.GUILDWAR_WARP_DESCLIST))
		self.typeButtonList[2].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_CTF_TITLE, localeInfo.GUILDWAR_CTF_DESCLIST))

		self.__ClickRadioButton(self.typeButtonList, 0)

	def __OnClickTypeButtonNormal(self):
		self.__ClickSelectedTypeRadioButton()

	def __OnClickTypeButtonWarp(self):
		self.__ClickSelectedTypeRadioButton()

	def __OnClickTypeButtonCTF(self):
		self.__ClickSelectedTypeRadioButton()

	def __ClickTypeRadioButton(self, type):
		self.__ClickRadioButton(self.typeButtonList, type)
		self.type=type

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.inputValue.SetMax(length)
		self.SetSlotWidth(width)
		self.SetBoardWidth(max(width + 50, 160))

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())

	def SetBoardWidth(self, width):
		self.board.SetSize(max(width + 50, 160), self.GetHeight())
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.SetAcceptEvent(ui.__mem_func__(event))

	def SAFE_SetCancelEvent(self, event):
		self.SetCancelEvent(ui.__mem_func__(event))

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetType(self):
		return self.type

	def GetText(self):
		return self.inputValue.GetText()

	def __CreateGameTypeToolTip(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)
		toolTip.AppendSpace(5)

		for desc in descList:
			toolTip.AutoAppendTextLine(desc)

		toolTip.AlignHorizonalCenter()
		return toolTip



class GuildWarScoreBoard(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Initialize(self):
		self.allyGuildID = 0
		self.enemyGuildID = 0
		self.allyDataDict = {}
		self.enemyDataDict = {}

	def Open(self, allyGuildID, enemyGuildID):

		self.allyGuildID = allyGuildID
		self.enemyGuildID = enemyGuildID

		self.SetPosition(10, wndMgr.GetScreenHeight() - 100)

		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetIndex(allyGuildID)
		mark.SetPosition(10, 10 + 18*0)
		mark.Show()
		scoreText = ui.TextLine()
		scoreText.SetParent(self)
		scoreText.SetPosition(30, 10 + 18*0)
		scoreText.SetHorizontalAlignLeft()
		scoreText.Show()
		self.allyDataDict["NAME"] = guild.GetGuildName(allyGuildID)
		self.allyDataDict["SCORE"] = 0
		self.allyDataDict["MEMBER_COUNT"] = -1
		self.allyDataDict["MARK"] = mark
		self.allyDataDict["TEXT"] = scoreText

		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetIndex(enemyGuildID)
		mark.SetPosition(10, 10 + 18*1)
		mark.Show()
		scoreText = ui.TextLine()
		scoreText.SetParent(self)
		scoreText.SetPosition(30, 10 + 18*1)
		scoreText.SetHorizontalAlignLeft()
		scoreText.Show()
		self.enemyDataDict["NAME"] = guild.GetGuildName(enemyGuildID)
		self.enemyDataDict["SCORE"] = 0
		self.enemyDataDict["MEMBER_COUNT"] = -1
		self.enemyDataDict["MARK"] = mark
		self.enemyDataDict["TEXT"] = scoreText

		self.__RefreshName()
		self.Show()

	def __GetDataDict(self, ID):
		if self.allyGuildID == ID:
			return self.allyDataDict
		if self.enemyGuildID == ID:
			return self.enemyDataDict

		return None

	def SetScore(self, gainGuildID, opponetGuildID, point):
		dataDict = self.__GetDataDict(gainGuildID)
		if not dataDict:
			return
		dataDict["SCORE"] = point
		self.__RefreshName()

	def UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2):
		dataDict1 = self.__GetDataDict(guildID1)
		dataDict2 = self.__GetDataDict(guildID2)
		if dataDict1:
			dataDict1["MEMBER_COUNT"] = memberCount1
		if dataDict2:
			dataDict2["MEMBER_COUNT"] = memberCount2
		self.__RefreshName()

	def __RefreshName(self):
		nameMaxLen = max(len(self.allyDataDict["NAME"]), len(self.enemyDataDict["NAME"]))

		if -1 == self.allyDataDict["MEMBER_COUNT"] or -1 == self.enemyDataDict["MEMBER_COUNT"]:
			self.SetSize(30+nameMaxLen*6+8*5, 50)
			self.allyDataDict["TEXT"].SetText("%s %d" % (self.allyDataDict["NAME"], self.allyDataDict["SCORE"]))
			self.enemyDataDict["TEXT"].SetText("%s %d" % (self.enemyDataDict["NAME"], self.enemyDataDict["SCORE"]))

		else:
			self.SetSize(30+nameMaxLen*6+8*5+15, 50)
			self.allyDataDict["TEXT"].SetText("%s(%d) %d" % (self.allyDataDict["NAME"], self.allyDataDict["MEMBER_COUNT"], self.allyDataDict["SCORE"]))
			self.enemyDataDict["TEXT"].SetText("%s(%d) %d" % (self.enemyDataDict["NAME"], self.enemyDataDict["MEMBER_COUNT"], self.enemyDataDict["SCORE"]))

class MouseReflector(ui.Window):
	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.AddFlag("not_pick")
		self.width = self.height = 0
		self.isDown = False

	def Down(self):
		self.isDown = True

	def Up(self):
		self.isDown = False

	def OnRender(self):

		if self.isDown:
			grp.SetColor(ui.WHITE_COLOR)
		else:
			grp.SetColor(ui.HALF_WHITE_COLOR)

		x, y = self.GetGlobalPosition()
		grp.RenderBar(x+2, y+2, self.GetWidth()-4, self.GetHeight()-4)

class EditableTextSlot(ui.ImageBox):
	def __init__(self, parent, x, y):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage("d:/ymir work/ui/public/Parameter_Slot_02.sub")

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		self.Enable = True
		self.textLine = ui.MakeTextLine(self)
		self.event = lambda *arg: None
		self.arg = 0
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetEvent(self, event, arg):
		self.event = event
		self.arg = arg

	def Disable(self):
		self.Enable = False

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event(self.arg)

class CheckBox(ui.ImageBox):
	def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = True
		self.image = image
		self.event = event
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
		else:
			self.image.Hide()

	def Disable(self):
		self.Enable = False

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()

class ChangeGradeNameDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
	def Open(self):
		self.gradeNameSlot.SetText("")
		self.gradeNameSlot.SetFocus()
		xMouse, yMouse = wndMgr.GetMousePosition()
		self.SetPosition(xMouse - self.GetWidth()/2, yMouse + 50)
		self.SetTop()
		self.Show()
	def Close(self):
		self.gradeNameSlot.KillFocus()
		self.Hide()
		return True

	def SetGradeNumber(self, gradeNumber):
		self.gradeNumber = gradeNumber
	def GetGradeNumber(self):
		return self.gradeNumber
	def GetGradeName(self):
		return self.gradeNameSlot.GetText()

	def OnPressEscapeKey(self):
		self.Close()
		return True

class CommentSlot(ui.Window):

	TEXT_LIMIT = 35

	def __init__(self):
		ui.Window.__init__(self)

		self.slotImage = ui.MakeImageBox(self, "d:/ymir work/ui/public/Parameter_Slot_06.sub", 0, 0)
		self.slotImage.AddFlag("not_pick")

		self.slotSimpleText = ui.MakeTextLine(self)
		self.slotSimpleText.SetPosition(2, 0)
		## 13.12.02 아랍수정
		if localeInfo.IsARABIC() :
			self.slotSimpleText.SetWindowHorizontalAlignCenter()
			self.slotSimpleText.SetHorizontalAlignCenter()
		else :
			self.slotSimpleText.SetWindowHorizontalAlignLeft()
			self.slotSimpleText.SetHorizontalAlignLeft()

		self.bar = ui.SlotBar()
		self.bar.SetParent(self)
		self.bar.AddFlag("not_pick")
		self.bar.Hide()

		self.slotFullText = ui.MakeTextLine(self)
		self.slotFullText.SetPosition(2, 0)
		self.slotFullText.SetWindowHorizontalAlignLeft()
		self.slotFullText.SetHorizontalAlignLeft()

		self.SetSize(self.slotImage.GetWidth(), self.slotImage.GetHeight())
		self.len = 0

	def SetText(self, text):
		self.len = len(text)
		if len(text) > self.TEXT_LIMIT:
			limitText = grpText.GetSplitingTextLine(text, self.TEXT_LIMIT-3, 0)
			self.slotSimpleText.SetText(limitText + "...")
			self.bar.SetSize(self.len * 6 + 5, 17)

		else:
			self.slotSimpleText.SetText(text)

		self.slotFullText.SetText(text)
		self.slotFullText.SetPosition(2, 0)
		self.slotFullText.Hide()

	def OnMouseOverIn(self):
		if self.len > self.TEXT_LIMIT:
			self.bar.Show()
			self.slotFullText.Show()

	def OnMouseOverOut(self):
		if self.len > self.TEXT_LIMIT:
			self.bar.Hide()
			self.slotFullText.Hide()

class GuildWindow(ui.ScriptWindow):

	JOB_NAME = {	0 : localeInfo.JOB_WARRIOR,
			1 : localeInfo.JOB_ASSASSIN,
			2 : localeInfo.JOB_SURA,
			3 : localeInfo.JOB_SHAMAN, }

	GUILD_SKILL_PASSIVE_SLOT = 0
	GUILD_SKILL_ACTIVE_SLOT = 1
	GUILD_SKILL_AFFECT_SLOT = 2

	GRADE_SLOT_NAME = 0
	GRADE_ADD_MEMBER_AUTHORITY = 1
	GRADE_REMOVE_MEMBER_AUTHORITY = 2
	GRADE_NOTICE_AUTHORITY = 3
	GRADE_SKILL_AUTHORITY = 4

	MEMBER_LINE_COUNT = 13

	class PageWindow(ui.ScriptWindow):
		def __init__(self, parent, filename):
			ui.ScriptWindow.__init__(self)
			self.SetParent(parent)
			self.filename = filename
		def GetScriptFileName(self):
			return self.filename

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded=0

		self.__Initialize()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " ==================================== DESTROIED GUILD WINDOW"

	def __Initialize(self):

		self.board = None
		self.pageName = None
		self.tabDict = None
		self.tabButtonDict = None
		self.pickDialog = None
		self.questionDialog = None
		self.offerDialog = None
		self.popupDialog = None	
		self.moneyDialog = None
		self.changeGradeNameDialog = None	
		self.popup = None

		self.popupMessage = None
		self.commentSlot = None

		self.pageWindow = None
		self.tooltipSkill = None

		self.memberLinePos = 0

		self.enemyGuildNameList = []

	def Open(self):
		self.Show()
		self.SetTop()

		guildID = net.GetGuildID()
		self.largeMarkBox.SetIndex(guildID)
		self.largeMarkBox.SetScale(3)

	def Close(self):
		self.__CloseAllGuildMemberPageGradeComboBox()
		self.offerDialog.Close()
		self.popupDialog.Hide()
		self.changeGradeNameDialog.Hide()
		self.tooltipSkill.Hide()
		self.Hide()

		self.pickDialog = None
		self.questionDialog = None
		self.popup = None

	def Destroy(self):
		self.ClearDictionary()

		if self.offerDialog:
			self.offerDialog.Destroy()
			
		if self.popupDialog:
			self.popupDialog.ClearDictionary()
			
		if self.changeGradeNameDialog:
			self.changeGradeNameDialog.ClearDictionary()
			
		if self.pageWindow:
			for window in self.pageWindow.values():
				window.ClearDictionary()

		self.__Initialize()

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__LoadWindow()

		self.RefreshGuildInfoPage()
		self.RefreshGuildBoardPage()
		self.RefreshGuildMemberPage()
		self.RefreshGuildSkillPage()
		self.RefreshGuildGradePage()

		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		global DISABLE_GUILD_SKILL
		try:
			pyScrLoader = ui.PythonScriptLoader()

			if localeInfo.IsARABIC() :
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "uiscript/guildwindow.py")

			self.popupDialog = ui.ScriptWindow()
			pyScrLoader.LoadScriptFile(self.popupDialog, "UIScript/PopupDialog.py")

			self.changeGradeNameDialog = ChangeGradeNameDialog()
			pyScrLoader.LoadScriptFile(self.changeGradeNameDialog, "uiscript/changegradenamedialog.py")

			if localeInfo.IsARABIC():
				self.pageWindow = {
					"GUILD_INFO"	: self.PageWindow(self, "uiscript/guildwindow_guildinfopage_eu.py"),
					"BOARD"			: self.PageWindow(self, "uiscript/guildwindow_boardpage.py"),
					"MEMBER"		: self.PageWindow(self, "uiscript/guildwindow_memberpage.py"),
					"BASE_INFO"		: self.PageWindow(self, "uiscript/guildwindow_baseinfopage.py"),
					"SKILL"			: self.PageWindow(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow_guildskillpage.py"),
					"GRADE"			: self.PageWindow(self, "uiscript/guildwindow_gradepage.py"),
				}
			elif localeInfo.IsJAPAN() :
				self.pageWindow = {
					"GUILD_INFO"	: self.PageWindow(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow_guildinfopage.py"),
					"BOARD"			: self.PageWindow(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow_boardpage.py"),
					"MEMBER"		: self.PageWindow(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow_memberpage.py"),
					"BASE_INFO"		: self.PageWindow(self, "uiscript/guildwindow_baseinfopage.py"),
					"SKILL"			: self.PageWindow(self, "uiscript/guildwindow_guildskillpage.py"),
					"GRADE"			: self.PageWindow(self, "uiscript/guildwindow_gradepage.py"),
				}
			elif localeInfo.IsVIETNAM() :   # 다표시 
				self.pageWindow = {
					"GUILD_INFO"	: self.PageWindow(self, "uiscript/guildwindow_guildinfopage_eu.py"),
					"BOARD"			: self.PageWindow(self, "uiscript/guildwindow_boardpage.py"),
					"MEMBER"		: self.PageWindow(self, "uiscript/guildwindow_memberpage.py"),
					"BASE_INFO"		: self.PageWindow(self, "uiscript/guildwindow_baseinfopage.py"),
					"SKILL"			: self.PageWindow(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "guildwindow_guildskillpage.py"),
					"GRADE"			: self.PageWindow(self, "uiscript/guildwindow_gradepage.py"),
				}
			elif localeInfo.IsEUROPE() and not app.GetLocalePath() == "locale/ca" :
				self.pageWindow = {
					"GUILD_INFO"	: self.PageWindow(self, "uiscript/guildwindow_guildinfopage_eu.py"),
					"BOARD"			: self.PageWindow(self, "uiscript/guildwindow_boardpage.py"),
					"MEMBER"		: self.PageWindow(self, "uiscript/guildwindow_memberpage.py"),
					"BASE_INFO"		: self.PageWindow(self, "uiscript/guildwindow_baseinfopage.py"),
					"SKILL"			: self.PageWindow(self, "uiscript/guildwindow_guildskillpage.py"),
					"GRADE"			: self.PageWindow(self, "uiscript/guildwindow_gradepage.py"),
				}
			else:
				self.pageWindow = {
					"GUILD_INFO"	: self.PageWindow(self, "uiscript/guildwindow_guildinfopage.py"),
					"BOARD"			: self.PageWindow(self, "uiscript/guildwindow_boardpage.py"),
					"MEMBER"		: self.PageWindow(self, "uiscript/guildwindow_memberpage.py"),
					"BASE_INFO"		: self.PageWindow(self, "uiscript/guildwindow_baseinfopage.py"),
					"SKILL"			: self.PageWindow(self, "uiscript/guildwindow_guildskillpage.py"),
					"GRADE"			: self.PageWindow(self, "uiscript/guildwindow_gradepage.py"),
				}
				
			for window in self.pageWindow.values():
				pyScrLoader.LoadScriptFile(window, window.GetScriptFileName())

		except:
			import exception
			exception.Abort("GuildWindow.__LoadWindow.LoadScript")

		try:
			getObject = self.GetChild

			self.board = getObject("Board")
			self.pageName = {
				"GUILD_INFO"	: localeInfo.GUILD_TILE_INFO,
				"BOARD"			: localeInfo.GUILD_TILE_BOARD,
				"MEMBER"		: localeInfo.GUILD_TILE_MEMBER,
				"BASE_INFO"		: localeInfo.GUILD_TILE_BASEINFO,
				"SKILL"			: localeInfo.GUILD_TILE_SKILL,
				"GRADE"			: localeInfo.GUILD_TILE_GRADE,
			}

			self.tabDict = {
				"GUILD_INFO"	: getObject("Tab_01"),
				"BOARD"			: getObject("Tab_02"),
				"MEMBER"		: getObject("Tab_03"),
				"BASE_INFO"		: getObject("Tab_04"),
				"SKILL"			: getObject("Tab_05"),
				"GRADE"			: getObject("Tab_06"),
			}
			self.tabButtonDict = {
				"GUILD_INFO"	: getObject("Tab_Button_01"),
				"BOARD"			: getObject("Tab_Button_02"),
				"MEMBER"		: getObject("Tab_Button_03"),
				"BASE_INFO"		: getObject("Tab_Button_04"),
				"SKILL"			: getObject("Tab_Button_05"),
				"GRADE"			: getObject("Tab_Button_06"),
			}

			## QuestionDialog
			self.popupMessage = self.popupDialog.GetChild("message")
			self.popupDialog.GetChild("accept").SetEvent(ui.__mem_func__(self.popupDialog.Hide))

			## ChangeGradeName
			self.changeGradeNameDialog.GetChild("AcceptButton").SetEvent(ui.__mem_func__(self.OnChangeGradeName))
			self.changeGradeNameDialog.GetChild("CancelButton").SetEvent(ui.__mem_func__(self.changeGradeNameDialog.Hide))
			self.changeGradeNameDialog.GetChild("Board").SetCloseEvent(ui.__mem_func__(self.changeGradeNameDialog.Hide))
			self.changeGradeNameDialog.gradeNameSlot = self.changeGradeNameDialog.GetChild("GradeNameValue")
			self.changeGradeNameDialog.gradeNameSlot.OnIMEReturn = ui.__mem_func__(self.OnChangeGradeName)
			self.changeGradeNameDialog.gradeNameSlot.OnPressEscapeKey = ui.__mem_func__(self.changeGradeNameDialog.Close)

			## Comment
			self.commentSlot = self.pageWindow["BOARD"].GetChild("CommentValue")
			self.commentSlot.OnIMEReturn = ui.__mem_func__(self.OnPostComment)
			#self.commentSlot.OnKeyDown = ui.__mem_func__(self.OnKeyDownInBoardPage)
			self.commentSlot.OnKeyDown = lambda key, argSelf=self: argSelf.OnKeyDownInBoardPage(key)

			## RefreshButton
			self.pageWindow["BOARD"].GetChild("RefreshButton").SetEvent(ui.__mem_func__(self.OnRefreshComments))

			## ScrollBar
			scrollBar = self.pageWindow["MEMBER"].GetChild("ScrollBar")
			scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScrollMemberLine))
			self.pageWindow["MEMBER"].scrollBar = scrollBar

		except:
			import exception
			exception.Abort("GuildWindow.__LoadWindow.BindObject")

		self.__MakeInfoPage()
		self.__MakeBoardPage()
		self.__MakeMemberPage()
		self.__MakeBaseInfoPage()
		self.__MakeSkillPage()
		self.__MakeGradePage()

		for page in self.pageWindow.values():
			page.UpdateRect()

		for key, btn in self.tabButtonDict.items():
			btn.SetEvent(self.SelectPage, key)

		self.tabButtonDict["BASE_INFO"].Disable()

		if DISABLE_GUILD_SKILL:
			self.tabButtonDict["SKILL"].Disable()

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.board.SetTitleColor(0xffffffff)
		self.SelectPage("GUILD_INFO")

		self.offerDialog = uiPickMoney.PickMoneyDialog()
		self.offerDialog.LoadDialog()
		self.offerDialog.SetMax(9)
		self.offerDialog.SetTitleName(localeInfo.GUILD_OFFER_EXP)
		self.offerDialog.SetAcceptEvent(ui.__mem_func__(self.OnOffer))

	def __MakeInfoPage(self):
		page = self.pageWindow["GUILD_INFO"]

		try:
			page.nameSlot = page.GetChild("GuildNameValue")
			page.masterNameSlot = page.GetChild("GuildMasterNameValue")
			page.guildLevelSlot = page.GetChild("GuildLevelValue")
			page.curExpSlot = page.GetChild("CurrentExperienceValue")
			page.lastExpSlot = page.GetChild("LastExperienceValue")
			page.memberCountSlot = page.GetChild("GuildMemberCountValue")
			page.levelAverageSlot = page.GetChild("GuildMemberLevelAverageValue")
			page.uploadMarkButton = page.GetChild("UploadGuildMarkButton")
			page.uploadSymbolButton = page.GetChild("UploadGuildSymbolButton")
			page.declareWarButton = page.GetChild("DeclareWarButton")

			try:	
				page.guildMoneySlot = page.GetChild("GuildMoneyValue")
			except KeyError:
				page.guildMoneySlot = None
 
			try:	
				page.GetChild("DepositButton").SetEvent(ui.__mem_func__(self.__OnClickDepositButton))
				page.GetChild("WithdrawButton").SetEvent(ui.__mem_func__(self.__OnClickWithdrawButton))
			except KeyError:
				pass

			page.uploadMarkButton.SetEvent(ui.__mem_func__(self.__OnClickSelectGuildMarkButton))
			page.uploadSymbolButton.SetEvent(ui.__mem_func__(self.__OnClickSelectGuildSymbolButton))
			page.declareWarButton.SetEvent(ui.__mem_func__(self.__OnClickDeclareWarButton))
			page.GetChild("OfferButton").SetEvent(ui.__mem_func__(self.__OnClickOfferButton))
			page.GetChild("EnemyGuildCancel1").Hide()
			page.GetChild("EnemyGuildCancel2").Hide()
			page.GetChild("EnemyGuildCancel3").Hide()
			page.GetChild("EnemyGuildCancel4").Hide()
			page.GetChild("EnemyGuildCancel5").Hide()
			page.GetChild("EnemyGuildCancel6").Hide()

			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName1"))
			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName2"))
			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName3"))
			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName4"))
			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName5"))
			self.enemyGuildNameList.append(page.GetChild("EnemyGuildName6"))

			self.largeMarkBox = page.GetChild("LargeGuildMark")
		except:
			import exception
			exception.Abort("GuildWindow.__MakeInfoPage")

		self.largeMarkBox.AddFlag("not_pick")

		self.markSelectDialog=uiUploadMark.MarkSelectDialog()
		self.markSelectDialog.SAFE_SetSelectEvent(self.__OnSelectMark)

		self.symbolSelectDialog=uiUploadMark.SymbolSelectDialog()
		self.symbolSelectDialog.SAFE_SetSelectEvent(self.__OnSelectSymbol)


	def __MakeBoardPage(self):

		i = 0
		lineStep = 20
		page = self.pageWindow["BOARD"]

		page.boardDict = {}

		for i in xrange(12):

			yPos = 25 + i * lineStep

			## NoticeMark
			if localeInfo.IsJAPAN():
				noticeMarkImage = ui.MakeImageBox(page, "d:/ymir work/ui/game/guild/notice_mark.sub", 15, yPos+3)
			else:
				noticeMarkImage = ui.MakeImageBox(page, "d:/ymir work/ui/game/guild/notice_mark.sub", 5, yPos+3)
			noticeMarkImage.Hide()
			page.Children.append(noticeMarkImage)

			## Name
			## 13.12.02 아랍수정
			if localeInfo.IsJAPAN():
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_100x18.sub", 9, yPos)
			elif localeInfo.IsARABIC():
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_03.sub", 255, yPos)
			else:
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_03.sub", 15, yPos)
			nameSlot = ui.MakeTextLine(nameSlotImage)
			page.Children.append(nameSlotImage)
			page.Children.append(nameSlot)

			## Delete Button
			if localeInfo.IsARABIC():
				deleteButton = ui.MakeButton(page, 3, yPos + 3, localeInfo.GUILD_DELETE, "d:/ymir work/ui/public/", "close_button_01.sub", "close_button_02.sub", "close_button_03.sub")
			else:
				deleteButton = ui.MakeButton(page, 340, yPos + 3, localeInfo.GUILD_DELETE, "d:/ymir work/ui/public/", "close_button_01.sub", "close_button_02.sub", "close_button_03.sub")
			deleteButton.SetEvent(ui.__mem_func__(self.OnDeleteComment), i)
			page.Children.append(deleteButton)

			## Comment
			## 13.12.02 아랍수정
			commentSlot = CommentSlot()
			commentSlot.SetParent(page)
			if localeInfo.IsARABIC():
				commentSlot.SetPosition(25, yPos)
			else:
				commentSlot.SetPosition(114, yPos)
			commentSlot.Show()
			page.Children.append(commentSlot)

			boardSlotList = []
			boardSlotList.append(noticeMarkImage)
			boardSlotList.append(nameSlot)
			boardSlotList.append(commentSlot)
			page.boardDict[i] = boardSlotList

		## PostComment - Have to make this here for that fit tooltip's position.
		## 13.12.02 아랍수정
		if localeInfo.IsARABIC():
			postCommentButton = ui.MakeButton(page, 3, 273, localeInfo.GUILD_COMMENT, "d:/ymir work/ui/game/taskbar/", "Send_Chat_Button_01.sub", "Send_Chat_Button_02.sub", "Send_Chat_Button_03.sub")
		else:
			postCommentButton = ui.MakeButton(page, 337, 273, localeInfo.GUILD_COMMENT, "d:/ymir work/ui/game/taskbar/", "Send_Chat_Button_01.sub", "Send_Chat_Button_02.sub", "Send_Chat_Button_03.sub")
		postCommentButton.SetEvent(ui.__mem_func__(self.OnPostComment))
		page.Children.append(postCommentButton)

	def __MakeMemberPage(self):

		page = self.pageWindow["MEMBER"]

		lineStep = 20
		page.memberDict = {}

		for i in xrange(self.MEMBER_LINE_COUNT):

			inverseLineIndex = self.MEMBER_LINE_COUNT - i - 1
			yPos = 28 + inverseLineIndex*lineStep
            ## 13.12.02 아랍 수정
			## Name
			if localeInfo.IsJAPAN():
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_100x18.sub", 15, yPos)
			elif localeInfo.IsARABIC():
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_100x18.sub", 255, yPos)
			else:
				nameSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_03.sub", 10, yPos)
			nameSlot = ui.MakeTextLine(nameSlotImage)
			page.Children.append(nameSlotImage)
			page.Children.append(nameSlot)

			## Grade
			gradeSlot = ui.ComboBox()
			gradeSlot.SetParent(page)
			if localeInfo.IsJAPAN():
				gradeSlot.SetPosition(117, yPos-1)
			elif localeInfo.IsARABIC():
				gradeSlot.SetPosition(192, yPos-1)
			else:
				gradeSlot.SetPosition(101, yPos-1)
			gradeSlot.SetSize(61, 18)
			gradeSlot.SetEvent(lambda gradeNumber, lineIndex=inverseLineIndex, argSelf=proxy(self): argSelf.OnChangeMemberGrade(lineIndex, gradeNumber))
			gradeSlot.Show()
			page.Children.append(gradeSlot)

			## Job
			if localeInfo.IsJAPAN():
				jobSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 181, yPos)
			elif localeInfo.IsARABIC():
				jobSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 145, yPos)
			else:
				jobSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 170, yPos)
			jobSlot = ui.MakeTextLine(jobSlotImage)
			page.Children.append(jobSlotImage)
			page.Children.append(jobSlot)

			## Level
			if localeInfo.IsJAPAN():
				levelSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 221, yPos)
			elif localeInfo.IsARABIC():
				levelSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 106, yPos)
			else:
				levelSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 210, yPos)
			levelSlot = ui.MakeTextLine(levelSlotImage)
			page.Children.append(levelSlotImage)
			page.Children.append(levelSlot)

			## Offer
			if localeInfo.IsJAPAN():
				offerSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 261, yPos)
			elif localeInfo.IsARABIC():
				offerSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 66, yPos)
			else:
				offerSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 250, yPos)
			offerSlot = ui.MakeTextLine(offerSlotImage)
			page.Children.append(offerSlotImage)
			page.Children.append(offerSlot)

			## General Enable
			event = lambda argSelf=proxy(self), argIndex=inverseLineIndex: apply(argSelf.OnEnableGeneral, (argIndex,))
			if localeInfo.IsJAPAN():
				generalEnableCheckBox = CheckBox(page, 307, yPos, event, "d:/ymir work/ui/public/Parameter_Slot_00.sub")
			elif localeInfo.IsARABIC():
				generalEnableCheckBox = CheckBox(page, 22, yPos, event, "d:/ymir work/ui/public/Parameter_Slot_00.sub")
			else:
				generalEnableCheckBox = CheckBox(page, 297, yPos, event, "d:/ymir work/ui/public/Parameter_Slot_00.sub")
			page.Children.append(generalEnableCheckBox)

			memberSlotList = []
			memberSlotList.append(nameSlot)
			memberSlotList.append(gradeSlot)
			memberSlotList.append(jobSlot)
			memberSlotList.append(levelSlot)
			memberSlotList.append(offerSlot)
			memberSlotList.append(generalEnableCheckBox)
			page.memberDict[inverseLineIndex] = memberSlotList

	def __MakeBaseInfoPage(self):

		page = self.pageWindow["BASE_INFO"]

		page.buildingDataDict = {}

		lineStep = 20
		GUILD_BUILDING_MAX_NUM = 7

		yPos = 95 + 35

		for i in xrange(GUILD_BUILDING_MAX_NUM):

			nameSlotImage = ui.MakeSlotBar(page, 15, yPos, 78, 17)
			nameSlot = ui.MakeTextLine(nameSlotImage)
			page.Children.append(nameSlotImage)
			page.Children.append(nameSlot)
			nameSlot.SetText(localeInfo.GUILD_BUILDING_NAME)

			gradeSlotImage = ui.MakeSlotBar(page, 99, yPos, 26, 17)
			gradeSlot = ui.MakeTextLine(gradeSlotImage)
			page.Children.append(gradeSlotImage)
			page.Children.append(gradeSlot)
			gradeSlot.SetText(localeInfo.GUILD_BUILDING_GRADE)

			RESOURCE_MAX_NUM = 6
			for j in xrange(RESOURCE_MAX_NUM):
				resourceSlotImage = ui.MakeSlotBar(page, 131 + 29*j, yPos, 26, 17)
				resourceSlot = ui.MakeTextLine(resourceSlotImage)
				page.Children.append(resourceSlotImage)
				page.Children.append(resourceSlot)
				resourceSlot.SetText(localeInfo.GUILD_GEM)

			event = lambda *arg: None
			powerSlot = CheckBox(page, 308, yPos, event, "d:/ymir work/ui/public/Parameter_Slot_00.sub")
			page.Children.append(powerSlot)

			yPos += lineStep

	def __MakeSkillPage(self):

		page = self.pageWindow["SKILL"]

		page.skillPoint = page.GetChild("Skill_Plus_Value")
		page.passiveSlot = page.GetChild("Passive_Skill_Slot_Table")
		page.activeSlot = page.GetChild("Active_Skill_Slot_Table")
		page.affectSlot = page.GetChild("Affect_Slot_Table")
		page.gpGauge = page.GetChild("Dragon_God_Power_Gauge")
		page.gpValue = page.GetChild("Dragon_God_Power_Value")
		page.btnHealGSP = page.GetChild("Heal_GSP_Button")

		page.activeSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		page.activeSlot.SetOverInItemEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OverInItem(slotNumber, type))
		page.activeSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		page.activeSlot.SetSelectItemSlotEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnPickUpGuildSkill(slotNumber, type))
		page.activeSlot.SetUnselectItemSlotEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnUseGuildSkill(slotNumber, type))
		page.activeSlot.SetPressedSlotButtonEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnUpGuildSkill(slotNumber, type))
		page.activeSlot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_down.sub")
		page.passiveSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		page.passiveSlot.SetOverInItemEvent(lambda slotNumber, type=self.GUILD_SKILL_PASSIVE_SLOT: self.OverInItem(slotNumber, type))
		page.passiveSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		page.passiveSlot.SetPressedSlotButtonEvent(lambda slotNumber, type=self.GUILD_SKILL_PASSIVE_SLOT: self.OnUpGuildSkill(slotNumber, type))
		page.passiveSlot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
										"d:/ymir work/ui/game/windows/btn_plus_down.sub")
		page.affectSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		page.affectSlot.SetOverInItemEvent(lambda slotNumber, type=self.GUILD_SKILL_AFFECT_SLOT: self.OverInItem(slotNumber, type))
		page.affectSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		page.btnHealGSP.SetEvent(ui.__mem_func__(self.__OnOpenHealGSPBoard))

		## Passive
		"""
		for i in xrange(len(playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = page.passiveSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST[i]

			page.passiveSlot.SetSkillSlot(slotIndex, skillIndex, 0)
			page.passiveSlot.RefreshSlot()
			guild.SetSkillIndex(slotIndex, i)
		"""

		## Active
		for i in xrange(len(playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = page.activeSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST[i]

			page.activeSlot.SetSkillSlot(slotIndex, skillIndex, 0)
			page.activeSlot.SetCoverButton(slotIndex)
			page.activeSlot.RefreshSlot()
			guild.SetSkillIndex(slotIndex, len(playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST)+i)

	def __MakeGradePage(self):

		lineStep = 18
		page = self.pageWindow["GRADE"]

		page.gradeDict = {}

		for i in xrange(15):

			yPos = 22 + i*lineStep
			index = i+1
			## 13.12.02 아랍 수정
			## GradeNumber
			if localeInfo.IsARABIC():
				gradeNumberSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 310, yPos)
			else:
				gradeNumberSlotImage = ui.MakeImageBox(page, "d:/ymir work/ui/public/Parameter_Slot_00.sub", 14, yPos)
			gradeNumberSlot = ui.MakeTextLine(gradeNumberSlotImage)
			gradeNumberSlot.SetText(str(i+1))
			page.Children.append(gradeNumberSlotImage)
			page.Children.append(gradeNumberSlot)

			## GradeName
			if localeInfo.IsARABIC():
				gradeNameSlot = EditableTextSlot(page, 242, yPos)
			else:
				gradeNameSlot = EditableTextSlot(page, 58, yPos)
			gradeNameSlot.SetEvent(ui.__mem_func__(self.OnOpenChangeGradeName), index)
			page.Children.append(gradeNameSlot)

			## Invite Authority
			event = lambda argSelf=proxy(self), argIndex=index, argAuthority=1<<0: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
			if localeInfo.IsARABIC():
				inviteAuthorityCheckBox = CheckBox(page, 185, yPos, event)
			else:
				inviteAuthorityCheckBox = CheckBox(page, 124, yPos, event)
			page.Children.append(inviteAuthorityCheckBox)

			## DriveOut Authority
			event = lambda argSelf=proxy(self), argIndex=index, argAuthority=1<<1: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
			if localeInfo.IsARABIC():
				driveoutAuthorityCheckBox = CheckBox(page, 128, yPos, event)
			else:
				driveoutAuthorityCheckBox = CheckBox(page, 181, yPos, event)
			page.Children.append(driveoutAuthorityCheckBox)

			## Notice Authority
			event = lambda argSelf=proxy(self), argIndex=index, argAuthority=1<<2: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
			if localeInfo.IsARABIC():
				noticeAuthorityCheckBox = CheckBox(page, 71, yPos, event)
			else:
				noticeAuthorityCheckBox = CheckBox(page, 238, yPos, event)
			page.Children.append(noticeAuthorityCheckBox)

			## Skill Authority
			event = lambda argSelf=proxy(self), argIndex=index, argAuthority=1<<3: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority))
			if localeInfo.IsARABIC():
				skillAuthorityCheckBox = CheckBox(page, 14, yPos, event)
			else:
				skillAuthorityCheckBox = CheckBox(page, 295, yPos, event)
			page.Children.append(skillAuthorityCheckBox)

			gradeSlotList = []
			gradeSlotList.append(gradeNameSlot)
			gradeSlotList.append(inviteAuthorityCheckBox)
			gradeSlotList.append(driveoutAuthorityCheckBox)
			gradeSlotList.append(noticeAuthorityCheckBox)
			gradeSlotList.append(skillAuthorityCheckBox)
			page.gradeDict[index] = gradeSlotList

		masterSlotList = page.gradeDict[1]
		for slot in masterSlotList:
			slot.Disable()

	def CanOpen(self):
		return guild.IsGuildEnable()

	def Open(self):
		self.Show()
		self.SetTop()

		guildID = net.GetGuildID()
		self.largeMarkBox.SetIndex(guildID)
		self.largeMarkBox.SetScale(3)
		## 13.12.02 아랍수정
		if localeInfo.IsARABIC():
			self.largeMarkBox.SetPosition(self.largeMarkBox.GetWidth()+32,1)

	def Close(self):
		self.__CloseAllGuildMemberPageGradeComboBox()
		self.offerDialog.Close()
		self.popupDialog.Hide()
		self.changeGradeNameDialog.Hide()
		self.Hide()

		if self.tooltipSkill:
			self.tooltipSkill.Hide()

		self.pickDialog = None
		self.questionDialog = None
		self.moneyDialog = None

	def Destroy(self):
		self.ClearDictionary()
		self.board = None
		self.pageName = None
		self.tabDict = None
		self.tabButtonDict = None
		self.pickDialog = None
		self.questionDialog = None
		self.markSelectDialog = None
		self.symbolSelectDialog = None

		if self.offerDialog:
			self.offerDialog.Destroy()
			self.offerDialog = None

		if self.popupDialog:
			self.popupDialog.ClearDictionary()
			self.popupDialog = None		

		if self.changeGradeNameDialog:
			self.changeGradeNameDialog.ClearDictionary()
			self.changeGradeNameDialog = None

		self.popupMessage = None
		self.commentSlot = None

		if self.pageWindow:
			for window in self.pageWindow.values():
				window.ClearDictionary()

		self.pageWindow = None
		self.tooltipSkill = None
		self.moneyDialog = None

		self.enemyGuildNameList = []

	def DeleteGuild(self):
		self.RefreshGuildInfoPage()
		self.RefreshGuildBoardPage()
		self.RefreshGuildMemberPage()
		self.RefreshGuildSkillPage()
		self.RefreshGuildGradePage()
		self.Hide()

	def SetSkillToolTip(self, tooltipSkill):
		self.tooltipSkill = tooltipSkill

	def SelectPage(self, arg):

		if "BOARD" == arg:
			self.OnRefreshComments()

		for key, btn in self.tabButtonDict.items():
			if arg != key:
				btn.SetUp()
		for key, img in self.tabDict.items():
			if arg == key:
				img.Show()
			else:
				img.Hide()
		for key, page in self.pageWindow.items():
			if arg == key:
				page.Show()
			else:
				page.Hide()
		self.board.SetTitleName(self.pageName[arg])
		self.__CloseAllGuildMemberPageGradeComboBox()

	def __CloseAllGuildMemberPageGradeComboBox(self):

		page = self.pageWindow["MEMBER"]
		for key, slotList in page.memberDict.items():
			slotList[1].CloseListBox()

	def RefreshGuildInfoPage(self):

		if self.isLoaded==0:
			return
		
		global DISABLE_DECLARE_WAR
		page = self.pageWindow["GUILD_INFO"]
		page.nameSlot.SetText(guild.GetGuildName())
		page.masterNameSlot.SetText(guild.GetGuildMasterName())
		page.guildLevelSlot.SetText(str(guild.GetGuildLevel()))
		if page.guildMoneySlot:
			page.guildMoneySlot.SetText(str(guild.GetGuildMoney()))

		curExp, lastExp = guild.GetGuildExperience()
		curExp *= 100
		lastExp *= 100
		page.curExpSlot.SetText(str(curExp))
		page.lastExpSlot.SetText(str(lastExp))

		curMemberCount, maxMemberCount = guild.GetGuildMemberCount()
		if maxMemberCount== 0xffff:
			page.memberCountSlot.SetText("%d / %s " % (curMemberCount, localeInfo.GUILD_MEMBER_COUNT_INFINITY))
		else:
			page.memberCountSlot.SetText("%d / %d" % (curMemberCount, maxMemberCount))

		page.levelAverageSlot.SetText(str(guild.GetGuildMemberLevelAverage()))

		## 길드장만 길드 마크와 길드전 신청 버튼을 볼 수 있음
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()

		if mainCharacterName == masterName:
			page.uploadMarkButton.Show()

			if DISABLE_DECLARE_WAR:
				page.declareWarButton.Hide()
			else:
				page.declareWarButton.Show()

			if guild.HasGuildLand():
				page.uploadSymbolButton.Show()
			else:
				page.uploadSymbolButton.Hide()
		else:
			page.uploadMarkButton.Hide()
			page.declareWarButton.Hide()
			page.uploadSymbolButton.Hide()

		## Refresh 시에 길드전 정보 업데이트
		for i in xrange(guild.ENEMY_GUILD_SLOT_MAX_COUNT):
			name = guild.GetEnemyGuildName(i)
			nameTextLine = self.enemyGuildNameList[i]
			if name:
				nameTextLine.SetText(name)
			else:
				nameTextLine.SetText(localeInfo.GUILD_INFO_ENEMY_GUILD_EMPTY)

	def __GetGuildBoardCommentData(self, index):
		commentID, chrName, comment = guild.GetGuildBoardCommentData(index)
		if 0==commentID:
			if ""==chrName:
				chrName=localeInfo.UI_NONAME
			if ""==comment:
				comment=localeInfo.UI_NOCONTENTS

		return commentID, chrName, comment

	def RefreshGuildBoardPage(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["BOARD"]

		self.BOARD_LINE_MAX_NUM = 12
		lineIndex = 0

		commentCount = guild.GetGuildBoardCommentCount()
		for i in xrange(commentCount):

			commentID, chrName, comment = self.__GetGuildBoardCommentData(i)

			if not comment:
				continue

			slotList = page.boardDict[lineIndex]

			if "!" == comment[0]:
				slotList[0].Show()
				slotList[1].SetText(chrName)
				slotList[2].SetText(comment[1:])

			else:
				slotList[0].Hide()
				slotList[1].SetText(chrName)
				slotList[2].SetText(comment)

			lineIndex += 1

		for i in xrange(self.BOARD_LINE_MAX_NUM - lineIndex):
			slotList = page.boardDict[lineIndex+i]
			slotList[0].Hide()
			slotList[1].SetText("")
			slotList[2].SetText("")

	def RefreshGuildMemberPage(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["MEMBER"]

		## ScrollBar
		count = guild.GetMemberCount()
		if count > self.MEMBER_LINE_COUNT:
			page.scrollBar.SetMiddleBarSize(float(self.MEMBER_LINE_COUNT) / float(count))
			page.scrollBar.Show()
		else:
			page.scrollBar.Hide()
		self.RefreshGuildMemberPageGradeComboBox()
		self.RefreshGuildMemberPageMemberList()

	def RefreshGuildMemberPageMemberList(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["MEMBER"]

		for line, slotList in page.memberDict.items():

			gradeComboBox = slotList[1]
			gradeComboBox.Disable()

			if not guild.IsMember(line):
				slotList[0].SetText("")
				slotList[2].SetText("")
				slotList[3].SetText("")
				slotList[4].SetText("")
				slotList[5].SetCheck(False)
				continue

			pid, name, grade, race, level, offer, general = self.GetMemberData(line)
			if pid < 0:
				continue

			job = chr.RaceToJob(race)

			guildExperienceSummary = guild.GetGuildExperienceSummary()

			offerPercentage = 0
			if guildExperienceSummary > 0:
				offerPercentage = int(float(offer) / float(guildExperienceSummary) * 100.0)

			slotList[0].SetText(name)
			slotList[2].SetText(self.JOB_NAME.get(job, "?"))
			slotList[3].SetText(str(level))
			slotList[4].SetText(str(offerPercentage) + "%")
			slotList[5].SetCheck(general)
			gradeComboBox.SetCurrentItem(guild.GetGradeName(grade))
			if 1 != grade:
				gradeComboBox.Enable()

	def RefreshGuildMemberPageGradeComboBox(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["MEMBER"]

		self.CAN_CHANGE_GRADE_COUNT = 15 - 1
		for key, slotList in page.memberDict.items():

			gradeComboBox = slotList[1]
			gradeComboBox.Disable()

			if not guild.IsMember(key):
				continue

			pid, name, grade, job, level, offer, general = self.GetMemberData(key)
			if pid < 0:
				continue

			gradeComboBox.ClearItem()
			for i in xrange(self.CAN_CHANGE_GRADE_COUNT):
				gradeComboBox.InsertItem(i+2, guild.GetGradeName(i+2))
			gradeComboBox.SetCurrentItem(guild.GetGradeName(grade))
			if 1 != grade:
				gradeComboBox.Enable()

	def RefreshGuildSkillPage(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["SKILL"]

		curPoint, maxPoint = guild.GetDragonPowerPoint()
		maxPoint = max(maxPoint, 1)
		page.gpValue.SetText(str(curPoint) + " / " + str(maxPoint))

		percentage = (float(curPoint) / float(maxPoint) * 100) * (float(173) / float(95))
		page.gpGauge.SetPercentage(int(percentage), 100)

		skillPoint = guild.GetGuildSkillPoint()
		page.skillPoint.SetText(str(skillPoint))

		page.passiveSlot.HideAllSlotButton()
		page.activeSlot.HideAllSlotButton()

		## Passive
		"""
		for i in xrange(len(playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = page.passiveSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST[i]
			skillLevel = guild.GetSkillLevel(slotIndex)
			skillMaxLevel = skill.GetSkillMaxLevel(skillIndex)

			page.passiveSlot.SetSlotCount(slotIndex, skillLevel)
			if skillPoint > 0:
				if skillLevel < skillMaxLevel:
					page.passiveSlot.ShowSlotButton(slotIndex)
		"""

		## Active
		for i in xrange(len(playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = page.activeSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST[i]
			skillLevel = guild.GetSkillLevel(slotIndex)
			skillMaxLevel = skill.GetSkillMaxLevel(skillIndex)

			page.activeSlot.SetSlotCount(slotIndex, skillLevel)

			if skillLevel <= 0:
				page.activeSlot.DisableCoverButton(slotIndex)
			else:
				page.activeSlot.EnableCoverButton(slotIndex)

			if skillPoint > 0:
				if skillLevel < skillMaxLevel:
					page.activeSlot.ShowSlotButton(slotIndex)

	def RefreshGuildGradePage(self):

		if self.isLoaded==0:
			return

		page = self.pageWindow["GRADE"]

		for key, slotList in page.gradeDict.items():
			name, authority = guild.GetGradeData(int(key))

			slotList[self.GRADE_SLOT_NAME].SetText(name)
			slotList[self.GRADE_ADD_MEMBER_AUTHORITY].SetCheck(authority & guild.AUTH_ADD_MEMBER)
			slotList[self.GRADE_REMOVE_MEMBER_AUTHORITY].SetCheck(authority & guild.AUTH_REMOVE_MEMBER)
			slotList[self.GRADE_NOTICE_AUTHORITY].SetCheck(authority & guild.AUTH_NOTICE)
			slotList[self.GRADE_SKILL_AUTHORITY].SetCheck(authority & guild.AUTH_SKILL)

	## GuildInfo

	def __PopupMessage(self, msg):
		self.popupMessage.SetText(msg)
		self.popupDialog.SetTop()
		self.popupDialog.Show()

	def __OnClickSelectGuildMarkButton(self):
		if guild.GetGuildLevel() < int(localeInfo.GUILD_MARK_MIN_LEVEL):
			self.__PopupMessage(localeInfo.GUILD_MARK_NOT_ENOUGH_LEVEL)
		elif not guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			self.__PopupMessage(localeInfo.GUILD_NO_NOTICE_PERMISSION)
		else:
			self.markSelectDialog.Open()

	def __OnClickSelectGuildSymbolButton(self):
		if guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			self.symbolSelectDialog.Open()
		else:
			self.__PopupMessage(localeInfo.GUILD_NO_NOTICE_PERMISSION)

	def __OnClickDeclareWarButton(self):
		inputDialog = DeclareGuildWarDialog()		
		inputDialog.Open()
		self.inputDialog = inputDialog
	
	def __OnSelectMark(self, markFileName):
		ret = net.UploadMark("upload/"+markFileName)

		# MARK_BUG_FIX
		if net.ERROR_MARK_UPLOAD_NEED_RECONNECT == ret:
			self.__PopupMessage(localeInfo.UPLOAD_MARK_UPLOAD_NEED_RECONNECT);					

		return ret
		# END_OF_MARK_BUG_FIX

	def __OnSelectSymbol(self, symbolFileName):
		net.UploadSymbol("upload/"+symbolFileName)

	def __OnClickOfferButton(self):

		curEXP = unsigned32(player.GetStatus(player.EXP))

		if curEXP <= 100:
			self.__PopupMessage(localeInfo.GUILD_SHORT_EXP);
			return

		self.offerDialog.Open(curEXP, 100)

	def __OnClickDepositButton(self):
		moneyDialog = uiPickMoney.PickMoneyDialog()
		moneyDialog.LoadDialog()
		moneyDialog.SetMax(6)
		moneyDialog.SetTitleName(localeInfo.GUILD_DEPOSIT)
		moneyDialog.SetAcceptEvent(ui.__mem_func__(self.OnDeposit))
		moneyDialog.Open(player.GetMoney())
		self.moneyDialog = moneyDialog

	def __OnClickWithdrawButton(self):
		moneyDialog = uiPickMoney.PickMoneyDialog()
		moneyDialog.LoadDialog()
		moneyDialog.SetMax(6)
		moneyDialog.SetTitleName(localeInfo.GUILD_WITHDRAW)
		moneyDialog.SetAcceptEvent(ui.__mem_func__(self.OnWithdraw))
		moneyDialog.Open(guild.GetGuildMoney())
		self.moneyDialog = moneyDialog

	def __OnBlock(self):
		popup = uiCommon.PopupDialog()
		popup.SetText(localeInfo.NOT_YET_SUPPORT)
		popup.SetAcceptEvent(self.__OnClosePopupDialog)
		popup.Open()
		self.popup = popup

	def __OnClosePopupDialog(self):
		self.popup = None

	def OnDeposit(self, money):
		net.SendGuildDepositMoneyPacket(money)

	def OnWithdraw(self, money):
		net.SendGuildWithdrawMoneyPacket(money)

	def OnOffer(self, exp):
		net.SendGuildOfferPacket(exp)

	## Board
	def OnPostComment(self):

		text = self.commentSlot.GetText()
		if not text:
			return False

		net.SendGuildPostCommentPacket(text[:50])
		self.commentSlot.SetText("")
		return True

	def OnDeleteComment(self, index):

		commentID, chrName, comment = self.__GetGuildBoardCommentData(index)
		net.SendGuildDeleteCommentPacket(commentID)

	def OnRefreshComments(self):
		net.SendGuildRefreshCommentsPacket(0)

	def OnKeyDownInBoardPage(self, key):
		if key == 63:
			self.OnRefreshComments()
		return True

	## Member
	## OnEnableGeneral
	def OnChangeMemberGrade(self, lineIndex, gradeNumber):
		PID = guild.MemberIndexToPID(lineIndex + self.memberLinePos)
		net.SendGuildChangeMemberGradePacket(PID, gradeNumber)

	def OnEnableGeneral(self, lineIndex):
		if not guild.IsMember(lineIndex):
			return

		pid, name, grade, job, level, offer, general = self.GetMemberData(lineIndex)
		if pid < 0:
			return

		net.SendGuildChangeMemberGeneralPacket(pid, 1 - general)

	## Grade
	def OnOpenChangeGradeName(self, arg):
		self.changeGradeNameDialog.SetGradeNumber(arg)
		self.changeGradeNameDialog.Open()

	def OnChangeGradeName(self):
		self.changeGradeNameDialog.Hide()
		gradeNumber = self.changeGradeNameDialog.GetGradeNumber()
		gradeName = self.changeGradeNameDialog.GetGradeName()

		if len(gradeName) == 0:
			gradeName = localeInfo.GUILD_DEFAULT_GRADE

		net.SendGuildChangeGradeNamePacket(gradeNumber, gradeName)
		return True

	def OnCheckAuthority(self, argIndex, argAuthority):
		name, authority = guild.GetGradeData(argIndex)
		net.SendGuildChangeGradeAuthorityPacket(argIndex, authority ^ argAuthority)

	def OnScrollMemberLine(self):
		scrollBar = self.pageWindow["MEMBER"].scrollBar
		pos = scrollBar.GetPos()

		count = guild.GetMemberCount()
		newLinePos = int(float(count - self.MEMBER_LINE_COUNT) * pos)

		if newLinePos != self.memberLinePos:
			self.memberLinePos = newLinePos
			self.RefreshGuildMemberPageMemberList()
			self.__CloseAllGuildMemberPageGradeComboBox()

	def GetMemberData(self, localPos):
		return guild.GetMemberData(localPos + self.memberLinePos)

	## Guild Skill
	def __OnOpenHealGSPBoard(self):

		curPoint, maxPoint = guild.GetDragonPowerPoint()

		if maxPoint - curPoint <= 0:
			self.__PopupMessage(localeInfo.GUILD_CANNOT_HEAL_GSP_ANYMORE)
			return

		pickDialog = uiPickMoney.PickMoneyDialog()
		pickDialog.LoadDialog()
		pickDialog.SetMax(9)
		pickDialog.SetTitleName(localeInfo.GUILD_HEAL_GSP)
		pickDialog.SetAcceptEvent(ui.__mem_func__(self.__OnOpenHealGSPQuestionDialog))
		pickDialog.Open(maxPoint - curPoint, 1)
		self.pickDialog = pickDialog

	def __OnOpenHealGSPQuestionDialog(self, healGSP):

		money = healGSP * constInfo.GUILD_MONEY_PER_GSP

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.GUILD_DO_YOU_HEAL_GSP % (money, healGSP))
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.__OnHealGSP))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.__OnCloseQuestionDialog))
		questionDialog.SetWidth(400)
		questionDialog.Open()
		questionDialog.healGSP = healGSP
		self.questionDialog = questionDialog

	def __OnHealGSP(self):
		net.SendGuildChargeGSPPacket(self.questionDialog.healGSP)
		self.__OnCloseQuestionDialog()

	def __OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()
		self.questionDialog = None

	def OnPickUpGuildSkill(self, skillSlotIndex, type):

		mouseController = mouseModule.mouseController

		if False == mouseController.isAttached():

			skillIndex = player.GetSkillIndex(skillSlotIndex)
			skillLevel = guild.GetSkillLevel(skillSlotIndex)

			if skill.CanUseSkill(skillIndex) and skillLevel > 0:

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, skillSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, skillSlotIndex, skillIndex)

		else:
			mouseController.DeattachObject()

	def OnUseGuildSkill(self, slotNumber, type):
		skillIndex = player.GetSkillIndex(slotNumber)
		skillLevel = guild.GetSkillLevel(slotNumber)

		if skillLevel <= 0:
			return

		player.UseGuildSkill(slotNumber)

	def OnUpGuildSkill(self, slotNumber, type):
		skillIndex = player.GetSkillIndex(slotNumber)
		net.SendChatPacket("/gskillup " + str(skillIndex))

	def OnUseSkill(self, slotNumber, coolTime):

		if self.isLoaded==0:
			return

		page = self.pageWindow["SKILL"]

		if page.activeSlot.HasSlot(slotNumber):
			page.activeSlot.SetSlotCoolTime(slotNumber, coolTime)

	def OnStartGuildWar(self, guildSelf, guildOpp):

		if self.isLoaded==0:
			return

		if guild.GetGuildID() != guildSelf:
			return

		guildName = guild.GetGuildName(guildOpp)
		for guildNameTextLine in self.enemyGuildNameList:
			if localeInfo.GUILD_INFO_ENEMY_GUILD_EMPTY == guildNameTextLine.GetText():
				guildNameTextLine.SetText(guildName)
				return

	def OnEndGuildWar(self, guildSelf, guildOpp):

		if self.isLoaded==0:
			return

		if guild.GetGuildID() != guildSelf:
			return

		guildName = guild.GetGuildName(guildOpp)
		for guildNameTextLine in self.enemyGuildNameList:
			if guildName == guildNameTextLine.GetText():
				guildNameTextLine.SetText(localeInfo.GUILD_INFO_ENEMY_GUILD_EMPTY)
				return

	## ToolTip
	def OverInItem(self, slotNumber, type):

		if mouseModule.mouseController.isAttached():
			return

		if None != self.tooltipSkill:
			skillIndex = player.GetSkillIndex(slotNumber)
			skillLevel = guild.GetSkillLevel(slotNumber)

			self.tooltipSkill.SetSkill(skillIndex, skillLevel)

	def OverOutItem(self):
		if None != self.tooltipSkill:
			self.tooltipSkill.HideToolTip()

	def OnPressEscapeKey(self):
		self.Close()
		return True


class BuildGuildBuildingWindow(ui.ScriptWindow):

	if localeInfo.IsJAPAN():
		GUILD_CATEGORY_LIST = (
				("HEADQUARTER", "딈멳뙕뭱븿"),
				("FACILITY", "둮뮗뙕뭱븿"),
				("OBJECT", "궩궻뫜"),
			)
	elif localeInfo.IsYMIR() or localeInfo.IsWE_KOREA():
		GUILD_CATEGORY_LIST = (
				("HEADQUARTER", "본건물"),
				("FACILITY", "기능건물"),
				("OBJECT", "조경물"),
			)
	elif localeInfo.IsEUROPE() or localeInfo.IsHONGKONG():
		GUILD_CATEGORY_LIST = (
				("HEADQUARTER", localeInfo.GUILD_HEADQUARTER),
				("FACILITY", 	localeInfo.GUILD_FACILITY),
				("OBJECT", 	localeInfo.GUILD_OBJECT),
			)
	else:
		try :
			GUILD_CATEGORY_LIST = (
					("HEADQUARTER", localeInfo.GUILD_HEADQUARTER),
					("FACILITY", 	localeInfo.GUILD_FACILITY),
					("OBJECT", 	localeInfo.GUILD_OBJECT),
				)
		except:
			GUILD_CATEGORY_LIST = (
					("HEADQUARTER", "Main Building"),
					("FACILITY", "Facility"),
					("OBJECT", "Object"),
				)

	MODE_VIEW = 0
	MODE_POSITIONING = 1
	MODE_PREVIEW = 2

	BUILDING_ALPHA = 0.55

	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)

	START_INSTANCE_INDEX = 123450
	#WALL_SET_INSTANCE = 14105

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

		self.closeEvent = None
		self.popup = None
		self.mode = self.MODE_VIEW
		self.race = 0
		self.type = None
		self.x = 0
		self.y = 0
		self.z = 0
		self.rot_x = 0
		self.rot_y = 0
		self.rot_z = 0
		self.rot_x_limit = 0
		self.rot_y_limit = 0
		self.rot_z_limit = 0
		self.needMoney = 0
		self.needStoneCount = 0
		self.needLogCount = 0
		self.needPlywoodCount = 0

		#self.index = 0
		self.indexList = []
		self.raceList = []
		self.posList = []
		self.rotList = []

		index = 0
		for category in self.GUILD_CATEGORY_LIST:
			self.categoryList.InsertItem(index, category[1])
			index += 1

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()
			if localeInfo.IsARABIC():
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "buildguildbuildingwindow.py")
			elif localeInfo.IsVIETNAM():
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "buildguildbuildingwindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "uiscript/buildguildbuildingwindow.py")
		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.categoryList = getObject("CategoryList")
			self.buildingList = getObject("BuildingList")
			self.listScrollBar = getObject("ListScrollBar")
			self.positionButton = getObject("PositionButton")
			self.previewButton = getObject("PreviewButton")
			self.posValueX = getObject("BuildingPositionXValue")
			self.posValueY = getObject("BuildingPositionYValue")
			self.ctrlRotationX = getObject("BuildingRotationX")
			self.ctrlRotationY = getObject("BuildingRotationY")
			self.ctrlRotationZ = getObject("BuildingRotationZ")
			self.buildingPriceValue = getObject("BuildingPriceValue")
			self.buildingMaterialStoneValue = getObject("BuildingMaterialStoneValue")
			self.buildingMaterialLogValue = getObject("BuildingMaterialLogValue")
			self.buildingMaterialPlywoodValue = getObject("BuildingMaterialPlywoodValue")

			self.positionButton.SetEvent(ui.__mem_func__(self.__OnSelectPositioningMode))
			self.previewButton.SetToggleDownEvent(ui.__mem_func__(self.__OnEnterPreviewMode))
			self.previewButton.SetToggleUpEvent(ui.__mem_func__(self.__OnLeavePreviewMode))
			self.ctrlRotationX.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.ctrlRotationY.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.ctrlRotationZ.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.listScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollBuildingList))

			getObject("CategoryList").SetEvent(ui.__mem_func__(self.__OnSelectCategory))
			getObject("BuildingList").SetEvent(ui.__mem_func__(self.__OnSelectBuilding))
			getObject("AcceptButton").SetEvent(ui.__mem_func__(self.Build))
			getObject("CancelButton").SetEvent(ui.__mem_func__(self.Close))
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("BuildGuildBuildingWindow.__LoadWindow - BindObject")

	def __CreateWallBlock(self, race, x, y, rot=0.0 ):
		idx = self.START_INSTANCE_INDEX + len(self.indexList)
		self.indexList.append(idx)
		self.raceList.append(race)
		self.posList.append((x, y))
		self.rotList.append(rot)
		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)
		chr.SetRotationAll(0.0, 0.0, rot)

		self.ctrlRotationX.SetSliderPos(0.5)
		self.ctrlRotationY.SetSliderPos(0.5)
		self.ctrlRotationZ.SetSliderPos(0.5)

	def __GetObjectSize(self, race):
		idx = self.START_INSTANCE_INDEX + 1000
		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		sx, sy, ex, ey = chr.GetBoundBoxOnlyXY(idx)
		chr.DeleteInstance(idx)
		return sx, sy, ex, ey	

	def __GetBuildInPosition(self):
			
		zList = []
		zList.append( background.GetHeight(self.x+self.sxPos, self.y+self.syPos) )		
		zList.append( background.GetHeight(self.x+self.sxPos, self.y+self.eyPos) )
		zList.append( background.GetHeight(self.x+self.exPos, self.y+self.syPos) )
		zList.append( background.GetHeight(self.x+self.exPos, self.y+self.eyPos) )
		zList.append( background.GetHeight(self.x+(self.exPos+self.sxPos)/2, self.y+(self.eyPos+self.syPos)/2) )
		zList.sort()
		return zList[3]

	def __CreateBuildInInstance(self,race):
		
		self.__DeleteInstance()

		object_base = race - race%10

		door_minX, door_minY, door_maxX, door_maxY = self.__GetObjectSize(object_base+4)
		corner_minX, corner_minY, corner_maxX, corner_maxY = self.__GetObjectSize(object_base+1)
		line_minX, line_minY, line_maxX, line_maxY = self.__GetObjectSize(object_base+2)
		line_width = line_maxX - line_minX
		line_width_half = line_width / 2

		X_SIZE_STEP = 2 * 2 ## 2의 단위로만 증가해야 함
		Y_SIZE_STEP = 8
		sxPos = door_maxX - corner_minX + (line_width_half*X_SIZE_STEP)
		exPos = -sxPos
		syPos = 0
		eyPos = -(corner_maxY*2 + line_width*Y_SIZE_STEP)
		
		self.sxPos = sxPos
		self.syPos = syPos
		self.exPos = exPos
		self.eyPos = eyPos

		z = self.__GetBuildInPosition()
		
		## Door
		self.__CreateWallBlock(object_base+4, 0.0, syPos)

		## Corner
		self.__CreateWallBlock(object_base+1, sxPos, syPos)
		self.__CreateWallBlock(object_base+1, exPos, syPos, 270.0)
		self.__CreateWallBlock(object_base+1, sxPos, eyPos, 90.0)
		self.__CreateWallBlock(object_base+1, exPos, eyPos,180.0 )

		## Line
		lineBlock = object_base+2
		line_startX = -door_maxX - line_minX - (line_width_half*X_SIZE_STEP)
		self.__CreateWallBlock(lineBlock, line_startX, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*1, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*2, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*3, eyPos)
		for i in xrange(X_SIZE_STEP):
			self.__CreateWallBlock(lineBlock, line_startX+line_width*(3+i+1), eyPos)
		for i in xrange(X_SIZE_STEP/2):
			self.__CreateWallBlock(lineBlock, door_minX - line_maxX - line_width*i, syPos)
			self.__CreateWallBlock(lineBlock, door_maxX - line_minX + line_width*i, syPos)
		for i in xrange(Y_SIZE_STEP):
			self.__CreateWallBlock(lineBlock, sxPos, line_minX + corner_minX - line_width*i, 90.0)
			self.__CreateWallBlock(lineBlock, exPos, line_minX + corner_minX - line_width*i, 90.0)

		self.SetBuildingPosition(int(self.x), int(self.y), self.__GetBuildInPosition())

	def __DeleteInstance(self):
		if not self.indexList:
			return

		for index in self.indexList:
			chr.DeleteInstance(index)

		self.indexList = []
		self.raceList = []
		self.posList = []
		self.rotList = []

	def __CreateInstance(self, race):

		self.__DeleteInstance()

		self.race = race

		idx = self.START_INSTANCE_INDEX
		self.indexList.append(idx)
		self.posList.append((0, 0))
		self.rotList.append(0)

		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)

		self.SetBuildingPosition(int(self.x), int(self.y), 0)
		self.ctrlRotationX.SetSliderPos(0.5)
		self.ctrlRotationY.SetSliderPos(0.5)
		self.ctrlRotationZ.SetSliderPos(0.5)

	def Build(self):

		if not self.__IsEnoughMoney():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MONEY)
			return
		if not self.__IsEnoughMaterialStone():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return
		if not self.__IsEnoughMaterialLog():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return
		if not self.__IsEnoughMaterialPlywood():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return

		## /build c vnum x y x_rot y_rot z_rot
		## /build d vnum		
		if "BUILDIN" == self.type:
			for i in xrange(len(self.raceList)):
				race = self.raceList[i]
				xPos, yPos = self.posList[i]
				rot = self.rotList[i]
				net.SendChatPacket("/build c %d %d %d %d %d %d" % (race, int(self.x+xPos), int(self.y+yPos), self.rot_x, self.rot_y, rot))
		else:
			net.SendChatPacket("/build c %d %d %d %d %d %d" % (self.race, int(self.x), int(self.y), self.rot_x, self.rot_y, self.rot_z))

		self.Close()

	def Open(self):
		x, y, z = player.GetMainCharacterPosition()
		app.SetCameraSetting(int(x), int(-y), int(z), 3000, 0, 30)

		background.VisibleGuildArea()

		self.x = x
		self.y = y
		self.z = z
		self.categoryList.SelectItem(0)
		self.buildingList.SelectItem(0)
		self.SetTop()
		self.Show()
		self.__DisablePCBlocker()

		import debugInfo
		if debugInfo.IsDebugMode():
			self.categoryList.SelectItem(2)
			self.buildingList.SelectItem(0)

	def Close(self):

		self.__DeleteInstance()

		background.DisableGuildArea()

		self.Hide()
		self.__OnClosePopupDialog()
		self.__EnablePCBlocker()
		self.__UnlockCameraMoving()
		if self.closeEvent:
			self.closeEvent()

	def Destory(self):
		self.Close()

		self.ClearDictionary()
		self.board = None
		self.categoryList = None
		self.buildingList = None
		self.listScrollBar = None
		self.positionButton = None
		self.previewButton = None
		self.posValueX = None
		self.posValueY = None
		self.ctrlRotationX = None
		self.ctrlRotationY = None
		self.ctrlRotationZ = None
		self.buildingPriceValue = None
		self.buildingMaterialStoneValue = None
		self.buildingMaterialLogValue = None
		self.buildingMaterialPlywoodValue = None
		self.closeEvent = None

	def SetCloseEvent(self, event):
		self.closeEvent = event

	def __PopupDialog(self, text):
		popup = uiCommon.PopupDialog()
		popup.SetText(text)
		popup.SetAcceptEvent(self.__OnClosePopupDialog)
		popup.Open()
		self.popup = popup

	def __OnClosePopupDialog(self):
		self.popup = None

	def __EnablePCBlocker(self):
		## PC Blocker 처리를 켠다. (투명해짐)
		chr.SetInstanceType(chr.INSTANCE_TYPE_BUILDING)

		for idx in self.indexList:
			chr.SetBlendRenderMode(idx, 1.0)

	def __DisablePCBlocker(self):
		## PC Blocker 처리를 끈다. (안투명해짐)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		for idx in self.indexList:
			chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)

	def __OnSelectPositioningMode(self):		
		if self.MODE_PREVIEW == self.mode:
			self.positionButton.SetUp()
			return

		self.mode = self.MODE_POSITIONING
		self.Hide()

	def __OnEnterPreviewMode(self):

		if self.MODE_POSITIONING == self.mode:
			self.previewButton.SetUp()
			return

		self.mode = self.MODE_PREVIEW
		self.positionButton.SetUp()
		self.__UnlockCameraMoving()
		self.__EnablePCBlocker()

	def __OnLeavePreviewMode(self):
		self.__RestoreViewMode()

	def __RestoreViewMode(self):
		self.__DisablePCBlocker()
		self.__LockCameraMoving()
		self.mode = self.MODE_VIEW
		self.positionButton.SetUp()
		self.previewButton.SetUp()

	def __IsEnoughMoney(self):

		if app.IsEnableTestServerFlag():
			return True

		curMoney = player.GetMoney()
		if curMoney < self.needMoney:
			return False
		return True

	def __IsEnoughMaterialStone(self):

		if app.IsEnableTestServerFlag():
			return True

		curStoneCount = player.GetItemCountByVnum(MATERIAL_STONE_ID)
		if curStoneCount < self.needStoneCount:
			return False
		return True

	def __IsEnoughMaterialLog(self):

		if app.IsEnableTestServerFlag():
			return True

		curLogCount = player.GetItemCountByVnum(MATERIAL_LOG_ID)
		if curLogCount < self.needLogCount:
			return False
		return True

	def __IsEnoughMaterialPlywood(self):

		if app.IsEnableTestServerFlag():
			return True

		curPlywoodCount = player.GetItemCountByVnum(MATERIAL_PLYWOOD_ID)
		if curPlywoodCount < self.needPlywoodCount:
			return False
		return True

	def __OnSelectCategory(self):
		self.listScrollBar.SetPos(0.0)
		self.__RefreshItem()

	def __SetBuildingData(self, data):
		self.buildingPriceValue.SetText(NumberToMoneyString(data["PRICE"]))

		self.needMoney = int(data["PRICE"])

		materialList = data["MATERIAL"]
		self.needStoneCount = int(materialList[MATERIAL_STONE_INDEX])
		self.needLogCount = int(materialList[MATERIAL_LOG_INDEX])
		self.needPlywoodCount = int(materialList[MATERIAL_PLYWOOD_INDEX])

		if (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/ca") and (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/br"):
			self.buildingMaterialStoneValue.SetText(materialList[MATERIAL_STONE_INDEX])
			self.buildingMaterialLogValue.SetText(materialList[MATERIAL_LOG_INDEX] )
			self.buildingMaterialPlywoodValue.SetText(materialList[MATERIAL_PLYWOOD_INDEX])
		else:
			self.buildingMaterialStoneValue.SetText(materialList[MATERIAL_STONE_INDEX] + localeInfo.THING_COUNT)
			self.buildingMaterialLogValue.SetText(materialList[MATERIAL_LOG_INDEX] + localeInfo.THING_COUNT)
			self.buildingMaterialPlywoodValue.SetText(materialList[MATERIAL_PLYWOOD_INDEX] + localeInfo.THING_COUNT)
		if self.__IsEnoughMoney():
			self.buildingPriceValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingPriceValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialStone():
			self.buildingMaterialStoneValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialStoneValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialLog():
			self.buildingMaterialLogValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialLogValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialPlywood():
			self.buildingMaterialPlywoodValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialPlywoodValue.SetPackedFontColor(self.DISABLE_COLOR)

		self.rot_x_limit = data["X_ROT_LIMIT"]
		self.rot_y_limit = data["Y_ROT_LIMIT"]
		self.rot_z_limit = data["Z_ROT_LIMIT"]
		self.ctrlRotationX.Enable()
		self.ctrlRotationY.Enable()
		self.ctrlRotationZ.Enable()
		if 0 == self.rot_x_limit:
			self.ctrlRotationX.Disable()
		if 0 == self.rot_y_limit:
			self.ctrlRotationY.Disable()
		if 0 == self.rot_z_limit:
			self.ctrlRotationZ.Disable()

	def __OnSelectBuilding(self):
		buildingIndex = self.buildingList.GetSelectedItem()
		if buildingIndex >= len(BUILDING_DATA_LIST):
			return

		categoryIndex = self.categoryList.GetSelectedItem()
		if categoryIndex >= len(self.GUILD_CATEGORY_LIST):
			return
		selectedType = self.GUILD_CATEGORY_LIST[categoryIndex][0]

		index = 0
		for data in BUILDING_DATA_LIST:
			type = data["TYPE"]
			vnum = data["VNUM"]
			if selectedType != type:
				continue
			
			if index == buildingIndex:
				self.type = type
				if "BUILDIN" == self.type:
					self.__CreateBuildInInstance(vnum)
				else:
					self.__CreateInstance(vnum)

				self.__SetBuildingData(data)

			index += 1

	def __OnScrollBuildingList(self):
		viewItemCount = self.buildingList.GetViewItemCount()
		itemCount = self.buildingList.GetItemCount()
		pos = self.listScrollBar.GetPos() * (itemCount-viewItemCount)
		self.buildingList.SetBasePos(int(pos))

	def __OnChangeRotation(self):
		self.rot_x = self.ctrlRotationX.GetSliderPos() * self.rot_x_limit - self.rot_x_limit/2
		self.rot_y = self.ctrlRotationY.GetSliderPos() * self.rot_y_limit - self.rot_y_limit/2
		self.rot_z = (self.ctrlRotationZ.GetSliderPos() * 360 + 180) % 360
		if "BUILDIN" == self.type:
			chr.SetRotationAll(self.rot_x, self.rot_y, self.rot_z)
		else:
			chr.SetRotationAll(self.rot_x, self.rot_y, self.rot_z)

	def __LockCameraMoving(self):
		app.SetCameraSetting(int(self.x), int(-self.y), int(self.z), 3000, 0, 30)

	def __UnlockCameraMoving(self):
		app.SetDefaultCamera()

	def __RefreshItem(self):

		self.buildingList.ClearItem()

		categoryIndex = self.categoryList.GetSelectedItem()
		if categoryIndex >= len(self.GUILD_CATEGORY_LIST):
			return
		selectedType = self.GUILD_CATEGORY_LIST[categoryIndex][0]

		index = 0
		for data in BUILDING_DATA_LIST:
			if selectedType != data["TYPE"]:
				continue

			if data["SHOW"]:
				self.buildingList.InsertItem(index, data["LOCAL_NAME"])

			index += 1

		self.buildingList.SelectItem(0)

		if self.buildingList.GetItemCount() < self.buildingList.GetViewItemCount():
			self.buildingList.SetSize(120, self.buildingList.GetHeight())
			self.buildingList.LocateItem()
			self.listScrollBar.Hide()
		else:
			self.buildingList.SetSize(105, self.buildingList.GetHeight())
			self.buildingList.LocateItem()
			self.listScrollBar.Show()

	def SettleCurrentPosition(self):
		guildID = miniMap.GetGuildAreaID(self.x, self.y)

		import debugInfo
		if debugInfo.IsDebugMode():
			guildID = player.GetGuildID()

		if guildID != player.GetGuildID():
			return

		self.__RestoreViewMode()
		self.__LockCameraMoving()
		self.Show()

	def SetBuildingPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.posValueX.SetText(str(int(x)))
		self.posValueY.SetText(str(int(y)))
		
		for i in xrange(len(self.indexList)):
			idx = self.indexList[i]
			xPos, yPos = self.posList[i]

			chr.SelectInstance(idx)
			if 0 != z:
				self.z = z
				chr.SetPixelPosition(int(x+xPos), int(y+yPos), int(z))
			else:
				chr.SetPixelPosition(int(x+xPos), int(y+yPos))

	def IsPositioningMode(self):
		if self.MODE_POSITIONING == self.mode:
			return True
		return False

	def IsPreviewMode(self):
		if self.MODE_PREVIEW == self.mode:
			return True
		return False

	def OnPressEscapeKey(self):
		self.Close()
		return True

"""
- 프로토콜

게임돌입시:
	RecvLandPacket:
		CPythonMiniMap::RegisterGuildArea

게임이동중:
	PythonPlayer::Update()
		CPythonPlayer::__Update_NotifyGuildAreaEvent()
			game.py.BINARY_Guild_EnterGuildArea
				uigameButton.GameButtonWindow.ShowBuildButton()
			game.py.BINARY_Guild_ExitGuildArea
				uigameButton.GameButtonWindow.HideBuildButton()

BuildButton:
!길드장인지 처리 없음
!건물이 있어도 짓기 버튼은 있음

!건물이 임시로 사용하는 VID 는 서버가 보내주는 것과 혼동될 염려가 있음
!건물 VNUM 은 BuildGuildBuildingWindow.BUILDING_VNUM_LIST 를 이용해 변환

!건물 지을때는 /build c(reate)
!건물 부술때는 /build d(estroy)
!rotation 의 단위는 degree

	interfaceModule.interface.__OnClickBuildButton:
		interfaceModule.interface.BUILD_OpenWindow:

AcceptButton:
	BuildGuildBuildingWindow.Build:
		net.SendChatPacket("/build c vnum x y x_rot y_rot z_rot")

PreviewButton:
	__OnPreviewMode:
	__RestoreViewMode:

건물 부수기:
	uiTarget.TargetBoard.__OnDestroyBuilding
		net.SendChatPacket("/build d vid")
"""

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui

	#wndMgr.SetOutlineFlag(True)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2 CLOSED BETA", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	import chrmgr
	chrmgr.CreateRace(0)
	chrmgr.SelectRace(0)
	chrmgr.SetPathName("d:/ymir Work/pc/warrior/")
	chrmgr.LoadRaceData("warrior.msm")
	chrmgr.SetPathName("d:/ymir work/pc/warrior/general/")
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_GENERAL)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_WAIT, "wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_GENERAL, chr.MOTION_RUN, "run.msa")

	def LoadGuildBuildingList(filename):
		handle = app.OpenTextFile(filename)
		count = app.GetTextFileLineCount(handle)
		for i in xrange(count):
			line = app.GetTextFileLine(handle, i)
			tokens = line.split("\t")

			TOKEN_VNUM = 0
			TOKEN_TYPE = 1
			TOKEN_NAME = 2
			TOKEN_LOCAL_NAME = 3
			NO_USE_TOKEN_SIZE_1 = 4
			NO_USE_TOKEN_SIZE_2 = 5
			NO_USE_TOKEN_SIZE_3 = 6
			NO_USE_TOKEN_SIZE_4 = 7
			TOKEN_X_ROT_LIMIT = 8
			TOKEN_Y_ROT_LIMIT = 9
			TOKEN_Z_ROT_LIMIT = 10
			TOKEN_PRICE = 11
			TOKEN_MATERIAL = 12
			TOKEN_NPC = 13
			TOKEN_GROUP = 14
			TOKEN_DEPEND_GROUP = 15
			TOKEN_ENABLE_FLAG = 16
			LIMIT_TOKEN_COUNT = 17

			if not tokens[TOKEN_VNUM].isdigit():
				continue

			if not int(tokens[TOKEN_ENABLE_FLAG]):
				continue

			if len(tokens) < LIMIT_TOKEN_COUNT:
				import dbg
				dbg.TraceError("Strange token count [%d/%d] [%s]" % (len(tokens), LIMIT_TOKEN_COUNT, line))
				continue

			ENABLE_FLAG_TYPE_NOT_USE = False
			ENABLE_FLAG_TYPE_USE = True
			ENABLE_FLAG_TYPE_USE_BUT_HIDE = 2

			if ENABLE_FLAG_TYPE_NOT_USE == int(tokens[TOKEN_ENABLE_FLAG]):
				continue

			vnum = int(tokens[TOKEN_VNUM])
			type = tokens[TOKEN_TYPE]
			name = tokens[TOKEN_NAME]
			localName = tokens[TOKEN_LOCAL_NAME]
			xRotLimit = int(tokens[TOKEN_X_ROT_LIMIT])
			yRotLimit = int(tokens[TOKEN_Y_ROT_LIMIT])
			zRotLimit = int(tokens[TOKEN_Z_ROT_LIMIT])
			price = tokens[TOKEN_PRICE]
			material = tokens[TOKEN_MATERIAL]

			folderName = ""
			if "HEADQUARTER" == type:
				folderName = "headquarter"
			elif "FACILITY" == type:
				folderName = "facility"
			elif "OBJECT" == type:
				folderName = "object"
			##"BuildIn" Is made by exist instance.

			materialList = ["0", "0", "0"]
			if material[0] == "\"":
				material = material[1:]
			if material[-1] == "\"":
				material = material[:-1]
			for one in material.split("/"):
				data = one.split(",")
				if 2 != len(data):
					continue
				itemID = int(data[0])
				count = data[1]

				if itemID == MATERIAL_STONE_ID:
					materialList[MATERIAL_STONE_INDEX] = count
				elif itemID == MATERIAL_LOG_ID:
					materialList[MATERIAL_LOG_INDEX] = count
				elif itemID == MATERIAL_PLYWOOD_ID:
					materialList[MATERIAL_PLYWOOD_INDEX] = count

			import chrmgr
			chrmgr.RegisterRaceSrcName(name, folderName)
			chrmgr.RegisterRaceName(vnum, name)

			appendingData = { "VNUM":vnum,
							  "TYPE":type,
							  "NAME":name,
							  "LOCAL_NAME":localName,
							  "X_ROT_LIMIT":xRotLimit,
							  "Y_ROT_LIMIT":yRotLimit,
							  "Z_ROT_LIMIT":zRotLimit,
							  "PRICE":price,
							  "MATERIAL":materialList,
							  "SHOW" : True }

			if ENABLE_FLAG_TYPE_USE_BUT_HIDE == int(tokens[TOKEN_ENABLE_FLAG]):
				appendingData["SHOW"] = False

			BUILDING_DATA_LIST.append(appendingData)

		app.CloseTextFile(handle)

	LoadGuildBuildingList(app.GetLocalePath()+"/GuildBuildingList.txt")

	class TestGame(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)

			x = 30000
			y = 40000

			self.wndGuildBuilding = None
			self.onClickKeyDict = {}
			self.onClickKeyDict[app.DIK_SPACE] = lambda: self.OpenBuildGuildBuildingWindow()

			background.Initialize()
			background.LoadMap("metin2_map_a1", x, y, 0)
			background.SetShadowLevel(background.SHADOW_ALL)

			self.MakeCharacter(1, 0, x, y)
			player.SetMainCharacterIndex(1)
			chr.SelectInstance(1)

		def __del__(self):
			ui.Window.__del__(self)

		def MakeCharacter(self, index, race, x, y):
			chr.CreateInstance(index)
			chr.SelectInstance(index)
			chr.SetVirtualID(index)
			chr.SetInstanceType(chr.INSTANCE_TYPE_PLAYER)

			chr.SetRace(race)
			chr.SetArmor(0)
			chr.SetHair(0)
			chr.Refresh()
			chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
			chr.SetLoopMotion(chr.MOTION_WAIT)

			chr.SetPixelPosition(x, y)
			chr.SetDirection(chr.DIR_NORTH)

		def OpenBuildGuildBuildingWindow(self):
			self.wndGuildBuilding = BuildGuildBuildingWindow()
			self.wndGuildBuilding.Open()
			self.wndGuildBuilding.SetParent(self)
			self.wndGuildBuilding.SetTop()

		def OnKeyUp(self, key):
			if key in self.onClickKeyDict:
				self.onClickKeyDict[key]()
			return True

		def OnMouseLeftButtonDown(self):
			if self.wndGuildBuilding:
				if self.wndGuildBuilding.IsPositioningMode():
					self.wndGuildBuilding.SettleCurrentPosition()
					return

			player.SetMouseState(player.MBT_LEFT, player.MBS_PRESS);
			return True

		def OnMouseLeftButtonUp(self):
			if self.wndGuildBuilding:
				return

			player.SetMouseState(player.MBT_LEFT, player.MBS_CLICK)
			return True

		def OnMouseRightButtonDown(self):
			player.SetMouseState(player.MBT_RIGHT, player.MBS_PRESS);
			return True

		def OnMouseRightButtonUp(self):
			player.SetMouseState(player.MBT_RIGHT, player.MBS_CLICK);
			return True

		def OnMouseMiddleButtonDown(self):
			player.SetMouseMiddleButtonState(player.MBS_PRESS)

		def OnMouseMiddleButtonUp(self):
			player.SetMouseMiddleButtonState(player.MBS_CLICK)

		def OnUpdate(self):
			app.UpdateGame()

			if self.wndGuildBuilding:
				if self.wndGuildBuilding.IsPositioningMode():
					x, y, z = background.GetPickingPoint()
					self.wndGuildBuilding.SetBuildingPosition(x, y, z)

		def OnRender(self):
			app.RenderGame()
			grp.PopState()
			grp.SetInterfaceRenderState()

	game = TestGame()
	game.SetSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	game.Show()

	wndGuildBuilding = BuildGuildBuildingWindow()
	wndGuildBuilding.Open()
	wndGuildBuilding.SetTop()

	app.Loop()

	"""
	- 프로토콜

게임돌입시:
	RecvLandPacket:
		CPythonMiniMap::RegisterGuildArea

게임이동중:
	PythonPlayer::Update()
		CPythonPlayer::__Update_NotifyGuildAreaEvent()
			game.py.BINARY_Guild_EnterGuildArea
				uigameButton.GameButtonWindow.ShowBuildButton()
			game.py.BINARY_Guild_ExitGuildArea
				uigameButton.GameButtonWindow.HideBuildButton()

BuildButton:
!길드장인지 처리 없음
!건물이 있어도 짓기 버튼은 있음

!건물이 임시로 사용하는 VID 는 서버가 보내주는 것과 혼동될 염려가 있음
!건물 VNUM 은 BuildGuildBuildingWindow.BUILDING_VNUM_LIST 를 이용해 변환

!건물 지을때는 /build c(reate)
!건물 부술때는 /build d(estroy)
!rotation 의 단위는 degree

	interfaceModule.interface.__OnClickBuildButton:
		interfaceModule.interface.BUILD_OpenWindow:

AcceptButton:
	BuildGuildBuildingWindow.Build:
		net.SendChatPacket("/build c vnum x y x_rot y_rot z_rot")

	x_rot, y_rot 는 AffectContainer에 저장

PreviewButton:
	__OnPreviewMode:
	__RestoreViewMode:

건물 부수기:
	uiTarget.TargetBoard.__OnDestroyBuilding
		net.SendChatPacket("/build d vid")
	"""

