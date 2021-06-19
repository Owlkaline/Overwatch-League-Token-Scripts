from OwlSettings import settings as owl_settings;
import time
import pyautogui 
import webbrowser
import sys;

url = 'https://accounts.google.com/signin';

my_account = [2513.0, 31.0];
signout_button = [2362.0, 435.0];
use_another_account = [1293.0, 4901.0];
username_box = [1353.0, 503.0]

settings = owl_settings.Settings();

if settings.should_skip_battlenet():
  sys.exit();

info = settings.google_info();
username = info[0];
password = info[1];

settings.log("Logging into google...");
time.sleep(10)

settings.open_system_browser(url);

time.sleep(5)
pyautogui.press('f11');
time.sleep(1)

settings.click(my_account);
settings.click(signout_button);
time.sleep(5)
settings.click(use_another_account);

settings.click(username_box);
pyautogui.press('f11');
time.sleep(5)

pyautogui.write(['Fn'])
pyautogui.typewrite(username)
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.write(['Fn'])
pyautogui.typewrite(password)
pyautogui.typewrite('\n')
settings.log("Google should now be logged in.");
time.sleep(5)
