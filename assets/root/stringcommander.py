import _weakref

class CallBackFunction:
	class __noarg_call__:
		def __init__(self, cls, obj, func):
			self.cls=cls
			self.obj=_weakref.proxy(obj)
			self.func=_weakref.proxy(func)

		def __call__(self, *arg):
			return self.func(self.obj)

	class __arg_call__:
		def __init__(self, cls, obj, func):
			self.cls=cls
			self.obj=_weakref.proxy(obj)
			self.func=_weakref.proxy(func)

		def __call__(self, *arg):
			return self.func(self.obj, *arg)

	def __init__(self, mfunc):
		self.argCount=mfunc.im_func.func_code.co_argcount

		if self.argCount>1:
			self.call=CallBackFunction.__arg_call__(mfunc.im_class, mfunc.im_self, mfunc.im_func)
		else:
			self.call=CallBackFunction.__noarg_call__(mfunc.im_class, mfunc.im_self, mfunc.im_func)

	def __call__(self, *arg):
		return self.call(*arg)

	def GetArgumentCount(self):
		return self.argCount

class Analyzer:
	def __init__(self):
		self.cmdDict={}

	def SAFE_RegisterCallBack(self, cmd, callBackFunc):
		self.cmdDict[cmd]=CallBackFunction(callBackFunc)

	def Run(self, line):		
		tokens=line.split()

		if len(tokens)==0:
			return 1

		cmd=tokens.pop(0)

		try:		
			callBackFunc=self.cmdDict[cmd]
		except KeyError:
			return 0

		argCount=callBackFunc.GetArgumentCount()-1

		if len(tokens)<argCount:
			raise RuntimeError, "Analyzer.Run(line=%s) - cmd=%s, curArgCount[%d]<needArgCount[%d]" % (line, cmd, len(tokens), argCount)
			return 0

		tokens=tokens[:argCount]
		callBackFunc(*tokens)
		return 1

