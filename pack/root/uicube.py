import ui
import net
import mouseModule
import player
import snd
import localeInfo
import item
import grp
import uiScriptLocale
import uiToolTip

class CubeResultWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CubeResultWindow.py")
		except:
			import exception
			exception.Abort("CubeResultWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.titleBar = GetObject("TitleBar")
			self.btnClose = GetObject("CloseButton")
			self.cubeSlot = GetObject("CubeSlot")

		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.BindObject")

		self.cubeSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.cubeSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnClose.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.itemVnum = 0

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.btnClose = None
		self.cubeSlot = None
		self.tooltipItem = None
		self.itemVnum = 0

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SetCubeResultItem(self, itemVnum, count):
		self.itemVnum = itemVnum

		if 0 == count:
			count = 1

		self.cubeSlot.SetItemSlot(0, itemVnum, count)

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def __OnCloseButtonClick(self):
		self.Close()

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			if 0 != self.itemVnum:
				self.tooltipItem.SetItemToolTip(self.itemVnum)

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnPressEscapeKey(self):
		if 0 != self.eventClose:
			self.eventClose()
		return True


class CubeWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.xShopStart = 0
		self.yShopStart = 0
		self.isUsable	= False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CubeWindow.py")
			
		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			if localeInfo.IsARABIC():
				self.board = GetObject("board")
				self.board.SetScale(-1.0, 1.0)
				self.board.SetRenderingRect(-1.0, 0.0, 1.0, 0.0)
				
			self.titleBar = GetObject("TitleBar")
			self.btnAccept = GetObject("AcceptButton")
			self.btnCancel = GetObject("CancelButton")
			self.cubeSlot = GetObject("CubeSlot")
			self.needMoney = GetObject("NeedMoney")
			self.contentScrollbar = GetObject("contentScrollbar")
			self.resultSlots = [GetObject("result1"), GetObject("result2"), GetObject("result3")]
			self.materialSlots = [ 
				[GetObject("material11"), GetObject("material12"), GetObject("material13"), GetObject("material14"), GetObject("material15")],
				[GetObject("material21"), GetObject("material22"), GetObject("material23"), GetObject("material24"), GetObject("material25")],
				[GetObject("material31"), GetObject("material32"), GetObject("material33"), GetObject("material34"), GetObject("material35")],
			]


			row = 0
			for materialRow in self.materialSlots:
				j = 0
				for material in materialRow:
					material.SetOverInItemEvent(lambda trash = 0, rowIndex = row,  col = j: self.__OverInMaterialSlot(trash, rowIndex, col))
					material.SetSelectItemSlotEvent(lambda trash = 0, rowIndex = row,  col = j: self.__OnSelectMaterialSlot(trash, rowIndex, col))
					material.SetOverOutItemEvent(lambda : self.__OverOutMaterialSlot())
					j = j + 1
				row = row + 1

			row = 0
			for resultSlot in self.resultSlots:
				resultSlot.SetOverInItemEvent(lambda trash = 0, rowIndex = row: self.__OverInCubeResultSlot(trash, rowIndex))
				resultSlot.SetOverOutItemEvent(lambda : self.__OverOutMaterialSlot())
				row = row + 1



		except:
			import exception
			exception.Abort("CubeWindow.LoadDialog.BindObject")

		self.contentScrollbar.SetScrollStep(0.15)
		self.contentScrollbar.SetScrollEvent(ui.__mem_func__(self.OnScrollResultList))
		self.cubeSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.cubeSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.cubeSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.cubeSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnCancel.SetEvent(ui.__mem_func__(self.__OnCloseButtonClick))
		self.btnAccept.SetEvent(ui.__mem_func__(self.__OnAcceptButtonClick))

		self.cubeItemInfo = {}
		self.cubeResultInfos = []
		self.cubeMaterialInfos = {}

		self.tooltipItem = None

		self.firstSlotIndex = 0
		self.RESULT_SLOT_COUNT = len(self.resultSlots)
		self.SLOT_SIZEX	= 32
		self.SLOT_SIZEY	= 32
		self.CUBE_SLOT_COUNTX = 8
		self.CUBE_SLOT_COUNTY = 3

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip

	def GetResultCount(self):
		return len(self.cubeResultInfos)

	def OnScrollResultList(self):
		count = self.GetResultCount()
		scrollLineCount = max(0, count - self.RESULT_SLOT_COUNT)
		startIndex = int(scrollLineCount * self.contentScrollbar.GetPos())

		if startIndex != self.firstSlotIndex:
			self.firstSlotIndex = startIndex
			self.Refresh()

	def AddCubeResultItem(self, itemVnum, count):
		self.cubeResultInfos.append((itemVnum, count))
		#self.Refresh()

	def AddMaterialInfo(self, itemIndex, orderIndex, itemVnum, itemCount):
		if itemIndex not in self.cubeMaterialInfos:
			self.cubeMaterialInfos[itemIndex] = [[], [], [], [], []]

		self.cubeMaterialInfos[itemIndex][orderIndex].append((itemVnum, itemCount))
		#print "AddMaterialInfo", itemIndex, orderIndex, itemVnum, itemCount, self.cubeMaterialInfos

	def ClearCubeResultItem(self):
		self.cubeResultInfos = []
		self.Refresh()

	def Destroy(self):
		self.ClearDictionary()
		
		self.titleBar = None
		self.btnAccept = None
		self.btnCancel = None
		self.cubeSlot = None
		self.tooltipItem = None
		self.needMoney = None

	def __OverOutMaterialSlot(self):
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(True)
		self.tooltipItem.HideToolTip()

	def __OverInCubeResultSlot(self, trash, resultIndex):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(True)

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(0)
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append((0, 0))

		#print "resultIndex, firstSlotIndex", resultIndex, self.firstSlotIndex

		resultIndex = resultIndex + self.firstSlotIndex
		itemVnum, itemCount = self.cubeResultInfos[resultIndex]

		self.tooltipItem.AddItemData(itemVnum, metinSlot, attrSlot)
		

	# 재료를 클릭하면 인벤토리에서 해당 아이템을 찾아서 등록함.
	def __OnSelectMaterialSlot(self, trash, resultIndex, materialIndex):
		resultIndex = resultIndex + self.firstSlotIndex
		if resultIndex not in self.cubeMaterialInfos:
			return

		materialInfo = self.cubeMaterialInfos[resultIndex]
		materialCount = len(materialInfo[materialIndex])

		if 0 == materialCount:
			return

		for itemVnum, itemCount in materialInfo[materialIndex]:
			bAddedNow = False	# 이번에 클릭함으로써 아이템이 추가되었나?
			item.SelectItem(itemVnum)
			itemSizeX, itemSizeY = item.GetItemSize()

			# 제조에 필요한 만큼의 재료를 가지고 있는가?
			if player.GetItemCountByVnum(itemVnum) >= itemCount:
				for i in xrange(player.INVENTORY_SLOT_COUNT):
					vnum = player.GetItemIndex(i)
					count= player.GetItemCount(i)

					if vnum == itemVnum and count >= itemCount:
						# 이미 같은 아이템이 등록되어 있는지 검사하고, 없다면 추가함
						bAlreadyExists = False
						for slotPos, invenPos in self.cubeItemInfo.items():
							if invenPos == i:
								bAlreadyExists = True

						if True == bAlreadyExists:
							continue #continue inventory iterating

						#print "Cube Status : ", self.cubeItemInfo

						# 여기 진입하면 큐브에 등록되지 않은 아이템이므로, 빈 큐브 슬롯에 해당 아이템 추가
						bCanAddSlot = False
						for slotPos in xrange(self.cubeSlot.GetSlotCount()):
							# 이 큐브 슬롯이 비어있는가?
							if not slotPos in self.cubeItemInfo:
								upperColumnItemSizeY = -1
								currentSlotLine = int(slotPos / self.CUBE_SLOT_COUNTX)
								cubeColumn = int(slotPos % self.CUBE_SLOT_COUNTX)


								# 만약 큐브에 3칸짜리 아이템이 등록되어 있다면, 이 열(column)은 더 이상 볼 것도 없이 넘어간다
								if cubeColumn in self.cubeItemInfo:
									columnVNUM = player.GetItemIndex(self.cubeItemInfo[cubeColumn])
									item.SelectItem(columnVNUM)
									columnItemSizeX, columnItemSizeY = item.GetItemSize()

									if 3 == columnItemSizeY:
										continue #continue cube slot iterating

								if 0 < currentSlotLine and slotPos - self.CUBE_SLOT_COUNTX in self.cubeItemInfo:
									upperColumnVNUM = player.GetItemIndex(self.cubeItemInfo[slotPos - self.CUBE_SLOT_COUNTX])
									item.SelectItem(upperColumnVNUM)
									columnItemSizeX, upperColumnItemSizeY = item.GetItemSize()
								
								# 1칸짜리 아이템은 바로 윗줄에 한칸짜리 아이템이 있어야 함
								if 1 == itemSizeY: 
									if 0 == currentSlotLine:
										bCanAddSlot = True
									elif 1 == currentSlotLine and 1 == upperColumnItemSizeY:
										bCanAddSlot = True
									elif 2 == currentSlotLine:
										bCanAddSlot = True
								# 2칸짜리 아이템은 위아래가 비어있어야 함
								elif 2 == itemSizeY:
									if 0 == currentSlotLine and not cubeColumn + self.CUBE_SLOT_COUNTX in self.cubeItemInfo:
										bCanAddSlot = True
									elif 1 == currentSlotLine and 1 == upperColumnItemSizeY and not cubeColumn + (self.CUBE_SLOT_COUNTX * 2) in self.cubeItemInfo:
										bCanAddSlot = True
								# 3칸짜리 아이템은 해당 Column 자체가 모두 비어있어야 함
								else:
									if not cubeColumn in self.cubeItemInfo and not cubeColumn + self.CUBE_SLOT_COUNTX in self.cubeItemInfo and not cubeColumn + (self.CUBE_SLOT_COUNTX * 2) in self.cubeItemInfo:
										bCanAddSlot = True

								if True == bCanAddSlot:
									self.cubeItemInfo[slotPos] = i
									self.cubeSlot.SetItemSlot(slotPos, vnum, count)
									net.SendChatPacket("/cube add %d %d" % (slotPos, i))
									
									bAddedNow = True

							if True == bAddedNow:
								break #break cube slot iterating

						if True == bAddedNow:
							break #break inventory iterating

				if True == bAddedNow:
					break #break material iterating

				

	def __OverInMaterialSlot(self, trash, resultIndex, col):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetCannotUseItemForceSetDisableColor(False)

		resultIndex = resultIndex + self.firstSlotIndex

		if resultIndex not in self.cubeMaterialInfos:
			return

		i = 0
		materialInfo = self.cubeMaterialInfos[resultIndex]
		materialCount = len(materialInfo[col])

		for itemVnum, count in materialInfo[col]:
			item.SelectItem(itemVnum)
			if player.GetItemCountByVnum(itemVnum) >= count:
				self.tooltipItem.AppendTextLine("%s" % (item.GetItemName()), grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)).SetFeather()
			else:
				self.tooltipItem.AppendTextLine("%s" % (item.GetItemName()), grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)).SetFeather()
			
			if i < materialCount - 1:
				self.tooltipItem.AppendTextLine(uiScriptLocale.CUBE_REQUIRE_MATERIAL_OR)
				
			i = i + 1

		self.tooltipItem.Show()
	

	def Open(self):
		self.cubeItemInfo = {}
		self.cubeResultInfos = []
		self.cubeMaterialInfos = {}

		self.Refresh()
		self.Show()

		self.isUsable	= True
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()

	def UpdateInfo(self, gold, itemVnum, count):
		if self.needMoney:
			self.needMoney.SetText(localeInfo.NumberToMoneyString(gold))

		self.Refresh()

	def OnPressEscapeKey(self):
		self.__OnCloseButtonClick()
		return True
	
	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.Hide()
		self.cubeItemInfo = {}
		self.cubeMaterialInfos = {}
		self.cubeResultInfos = {}
		self.firstSlotIndex = 0
		self.contentScrollbar.SetPos(0)

		if self.needMoney:
			self.needMoney.SetText("0")		

	def Clear(self):
		self.Refresh()

	def Refresh(self):
		for slotPos in xrange(self.cubeSlot.GetSlotCount()):

			if not slotPos in self.cubeItemInfo:
				self.cubeSlot.ClearSlot(slotPos)
				continue

			invenPos = self.cubeItemInfo[slotPos]
			itemCount = player.GetItemCount(invenPos)
			if itemCount > 0:
				self.cubeSlot.SetItemSlot(slotPos, player.GetItemIndex(invenPos), itemCount)
			else:
				del self.cubeItemInfo[slotPos]
				self.cubeSlot.ClearSlot(slotPos)

		i = 0
		for itemVnum, count in self.cubeResultInfos[self.firstSlotIndex:]:
			currentSlot = self.resultSlots[i]

			item.SelectItem(itemVnum)
			
			currentSlot.SetItemSlot(0, itemVnum, count)
			currentSlot.Show()

			# Center Align
			item.SelectItem(itemVnum)
			sizeX, sizeY = item.GetItemSize()
			localX, localY = currentSlot.GetLocalPosition()

			currentSlot.SetSize(self.SLOT_SIZEX, self.SLOT_SIZEY * sizeY)

			adjustLocalY = 0
			if sizeY < 3:
				adjustLocalY = int(32 / sizeY)

			currentSlot.SetPosition(localX, 0 + adjustLocalY)

			i = i + 1
			if 3 <= i:
				break

		#print "self.cubeMaterialInfos : ", self.cubeMaterialInfos
		if self.firstSlotIndex in self.cubeMaterialInfos:
			for i in xrange(self.RESULT_SLOT_COUNT):
				materialList = self.cubeMaterialInfos[self.firstSlotIndex + i]
				#print "Refresh ::: ", materialList
				j = 0
				for materialInfo in materialList:
					if 0 < len(materialInfo):
						currentSlot = self.materialSlots[i][j]
						itemVnum, itemCount = materialInfo[0]
						currentSlot.SetItemSlot(0, itemVnum, itemCount)
						j = j + 1

						# Center Align
						item.SelectItem(itemVnum)
						sizeX, sizeY = item.GetItemSize()
						localX, localY = currentSlot.GetLocalPosition()

						currentSlot.SetSize(self.SLOT_SIZEX, self.SLOT_SIZEY * sizeY)

						adjustLocalY = 0
						if sizeY < 3:
							adjustLocalY = int(32 / sizeY)

						currentSlot.SetPosition(localX, 0 + adjustLocalY)

				for k in xrange(5):
					if k >= j:
						self.materialSlots[i][k].ClearSlot(0)

				if self.RESULT_SLOT_COUNT <= i:
					break

		self.cubeSlot.RefreshSlot()

	def __OnCloseButtonClick(self):
		if self.isUsable:
			self.isUsable = False

			print "큐브 닫기"
			net.SendChatPacket("/cube close")

		self.Close()

	def __OnAcceptButtonClick(self):
		if len(self.cubeItemInfo) == 0:
			"빈 큐브"
			return
		
		print "큐브 제작 시작"		
		#for invenPos in self.cubeItemInfo.values():
		#	net.SendChatPacket("/cube add " + str(invenPos))
		net.SendChatPacket("/cube make")			
		
	def __OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return

			for slotPos, invenPos in self.cubeItemInfo.items():
				if invenPos == attachedSlotPos:
					del self.cubeItemInfo[slotPos]
			
			self.cubeItemInfo[selectedSlotPos] = attachedSlotPos
			net.SendChatPacket("/cube add %d %d" % (selectedSlotPos, attachedSlotPos))

			self.Refresh()

	def __OnSelectItemSlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if not selectedSlotPos in self.cubeItemInfo:
				return

			snd.PlaySound("sound/ui/drop.wav")

			net.SendChatPacket("/cube del %d " % selectedSlotPos)
			del self.cubeItemInfo[selectedSlotPos]

			self.Refresh()

	def __OnOverInItem(self, slotIndex):
		if self.tooltipItem:
			if self.cubeItemInfo.has_key(slotIndex):
				self.tooltipItem.SetInventoryItem(self.cubeItemInfo[slotIndex])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnUpdate(self):
		USE_SHOP_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.__OnCloseButtonClick()

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
	app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()

	class TestGame(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)

			localeInfo.LoadLocaleData()

			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()

			self.cubeWindow = CubeWindow()
			self.cubeWindow.LoadWindow()
			self.cubeWindow.SetItemToolTip(self.tooltipItem)
			self.cubeWindow.Open()

			self.cubeResultWindow = CubeResultWindow()
			self.cubeResultWindow.LoadWindow()
			self.cubeResultWindow.SetItemToolTip(self.tooltipItem)
			self.cubeResultWindow.SetCubeResultItem(27001, 1)
			self.cubeResultWindow.Open()

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
