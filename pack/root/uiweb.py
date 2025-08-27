import ui
import uiScriptLocale
import net
import snd
import app
import mouseModule
import constInfo

class WebWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self, "TOP_MOST")

		self.oldPos = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			if constInfo.IN_GAME_SHOP_ENABLE:
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "WebWindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/WebWindow.py")
		except:
			import exception
			exception.Abort("WebWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.titleBar = GetObject("TitleBar")

		except:
			import exception
			exception.Abort("WebWindow.LoadDialog.BindObject")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))

	def Destroy(self):
		app.HideWebPage()
		self.ClearDictionary()
		self.titleBar = None

	def Open(self, url):
		self.Refresh()
		self.Show()
		self.SetCenterPosition()

		x, y = self.GetGlobalPosition()
		sx, sy = x + 10, y + 30
		ex, ey = sx + self.GetWidth() - 20, sy + self.GetHeight() - 40

		app.ShowWebPage(url, (sx, sy, ex, ey))
		

	def Close(self):
		app.HideWebPage()
		self.Hide()

	def Clear(self):
		self.Refresh()

	def Refresh(self):
		pass

	def __OnCloseButtonClick(self):
		print "close_web:click_close_button"
		self.Close()

	def OnPressEscapeKey(self):
		print "close_web:esc_key"
		self.Close()
		return True

	def OnUpdate(self):
		newPos = self.GetGlobalPosition()
		if newPos == self.oldPos:
			return

		self.oldPos = newPos

		x, y = newPos
		sx, sy = x + 10, y + 30
		ex, ey = sx + self.GetWidth() - 20, sy + self.GetHeight() - 40
		app.MoveWebPage((sx, sy, ex, ey))

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	import uiToolTip
	import localeInfo

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(True)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("METIN2", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	class TestGame(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)

			localeInfo.LoadLocaleData()

			self.mallWindow = WebWindow()
			self.mallWindow.LoadWindow()
			self.mallWindow.Open()

		def __del__(self):
			ui.Window.__del__(self)

		def OnUpdate(self):
			app.UpdateGame()

		def OnRender(self):
			app.RenderGame()
			grp.PopState()
			grp.SetInterfaceRenderState()

	game = TestGame()
	game.SetSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	game.Show()

	app.Loop()
