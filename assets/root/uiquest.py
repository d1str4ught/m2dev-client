import ui
import dbg
import app
import grp
import grpImage
import event
import time
import wndMgr
import net
import sys

QUEST_BOARD_IMAGE_DIR = 'd:/ymir work/ui/game/questboard/'

cur_questpage_number = 1
entire_questbutton_number = 0
entire_questpage_number = 1


# TOOLTIP_IMAGE_BOX
class ToolTipImageBox(ui.ImageBox):
	def __init__(self):
		ui.ImageBox.__init__(self)
		self.DestroyToolTip()
	def __del__(self):
		ui.ImageBox.__del__(self)

	def CreateToolTip(self, parent, title, desc, x, y):
		import uiToolTip
		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.SetWindowHorizontalAlignCenter()
		self.toolTip.SetFollow(False)
		self.toolTip.SetTitle(title)
		self.toolTip.SetPosition(x, y)

		desc = desc.replace("|", "/")
		for line in desc.split("/"):
			self.toolTip.AutoAppendTextLine(line)

		self.toolTip.ResizeToolTip()
		self.toolTip.Hide()

	def DestroyToolTip(self):
		self.toolTip = None

	def OnMouseOverIn(self):
		if self.toolTip:
			self.toolTip.SetTop()
			self.toolTip.Show()

	def OnMouseOverOut(self):
		if self.toolTip:
			self.toolTip.Hide()
# END_OF_TOOLTIP_IMAGE_BOX

class QuestCurtain(ui.Window):
	CURTAIN_TIME = 0.25
	CURTAIN_SPEED = 200
	BarHeight = 60
	OnDoneEventList = []
	def __init__(self,layer="TOP_MOST"):
		ui.Window.__init__(self,layer)
		self.TopBar = ui.Bar("TOP_MOST")
		self.BottomBar = ui.Bar("TOP_MOST")

		self.TopBar.Show()
		self.BottomBar.Show()

		self.TopBar.SetColor(0xff000000)
		self.BottomBar.SetColor(0xff000000)

		self.TopBar.SetPosition(0,-self.BarHeight)
		self.TopBar.SetSize(wndMgr.GetScreenWidth(),self.BarHeight)

		self.BottomBar.SetPosition(0,wndMgr.GetScreenHeight())
		self.BottomBar.SetSize(wndMgr.GetScreenWidth(),self.BarHeight)

		self.CurtainMode = 0

		self.lastclock = time.clock()

	def Close(self):
		self.CurtainMode = 0
		self.TopBar.SetPosition(0, -self.BarHeight-1)
		self.BottomBar.SetPosition(0, wndMgr.GetScreenHeight()+1)
		for OnDoneEvent in QuestCurtain.OnDoneEventList:
			apply(OnDoneEvent,(self,))
		QuestCurtain.OnDoneEventList = []

	def OnUpdate(self):
		dt = time.clock() - self.lastclock
		if self.CurtainMode>0:
			self.TopBar.SetPosition(0, int(self.TopBar.GetGlobalPosition()[1]+dt*self.CURTAIN_SPEED))
			self.BottomBar.SetPosition(0, int(self.BottomBar.GetGlobalPosition()[1]-dt*self.CURTAIN_SPEED))
			if self.TopBar.GetGlobalPosition()[1]>0:
				self.TopBar.SetPosition(0,0)
				self.BottomBar.SetPosition(0,wndMgr.GetScreenHeight()-self.BarHeight)
				self.CurtainMode = 0

		elif self.CurtainMode<0:
			self.TopBar.SetPosition(0, int(self.TopBar.GetGlobalPosition()[1]-dt*self.CURTAIN_SPEED))
			self.BottomBar.SetPosition(0, int(self.BottomBar.GetGlobalPosition()[1]+dt*self.CURTAIN_SPEED))
			if self.TopBar.GetGlobalPosition()[1]<-self.BarHeight:
				self.TopBar.SetPosition(0,-self.BarHeight-1)
				self.BottomBar.SetPosition(0,wndMgr.GetScreenHeight()+1)
				self.Close()

		self.lastclock = time.clock()

class EventCurtain(ui.Bar):

	COLOR_WHITE = 0.0
	COLOR_BLACK = 1.0

	DEFAULT_FADE_SPEED = 0.035

	STATE_WAIT = 0
	STATE_OUT = 1
	STATE_IN = 2

	def __init__(self, index):
		print "NEW EVENT CURTAIN  ----------------------------------------------------------------------------"
		ui.Bar.__init__(self, "CURTAIN")
		self.SetWindowName("EventCurtain")
		self.AddFlag("float")
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.Hide()

		self.fadeColor = 1.0
		self.curAlpha = 0.0
		self.FadeInFlag = False
		self.state = self.STATE_WAIT
		self.speed = 1.0
		self.eventIndex = index

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE EVENT CURTAIN"
		ui.Bar.__del__(self)

	def SetAlpha(self, alpha):
		color = grp.GenerateColor(self.fadeColor, self.fadeColor, self.fadeColor, alpha)
		self.SetColor(color)

	def FadeOut(self, speed):
		self.curAlpha = 0.0
		self.__StartFade(self.STATE_OUT, 0.0, speed)

	def FadeIn(self, speed):
		self.curAlpha = 1.0
		self.__StartFade(self.STATE_IN, 0.0, speed)

	def WhiteOut(self, speed):
		self.curAlpha = 0.0
		self.__StartFade(self.STATE_OUT, 1.0, speed)

	def WhiteIn(self, speed):
		self.curAlpha = 1.0
		self.__StartFade(self.STATE_IN, 1.0, speed)

	def __StartFade(self, state, color, speed):
		self.state = state
		self.fadeColor = color
		self.Show()

		self.speed = self.DEFAULT_FADE_SPEED
		if 0 != speed:
			self.speed = speed

	def __EndFade(self):
		event.EndEventProcess(self.eventIndex)

	def OnUpdate(self):

		if self.STATE_OUT == self.state:

			self.curAlpha += self.speed

			if self.curAlpha >= 1.0:

				self.state = self.STATE_WAIT
				self.curAlpha = 1.0
				self.__EndFade()

		elif self.STATE_IN == self.state:

			self.curAlpha -= self.speed

			if self.curAlpha <= 0.0:

				self.state = self.STATE_WAIT
				self.curAlpha = 0.0
				self.__EndFade()
				self.Hide()

		self.SetAlpha(self.curAlpha)

class BarButton(ui.Button):
	ColorUp = 0x40999999
	ColorDown = 0x40aaaacc
	ColorOver = 0x40ddddff

	UP=0
	DOWN=1
	OVER=2

	def __init__(self, layer = "UI", 
			aColorUp   = ColorUp, 
			aColorDown = ColorDown, 
			aColorOver = ColorOver):
		ui.Button.__init__(self,layer)
		self.state = self.UP
		self.colortable = aColorUp, aColorDown, aColorOver

	def OnRender(self):
		x,y = self.GetGlobalPosition()
		grp.SetColor(self.colortable[self.state])
		grp.RenderBar(x,y,self.GetWidth(),self.GetHeight())

	def CallEvent(self):
		self.state = self.UP
		ui.Button.CallEvent(self)

	def DownEvent(self):
		self.state = self.DOWN

	def ShowToolTip(self):
		self.state = self.OVER

	def HideToolTip(self):
		self.state = self.UP

class DescriptionWindow(ui.Window):
	def __init__(self,idx):
		ui.Window.__init__(self, "TOP_MOST")
		self.descIndex = idx 
	def __del__(self):
		ui.Window.__del__(self)
	def OnRender(self):
		event.RenderEventSet(self.descIndex)

class QuestDialog(ui.ScriptWindow):

	TITLE_STATE_NONE = 0
	TITLE_STATE_APPEAR = 1
	TITLE_STATE_SHOW = 2
	TITLE_STATE_DISAPPEAR = 3

	SKIN_NONE = 0
	SKIN_CINEMA = 5
	
	QUEST_BUTTON_MAX_NUM = 8

	def __init__(self,skin,idx):

		ui.ScriptWindow.__init__(self)
		self.SetWindowName("quest dialog")

		self.focusIndex = 0
		
		self.board = None
		self.sx = 0
		self.sy = 0

		self.skin = skin
		if skin == 3:
			event.SetRestrictedCount(idx,36)
		else:
			event.SetRestrictedCount(idx,60)

		QuestCurtain.BarHeight = (wndMgr.GetScreenHeight()-wndMgr.GetScreenWidth()*9/16)/2

		if QuestCurtain.BarHeight<0:
			QuestCurtain.BarHeight = 50
		if not ('QuestCurtain' in QuestDialog.__dict__):
			QuestDialog.QuestCurtain = QuestCurtain()
			QuestDialog.QuestCurtain.Show()

		QuestDialog.QuestCurtain.CurtainMode = 1
		self.nextCurtainMode = 0
		if self.skin:
			QuestDialog.QuestCurtain.CurtainMode = 1
			self.nextCurtainMode = 0
			self.LoadDialog(self.skin)
		else:
			QuestDialog.QuestCurtain.CurtainMode = -1
			self.nextCurtainMode = -1

		self.descIndex = idx
		self.descWindow = DescriptionWindow(idx)
		self.descWindow.Show()
		self.eventCurtain = EventCurtain(idx)
		event.SetEventHandler(idx, self)

		self.OnCloseEvent = None
		self.btnAnswer = None
		self.btnNext = None
		self.imgLeft = None
		self.imgTop = None
		self.imgBackground = None
		self.imgTitle = None
		self.titleState = self.TITLE_STATE_NONE
		self.titleShowTime = 0
		self.images = []
		self.prevbutton = None
		self.nextbutton = None

		# QUEST_INPUT		
		self.needInputString = False
		self.editSlot = None
		self.editLine = None
		# END_OF_QUEST_INPUT

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self, skin):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "uiscript/questdialog.py")
		except RuntimeError:
			dbg.TraceError("QuestDialog.LoadDialog")

		try:
			self.board = self.GetChild('board')
		except RuntimeError:
			dbg.TraceError("QuestDialog.BindObject")

		self.SetCenterPosition()
		if self.SKIN_CINEMA == skin:
			self.board.Hide()

	# QUEST_CANCEL
	def OnCancel(self):
		self.nextCurtainMode = -1
		self.CloseSelf()
	# END_OF_QUEST_CANCEL

	def CloseSelf(self):
		QuestDialog.QuestCurtain.CurtainMode = self.nextCurtainMode
		self.btnNext = None
		self.descWindow = None
		self.btnAnswer = None
		self.Destroy()
		if self.descIndex:
			event.ClearEventSet(self.descIndex)
			self.descIndex = None

		self.focusIndex = 0
	
	def Destroy(self):
		self.ClearDictionary()
		if self.OnCloseEvent:
			self.OnCloseEvent()
			self.OnCloseEvent = None

			# QUEST_INPUT
			if self.needInputString:
				if self.editLine:
					text = self.editLine.GetText()
					net.SendQuestInputStringPacket(text)
			# END_OF_QUEST_INPUT

		self.imgTitle = None
		self.images = None
		self.eventCurtain = None
		self.board = None

	def OnUpdate(self):	
		if self.skin == self.SKIN_CINEMA:
			event.UpdateEventSet(self.descIndex, 50, -(wndMgr.GetScreenHeight() - 44))
			
		# AUTO_RESIZE_BOARD
		elif self.skin == 3:			
			if self.board:
				event.UpdateEventSet(self.descIndex, self.board.GetGlobalPosition()[0]+20+self.sx, -self.board.GetGlobalPosition()[1]-20-self.sy)
				event.SetEventSetWidth(self.descIndex, self.board.GetWidth()-40)
		elif self.skin:			
			if self.board:
				event.UpdateEventSet(self.descIndex, self.board.GetGlobalPosition()[0]+20, -self.board.GetGlobalPosition()[1]-20)
				event.SetEventSetWidth(self.descIndex, self.board.GetWidth()-40)
		# END_OF_AUTO_RESIZE_BOARD
		else:
			event.UpdateEventSet(self.descIndex, 0, 0)

		if self.TITLE_STATE_NONE != self.titleState:

			curTime = app.GetTime()
			elapsedTime = app.GetTime() - self.titleShowTime

			if self.TITLE_STATE_APPEAR == self.titleState:
				self.imgTitle.SetAlpha(elapsedTime*2)
				if elapsedTime > 0.5:
					self.titleState = self.TITLE_STATE_SHOW
					self.titleShowTime = curTime

			elif self.TITLE_STATE_SHOW == self.titleState:
				if elapsedTime > 1.0:
					self.titleState = self.TITLE_STATE_DISAPPEAR
					self.titleShowTime = curTime

			elif self.TITLE_STATE_DISAPPEAR == self.titleState:
				self.imgTitle.SetAlpha(1.0 - elapsedTime*2)
				if elapsedTime > 0.5:
					self.titleState = self.TITLE_STATE_NONE
					self.titleShowTime = curTime

	## Set Variables

	def AddOnCloseEvent(self,f):
		if self.OnCloseEvent:
			self.OnCloseEvent = lambda z=[self.OnCloseEvent, f]:map(apply,z)
		else:
			self.OnCloseEvent = f

	def AddOnDoneEvent(self,f):
		QuestCurtain.OnDoneEventList.append(f)

	def SetOnCloseEvent(self,f):
		self.OnCloseEvent = f

	def SetEventSetPosition(self, x, y):
		self.sx = x
		self.sy = y

	def AdjustEventSetPosition(self, x, y):
		self.sx += x
		self.sy += y

	## Event
	# QUEST_CANCEL
	def MakeNextButton(self, button_type):
		if self.SKIN_NONE == self.skin:
			return

		yPos = event.GetEventSetLocalYPosition(self.descIndex)

		b = BarButton()
		b.SetParent(self.board)

		b.SetSize(100,26)
		b.SetPosition(self.sx+self.board.GetWidth()/2-50,self.sy+yPos)

		self.nextButtonType = button_type;
		
		import localeInfo
		if event.BUTTON_TYPE_CANCEL == button_type:
			b.SetEvent(lambda s=self:event.SelectAnswer(s.descIndex, 254) or s.OnCancel())
			b.SetText(localeInfo.UI_CANCEL)
		elif event.BUTTON_TYPE_DONE == button_type:
			b.SetEvent(lambda s=self:s.CloseSelf())
			b.SetText(localeInfo.UI_OK)
		elif event.BUTTON_TYPE_NEXT == button_type:
			b.SetEvent(lambda s=self:event.SelectAnswer(s.descIndex, 254) or s.CloseSelf())
			b.SetText(localeInfo.UI_NEXT)
		b.Show()
		b.SetTextColor(0xffffffff)
		self.btnNext = b
		
	# END_OF_QUEST_CANCEL
	
	def MakeQuestion(self, n):  # n은 모든 퀘스트 대화창의 마지막 버튼인 "닫기"를 포함한 전체 퀘스트 버튼 개수. by 김준호
		global entire_questbutton_number
		global entire_questpage_number
		global cur_questpage_number
		entire_questpage_number = ((n-2)/7)+1
		entire_questbutton_number = n
		
		if not self.board:
			return

		self.btnAnswer = [self.MakeEachButton(i) for i in xrange (n)]
			
		import localeInfo
		self.prevbutton = self.MakeNextPrevPageButton()
		self.prevbutton.SetPosition(self.sx+self.board.GetWidth()/2-164, self.board.GetHeight()/2-16)
		self.prevbutton.SetText(localeInfo.UI_PREVPAGE)
		self.prevbutton.SetEvent(self.PrevQuestPageEvent, 1, n)
		
		self.nextbutton = self.MakeNextPrevPageButton()
		self.nextbutton.SetPosition(self.sx+self.board.GetWidth()/2+112, self.board.GetHeight()/2-16)
		self.nextbutton.SetText(localeInfo.UI_NEXTPAGE)		
		self.nextbutton.SetEvent(self.NextQuestPageEvent, 1, n)
		
		if cur_questpage_number != 1:
			cur_questpage_number = 1		

	def MakeEachButton(self, i):
		if self.skin == 3:
			button = BarButton("TOP_MOST",0x50000000, 0x50404040, 0x50606060)
			button.SetParent(self.board)
			button.SetSize(106,26)
			button.SetPosition(self.sx + self.board.GetWidth()/2+((i*2)-1)*56-56, self.sy+(event.GetLineCount(self.descIndex))*16+20+5)
			button.SetText("a")
			button.SetTextColor(0xff000000)
		else:
			i = i % 8
			button = BarButton("TOP_MOST")
			button.SetParent(self.board)
			button.SetSize(200,26)
			button.SetPosition(self.sx + self.board.GetWidth()/2-100,self.sy+(event.GetLineCount(self.descIndex)+i*2)*16+20+5)
			button.SetText("a")
			button.SetTextColor(0xffffffff)
		return button
		
	def MakeNextPrevPageButton(self):
		button = BarButton("TOP_MOST")
		button.SetParent(self.board)
		button.SetSize(52,26)
		button.SetText("a")
		button.SetTextColor(0xffffffff)
		return button
		
	def RefreshQuestPage(self, n):
		global cur_questpage_number	
		global entire_questpage_number
		num = 0
		Showing_button_inx = (cur_questpage_number-1)* self.QUEST_BUTTON_MAX_NUM

		while num < n:
			if num >= Showing_button_inx and num < Showing_button_inx + self.QUEST_BUTTON_MAX_NUM:
				self.btnAnswer[num].Show()
			else:
				self.btnAnswer[num].Hide()
			num = num + 1

		if cur_questpage_number == 1:
			self.prevbutton.Hide()
			self.nextbutton.Show()
		elif cur_questpage_number == entire_questpage_number:
			self.prevbutton.Show()
			self.nextbutton.Hide()
		else:
			self.prevbutton.Show()
			self.nextbutton.Show()
		
	def NextQuestPageEvent(self, one, n):
		global cur_questpage_number	
		cur_questpage_number = cur_questpage_number + one
		self.RefreshQuestPage(n)
			
	def PrevQuestPageEvent(self, one, n):
		global cur_questpage_number
		cur_questpage_number = cur_questpage_number - one
		self.RefreshQuestPage(n)
		
	def ClickAnswerEvent(self, ai):
		event.SelectAnswer(self.descIndex, ai)
		self.nextbutton = None
		self.prevbutton = None
		self.CloseSelf()	

	def AppendQuestion(self, name, idx):  # idx는 0부터 시작함. PythonEventManager.cpp line 881 참고. by 김준호
		if not self.btnAnswer:
			return

		self.btnAnswer[idx].SetText(name)
		x, y= self.btnAnswer[idx].GetGlobalPosition()

		self.btnAnswer[idx].SetEvent(self.ClickAnswerEvent, idx)
		
		global entire_questbutton_number
		
		Showing_button_idx = (cur_questpage_number-1)* self.QUEST_BUTTON_MAX_NUM
		
		if Showing_button_idx <= idx and idx < Showing_button_idx + self.QUEST_BUTTON_MAX_NUM:
			self.btnAnswer[idx].Show()
		else:
			self.btnAnswer[idx].Hide()
		if entire_questbutton_number >= self.QUEST_BUTTON_MAX_NUM:
			self.nextbutton.Show()
		
	def FadeOut(self, speed):
		self.eventCurtain.FadeOut(speed)

	def FadeIn(self, speed):
		self.eventCurtain.FadeIn(speed)

	def WhiteOut(self, speed):
		self.eventCurtain.WhiteOut(speed)

	def WhiteIn(self, speed):
		self.eventCurtain.WhiteIn(speed)

	def DoneEvent(self):
		self.nextCurtainMode = -1
		if self.SKIN_NONE == self.skin or self.SKIN_CINEMA == self.skin:
			self.CloseSelf()

	def __GetQuestImageFileName(self, filename):
		if len(filename) > 1:
			if filename[1]!=':':
				filename = QUEST_BOARD_IMAGE_DIR+filename

		return filename
	
	# QUEST_INPUT
	def OnKeyDown(self, key):
		if self.btnAnswer == None:
			## 선택문이 없고 '다음', '확인' 등의 일방 버튼만 있는 경우에 대한 처리
			if None != self.btnNext:
				if app.DIK_RETURN == key:
					self.OnPressEscapeKey()
				
				if app.DIK_UP == key or app.DIK_DOWN == key:
					self.btnNext.ShowToolTip()
				
			return True
			
		focusIndex = self.focusIndex;
		lastFocusIndex = focusIndex;
		
		#print "QuestDialog key down - focus, last : ", focusIndex, lastFocusIndex
		
		answerCount = len(self.btnAnswer)
		
		if app.DIK_DOWN == key:
			focusIndex += 1
			
		if app.DIK_UP == key:
			focusIndex -= 1
			
		if focusIndex < 0:
			focusIndex = answerCount - 1
			
		if focusIndex >= answerCount:
			focusIndex = 0
		
		self.focusIndex = focusIndex;

		focusBtn = self.btnAnswer[focusIndex]
		lastFocusBtn = self.btnAnswer[lastFocusIndex]
		
		if focusIndex != lastFocusIndex:
			focusBtn.ShowToolTip()
			lastFocusBtn.HideToolTip()

		if app.DIK_RETURN == key:
			focusBtn.CallEvent()
			
		return True
		
	def OnPressEscapeKey(self):

		# ESC키가 눌린 경우 "다음" 버튼을 누른 것과 같은 효과를 내도록 함.
		if None != self.btnNext:
		    ##퀘스트문자들이 전부다 나왔을경우의 ESC버튼
			if event.BUTTON_TYPE_CANCEL == self.nextButtonType:
				event.SelectAnswer(self.descIndex, 254)
				self.CloseSelf()
			## 아무 작업을 하지 않을때
			elif event.BUTTON_TYPE_DONE == self.nextButtonType:
				self.CloseSelf()
			## 엔터나 다음화면으로 넘어가려고 할경우 
			elif event.BUTTON_TYPE_NEXT == self.nextButtonType:
				event.SelectAnswer(self.descIndex, 254)
				self.CloseSelf()
		else:
		## 도중에 꺼버리거나, ESC버튼이 나왓을경우 
			event.SelectAnswer(self.descIndex, entire_questbutton_number -1 )		
			self.nextbutton = None
			self.prevbutton = None
			self.OnCancel()	
		return True

	def OnIMEReturn(self):
		if self.needInputString:
			self.CloseSelf()
			return True

	def OnIMEUpdate(self):
		if not self.needInputString:
			return

		if not self.editLine:
			return

		self.editLine.OnIMEUpdate()
		
	def OnInput(self):

		self.needInputString = True

		event.AddEventSetLocalYPosition(self.descIndex, 5+10)
		yPos = event.GetEventSetLocalYPosition(self.descIndex)

		self.editSlot = ui.SlotBar()
		self.editSlot.SetSize(200, 18)
		self.editSlot.SetPosition(0, yPos)
		self.editSlot.SetParent(self.board)
		self.editSlot.SetWindowHorizontalAlignCenter()
		self.editSlot.Show()

		self.editLine = ui.EditLine()
		self.editLine.SetParent(self.editSlot)
		self.editLine.SetPosition(3, 3)
		self.editLine.SetSize(200, 17)
		self.editLine.SetMax(30)
		self.editLine.SetFocus()
		self.editLine.Show()

		event.AddEventSetLocalYPosition(self.descIndex, 25+10)

		self.MakeNextButton(event.BUTTON_TYPE_DONE)

		self.editLine.UpdateRect()
		self.editSlot.UpdateRect()
		self.board.UpdateRect()
	# END_OF_QUEST_INPUT

	def OnImage(self, x, y, filename, desc=""):
		filename = self.__GetQuestImageFileName(filename)

		# IMAGE_EXCEPTION_BUG_FIX
		try:
			img = ui.MakeImageBox(self.board, filename, x, y)
			self.images.append(img)
		except RuntimeError:
			pass
		# END_OF_IMAGE_EXCEPTION_BUG_FIX

	# QUEST_IMAGE
	def OnInsertItemIcon(self, type, idx, title, desc, index=0, total=1):
		if "item" != type:
			return

		import item
		item.SelectItem(idx)
		filename = item.GetIconImageFileName()

		underTitle = title

		if not title and not desc:
			title = item.GetItemName()
			desc = item.GetItemDescription()

			tempDesc = desc
			desc = ""

			import grpText
			lineCount = grpText.GetSplitingTextLineCount(tempDesc, 25)
			for i in xrange(lineCount):
				desc += grpText.GetSplitingTextLine(tempDesc, 25, i) + "/"

			desc = desc[:-1]

		self.OnInsertImage(filename, underTitle, title, desc, index, total)

	def OnInsertImage(self, filename, underTitle, title, desc, index=0, total=1):
		
		if index == 0:
			event.AddEventSetLocalYPosition(self.descIndex, 24)
			
		y = event.GetEventSetLocalYPosition(self.descIndex)
		xBoard, yBoard = self.board.GetGlobalPosition()

		try:
			img = ToolTipImageBox()
			img.SetParent(self.board)
			img.LoadImage(filename)
			pos_x = (self.board.GetWidth() * (index + 1) / (total + 1)) - (img.GetWidth() / 2)
			img.SetPosition(pos_x, y)
			#img.SetWindowHorizontalAlignCenter()
			img.DestroyToolTip()
			if title and desc:
				img.CreateToolTip(self.board, title, desc, 0, yBoard + y + img.GetHeight())
			img.Show()
			self.images.append(img)
		except RuntimeError:
			pass

		event.AddEventSetLocalYPosition(self.descIndex, img.GetHeight() - 20)

		if underTitle:
			event.AddEventSetLocalYPosition(self.descIndex, 3)
			event.InsertTextInline(self.descIndex, underTitle, (self.board.GetWidth() * (index + 1) / (total + 1)))
			if index != total - 1:
				event.AddEventSetLocalYPosition(self.descIndex, -( 3 + 16 ))
		else:
			if index == total - 1:
				event.AddEventSetLocalYPosition(self.descIndex, 4)
		
		if index != total - 1:
			event.AddEventSetLocalYPosition(self.descIndex, -(img.GetHeight() - 20))
			
				
	# END_OF_QUEST_IMAGE

	def OnSize(self, width, height):
		self.board.SetSize(width, height)

	def OnTitleImage(self, filename):
		img = ui.ImageBox("TOP_MOST")

		try:
			img.SetWindowHorizontalAlignCenter()
			img.LoadImage(filename)
			img.SetPosition(0, wndMgr.GetScreenHeight() - (75/2) - (32/2))
			img.SetAlpha(0.0)
			img.Show()
		except RuntimeError:
			dbg.TraceError("QuestDialog.OnTitleImage(%s)" % filename)
			img.Hide()

		self.imgTitle = img
		self.titleState = self.TITLE_STATE_APPEAR
		self.titleShowTime = app.GetTime()

	def OnLeftImage(self, imgfile):
		imgfile = self.__GetQuestImageFileName(imgfile)
		if not self.imgLeft:
			self.imgLeft = ui.ExpandedImageBox("TOP_MOST")
			self.imgLeft.SetParent(self)
			self.imgLeft.SetPosition(0,0)
			bd = self.board
			bx, by = bd.GetLocalPosition()
			bd.SetPosition(160,by)
			if self.imgTop:
				tx, ty = self.imgTop.GetLocalPosition()
				self.imgTop.SetPosition(160,ty)

		try:
			self.imgLeft.LoadImage(imgfile)
			self.imgLeft.SetSize(400,450)
			self.imgLeft.SetOrigin(self.imgLeft.GetWidth()/2,self.imgLeft.GetHeight()/2)
			self.imgLeft.Show()
		except RuntimeError:
			import dbg
			dbg.TraceError("QuestDialog.OnLeftImage(%s)" % imgfile)
			self.imgLeft.Hide()

	def OnTopImage(self, imgfile):
		imgfile = self.__GetQuestImageFileName(imgfile)

		bd = self.board
		bx, by = bd.GetLocalPosition()
		if not self.imgTop:
			self.imgTop = ui.ExpandedImageBox("TOP_MOST")
			self.imgTop.SetParent(self)
			bd.SetPosition(bx,190)
			self.imgTop.SetPosition(bx,10)

		try:
			self.imgTop.LoadImage(imgfile)
			h = self.imgTop.GetHeight()
			if h>170:
				# need adjust board size
				bd.SetPosition(bx,20+h)
				bd.SetSize(350,420-h)
				self.imgTop.SetSize(350,h)
			else:
				self.imgTop.SetSize(350,170)
				bd.SetPosition(bx,190)
				bd.SetSize(350,250)
			self.imgTop.SetOrigin(self.imgTop.GetWidth()/2,self.imgTop.GetHeight()/2)
			self.imgTop.Show()
		except RuntimeError:
			dbg.TraceError("QuestDialog.OnTopImage(%s)" % imgfile)
			self.imgTop.Hide()

	def OnBackgroundImage(self, imgfile):
		imgfile = self.__GetQuestImageFileName(imgfile)
		c = self.board
		w = c.GetWidth()
		h = c.GetHeight()
		px, py = c.GetLocalPosition()
		moved = 0
		if not self.imgBackground:
			self.imgBackground = ui.ExpandedImageBox("TOP_MOST")
			self.imgBackground.SetParent(c)
			self.imgBackground.SetPosition(0,0)
		self.imgBackground.LoadImage(imgfile)
		iw = self.imgBackground.GetWidth()
		ih = self.imgBackground.GetHeight()
		if self.skin==3:
			iw = 256
			ih = 333
			self.imgBackground.SetSize(iw,ih)
		if w < iw:
			px -= (iw-w)/2
			c.SetPosition(px,py)
			w = iw
		if h < ih:
			py -= (ih-h)/2
			c.SetPosition(px,py)
			h = ih
		if self.skin == 3:
			w=256
			h = 333
			self.sx = 0
			self.sy = 100

		c.SetSize(w,h)
		c.HideInternal()

		c.SetWindowHorizontalAlignCenter()
		c.SetWindowVerticalAlignCenter()

		c.SetPosition(0,0)
		if self.skin==3:
			c.SetPosition(-190,0)

		self.imgBackground.SetWindowHorizontalAlignCenter()
		self.imgBackground.SetWindowVerticalAlignCenter()
		self.imgBackground.SetPosition(0,0)
		self.imgBackground.Show()
