# conky-steam-friends

### Description
Simple script that grabs your steam friends username and status.  While this script could easily be used as a stand alone script, it was written with the intention of being used with Conky.


### Prerequisites
<b>Note:</b> The following instructions are written for Ubuntu systems.  Commands may vary based off of which distribution you are using.

#### 1. Python 3
You can check to see if Python 3 is installed on your system by running the following command:

`which python3`

If Python 3 is installed the above command will return your Python 3 path, such as `/usr/bin/python3`.

If nothing is returned then you will need to install Python 3.  Below are the commands needed to install Python 3.

`sudo apt-get update`

`sudo apt-get install python3`

#### 2. Beautiful Soup 4
Beautiful Soup 4 for Python 3 is needed for the script to run correctly.  Below are the commands needed to install Beautiful Soup 4.

`sudo apt-get update`

`sudo apt-get install python3-bs4`

#### 3. Conky (Optional)
<b>Note:</b> This step is only needed if you intend to use `steamfriends.py` with Conky.

If you don't already have Conky installed, you can install it by running the following commands:

`sudo apt-get update`

`sudo apt-get install conky`

Once you are done installing Conky you can run Conky with the following command:

`conky &`

If you want Conky to startup automatically on boot you can follow the instructions from the link below.

[Guide to Starting Conky on Boot](https://help.ubuntu.com/community/SettingUpConky#Set_Conky_To_Start_At_Boot)

### Script Setup
Download the `steamfriends.py` script and place it in you home directory in a new folder called `scripts`.

Make sure the script has execute permissions with the following command:

`chmod u+x steamfriends.py`

At this point your file/folder structure should look like the following:

`/home/[username]/scripts/steamfriends.py`

Next you will need to find out what your Steam ID is.  To do this, open up you Steam client and go to your profile page.  Right click on the screen and click 'Copy Page URL'.  Paste the URL in a text editor and you should get something like this:

`http://steamcommunity.com/profiles/12345678901234567/home`

Every Steam account has a different Steam ID.  From the example above the Steam ID would be: `12345678901234567`.  Yours will obviously be different.

Now that you have your Steam ID you will need to modify the variable `steamid` in `steamfriends.py`. 

Example:

`steamid = "12345678901234567"`

Save your changes to `steamfriends.py` and the script is now ready.  You can test out the script by running the following command:

`/home/[username]/scripts/steamfriends.py`

This should return a list of all your Steam friends and their current status.
    
### Conky Setup (Optional)
<b>Note:</b> This step is only needed if you intend to use `steamfriends.py` with Conky.

Insert the following line at the bottom of `/etc/conky/conky.conf`:

`Steam Friends`

`$hr`

`${execi 300 ~/scripts/steamfriends.py}`
    
<b>Important Note:</b> Remember to change the path above to reflect your `steamfriends.py` location.  I also recommend not changing the `execi` timer to anything less than `300`. Doing so may poll the Steam servers too frequently resulting in being blocked.

Depending on how large your friends list is you may also have to change/add the following line into the top of your `conky.cong`:

`text_buffer_size 4096`

You can adjust your buffer size as needed.  After making these changes it is recommended that you restart Conky, you can restart Conky with the following commands:

`killall conky`

`conky &`

### Screenshots
![alt tag](http://i.imgur.com/jujbg8x.png)
![alt tag](http://i.imgur.com/7sjASzK.png)
