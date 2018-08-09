# -*- coding:utf-8 -*-
from appium import webdriver
import re
import os
base_path=os.path.abspath("..")
driver_caps={}
driver_caps["platformName"]="Android"
driver_caps["platformVersion"]="8.1.0"
driver_caps["deviceName"]="PACM00"
driver_caps["appWaitActivity"]=""
driver_caps["app"]=base_path+r"/app/app-debug.apk"
driver=webdriver.Remote("http://localhost:4723/wd/hub",driver_caps)