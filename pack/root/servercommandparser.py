import net
import background
import stringCommander
import constInfo

class ServerCommandParser(object):

	def __init__(self):
		net.SetServerCommandParserWindow(self)
		self.__ServerCommand_Build()

	def __ServerCommand_Build(self):
		serverCommandList={
			"DayMode"				: self.__DayMode_Update, 
			"xmas_snow"				: self.__XMasSnow_Enable,
			"xmas_boom"				: self.__XMasBoom_Enable,
			"xmas_tree"				: self.__XMasTree_Enable,
			"newyear_boom"			: self.__XMasBoom_Enable,
			"item_mall"				: self.__ItemMall_Open,
			
		}

		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)

	def BINARY_ServerCommand_Run(self, line):
		try:
			print " BINARY_ServerCommand_Reserve", line
			return self.serverCommander.Run(line)
		except RuntimeError, msg:
			import dbg
			dbg.TraceError(msg)
			return 0

	def __PreserveCommand(self, line):
		net.PreserveServerCommand(line)	

	def __DayMode_Update(self, mode):
		self.__PreserveCommand("PRESERVE_DayMode " + mode)

	def __ItemMall_Open(self):
		self.__PreserveCommand("item_mall")

	## юс╫ц
	def __XMasBoom_Enable(self, mode):
		if "1"==mode:
			self.__PreserveCommand("PRESERVE_DayMode dark")
		else:
			self.__PreserveCommand("PRESERVE_DayMode light")
	def __XMasSnow_Enable(self, mode):
		self.__PreserveCommand("xmas_snow " + mode)
	def __XMasTree_Enable(self, grade):
		self.__PreserveCommand("xmas_tree " + grade)

parserWnd = ServerCommandParser()
