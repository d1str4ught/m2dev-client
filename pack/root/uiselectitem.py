import ui
import player
import item
import wndMgr
import net

class SelectItemWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.tooltipItem = None
		self.inventorySlotPosDict = {}

		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/selectitemwindow.py")
		except:
			import exception
			exception.Abort("ItemSelectWindow.LoadDialog.LoadObject")

		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.titleBar = GetObject("TitleBar")
			self.itemSlot = GetObject("ItemSlot")
			self.btnExit = GetObject("ExitButton")
		except:
			import exception
			exception.Abort("ItemSelectWindow.LoadDialog.BindObject")

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.btnExit.SetEvent(ui.__mem_func__(self.Close))
		self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlot.SAFE_SetButtonEvent("LEFT", "EXIST", self.SelectItemSlot)
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

	def Open(self):
		self.RefreshSlot()
		self.Show()

	def Close(self):
		wndMgr.OnceIgnoreMouseLeftButtonUpEvent()
		net.SendSelectItemPacket(0)
		self.Hide()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SelectItemSlot(self, slotPos):
		wndMgr.OnceIgnoreMouseLeftButtonUpEvent()
		inventorySlotPos = self.inventorySlotPosDict[slotPos]
		net.SendSelectItemPacket(inventorySlotPos)
		self.Hide()

	def SetTableSize(self, size):

		SLOT_X_COUNT = 5
		self.itemSlot.ArrangeSlot(0, SLOT_X_COUNT, size, 32, 32, 0, 0)
		self.itemSlot.RefreshSlot()
		self.itemSlot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)

		self.board.SetSize(self.board.GetWidth(), 76 + 32*size)
		self.SetSize(self.board.GetWidth(), 76 + 32*size)
		self.UpdateRect()

	def RefreshSlot(self):

		slotPos = 0
		self.inventorySlotPosDict = {}

		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.itemSlot.SetItemSlot

		for i in xrange(player.INVENTORY_PAGE_SIZE*2):
			slotNumber = i

			itemVNum = getItemVNum(slotNumber)
			if 0 == itemVNum:
				continue

			if not item.IsMetin(itemVNum):
				continue

			itemGrade = player.GetItemGrade(slotNumber)
			if itemGrade > 2:
				continue

			self.inventorySlotPosDict[slotPos] = i

			slotPos += 1

			if slotPos > 54:
				break

		itemCount = len(self.inventorySlotPosDict)
		if itemCount < 15:
			self.SetTableSize(3)

		else:
			lineCount = 3
			lineCount += (itemCount - 15) / 5
			if itemCount % 5:
				lineCount += 1
			self.SetTableSize(lineCount)

		for selectWndPos, inventoryPos in self.inventorySlotPosDict.items():
			itemVNum = getItemVNum(inventoryPos)
			itemCount = getItemCount(inventoryPos)

			if itemCount <= 1:
				itemCount = 0

			setItemVNum(selectWndPos, itemVNum, itemCount)

		self.itemSlot.RefreshSlot()

	def OverOutItem(self):
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OverInItem(self, slotIndex):
		if None != self.tooltipItem:
			inventorySlotPos = self.inventorySlotPosDict[slotIndex]
			self.tooltipItem.SetInventoryItem(inventorySlotPos)

