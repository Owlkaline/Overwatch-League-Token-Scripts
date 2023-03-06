import time
import pyautogui
from os.path import exists
import platform
from enum import Enum;
import os;

from selenium import webdriver
import webbrowser

from pathlib import Path

settings_file = "/owl_settings.ini"

class Browser(Enum):
  Firefox = 0
  Chrome = 1

class Settings:
  def __init__(self):
    self.open_automatically = True;
    self.skip_battlenet = False;
    self.skip_google = False;
    self.screen_width = 1920;
    self.screen_height = 1080;
    self.google_username = '';
    self.google_password = '';
    self.battlenet_username = '';
    self.battlenet_password = '';
    self.home = str(Path.home());
    self.browser = Browser.Firefox;
    
    self.browser_location = '/usr/bin/firefox'
    #self.driver = '/usr/local/bin/geckodriver';
    self.driver = '/usr/bin/geckodriver';
    
    if "Windows" in platform.system():
      self.browser_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    
    if exists(self.home + settings_file):
      with open(self.home + settings_file, 'r') as o:
        lines = o.readlines();
        for line in lines:
          if line[0] == "#" or line[0] == "/":
            continue;
          
          if "OpenAutomatically" in line:
            self.open_automatically = "True" in line.split('OpenAutomatically=')[1].split('\n')[0].split('\r')[0];
          if "SkipGoogleLogin" in line:
            self.skip_google = "True" in line.split('SkipGoogleLogin=')[1].split('\n')[0].split('\r')[0];
          if "SkipBattleNetLogin" in line:
            self.skip_battlenet = "True" in line.split('SkipBattleNetLogin=')[1].split('\n')[0].split('\r')[0];
          if "ScreenXResolution" in line:
            self.screen_width = int(line.split('ScreenXResolution=')[1].split('\n')[0].split('\r')[0]);
          if "ScreenYResolution" in line:
            self.screen_height = int(line.split('ScreenYResolution=')[1].split('\n')[0].split('\r')[0]);
          if "BrowserLocation" in line:
            self.browser_location = str(line.split("BrowserLocation=")[1].split('\n')[0].split('\r')[0]);
          if "DriverLocation" in line:
            self.driver = str(line.split("DriverLocation=")[1].split('\n')[0].split('\r')[0]);
          if "GoogleUsername" in line:
            self.google_username = str(line.split("GoogleUsername=")[1].split('\n')[0].split('\r')[0]);
          if "GooglePassword" in line:
            self.google_password = str(line.split("GooglePassword=")[1].split('\n')[0].split('\r')[0]);
          if "BattlenetUsername" in line:
            self.battlenet_username = str(line.split("BattlenetUsername=")[1].split('\n')[0].split('\r')[0]);
          if "BattlenetPassword" in line:
            self.battlenet_password = str(line.split("BattlenetPassword=")[1].split('\n')[0].split('\r')[0]);
          if "UseChromeInstead" in line:
            if "True" in line.split('UseChromeInstead=')[1].split('\n')[0].split('\r')[0]:
              self.browser = Browser.Chrome
    
    if self.google_username == '' or self.google_password == '':
      self.skip_google = True;
    if self.battlenet_username == '' or self.battlenet_password == '':
      self.skip_battlenet = True;
    
  def log(self, message):
    localtime = time.asctime(time.localtime(time.time()));
    print(localtime + ": " + message);
  
  def resolution(self):
    return [self.screen_width, self.screen_height]
  
  def should_skip_google(self):
    return self.skip_google;
  
  def should_skip_battlenet(self):
    return self.skip_battlenet;
  
  def should_open_automatically(self):
    return self.open_automatically;

  def battlenet_info(self):
    return [self.battlenet_username, self.battlenet_password];
  
  def google_info(self):
    return [self.google_username, self.google_password];
  
  def home_dir(self):
    return self.home
  
  def click(self, pos):
    x = pos[0]/2560.0 * self.screen_width;
    y = pos[1]/1080.0 * self.screen_height;
    pyautogui.moveTo(x, y, duration=0.1);
    time.sleep(0.1)
    pyautogui.click()
  
  def open_system_browser(self, url):
    webbrowser.register('sys_browser', None, webbrowser.BackgroundBrowser(self.browser_location))
    webbrowser.get('sys_browser').open_new(url)
  
  def new_browser_driver(self):
    options = webdriver.FirefoxOptions()
    
    if self.browser == Browser.Chrome:
      options = webdriver.ChromeOptions()
    
    options.add_argument('--headless')
    
    if self.browser == Browser.Chrome:
      return webdriver.Chrome(executable_path=self.driver, service_log_path=os.path.devnull, options=options)
    else:
      return webdriver.Firefox(executable_path=self.driver, service_log_path=os.path.devnull, options=options)
