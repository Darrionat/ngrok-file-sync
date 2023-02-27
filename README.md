# ngrok-file-sync
This small bit of code will boot ngrok, grab the hostname, and then save a file containing the hostname to a desired destination. This is useful if you want to save the hostname to Dropbox or something.

## Why would I use this?
If you want to SSH into your machine, but you aren't able to / don't want to mess with network settings or open ports on your router, then ngrok is a good solution.
ngrok creates a secure tunnel to your machine from the ngrok servers.

# Installation Guide
Download the files in this respository and put them in whatever folder you want.

Install tmux with:
```
sudo apt-get install tmux
```



Open `launchNgrok.sh` and change the line `cd ~/code/scripts` to change directory to where ngrokInfo.py is. Save the file.

Open `ngrokInfo.py` and change the variable for `PATH` to have whatever directory you want to save the ngrok hostname file to. Then save the file.
Note that if you want to save inside your home directory, Python does not recognize `~`, so you must use `/home` instead. 

Since ngrok changes the hostname everytime you create a new tunnel, you probably want this to run on startup.
You can do this by typing `crontab -e`, and add 
```
@reboot [path to launchNgrok.sh]
```
to the file. Make sure to not include the brackets in the actual file.

Then reboot your machine and ngrok should automatically be running in a tmux session, and the hostname for your ngrok session should be saved wherever you defined it to save in the `ngrokInfo.py` file. 