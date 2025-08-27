import grp
import ui
import wndMgr
import app

class PhaseCurtain(ui.Bar):

	def __init__(self):
		print "NEW CURTAIN  ----------------------------------------------------------------------------"
		ui.Bar.__init__(self, "CURTAIN")
		self.speed = 0.1
		self.curAlpha = 0.0
		self.event = 0
		self.args = -1
		self.FadeInFlag = False
		self.SetWindowName("PhaseCurtain")
		self.AddFlag("float")

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE CURTAIN"
		ui.Bar.__del__(self)

	def SAFE_FadeOut(self, event, args = -1):
		self.FadeOut(ui.__mem_func__(event), args)

	def FadeOut(self, event, args = -1):
		self.curAlpha = 0.0
		self.SetAlpha(self.curAlpha)
		#self.SetTop()
		self.Show()
		self.event = event
		self.args = args

	def FadeIn(self):
		self.event = 0
		self.FadeInFlag = True

	def SetAlpha(self, alpha):
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

		color = grp.GenerateColor(0.0, 0.0, 0.0, alpha)
		self.SetColor(color)

	def OnUpdate(self):

		if 0 != self.event:

			self.curAlpha += self.speed
			if self.curAlpha >= 1.0:
				self.curAlpha = 1.0

				# 이벤트 중간에 멈출경우를 대비해 미리 제거
				event=self.event
				self.event = 0

				#print "페이드 아웃 완료 이벤트 실행"

				if -1 != self.args:
					event(self.args)
				else:
					event()

		elif True == self.FadeInFlag:

			self.curAlpha -= self.speed
			if self.curAlpha <= 0.0:
				self.curAlpha = 0.0
				self.eventFadeIn = 0
				self.FadeInFlag = False
				self.Hide()

		self.SetAlpha(self.curAlpha)
