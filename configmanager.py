# -*- coding: utf-8 -*-
#-------------------------------------------------
#-- ConfigManager()
#--
#-- microelly 2015
#--
#-- GNU Lesser General Public License (LGPL)
#-------------------------------------------------
DEBUG = True
if DEBUG:
    import ptvsd
    print("Waiting for debugger attach")
    # 5678 is the default attach port in the VS Code debug configurations
    #ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.enable_attach(address=('localhost', 5678))
    ptvsd.wait_for_attach()

import FreeCAD
import platform
import unicodedata

class ConfigManager():

	def __init__(self,name):
		self.name="Plugins/"+name

	def get(self,param,default,defaultWindows=None,defaultMac=None):
		os=platform.system()
		# expected values
		#os='Linux'
		#os='Windows'
		#os='Darwin'
		
		if not defaultWindows:
			defaultWindows=default
		if not defaultMac:
			defaultMac=default
		if os =='Windows' :
			default= defaultWindows
		if os =='Darwin' :
			default= defaultMac
#		if default.__class__ == unicode:
		if default.__class__ == str:
			default=str(default)
		if default.__class__ == int:
			v=FreeCAD.ParamGet('User parameter:'+self.name).GetInt(param)
			if not v:
				FreeCAD.ParamGet('User parameter:'+self.name).SetInt(param,default)
		if default.__class__ == float:
			v=FreeCAD.ParamGet('User parameter:'+self.name).GetFloat(param)
			if not v:
				FreeCAD.ParamGet('User parameter:'+self.name).SetFloat(param,default)
		if default.__class__ == str:
			v=FreeCAD.ParamGet('User parameter:'+self.name).GetString(param)
			if not v:
				FreeCAD.ParamGet('User parameter:'+self.name).SetString(param,default)
		if default.__class__ == bool:
			v=FreeCAD.ParamGet('User parameter:'+self.name).GetBool(param)
			if not v:
				FreeCAD.ParamGet('User parameter:'+self.name).SetBool(param,default)
		if not v:
			v=default
		return v
