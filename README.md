# Overwatch-League-Token-Scripts
A set of scripts that check if OWL or OW Contenders is live and automatically logs in and starts the stream to collect viewer ship Overwatch League Tokens and skins.
## Setup
1. Create a folder in your home directory called .owl
2. Copy all python files (*.py) and the OWLSettings folder in the root of this repository to the newly created .owl folder.
3. Move the owl_settings.ini file to your home directory from the OwlSettings file.
4. Customise the settings, see Configure Settings. (Highly Recommended)
4. Setup CheckChannelLive.py to run every ~30min
## Configure Settings
## Automation with Linux
### Using Crontab
1. Open crontab
```
crontab -e
```
2. Setup crontab similar to the following, which checks if ow channel is live every 30min and Upcoming streams evey 6hours.
```
DISPLAY=:1
*/30 * * * * /usr/bin/python ~/.owl/CheckChannelLive.py >> ~/.owl/ow_channel_live.log'
0 */6 * * * /usr/bin/python ~/.owl/CheckUpcomingStreams.py >> ~/.owl/ow_check_upcoming.log'
```
## Automation with Windows


