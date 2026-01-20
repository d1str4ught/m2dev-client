# -*- coding: utf-8 -*-
"""
Locale Selector UI Component
=============================

A reusable UI component for selecting and changing the client language.
Can be added to any window (login, game settings, etc.).

Usage:
    from uilocaleselector import LocaleSelector

    # In your window class:
    self.localeSelector = LocaleSelector()
    self.localeSelector.Create(self)
    self.localeSelector.SetLocaleChangedEvent(ui.__mem_func__(self.__OnLocaleChanged))

    # Implement the callback:
    def __OnLocaleChanged(self, newLocaleCode):
        # Handle UI recreation here
        pass
"""

import ui
import uiCommon
import localeInfo
import wndMgr


# Available locales configuration
AVAILABLE_LOCALES = [
	{"code": "ae", "name": "Arabic", "flag": "ae"},
	{"code": "br", "name": "Português Brasileiro", "flag": "br"},
	{"code": "en", "name": "English", "flag": "en"},
	{"code": "cz", "name": "Čeština", "flag": "cz"},
	{"code": "de", "name": "Deutsch", "flag": "de"},
	{"code": "dk", "name": "Dansk", "flag": "dk"},
	{"code": "es", "name": "Español", "flag": "es"},
	{"code": "fr", "name": "Français", "flag": "fr"},
	{"code": "gr", "name": "Ελληνικά", "flag": "gr"},
	{"code": "hu", "name": "Magyar", "flag": "hu"},
	{"code": "it", "name": "Italiano", "flag": "it"},
	{"code": "nl", "name": "Nederlands", "flag": "nl"},
	{"code": "pl", "name": "Polski", "flag": "pl"},
	{"code": "pt", "name": "Português", "flag": "pt"},
	{"code": "ro", "name": "Română", "flag": "ro"},
	{"code": "ru", "name": "Русский", "flag": "ru"},
	{"code": "tr", "name": "Türkçe", "flag": "tr"},
]

# Flag image path template
FLAG_IMAGE_PATH = "d:/ymir work/ui/intro/login/server_flag_%s.sub"


class LocaleSelector(ui.Window):
	"""
	UI component for selecting and changing client language.

	Features:
	- Displays flag buttons for all available locales
	- Shows confirmation dialog before changing
	- Triggers callback when locale is confirmed
	- Self-contained and reusable
	"""

	def __init__(self):
		ui.Window.__init__(self)
		self.background = None
		self.flagButtons = []
		self.confirmDialog = None
		self.selectedLocaleCode = None
		self.eventLocaleChanged = None

	def __del__(self):
		ui.Window.__del__(self)

	def Destroy(self):
		"""Clean up resources when destroying the selector."""
		self.eventLocaleChanged = None
		self.selectedLocaleCode = None

		if self.confirmDialog:
			self.confirmDialog.Close()
			self.confirmDialog = None

		for btn in self.flagButtons:
			btn.Hide()
			btn = None
		self.flagButtons = []

		if self.background:
			self.background.Hide()
			self.background = None

	def Create(self, parent):
		"""
		Create and display the locale selector UI.

		Args:
			parent: The parent window to attach to
		"""
		self.SetParent(parent)
		self.SetSize(wndMgr.GetScreenWidth(), 35)
		self.SetPosition(0, 20)

		# Create background board
		self.background = ui.ThinBoard()
		self.background.SetParent(self)
		self.background.SetSize(wndMgr.GetScreenWidth(), 35)
		self.background.SetPosition(0, 0)
		self.background.Show()

		# Create flag buttons
		self._CreateFlagButtons()

		self.Show()

	def _CreateFlagButtons(self):
		"""Create flag buttons for all available locales."""
		localeCount = len(AVAILABLE_LOCALES)
		if localeCount == 0:
			return

		buttonSpacing = wndMgr.GetScreenWidth() / localeCount
		xPosition = 0

		for locale in AVAILABLE_LOCALES:
			flagPath = FLAG_IMAGE_PATH % locale["flag"]

			button = ui.Button()
			button.SetParent(self.background)
			button.SetPosition(xPosition + 15, 10)
			button.SetUpVisual(flagPath)
			button.SetOverVisual(flagPath)
			button.SetDownVisual(flagPath)
			button.SetToolTipText(locale["name"])
			button.SetEvent(ui.__mem_func__(self._OnClickFlag), locale["code"])
			button.Show()

			self.flagButtons.append(button)
			xPosition += buttonSpacing

	def _OnClickFlag(self, localeCode):
		"""
		Handle flag button click - show confirmation dialog.

		Args:
			localeCode: The locale code that was clicked
		"""
		self.selectedLocaleCode = localeCode

		# Get locale name for display
		localeName = "Unknown"
		for locale in AVAILABLE_LOCALES:
			if locale["code"] == localeCode:
				localeName = locale["name"]
				break

		# Show confirmation dialog
		if not self.confirmDialog:
			self.confirmDialog = uiCommon.QuestionDialog()

		self.confirmDialog.SetText(localeInfo.LOCALE_CHANGE_CONFIRM % localeName)
		self.confirmDialog.SetAcceptEvent(ui.__mem_func__(self._OnConfirmLocaleChange))
		self.confirmDialog.SetCancelEvent(ui.__mem_func__(self._OnCancelLocaleChange))
		self.confirmDialog.Open()

	def _OnConfirmLocaleChange(self):
		"""User confirmed locale change - trigger the callback."""
		if self.confirmDialog:
			self.confirmDialog.Close()

		if not self.selectedLocaleCode:
			return

		# Notify parent window to handle the locale change
		if self.eventLocaleChanged:
			self.eventLocaleChanged(self.selectedLocaleCode)

	def _OnCancelLocaleChange(self):
		"""User cancelled locale change."""
		if self.confirmDialog:
			self.confirmDialog.Close()
		self.selectedLocaleCode = None

	def SetLocaleChangedEvent(self, event):
		"""
		Set callback function to be called when locale is confirmed.

		Args:
			event: Callback function(localeCode) to handle locale change
		"""
		self.eventLocaleChanged = event
