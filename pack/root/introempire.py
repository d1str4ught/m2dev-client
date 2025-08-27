import ui
import net
import wndMgr
import dbg
import app
import event
import _weakref
import localeInfo
import uiScriptLocale

LOCALE_PATH = "uiscript/"+uiScriptLocale.CODEPAGE+"_"

class SelectEmpireWindow(ui.ScriptWindow):

	EMPIRE_DESCRIPTION_TEXT_FILE_NAME = {	
		net.EMPIRE_A : uiScriptLocale.EMPIREDESC_A,
		net.EMPIRE_B : uiScriptLocale.EMPIREDESC_B,
		net.EMPIRE_C : uiScriptLocale.EMPIREDESC_C, }

	class EmpireButton(ui.Window):
		def __init__(self, owner, arg):
			ui.Window.__init__(self)
			self.owner = owner
			self.arg = arg
		def OnMouseOverIn(self):
			self.owner.OnOverInEmpire(self.arg)
		def OnMouseOverOut(self):
			self.owner.OnOverOutEmpire(self.arg)
		def OnMouseLeftButtonDown(self):
			if self.owner.empireID != self.arg:
				self.owner.OnSelectEmpire(self.arg)

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

	def __init__(self, stream):
		print "NEW EMPIRE WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, self)

		self.stream=stream
		self.empireID=app.GetRandom(1, 3)
		self.descIndex=0
		self.empireArea = {}
		self.empireAreaFlag = {}
		self.empireFlag = {}
		self.empireAreaButton = {}
		self.empireAreaCurAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }
		self.empireAreaDestAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }
		self.empireAreaFlagCurAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }
		self.empireAreaFlagDestAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }
		self.empireFlagCurAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }
		self.empireFlagDestAlpha = { net.EMPIRE_A:0.0, net.EMPIRE_B:0.0, net.EMPIRE_C:0.0 }

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, 0)
		print "---------------------------------------------------------------------------- DELETE EMPIRE WINDOW"

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE EMPIRE WINDOW"		

		self.ClearDictionary()
		self.leftButton = None
		self.rightButton = None
		self.selectButton = None
		self.exitButton = None
		self.textBoard = None
		self.descriptionBox = None
		self.empireArea = None
		self.empireAreaButton = None

		self.KillFocus()
		self.Hide()

		app.HideCursor()
		event.Destroy()

	def Open(self):
		print "OPEN EMPIRE WINDOW ----------------------------------------------------------------------------"

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectEmpireWindow")
		self.Show()	

		if not self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "SelectEmpireWindow.py"):
			dbg.TraceError("SelectEmpireWindow.Open - __LoadScript Error")
			return

		self.OnSelectEmpire(self.empireID)
		self.__CreateButtons()
		self.__CreateDescriptionBox()
		app.ShowCursor()

	def __CreateButtons(self):
		for key, img in self.empireArea.items():

			img.SetAlpha(0.0)

			(x, y) = img.GetGlobalPosition()
			btn = self.EmpireButton(_weakref.proxy(self), key)
			btn.SetParent(self)
			btn.SetPosition(x, y)
			btn.SetSize(img.GetWidth(), img.GetHeight())
			btn.Show()
			self.empireAreaButton[key] = btn

	def __CreateDescriptionBox(self):
		self.descriptionBox = self.DescriptionBox()
		self.descriptionBox.Show()

	def OnOverInEmpire(self, arg):
		self.empireAreaDestAlpha[arg] = 1.0

	def OnOverOutEmpire(self, arg):
		if arg != self.empireID:
			self.empireAreaDestAlpha[arg] = 0.0

	def OnSelectEmpire(self, arg):
		for key in self.empireArea.keys():
			self.empireAreaDestAlpha[key] = 0.0
			self.empireAreaFlagDestAlpha[key] = 0.0
			self.empireFlagDestAlpha[key] = 0.0
		self.empireAreaDestAlpha[arg] = 1.0
		self.empireAreaFlagDestAlpha[arg] = 1.0
		self.empireFlagDestAlpha[arg] = 1.0
		self.empireID = arg
		
		event.ClearEventSet(self.descIndex)
		if self.EMPIRE_DESCRIPTION_TEXT_FILE_NAME.has_key(arg):
			self.descIndex = event.RegisterEventSet(self.EMPIRE_DESCRIPTION_TEXT_FILE_NAME[arg])

			if localeInfo.IsARABIC():
				event.SetEventSetWidth(self.descIndex, 170)
			else:
				event.SetRestrictedCount(self.descIndex, 35)

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

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)	
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.LoadObject")

		try:
			GetObject=self.GetChild
			self.leftButton		= GetObject("left_button")
			self.rightButton	= GetObject("right_button")
			self.selectButton	= GetObject("select_button")
			self.exitButton		= GetObject("exit_button")
			self.textBoard		= GetObject("text_board")
			self.empireArea[net.EMPIRE_A]	= GetObject("EmpireArea_A")
			self.empireArea[net.EMPIRE_B]	= GetObject("EmpireArea_B")
			self.empireArea[net.EMPIRE_C]	= GetObject("EmpireArea_C")
			self.empireAreaFlag[net.EMPIRE_A]	= GetObject("EmpireAreaFlag_A")
			self.empireAreaFlag[net.EMPIRE_B]	= GetObject("EmpireAreaFlag_B")
			self.empireAreaFlag[net.EMPIRE_C]	= GetObject("EmpireAreaFlag_C")
			self.empireFlag[net.EMPIRE_A]	= GetObject("EmpireFlag_A")
			self.empireFlag[net.EMPIRE_B]	= GetObject("EmpireFlag_B")
			self.empireFlag[net.EMPIRE_C]	= GetObject("EmpireFlag_C")
			GetObject("prev_text_button").SetEvent(ui.__mem_func__(self.PrevDescriptionPage))
			GetObject("next_text_button").SetEvent(ui.__mem_func__(self.NextDescriptionPage))
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.BindObject")					

		self.selectButton.SetEvent(ui.__mem_func__(self.ClickSelectButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.ClickExitButton))
		self.leftButton.SetEvent(ui.__mem_func__(self.ClickLeftButton))
		self.rightButton.SetEvent(ui.__mem_func__(self.ClickRightButton))
		for flag in self.empireAreaFlag.values():
			flag.SetAlpha(0.0)
		for flag in self.empireFlag.values():
			flag.SetAlpha(0.0)

		return 1

	def ClickLeftButton(self):
		self.empireID-=1
		if self.empireID<1:
			self.empireID=3

		self.OnSelectEmpire(self.empireID)

	def ClickRightButton(self):
		self.empireID+=1
		if self.empireID>3:
			self.empireID=1

		self.OnSelectEmpire(self.empireID)

	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetSelectCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetLoginPhase()

	def OnUpdate(self):
		(xposEventSet, yposEventSet) = self.textBoard.GetGlobalPosition()
		event.UpdateEventSet(self.descIndex, xposEventSet+7, -(yposEventSet+7))
		self.descriptionBox.SetIndex(self.descIndex)

		self.__UpdateAlpha(self.empireArea, self.empireAreaCurAlpha, self.empireAreaDestAlpha)
		self.__UpdateAlpha(self.empireAreaFlag, self.empireAreaFlagCurAlpha, self.empireAreaFlagDestAlpha)
		self.__UpdateAlpha(self.empireFlag, self.empireFlagCurAlpha, self.empireFlagDestAlpha)

	def __UpdateAlpha(self, dict, curAlphaDict, destAlphaDict):
		for key, img in dict.items():

			curAlpha = curAlphaDict[key]
			destAlpha = destAlphaDict[key]

			if abs(destAlpha - curAlpha) / 10 > 0.0001:
				curAlpha += (destAlpha - curAlpha) / 7
			else:
				curAlpha = destAlpha

			curAlphaDict[key] = curAlpha
			img.SetAlpha(curAlpha)

	def OnPressEscapeKey(self):
		self.ClickExitButton()
		return True

class ReselectEmpireWindow(SelectEmpireWindow):
	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetCreateCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetSelectCharacterPhase()
