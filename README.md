quick-shutdown
==============

a script that checks your uptime and prompts you to shut down if it is on for more than 15 hours

Just add this script to /etc/cron.d
Edit the /etc/crontab file
* * */3 * * * root /etc/cron.d/popup.py

Requires python-easygui pasckage
aptitude install python-easygui
