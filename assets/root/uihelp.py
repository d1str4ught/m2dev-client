import app
import ui
import localeInfo
import uiScriptLocale

ENABLE_HELP_MULTIPAGE = 0

class HelpWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self, "TOP_MOST")
		self.eventClose = 0
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		if ENABLE_HELP_MULTIPAGE:
			self.LoadDialogMultiPage()
		else:
			self.LoadDialogSinglePage()
	
	def LoadDialogSinglePage(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			
			if localeInfo.IsARABIC():
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "HelpWindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/HelpWindow.py")
		except:
			import exception
			exception.Abort("HelpWindow.LoadDialogSinglePage.LoadScript")

		try:
			GetObject=self.GetChild
			self.btnClose = GetObject("close_button")
		except:
			import exception
			exception.Abort("DialogWindow.LoadDialogSinglePage.BindObject")


	def LoadDialogMultiPage(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/HelpWindow2.py")
		except:
			import exception
			exception.Abort("HelpWindow.LoadDialogMultiPage.LoadScript")

		try:
			GetObject=self.GetChild
			self.btnClose = GetObject("close_button")
			self.pages = {}
			self.btnPages = {}
			self.pages[0] = GetObject("page_1")
			self.pages[1] = GetObject("page_2")
			self.btnPages[0] = GetObject("page_1_button")
			self.btnPages[1] = GetObject("page_2_button")
			self.btnPages[0].SAFE_SetEvent(self.__OnClickPage1)
			self.btnPages[1].SAFE_SetEvent(self.__OnClickPage2)

			self.__SelectPage(0)

		except:
			import exception
			exception.Abort("DialogWindow.LoadDialogMultiPage.BindObject")

	def __OnClickPage1(self):
		self.__SelectPage(0)

	def __OnClickPage2(self):
		self.__SelectPage(1)

	def Destroy(self):
		self.eventClose = 0
		self.closeButton = 0
		self.pages = {}
		self.btnPages = {}

	def SetCloseEvent(self, event):
		self.eventClose = event
		self.btnClose.SetEvent(event)

	def Open(self):
		self.Lock()
		self.Show()

	def Close(self):
		self.Unlock()
		self.Hide()

	def OnKeyDown(self, key):
		if app.DIK_H == key and 0 != self.eventClose:
			self.eventClose()
			
		return True

	def OnIMEReturn(self):
		return True

	def OnPressEscapeKey(self):
		if 0 != self.eventClose:
			self.eventClose()
		return True

	def OnPressExitKey(self):
		if 0 != self.eventClose:
			self.eventClose()
		return True

	def __SelectPage(self, pageIndex):
		for page in self.pages.values():
			page.Hide()
		for btn in self.btnPages.values():
			btn.SetUp()

		self.pages[pageIndex].Show()
		self.btnPages[pageIndex].Down()

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	wnd = HelpWindow()
	wnd.LoadDialog()
	wnd.Open()
	app.Loop()
	wnd = None

