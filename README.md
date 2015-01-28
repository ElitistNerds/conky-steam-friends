# conky-steam-friends

### Description
Simple script that grabs your steam friends username and status.  While this script could easily be used as a stand alone script, it was written with the intention of being used with Conky.

### Prerequisites
1. Python 3
2. Beautiful Soup 4
3. Conky

### Script Setup
Modify variable `steamid` in `steamfriends.py` to reflect your Steam ID.  

Example: `steamid = "12345678901234567"`
    
<b>Important Note:</b> This has to be your Steam ID not your Steam Username.

### Conky Setup
Insert the following line into `/etc/conky/conky.conf`:

    ${execi 300 ~/scripts/steamfriends.py}
    
<b>Important Note:</b> Remember to change the path above to reflect your `steamfriends.py` location.  I also recommend not changing the `execi` timer to anything less than `300`. Doing so may poll the Steam servers too frequently resulting in being blocked.

### Screenshots
![alt tag](screenshot-1.png)
![alt tag](screenshot-2.png)
