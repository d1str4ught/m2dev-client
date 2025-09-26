import app
import ui
import localeInfo
import uiScriptLocale
import net
import chat
import threading
import time

class MarkItem(ui.ListBoxEx.Item):
    def __init__(self, fileName):
        ui.ListBoxEx.Item.__init__(self)
        self.imgWidth = 0
        self.imgHeight = 0
        self.canLoad = 0
        self.fileName = fileName
        self.textLine = self.__CreateTextLine(fileName)
        self.imgBox = self.__CreateImageBox("upload/" + fileName)

    def __del__(self):
        ui.ListBoxEx.Item.__del__(self)

    def GetText(self):
        return self.textLine.GetText()

    def GetFileName(self):
        return self.fileName

    def SetSize(self, width, height):
        ui.ListBoxEx.Item.SetSize(self, 20 + 6 * len(self.textLine.GetText()) + 4, height)

    def __CreateTextLine(self, fileName):
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetPosition(20, 0)
        textLine.SetText(fileName)
        textLine.Show()
        return textLine

    def __CreateImageBox(self, fileName):
        (self.canLoad, self.imgWidth, self.imgHeight) = app.GetImageInfo(fileName)

        if self.canLoad == 1:
            if self.imgWidth <= 256 and self.imgHeight <= 256:
                imgBox = ui.ImageBox()
                imgBox.AddFlag("not_pick")
                imgBox.SetParent(self)
                imgBox.SetPosition(0, 2)
                imgBox.LoadImageFromFile(fileName)
                imgBox.Show()
                return imgBox
        return None

class UploadDialog(ui.ScriptWindow):
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.selectEvent = None
        self.isLoaded = 0
        self.uploadInProgress = False

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Show(self):
        if self.isLoaded == 0:
            self.isLoaded = 1
            self.__Load()
        ui.ScriptWindow.Show(self)

    def Open(self):
        self.Show()
        self.SetCenterPosition()
        self.SetTop()
        if self.markListBox.IsEmpty():
            self.__PopupMessage("No marks found in upload folder")

    def Close(self):
        if hasattr(self, 'popupDialog'):
            self.popupDialog.Hide()
        self.Hide()

    def OnPressEscapeKey(self):
        self.Close()
        return True

    def SAFE_SetSelectEvent(self, event):
        self.selectEvent = ui.__mem_func__(event)

    def __Load(self):
        self.popupDialog = PopupDialog(self)

        try:
            pyScrLoader = ui.PythonScriptLoader()
            pyScrLoader.LoadScriptFile(self, "UIScript/MarkListWindow.py")
        except:
            import exception
            exception.Abort("UploadDialog.__Load")

        try:
            self.markListBox = self.__CreateMarkListBox()
            self.markListBox.SetScrollBar(self.GetChild("ScrollBar"))

            self.board = self.GetChild("board")
            self.okButton = self.GetChild("ok")
            self.cancelButton = self.GetChild("cancel")
            self.refreshButton = self.GetChild("refresh")

            self.progressBar = ui.Gauge()
            self.progressBar.SetParent(self.board)
            self.progressBar.SetPosition(15, 200)
            self.progressBar.SetSize(200, 15)
            self.progressBar.Hide()

            self.statusText = ui.TextLine()
            self.statusText.SetParent(self.board)
            self.statusText.SetPosition(15, 220)
            self.statusText.SetText("")
            self.statusText.Hide()

        except:
            import exception
            exception.Abort("UploadDialog.__Bind")

        self.refreshButton.SetEvent(ui.__mem_func__(self.__OnRefresh))
        self.cancelButton.SetEvent(ui.__mem_func__(self.__OnCancel))
        self.okButton.SetEvent(ui.__mem_func__(self.__OnOK))
        self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
        self.UpdateRect()
        self.__RefreshFileList()

    def __CreateMarkListBox(self):
        markListBox = ui.ListBoxEx()
        markListBox.SetParent(self)
        markListBox.SetPosition(15, 50)
        markListBox.Show()
        return markListBox

    def __PopupMessage(self, msg):
        self.popupDialog.Open(msg)

    def __OnOK(self):
        if self.uploadInProgress:
            return

        selItem = self.markListBox.GetSelectedItem()
        if selItem:
            if selItem.canLoad != 1:
                self.__PopupMessage("Invalid file format")
            elif selItem.imgWidth > 256:
                self.__PopupMessage("Image width must be <= 256 pixels")
            elif selItem.imgHeight > 256:
                self.__PopupMessage("Image height must be <= 256 pixels")
            else:
                self.__StartUpload(selItem.GetFileName())
        else:
            self.__PopupMessage("Please select a mark")

    def __OnCancel(self):
        if not self.uploadInProgress:
            self.Hide()

    def __OnRefresh(self):
        self.__RefreshFileList()

    def __StartUpload(self, fileName):
        self.uploadInProgress = True
        self.okButton.Down()
        self.progressBar.Show()
        self.statusText.Show()
        self.statusText.SetText("Uploading...")

        try:
            with open("upload/" + fileName, "rb") as f:
                data = f.read()

            format = fileName.split('.')[-1].lower()
            if format == "jpg":
                format = "jpeg"

            net.SendGuildMarkUpload(data, format)

            def upload_thread():
                for i in range(101):
                    if not self.uploadInProgress:
                        break
                    self.progressBar.SetPercentage(i, 100)
                    time.sleep(0.02)

                self.__FinishUpload(True)

            thread = threading.Thread(target=upload_thread)
            thread.daemon = True
            thread.start()

        except Exception as e:
            self.__FinishUpload(False, str(e))

    def __FinishUpload(self, success, error=None):
        self.uploadInProgress = False
        self.okButton.SetUp()
        self.progressBar.Hide()

        if success:
            self.statusText.SetText("Upload completed!")
            chat.AppendChat(3, "Guild mark uploaded successfully")
            if self.selectEvent:
                self.selectEvent()
            self.Hide()
        else:
            self.statusText.SetText("Upload failed: " + (error or "Unknown error"))

    def __RefreshFileList(self):
        self.__ClearFileList()
        self.__AppendFileList("png")
        self.__AppendFileList("jpg")
        self.__AppendFileList("jpeg")
        self.__AppendFileList("gif")
        self.__AppendFileList("bmp")

    def __ClearFileList(self):
        self.markListBox.RemoveAllItems()

    def __AppendFileList(self, filter):
        fileNameList = app.GetFileList("upload/*." + filter)
        for fileName in fileNameList:
            self.__AppendFile(fileName)

    def __AppendFile(self, fileName):
        self.markListBox.AppendItem(MarkItem(fileName))

class PopupDialog(ui.ScriptWindow):
    def __init__(self, parent):
        ui.ScriptWindow.__init__(self)
        self.__Load()
        self.__Bind()

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def __Load(self):
        try:
            pyScrLoader = ui.PythonScriptLoader()
            pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
        except:
            import exception
            exception.Abort("PopupDialog.__Load")

    def __Bind(self):
        try:
            self.textLine = self.GetChild("message")
            self.okButton = self.GetChild("accept")
        except:
            import exception
            exception.Abort("PopupDialog.__Bind")

        self.okButton.SetEvent(ui.__mem_func__(self.__OnOK))

    def Open(self, msg):
        self.textLine.SetText(msg)
        self.SetCenterPosition()
        self.Show()
        self.SetTop()

    def __OnOK(self):
        self.Hide()