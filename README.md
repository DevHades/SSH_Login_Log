# SSH_Login_Log
- This was created for personal usage. The script itself hasnt been perfected to work with all OS. I was running Ubuntu 20.04. 
- Please create an issue if you find any bugs id be happy to make improvements. 

# How To Setup

1) Edit the discord webhook url
2) put the script into the start up programs on your machine

# Known Bugs
- Script will panic when being ran as root. This is due to `os.environ.get("SSH_CONNECTION")`. Ive not found a way to fix this thus far. 
