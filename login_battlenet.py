from OwlSettings import settings as owl_settings;
import time
import pyautogui 
import webbrowser
import sys;

url = 'https://www.blizzard.com/en-us/';

my_account = [1979, 28];
logout_button = [1860, 250];
login_button = [1939, 89];
username_box = [1228, 251];
password_box = [1228, 307];

settings = owl_settings.Settings();

if settings.should_skip_battlenet():
  sys.exit();

info = settings.battlenet_info();
username = info[0];
password = info[1];

settings.log("Logging into battle.net...");
time.sleep(10)

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(settings.firefox_location()))
webbrowser.get('firefox').open_new(url)

time.sleep(5)
pyautogui.press('f11');
time.sleep(1)
settings.click(my_account)
settings.click(logout_button)
time.sleep(5)

settings.click(my_account)
settings.click(login_button)
time.sleep(5)

settings.click(username_box)
pyautogui.hotkey('ctrl', 'a');
time.sleep(1)
pyautogui.press('backspace');

pyautogui.typewrite(username)

settings.click(password_box)

pyautogui.typewrite(password)
pyautogui.typewrite('\n')
pyautogui.press('f11');
settings.log("Battle.net should now be logged in.");
time.sleep(10)
