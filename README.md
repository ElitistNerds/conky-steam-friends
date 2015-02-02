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
Modify variable `steamid` in `steamfriends.py` to reflect your Steam ID.  

Example: `steamid = "12345678901234567"`
    
<b>Important Note:</b> This has to be your Steam ID not your Steam Username.

### Conky Setup
Insert the following line into `/etc/conky/conky.conf`:

    ${execi 300 ~/scripts/steamfriends.py}
    
<b>Important Note:</b> Remember to change the path above to reflect your `steamfriends.py` location.  I also recommend not changing the `execi` timer to anything less than `300`. Doing so may poll the Steam servers too frequently resulting in being blocked.

### Screenshots
![alt tag](http://i.imgur.com/jujbg8x.png)
![alt tag](http://i.imgur.com/7sjASzK.png)
