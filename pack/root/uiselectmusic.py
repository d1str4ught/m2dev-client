import app
import ui
import localeInfo
import uiScriptLocale

FILE_NAME_LEN = 20 
DEFAULT_THEMA = localeInfo.MUSIC_METIN2_DEFAULT_THEMA

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:FILE_NAME_LEN])

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)

		if localeInfo.IsARABIC():
			textLine.SetPosition(6*len(fileName) + 6, 0)
		else:
			textLine.SetPosition(0, 0)

		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class PopupDialog(ui.ScriptWindow):
	def __init__(self, parent):
		print "NEW POPUP WINDOW   ----------------------------------------------------------------------------"	
		ui.ScriptWindow.__init__(self)

		self.__Load()
		self.__Bind()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE POPUP WINDOW"

	def __Load(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
		except:
			import exception
			exception.Abort("PopupDialog.__Load")

	def __Bind(self):
		try:
			self.textLine=self.GetChild("message")
			self.okButton=self.GetChild("accept")
		except:
			import exception
			exception.Abort("PopupDialog.__Bind")

		self.okButton.SAFE_SetEvent(self.__OnOK)

	def Open(self, msg):
		self.textLine.SetText(msg)
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def __OnOK(self):
		self.Hide()

class FileListDialog(ui.ScriptWindow):
	def __init__(self):
		print "NEW LIST DIALOG   ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)

		self.isLoaded=0
		self.selectEvent=None
		self.fileListBox=None

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE LIST DIALOG"

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__Load()

		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()

		self.SetCenterPosition()
		self.SetTop()

		if self.fileListBox.IsEmpty():
			self.__PopupMessage(localeInfo.MUSIC_EMPTY_MUSIC_LIST)

	def Close(self):
		self.popupDialog.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def SAFE_SetSelectEvent(self, event):
		self.selectEvent=ui.__mem_func__(event)

	def __CreateFileListBox(self):
		fileListBox=ui.ListBoxEx()
		fileListBox.SetParent(self)
		
		if localeInfo.IsARABIC():
			fileListBox.SetPosition( self.GetWidth() - fileListBox.GetWidth() - 10, 50)
		else:
			fileListBox.SetPosition(15, 50)

		fileListBox.Show()
		return fileListBox

	def __Load(self):
		self.popupDialog=PopupDialog(self)

		if localeInfo.IsARABIC():
			self.__Load_LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "MusicListWindow.py")
		else:
			self.__Load_LoadScript("UIScript/MusicListWindow.py")

		self.__Load_BindObject()

		self.refreshButton.SAFE_SetEvent(self.__OnRefresh)
		self.cancelButton.SAFE_SetEvent(self.__OnCancel)
		self.okButton.SAFE_SetEvent(self.__OnOK)
		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
		self.UpdateRect()

		self.__RefreshFileList()

	def __Load_LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("MusicListBox.__Load")

	def __Load_BindObject(self):
		try:
			self.fileListBox=self.__CreateFileListBox()
			self.fileListBox.SetScrollBar(self.GetChild("ScrollBar"))

			self.board=self.GetChild("board")
			self.okButton=self.GetChild("ok")
			self.cancelButton=self.GetChild("cancel")
			self.refreshButton=self.GetChild("refresh")

			self.popupText = self.popupDialog.GetChild("message")

		except:
			import exception
			exception.Abort("MusicListBox.__Bind")

	def __PopupMessage(self, msg):
		self.popupDialog.Open(msg)

	def __OnOK(self):
		selItem=self.fileListBox.GetSelectedItem()
		if selItem:
			if self.selectEvent:
				self.selectEvent(selItem.GetText())
			self.Hide()
		else:
			self.__PopupMessage(localeInfo.MUSIC_NOT_SELECT_MUSIC)

	def __OnCancel(self):
		self.Hide()

	def __OnRefresh(self):
		self.__RefreshFileList()

	def __RefreshFileList(self):
		self.__ClearFileList()
		self.__AppendFile(DEFAULT_THEMA)
		self.__AppendFileList("mp3")

	def __ClearFileList(self):
		self.fileListBox.RemoveAllItems()

	def __AppendFileList(self, filter):
		fileNameList=app.GetFileList("BGM/*."+filter)
		for fileName in fileNameList:
			self.__AppendFile(fileName)

	def __AppendFile(self, fileName):
		self.fileListBox.AppendItem(Item(fileName))


