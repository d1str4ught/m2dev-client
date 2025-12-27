import app
import net
import ui
import snd
import wndMgr
import uiScriptLocale
import localeInfo

# Most related code is in PythonApplicationLogo.cpp

app.SetGuildMarkPath("test")

class LogoWindow(ui.ScriptWindow):

	# List of videos to display (shown in array order)
	videoList = []
	
	def __init__(self, stream):
		print "NEW LOGO WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGO, self)
		self.stream = stream
		self.playingVideo = 0
		self.bNeedUpdate = True
		self.nextLogoIndex = 0
		self.videoList = ["logo1.avi", "logo2.avi"]
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGO, 0)
		print "---------------------------------------------------------------------------- DELETE LOGO WINDOW"
		
	def Open(self):
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectLogoWindow")
		self.Show()
		
		self.LoadNextVideo()

		app.ShowCursor()
		print "OPEN LOGO WINDOW  ----------------------------------------------------------------------------"
		
	def Close(self):
		print "---------------------------------------------------------------CLOSE LOGO WINDOW"
		app.OnLogoClose()
		self.KillFocus()
		self.Hide()
		
		app.HideCursor()
		
	# Skip to introLogin if video playback is impossible or videos are not provided.
	def OnUpdate(self):
		if self.bNeedUpdate:
			if self.playingVideo == 0:
				if self.nextLogoIndex < len(self.videoList):
					self.CloseVideo()
					self.LoadNextVideo()
				else:
					self.bNeedUpdate = False
					self.stream.SetLoginPhase()
			else:
				self.playingVideo = app.OnLogoUpdate()
		
		
	def OnRender(self):
		if self.playingVideo:
			app.OnLogoRender()
			
	def LoadNextVideo(self):
		if self.nextLogoIndex < len(self.videoList):
			self.playingVideo = app.OnLogoOpen(self.videoList[self.nextLogoIndex])
			self.nextLogoIndex = self.nextLogoIndex + 1
			
	def CloseVideo(self):
		app.OnLogoClose()
		
