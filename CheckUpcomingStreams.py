#!/usr/bin/python3
from OwlSettings import settings as owl_settings;

import selenium
from selenium import webdriver
import time
import os;

urls = [['OWL', 'https://www.youtube.com/channel/UCiAInBL9kUzz1XRxk66v-gw'],
        ['Contenders', 'https://www.youtube.com/channel/UCWPW0pjx6gncOEnTW8kYzrg']]

from array import *

settings = owl_settings.Settings();

settings.log("Checking for upcoming streams...");

schedules = [[]];

i = 0;

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=settings.geckodriver_location(), service_log_path=os.path.devnull, options=firefox_options)

for url in urls:
  driver.get(url[1])
  time.sleep(10)
  
  future_stream1 = True;
  date1 = "";
  future_stream2 = True;
  date2 = "";
  
  schedules.append([]);
  
  for j in range(4):
    for k in range(13):
      date = ""
       
      try:
        date = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[' + str(j) + ']/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-grid-video-renderer[' + str(k)  + ']/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[2]').text;
      except selenium.common.exceptions.NoSuchElementException:
        a = 1
      
      if "Scheduled" in date:
        if date not in schedules[i]:
          settings.log("Upcoming stream " + date);
          schedules[i].append(date);
      
      try:
        date = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[' + str(j) + ']/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-grid-video-renderer[' + str(k)  + ']/div[1]/div[1]/div[1]/div/div[1]/div[2]/span').text
      except selenium.common.exceptions.NoSuchElementException:
        a = 1
      
      if "Scheduled" in date:
        if date not in schedules[i]:
          settings.log("Upcoming stream " + date);
          schedules[i].append(date);
  
  for j in range(4):
    date2 = "";
    try: 
      date2 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[' + str(j) + ']/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]').text;
    except selenium.common.exceptions.NoSuchElementException:
      a = 1;
    
    if "Scheduled" in date:
      if date not in schedules[i]:
        settings.log("Upcoming stream " + date);
        schedules[i].append(date);
    
    try: 
      date2 = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[' + str(j) + ']/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span').text;
    except selenium.common.exceptions.NoSuchElementException:
      a = 1;
    
    if "Scheduled" in date2:
      if date2 not in schedules[i]:
        settings.log("Upcoming stream " + date2);
        schedules[i].append(date2);
  
  i += 1;
  
driver.quit();

i = 0;

for url in urls:
  with open(settings.home_dir() + "/" + url[0], "w") as o:
    for time_date in schedules[i]:
      o.write(time_date);
      o.write('\n');
  i += 1;

