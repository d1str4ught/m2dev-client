import dbg
import app
import localeInfo
import wndMgr
import systemSetting
import mouseModule
import networkModule
import uiCandidate
import constInfo
import musicInfo
import stringCommander



#bind_me(locals().values())

def RunApp():
	musicInfo.LoadLastPlayFieldMusic()
	
	app.SetHairColorEnable(constInfo.HAIR_COLOR_ENABLE)
	app.SetArmorSpecularEnable(constInfo.ARMOR_SPECULAR_ENABLE)
	app.SetWeaponSpecularEnable(constInfo.WEAPON_SPECULAR_ENABLE)

	app.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())

	try:
		app.Create(localeInfo.APP_TITLE, systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	except RuntimeError, msg:
		msg = str(msg)
		if "CREATE_DEVICE" == msg:
			dbg.LogBox("Sorry, Your system does not support 3D graphics,\r\nplease check your hardware and system configeration\r\nthen try again.")
		else:
			dbg.LogBox("Metin2.%s" % msg)
		return

	app.SetCamera(1500.0, 30.0, 0.0, 180.0)

	#Gets and sets the floating-point control word
	#app.SetControlFP()

	if not mouseModule.mouseController.Create():
		return

	mainStream = networkModule.MainStream()
	mainStream.Create()	
	
	#mainStream.SetLoadingPhase()
	mainStream.SetLogoPhase()

	#mainStream.SetLoginPhase()
	#mainStream.SetSelectCharacterPhase()
	#mainStream.SetCreateCharacterPhase()
	#mainStream.SetSelectEmpirePhase()
	#mainStream.SetGamePhase()
	app.Loop()

	mainStream.Destroy()

RunApp()

