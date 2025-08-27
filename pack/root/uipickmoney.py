import wndMgr
import ui
import ime
import localeInfo

class PickMoneyDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.unitValue = 1
		self.maxValue = 0
		self.eventAccept = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PickMoneyDialog.py")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.maxValueTextLine = self.GetChild("max_value")
			self.pickValueEditLine = self.GetChild("money_value")
			self.acceptButton = self.GetChild("accept_button")
			self.cancelButton = self.GetChild("cancel_button")
		except:
			import exception
			exception.Abort("MoneyDialog.LoadDialog.BindObject")

		self.pickValueEditLine.SetReturnEvent(ui.__mem_func__(self.OnAccept))
		self.pickValueEditLine.SetEscapeEvent(ui.__mem_func__(self.Close))
		self.acceptButton.SetEvent(ui.__mem_func__(self.OnAccept))
		self.cancelButton.SetEvent(ui.__mem_func__(self.Close))
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

	def Destroy(self):
		self.ClearDictionary()
		self.eventAccept = 0
		self.maxValue = 0
		self.pickValueEditLine = 0		
		self.acceptButton = 0
		self.cancelButton = 0
		self.board = None

	def SetTitleName(self, text):
		self.board.SetTitleName(text)

	def SetAcceptEvent(self, event):
		self.eventAccept = event

	def SetMax(self, max):
		self.pickValueEditLine.SetMax(max)

	def Open(self, maxValue, unitValue=1):

		if localeInfo.IsYMIR() or localeInfo.IsCHEONMA() or localeInfo.IsHONGKONG():
			unitValue = ""

		width = self.GetWidth()
		(mouseX, mouseY) = wndMgr.GetMousePosition()

		if mouseX + width/2 > wndMgr.GetScreenWidth():
			xPos = wndMgr.GetScreenWidth() - width
		elif mouseX - width/2 < 0:
			xPos = 0
		else:
			xPos = mouseX - width/2

		self.SetPosition(xPos, mouseY - self.GetHeight() - 20)

		if localeInfo.IsARABIC():
			self.maxValueTextLine.SetText("/" + str(maxValue))
		else:
			self.maxValueTextLine.SetText(" / " + str(maxValue))

		self.pickValueEditLine.SetText(str(unitValue))
		self.pickValueEditLine.SetFocus()

		ime.SetCursorPosition(1)

		self.unitValue = unitValue
		self.maxValue = maxValue
		self.Show()
		self.SetTop()

	def Close(self):
		self.pickValueEditLine.KillFocus()
		self.Hide()

	def OnAccept(self):

		text = self.pickValueEditLine.GetText()

		if len(text) > 0 and text.isdigit():

			money = int(text)
			money = min(money, self.maxValue)

			if money > 0:
				if self.eventAccept:
					self.eventAccept(money)

		self.Close()
