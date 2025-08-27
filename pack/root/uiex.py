import app
import wndMgr
import systemSetting
import mouseModule
import ui

class Window(ui.Window):
	def __init__(self, skinFileName = ""):		
		ui.Window.__init__(self, "UI")

		self.children = []
		self.childDict = {}

		self.__LoadSkin(skinFileName)

		self.Show()

	def __del__(self):
		ui.Window.__del__(self)	

	def ClearDictionary(self):
		self.children	= []
		self.childDict	= {}

	def InsertChild(self, name, child):
		self.childDict[name] = child

	def IsChild(self, name):
		return name in self.childDict

	def GetChild(self, name):
		return self.childDict[name]

	def __LoadSkin(self, fileName):
		loader = ui.PythonScriptLoader()
		loader.LoadScriptFile(self, fileName)


#wndMgr.SetOutlineFlag(True)

class App:
	def __init__(self, title = "METIN2 UI TEST"):
		app.SetMouseHandler(mouseModule.mouseController)
		app.SetHairColorEnable(True)
		wndMgr.SetMouseHandler(mouseModule.mouseController)

		width	= systemSetting.GetWidth()
		height	= systemSetting.GetHeight()
		wndMgr.SetScreenSize(width, height)
		app.Create(title, width, height, 1)
		mouseModule.mouseController.Create()

		self.OnInit()

	def MainLoop(self):
		app.Loop()

	def OnInit(self):
		pass


if __name__ == "__main__":
	class TestWindow(Window):
		def __init__(self, skinFileName):
			Window.__init__(self, skinFileName)

		def __del__(self):
			Window.__del__(self)

	class TestApp(App):
		def OnInit(self):
			self.test = TestWindow("locale/ymir_ui/matrixwindow.py")
			pass
	
	TestApp().MainLoop()
