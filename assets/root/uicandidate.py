import ui
import ime
import wndMgr

class VerticalCandidateBoard(ui.Board):

	CORNER_WIDTH = 3
	CORNER_HEIGHT = 3
	LINE_WIDTH = 16
	LINE_HEIGHT = 16

	SLOT_WIDTH = 14
	SLOT_HEIGHT = 14

	def __init__(self):
		ui.Window.__init__(self, "CURTAIN")

		self.Base = None
		self.BaseBar = None
		self.numberList = []
		self.slotList = []

	def __del__(self):
		ui.Board.__del__(self)

	def SetCharacterCount(self, xCount, yCount):
		self.SetSize(xCount*14 + 14, yCount*14 + 7)
		self.BaseBar.SetSize(xCount*14 + 1, yCount*14 + 1)

		self.numberList = []
		self.slotList = []

		for y in xrange(yCount):

			number = ui.ImageBox()
			number.SetParent(self.BaseBar)
			number.LoadImage("d:/ymir work/ui/pattern/ime/%d.tga" % (y+1))
			number.SetPosition(5 - 10, 8 + y * 14 - 3)
			number.Show()
			self.numberList.append(number)

			slot = ui.Bar()
			slot.SetParent(self.BaseBar)
			slot.SetPosition(10 + 1 - 10, 3 + y*14 + 1 - 3)
			slot.SetSize(xCount*14 - 1, 13)
			slot.SetColor(0xFF302C2A)
			slot.Show()
			self.slotList.append(slot)

	#################################################################

	def SetCandidatePosition(self, x, y, textCount):
		xPos = x + (textCount - 5) * 6 + 2
		yPos = y - self.GetHeight() - 2
		self.SetPosition(xPos, yPos)

	def Load(self):
		self.MakeBoard("d:/ymir work/ui/pattern/ime/corner_", "d:/ymir work/ui/pattern/ime/bar_")

		BaseBar = ui.Bar()
		BaseBar.SetParent(self)
		BaseBar.SetPosition(10, 3)
		BaseBar.SetColor(0xff000000)
		BaseBar.Show()
		self.BaseBar = BaseBar

		candidateListBox = ui.CandidateListBox(ui.CandidateListBox.VERTICAL_MODE)
		candidateListBox.SetParent(self)
		candidateListBox.SetPosition(11, 4)
		candidateListBox.SetItemSize(16, 14)
		candidateListBox.SetItemStep(14)
		candidateListBox.Show()
		self.candidateListBox = candidateListBox

	def Clear(self):
		self.candidateListBox.RemoveAllItems()

	def Append(self, text):
		self.candidateListBox.AppendItem(ui.CandidateListBox.Item(text))

	def Refresh(self):

		maxTextLength = 0
		yCount = ime.GetCandidateCount()

		for i in xrange(yCount):
			text, length = ime.GetCandidate(i)
			self.Append(text)

			if length > maxTextLength:
				maxTextLength = length

		if maxTextLength > 0:
			self.SetCharacterCount(maxTextLength, yCount)

		self.candidateListBox.SelectIndex(ime.GetCandidateSelection())

class KORCandidateWindow(ui.ScriptWindow):	

	def __init__(self):
		ui.Window.__init__(self, "CURTAIN")
		self.candidateListBox=None

	def __del__(self):
		ui.Window.__del__(self)

	def SetCandidatePosition(self, x, y, textCount):
		xPos = x + textCount*6 - 20
		yPos = y + 20
		xPos = min(xPos, wndMgr.GetScreenWidth() - self.GetWidth())
		self.SetPosition(xPos, yPos)

	def Clear(self):
		self.candidateListBox.RemoveAllItems()

	def Append(self, text):
		self.candidateListBox.AppendItem(ui.CandidateListBox.Item(text))

	def Refresh(self):
		for i in xrange(9):
			text, length = ime.GetCandidate(i)
			self.Append(text)

		self.candidateListBox.SelectIndex(ime.GetCandidateSelection())

	def Select(self, pos):
		self.candidateListBox.SelectIndex(pos)

	def Load(self):
		self.__LoadScript()
		self.__BindObject()

	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/IMEKOR.py")
		except:
			import exception
			exception.Abort("CandidateWindow.__LoadScript")

	def __BindObject(self):
		try:
			self.candidateListBox=self.GetChild("CandidateList")

		except:
			import exception
			exception.Abort("CandidateWindow.__BindObject")

ui.RegisterCandidateWindowClass(949, KORCandidateWindow)
ui.RegisterCandidateWindowClass(932, VerticalCandidateBoard)
ui.RegisterCandidateWindowClass(936, VerticalCandidateBoard)
ui.RegisterCandidateWindowClass(950, VerticalCandidateBoard)
