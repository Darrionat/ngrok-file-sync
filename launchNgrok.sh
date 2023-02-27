#!/bin/bash
# Create new tmux session with ngrok running in the background
/usr/bin/tmux new -d -s ngrok "ngrok tcp 22"

# Change the following line to whatever directory the ngrokInfo.py
# file is in.
cd ~/code/scripts
sleep 10
/usr/bin/python3 ngrokInfo.py >&ngrokBoot.log
