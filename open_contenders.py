from OwlSettings import settings as owl_settings;

import webbrowser
import time
import runpy
import pyautogui

url = 'https://overwatchleague.com/en-us/contenders';

video_location = [836, 1036];

settings = owl_settings.Settings();

home = settings.home_dir();

if not settings.should_skip_google():
  runpy.run_path(path_name=home + '/.owl/login_google.py');

if not settings.should_skip_battlenet():
  runpy.run_path(path_name=home + '/.owl/login_battlenet.py');

settings.log("Opening Contenders.");
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(settings.firefox_location()))
webbrowser.get('firefox').open_new(url)
time.sleep(10);
pyautogui.press('f11');
time.sleep(5);
settings.click(video_location);
pyautogui.press('f11');
#pyautogui.press('space');

