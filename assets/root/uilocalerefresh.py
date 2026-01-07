"""
Generic UI Locale Refresh System
This module provides automatic locale refresh for UI windows without hardcoding element names.
"""

import dbg
import ui

class LocaleRefreshHelper:
	"""
	Helper class to automatically refresh UI text elements when locale changes.
	Works by re-reading the original UI script and applying new locale strings.
	"""

	def __init__(self):
		self.scriptCache = {}  # Cache loaded UI scripts

	def RefreshWindow(self, window, scriptPath):
		"""
		Automatically refresh all text elements in a window by re-reading the UI script.

		Args:
			window: The ui.ScriptWindow instance to refresh
			scriptPath: Path to the UI script file (e.g., "UIScript/LoginWindow.py")

		Returns:
			Number of elements successfully refreshed
		"""
		import uiScriptLocale
		import localeInfo

		dbg.TraceError("LocaleRefreshHelper: Refreshing window from %s" % scriptPath)

		# Load the UI script to get the original text definitions
		try:
			scriptData = self._LoadUIScript(scriptPath)
		except Exception as e:
			dbg.TraceError("LocaleRefreshHelper: Failed to load script %s: %s" % (scriptPath, str(e)))
			return 0

		# Recursively refresh all elements
		refreshCount = self._RefreshElement(window, scriptData.get("window", {}), window)

		dbg.TraceError("LocaleRefreshHelper: Refreshed %d elements" % refreshCount)
		return refreshCount

	def RefreshElementsByMapping(self, elementMap):
		"""
		Refresh UI elements using a manual mapping dictionary.
		Useful for elements that can't be auto-detected.

		Args:
			elementMap: Dict of {element_instance: locale_string_name}

		Example:
			mapping = {
				self.loginButton: "LOGIN_CONNECT",
				self.exitButton: "LOGIN_EXIT"
			}
			helper.RefreshElementsByMapping(mapping)
		"""
		import uiScriptLocale
		import localeInfo

		refreshCount = 0
		for element, localeKey in elementMap.items():
			try:
				# Try uiScriptLocale first, then localeInfo
				if hasattr(uiScriptLocale, localeKey):
					text = getattr(uiScriptLocale, localeKey)
				elif hasattr(localeInfo, localeKey):
					text = getattr(localeInfo, localeKey)
				else:
					dbg.TraceError("LocaleRefreshHelper: Locale key not found: %s" % localeKey)
					continue

				# Set the text
				if hasattr(element, 'SetText'):
					element.SetText(text)
					refreshCount += 1
			except Exception as e:
				dbg.TraceError("LocaleRefreshHelper: Failed to refresh element with key %s: %s" % (localeKey, str(e)))

		return refreshCount

	def RefreshDictionaries(self, targetDict, localeModule="localeInfo"):
		"""
		Rebuild a dictionary with fresh locale strings.
		Useful for error message dictionaries, etc.

		Args:
			targetDict: Dictionary to rebuild with format {key: "LOCALE_CONSTANT_NAME"}
			localeModule: Name of the locale module ("localeInfo" or "uiScriptLocale")

		Returns:
			New dictionary with fresh locale values

		Example:
			template = {
				"WRONGPWD": "LOGIN_FAILURE_WRONG_PASSWORD",
				"FULL": "LOGIN_FAILURE_TOO_MANY_USER"
			}
			newDict = helper.RefreshDictionaries(template)
		"""
		import localeInfo
		import uiScriptLocale

		module = localeInfo if localeModule == "localeInfo" else uiScriptLocale
		newDict = {}

		for key, localeKey in targetDict.items():
			if hasattr(module, localeKey):
				newDict[key] = getattr(module, localeKey)
			else:
				dbg.TraceError("LocaleRefreshHelper: Locale key not found: %s" % localeKey)

		return newDict

	def _LoadUIScript(self, scriptPath):
		"""Load and cache a UI script file."""
		if scriptPath in self.scriptCache:
			return self.scriptCache[scriptPath]

		# Execute the UI script to get its data
		scriptData = {}
		try:
			execfile(scriptPath, scriptData)
			self.scriptCache[scriptPath] = scriptData
		except Exception as e:
			dbg.TraceError("LocaleRefreshHelper: Failed to execute script %s: %s" % (scriptPath, str(e)))
			raise

		return scriptData

	def _RefreshElement(self, windowInstance, elementDef, currentElement):
		"""
		Recursively refresh an element and its children.

		Args:
			windowInstance: The root window instance
			elementDef: Element definition from UI script
			currentElement: Current UI element instance

		Returns:
			Number of elements refreshed
		"""
		import uiScriptLocale
		import localeInfo

		refreshCount = 0

		# If this element has text defined in the script, refresh it
		if isinstance(elementDef, dict) and "text" in elementDef:
			textDef = elementDef["text"]

			# Check if it's a locale reference (starts with uiScriptLocale or localeInfo)
			if isinstance(textDef, str):
				text = self._ResolveLocaleString(textDef)
				if text and hasattr(currentElement, 'SetText'):
					try:
						currentElement.SetText(text)
						refreshCount += 1
					except:
						pass

		# Recursively process children
		if isinstance(elementDef, dict) and "children" in elementDef:
			children = elementDef.get("children", [])
			for childDef in children:
				if isinstance(childDef, dict) and "name" in childDef:
					childName = childDef["name"]
					try:
						childElement = windowInstance.GetChild(childName)
						refreshCount += self._RefreshElement(windowInstance, childDef, childElement)
					except:
						pass

		return refreshCount

	def _ResolveLocaleString(self, textDef):
		"""
		Resolve a locale string reference to its current value.

		Args:
			textDef: String like "uiScriptLocale.LOGIN_CONNECT" or direct text

		Returns:
			The resolved locale string or None
		"""
		import uiScriptLocale
		import localeInfo

		# Check if it's a locale reference
		if "uiScriptLocale." in str(textDef):
			# Extract the attribute name
			parts = str(textDef).split(".")
			if len(parts) >= 2:
				attrName = parts[-1]
				if hasattr(uiScriptLocale, attrName):
					return getattr(uiScriptLocale, attrName)

		elif "localeInfo." in str(textDef):
			parts = str(textDef).split(".")
			if len(parts) >= 2:
				attrName = parts[-1]
				if hasattr(localeInfo, attrName):
					return getattr(localeInfo, attrName)

		return None


# Global helper instance for easy access
_globalHelper = LocaleRefreshHelper()

def RefreshWindowByScript(window, scriptPath):
	"""
	Convenience function to refresh a window using its UI script.

	Args:
		window: The ui.ScriptWindow instance
		scriptPath: Path to UI script (e.g., "UIScript/LoginWindow.py")
	"""
	return _globalHelper.RefreshWindow(window, scriptPath)

def RefreshByMapping(elementMap):
	"""
	Convenience function to refresh elements by mapping.

	Args:
		elementMap: Dict of {element: "LOCALE_KEY"}
	"""
	return _globalHelper.RefreshElementsByMapping(elementMap)

def RebuildDictionary(template, localeModule="localeInfo"):
	"""
	Convenience function to rebuild a dictionary with fresh locale strings.

	Args:
		template: Dict of {key: "LOCALE_KEY"}
		localeModule: "localeInfo" or "uiScriptLocale"
	"""
	return _globalHelper.RefreshDictionaries(template, localeModule)
