# -*- coding：utf-8 -*-
from appium import webdriver
import json
import re
desired_caps={}
jsondata='''
{
  "platformName": "Android",
  "appPackage": "com.mobike.mobikeapp",
  "appActivity": ".SplashActivity",
  "automationName": "uiautomator2",
  "deviceName": "PACM00",
  "platformVersion": "8.1.0"
}'''
desired_caps=json.loads(jsondata)

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
