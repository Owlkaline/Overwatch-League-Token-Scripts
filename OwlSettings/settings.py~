import time
import pyautogui
from os.path import exists
import platform

from pathlib import Path

settings_file = "/owl_settings.ini"

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
    
    self.firefox = '/usr/bin/firefox'
    self.geckodriver = '/usr/local/bin/geckodriver';
    
    if "Windows" in platform.system():
      self.firefox= "C:/Program Files/Mozilla Firefox/firefox.exe"
    
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
          if "FirefoxLocation" in line:
            self.firefox = str(line.split("FirefoxLocation=")[1].split('\n')[0].split('\r')[0]);
          if "GeckoDriverLocation" in line:
            self.geckodriver = str(line.split("GeckoDriverLocation=")[1].split('\n')[0].split('\r')[0]);
          if "GoogleUsername" in line:
            self.google_username = str(line.split("GoogleUsername=")[1].split('\n')[0].split('\r')[0]);
          if "GooglePassword" in line:
            self.google_password = str(line.split("GooglePassword=")[1].split('\n')[0].split('\r')[0]);
          if "BattlenetUsername" in line:
            self.battlenet_username = str(line.split("BattlenetUsername=")[1].split('\n')[0].split('\r')[0]);
          if "BattlenetPassword" in line:
            self.battlenet_password = str(line.split("BattlenetPassword=")[1].split('\n')[0].split('\r')[0]);
    
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
  
  def firefox_location(self):
    return self.firefox
  
  def geckodriver_location(self):
    return self.geckodriver
  
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
