# mogrt
mogrt.py is a script for conforming After Effects mogrts into a zip bundle for stock submissions with proper folder structure.

# Usage
`mogrt.py [-h] src_dir`

Or you can use the following if you've modified your environment as I mention below:
`mogrt [-h] src_dir`

# Help
It's just one argument (the source directory of your After Effects project) but if you forget, there's a -h option to remind you. You'll have to modify the path you use to your batch delivery folder and temp folder. Note: the temp folder will be removed upon completion. If you require a different folder structure, just modify this script.

While you can add this file to your path, I've chosen to add it as a function in my .zshenv file on macOS. You can do that with the following command:
`sudo nano .zshenv`

After that add the following code with the proper file path to wherever you put it:
```
function mogrt() {
 python3 /Volumes/Dropbox/Dropbox/Apps/Python/mogrt.py "$@"
}
```

Hit `Ctrl+X`, then `Y` to save and exit your terminal. Open a new terminal window and you're all set to just use `mogrt` from anywhere.
