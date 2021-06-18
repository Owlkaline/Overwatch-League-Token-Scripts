#!/usr/bin/python3
from OwlSettings import settings as owl_settings;

import os;
import time
from os.path import exists

import selenium
from selenium import webdriver

import pyautogui 
import webbrowser

import runpy

urls = [['OWL', 'https://www.youtube.com/channel/UCiAInBL9kUzz1XRxk66v-gw/live'],
        ['Contenders', 'https://www.youtube.com/channel/UCWPW0pjx6gncOEnTW8kYzrg/live']]

def report_not_live(settings, url):
  settings.log(url + " is not live.");
  if exists(settings.home_dir() + "/" + url_live):
    os.remove(settings.home_dir() + "/" + url_live)

settings = owl_settings.Settings();

settings.log("Checking if ow channels are live.");
for url in urls:
  url_live = url[0] + 'Live';
  
  firefox_options = webdriver.FirefoxOptions()
  firefox_options.add_argument('--headless')
  driver = webdriver.Firefox(executable_path=settings.geckodriver_location(), service_log_path=os.path.devnull, options=firefox_options)
  driver.get(url[1])
  time.sleep(20)

  live = True;
  rewards_enabled = False;
  waiting_for_stream = False;
  
  contenders_vid_started = False;
  
  try:
    rewards = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[2]/ytd-account-link-button-renderer/div/ytd-button-renderer/a');
    stream_waiting = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/ytd-video-view-count-renderer/span[1]').text;
    rewards_enabled = rewards.text == "REWARDS";
    
    waiting_for_stream = 'waiting' in stream_waiting;
    
  except selenium.common.exceptions.NoSuchElementException:
    live = False;
  
  if url[0] == "Contenders":
    driver.get("https://overwatchleague.com/en-us/contenders");
    time.sleep(20);
    try:
     contenders_rewards = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/div[1]/div[3]/div/div/div/p").text;
     print(contenders_rewards)
     contenders_vid_started = "CONTENDERS VIEWERSHIP REWARDS" in contenders_rewards;
    except:
      contenders_vid_started = False;
  
  driver.quit();

  if live and not waiting_for_stream: #and rewards_enabled and not waiting_for_stream:
    if url[0] == "Contenders" and not contenders_vid_started:
      report_not_live(settings, url[0]);
      continue;
    
    if url[0] == "OWL" and not rewards:
      report_not_live(settings, url[0]);
      continue;
    
    settings.log(url[0] + " is live!");
    if exists(settings.home_dir() + "/" + url_live):
      continue;
    
    with open(settings.home_dir() + "/" + url_live, "w") as o:
      o.write("\n");
    
    if not settings.should_open_automatically():
      settings.log("Automatic mode is off, checking with user.");
      title = 'Gain Overwatch Tokens';
      text = 'Overwatch League is Live!';
      if url_live == 'ContendersLive':
        title = 'Gain Contender skins';
        text = 'Overwatch Contenders is Live!';
      result = pyautogui.confirm(text=text, title=title, buttons=['Watch', 'Not now']);
      print(result)
      if result == 'Not now':
        settings.log("User declined.");
        continue;
      settings.log("User accepted.");
    
    if url[0] == 'OWL':
      runpy.run_path(path_name=settings.home_dir() + "/.owl/open_owl.py");
    else:
      runpy.run_path(path_name=settings.home_dir() + "/.owl/open_contenders.py");
  else:
    report_not_live(settings, url[0]);
