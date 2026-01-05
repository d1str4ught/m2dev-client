# -*- coding: utf-8 -*-
"""
Multi-Language Hot-Reload System
=================================

This module provides a clean, reusable system for hot-reloading locale changes
without restarting the client. It's designed to be window-agnostic and can be
used with any UI window (login, game, etc.).

Architecture:
- C++ side handles:  LoadConfig() → LoadLocaleData() → Clear Python module cache
- Python side handles: Module reimport → UI state save/restore → Window recreation

Usage:
    from uilocalechange import LocaleChangeManager

    # In your window class __init__:
    self.localeChangeManager = LocaleChangeManager(self)

    # When locale changes (e.g., from a locale selector):
    self.localeChangeManager.ReloadWithNewLocale(newLocaleCode)

Features:
- Automatically saves and restores UI state (text inputs, selections, etc.)
- Handles board visibility states
- Preserves virtual keyboard state
- Works with any window that follows the standard pattern
"""

import app
import dbg
import ui
import sys


class LocaleChangeManager:
	"""
	Manages locale hot-reload for a UI window.

	This class handles the complete lifecycle of a locale change:
	1. Save current UI state
	2. Call C++ to reload locale data
	3. Reimport Python locale modules
	4. Recreate UI with new locale
	5. Restore saved state
	"""

	def __init__(self, window):
		"""
		Initialize the locale change manager.

		Args:
			window: The UI window instance to manage (e.g., LoginWindow, GameWindow)
		"""
		self.window = window
		self.stateHandlers = {}
		self._RegisterDefaultStateHandlers()

	def _RegisterDefaultStateHandlers(self):
		"""Register default state save/restore handlers for common UI elements."""
		# Text input fields
		self.RegisterStateHandler("idEditLine", self._SaveEditLineText, self._RestoreEditLineText)
		self.RegisterStateHandler("pwdEditLine", self._SaveEditLineText, self._RestoreEditLineText)

		# List selections
		self.RegisterStateHandler("serverList", self._SaveListSelection, self._RestoreListSelection)
		self.RegisterStateHandler("channelList", self._SaveListSelection, self._RestoreListSelection)

		# Virtual keyboard
		self.RegisterStateHandler("virtualKeyboard", self._SaveVisibility, self._RestoreVisibility)

		# Server info text
		self.RegisterStateHandler("serverInfo", self._SaveTextLineText, self._RestoreTextLineText)

	def RegisterStateHandler(self, elementName, saveFunc, restoreFunc):
		"""
		Register a custom state handler for a UI element.

		Args:
			elementName: The attribute name of the UI element (e.g., "idEditLine")
			saveFunc: Function(element) -> stateData to save state
			restoreFunc: Function(element, stateData) to restore state
		"""
		self.stateHandlers[elementName] = (saveFunc, restoreFunc)

	def _SaveEditLineText(self, editLine):
		"""Save text from an edit line."""
		if editLine:
			return editLine.GetText()
		return ""

	def _RestoreEditLineText(self, editLine, text):
		"""Restore text to an edit line."""
		if editLine and text:
			editLine.SetText(text)

	def _SaveListSelection(self, listBox):
		"""Save selected item ID from a list box."""
		if listBox:
			return listBox.GetSelectedItem()
		return None

	def _RestoreListSelection(self, listBox, selectedID):
		"""Restore selected item in a list box by finding its position."""
		if listBox and selectedID is not None:
			# Find position for the saved ID
			for position, itemID in listBox.keyDict.items():
				if itemID == selectedID:
					listBox.SelectItem(position)
					return True
		return False

	def _SaveVisibility(self, element):
		"""Save visibility state of an element."""
		if element:
			return element.IsShow()
		return False

	def _RestoreVisibility(self, element, wasVisible):
		"""Restore visibility state of an element."""
		if element:
			if wasVisible:
				element.Show()
			else:
				element.Hide()

	def _SaveTextLineText(self, textLine):
		"""Save text from a text line."""
		if textLine:
			return textLine.GetText()
		return ""

	def _RestoreTextLineText(self, textLine, text):
		"""Restore text to a text line."""
		if textLine and text:
			textLine.SetText(text)

	def SaveLocaleCode(self, localeCode):
		"""
		Save locale code to config/locale.cfg file.

		Args:
			localeCode: Two-letter locale code (e.g., "en", "ro", "de")

		Returns:
			True if saved successfully, False otherwise
		"""
		try:
			import os
			if not os.path.exists("config"):
				os.makedirs("config")
			with open("config/locale.cfg", "w") as f:
				f.write(localeCode)
			return True
		except Exception as e:
			dbg.TraceError("Failed to save locale config: %s" % str(e))
			return False

	def ReloadWithNewLocale(self, newLocaleCode, scriptPath="uiscript/LoginWindow.py"):
		"""
		Hot-reload the UI with a new locale.

		This is the main entry point for locale changes. It handles the complete
		reload process:
		1. Save locale code to config file
		2. Call C++ to reload locale data and clear Python module cache
		3. Reimport Python locale modules
		4. Save current UI state
		5. Recreate UI
		6. Restore UI state

		Args:
			newLocaleCode: The new locale code to switch to
			scriptPath: Path to the UI script file to reload (default: LoginWindow.py)

		Returns:
			True if reload succeeded, False otherwise
		"""
		try:
			dbg.TraceError("=== Starting Locale Hot-Reload to '%s' ===" % newLocaleCode)

			# Step 1: Save locale code to file
			if not self.SaveLocaleCode(newLocaleCode):
				dbg.TraceError("Failed to save locale code")
				return False

			# Step 2: Call C++ comprehensive reload
			# This does: LoadConfig() → LoadLocaleData() → Clear Python module cache
			reloadSuccess = app.ReloadLocale()
			if not reloadSuccess:
				dbg.TraceError("C++ ReloadLocale() failed")
				return False

			# Step 3: Reimport Python locale modules
			self._ReimportLocaleModules()

			# Step 4: Save current UI state
			savedState = self._SaveWindowState()

			# Step 5: Recreate UI
			self._RecreateUI(scriptPath)

			# Step 6: Restore UI state
			self._RestoreWindowState(savedState)

			dbg.TraceError("=== Locale Hot-Reload Complete ===")
			return True

		except Exception as e:
			dbg.TraceError("Error in ReloadWithNewLocale: %s" % str(e))
			import exception
			exception.Abort("ReloadWithNewLocale")
			return False

	def _ReimportLocaleModules(self):
		"""Force reimport of locale modules after C++ cleared the cache."""
		dbg.TraceError("Reimporting locale modules...")

		# Import fresh modules - C++ already deleted them from sys.modules
		localeInfo = __import__('localeInfo')
		uiScriptLocale = __import__('uiScriptLocale')

		# Update sys.modules references
		sys.modules['localeInfo'] = localeInfo
		sys.modules['uiScriptLocale'] = uiScriptLocale

		# CRITICAL: Update the window module's globals, not ours!
		# Get the window's module (e.g., intrologin module)
		windowModule = sys.modules.get(self.window.__module__)
		if windowModule:
			dbg.TraceError("Updating globals in module: %s" % self.window.__module__)
			windowModule.localeInfo = localeInfo
			windowModule.uiScriptLocale = uiScriptLocale
		else:
			dbg.TraceError("WARNING: Could not find window module: %s" % self.window.__module__)

		# Also update this module's globals for safety
		globals()['localeInfo'] = localeInfo
		globals()['uiScriptLocale'] = uiScriptLocale

		dbg.TraceError("Locale modules reimported successfully")

	def _SaveWindowState(self):
		"""
		Save the current state of all registered UI elements.

		Returns:
			Dictionary containing saved state data
		"""
		state = {
			"elements": {},
			"visibleBoard": None,
		}

		# Save state of registered elements
		for elementName, (saveFunc, _) in self.stateHandlers.items():
			if hasattr(self.window, elementName):
				element = getattr(self.window, elementName)
				if element:
					state["elements"][elementName] = saveFunc(element)

		# Determine which board is currently visible
		for boardName in ["loginBoard", "serverBoard", "connectBoard"]:
			if hasattr(self.window, boardName):
				board = getattr(self.window, boardName)
				if board and board.IsShow():
					state["visibleBoard"] = boardName
					break

		dbg.TraceError("Saved window state: visibleBoard=%s" % state["visibleBoard"])
		return state

	def _RecreateUI(self, scriptPath):
		"""
		Recreate the UI by clearing and reloading the script.

		Args:
			scriptPath: Path to the UI script file
		"""
		dbg.TraceError("Recreating UI from script: %s" % scriptPath)

		# Completely destroy the locale selector - we'll recreate it fresh
		if hasattr(self.window, 'localeSelector') and self.window.localeSelector:
			dbg.TraceError("Destroying old locale selector before UI recreation")
			self.window.localeSelector.Destroy()
			self.window.localeSelector = None

		# Clear existing UI elements
		if hasattr(self.window, 'ClearDictionary'):
			self.window.ClearDictionary()

		# Reload the UI script file with new locale strings
		# This will create a fresh locale selector through __LoadScript
		if hasattr(self.window, '_LoginWindow__LoadScript'):
			# Private method name mangling for LoginWindow
			self.window._LoginWindow__LoadScript(scriptPath)
		elif hasattr(self.window, 'LoadScript'):
			self.window.LoadScript(scriptPath)

		# __LoadScript should have created a new locale selector
		# Make sure it's visible
		if hasattr(self.window, 'localeSelector') and self.window.localeSelector:
			dbg.TraceError("Locale selector created by __LoadScript, ensuring visibility")
			self.window.localeSelector.Show()
			self.window.localeSelector.SetTop()
		else:
			# If __LoadScript didn't create it, create it manually
			dbg.TraceError("Creating locale selector manually")
			from uilocaleselector import LocaleSelector
			self.window.localeSelector = LocaleSelector()
			self.window.localeSelector.Create(self.window)
			# Set the event handler to call back to the window's method
			if hasattr(self.window, '_LoginWindow__OnLocaleChanged'):
				import ui
				self.window.localeSelector.SetLocaleChangedEvent(ui.__mem_func__(self.window._LoginWindow__OnLocaleChanged))
			self.window.localeSelector.Show()
			self.window.localeSelector.SetTop()

		# Hide all boards to reset state
		for boardName in ["loginBoard", "serverBoard", "connectBoard"]:
			if hasattr(self.window, boardName):
				board = getattr(self.window, boardName)
				if board:
					board.Hide()

		# Hide virtual keyboard
		if hasattr(self.window, "virtualKeyboard"):
			vk = getattr(self.window, "virtualKeyboard")
			if vk:
				vk.Hide()

	def _RestoreWindowState(self, state):
		"""
		Restore the saved UI state.

		Args:
			state: Dictionary containing saved state data
		"""
		dbg.TraceError("Restoring window state...")

		# Restore element states
		for elementName, savedData in state["elements"].items():
			if elementName in self.stateHandlers:
				_, restoreFunc = self.stateHandlers[elementName]
				if hasattr(self.window, elementName):
					element = getattr(self.window, elementName)
					if element:
						restoreFunc(element, savedData)

		# Rebuild locale-dependent dictionaries (like loginFailureMsgDict)
		self._RebuildLocaleDictionaries()

		# Restore visible board
		visibleBoard = state.get("visibleBoard")
		if visibleBoard:
			self._RestoreBoardVisibility(visibleBoard, state)

		# CRITICAL: Make sure locale selector is visible and on top after everything is restored
		if hasattr(self.window, 'localeSelector') and self.window.localeSelector:
			dbg.TraceError("Final check: ensuring locale selector is visible")
			self.window.localeSelector.Show()
			self.window.localeSelector.SetTop()

	def _RebuildLocaleDictionaries(self):
		"""Rebuild any dictionaries that depend on localeInfo strings."""
		# Check if this is a LoginWindow with loginFailureMsgDict
		if hasattr(self.window, 'loginFailureMsgDict'):
			import localeInfo
			dbg.TraceError("Rebuilding loginFailureMsgDict with new locale strings")
			self.window.loginFailureMsgDict = {
				"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
				"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
				"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
				"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
				"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
				"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
				"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
				"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
				"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
				"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
				"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
				"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
				"BADSCLID"	: localeInfo.LOGIN_FAILURE_WRONG_SOCIALID,
				"AGELIMIT"	: localeInfo.LOGIN_FAILURE_SHUTDOWN_TIME,
			}

		if hasattr(self.window, 'loginFailureFuncDict'):
			self.window.loginFailureFuncDict = {
				"WRONGPWD"	: self.window._LoginWindow__DisconnectAndInputPassword if hasattr(self.window, '_LoginWindow__DisconnectAndInputPassword') else None,
				"QUIT"		: __import__('app').Exit,
			}

	def _RestoreBoardVisibility(self, boardName, state):
		"""
		Restore the visibility of a specific board and its state.

		Args:
			boardName: Name of the board to show ("loginBoard", "serverBoard", "connectBoard")
			state: Full saved state dictionary
		"""
		dbg.TraceError("Restoring board visibility: %s" % boardName)

		if boardName == "loginBoard":
			self._RestoreLoginBoard()
		elif boardName == "serverBoard":
			self._RestoreServerBoard(state)
		elif boardName == "connectBoard":
			self._RestoreConnectBoard()

	def _RestoreLoginBoard(self):
		"""Show and configure the login board."""
		if hasattr(self.window, "loginBoard"):
			self.window.loginBoard.Show()

	def _RestoreServerBoard(self, state):
		"""Show and configure the server board with saved selections."""
		if not hasattr(self.window, "serverBoard"):
			return

		self.window.serverBoard.Show()

		# Refresh server list first
		if hasattr(self.window, '_LoginWindow__RefreshServerList'):
			self.window._LoginWindow__RefreshServerList()

		# Now restore server selection AFTER the list is refreshed
		savedServerID = state["elements"].get("serverList")
		if savedServerID is not None and hasattr(self.window, 'serverList') and self.window.serverList:
			# Find the position index for the saved server ID
			# keyDict maps position -> server ID
			for position, serverID in self.window.serverList.keyDict.items():
				if serverID == savedServerID:
					# SelectItem expects position index, not server ID
					self.window.serverList.SelectItem(position)

					# Refresh channel list for the selected server
					if hasattr(self.window, '_LoginWindow__RequestServerStateList'):
						self.window._LoginWindow__RequestServerStateList()
					if hasattr(self.window, '_LoginWindow__RefreshServerStateList'):
						self.window._LoginWindow__RefreshServerStateList()

					# Restore channel selection AFTER channel list is refreshed
					savedChannelID = state["elements"].get("channelList")
					if savedChannelID is not None and hasattr(self.window, 'channelList') and self.window.channelList:
						# Find the position index for the saved channel ID
						for channelPos, channelID in self.window.channelList.keyDict.items():
							if channelID == savedChannelID:
								self.window.channelList.SelectItem(channelPos)
								break
					break

	def _RestoreConnectBoard(self):
		"""Show and configure the connect board."""
		if not hasattr(self.window, "connectBoard"):
			return

		# Connect board overlays login board
		if hasattr(self.window, "loginBoard"):
			self.window.loginBoard.Show()

		self.window.connectBoard.Show()

		# Explicitly show connect board children (they may not auto-show)
		if hasattr(self.window, "selectConnectButton"):
			btn = getattr(self.window, "selectConnectButton")
			if btn:
				btn.Show()

		if hasattr(self.window, "serverInfo"):
			info = getattr(self.window, "serverInfo")
			if info:
				info.Show()
