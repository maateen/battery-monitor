# Battery Monitor
Battery Monitor is a utility tool developed on Python3 and PyGtk3. It will notify user about charging, discharging, not charging and critically low battery state of the battery on Linux (Surely if battery is present). 
##Dependencies
* python3
* python3-gi
* libnotify-dev
* acpi

To use **Battery Monitor** you need these dependencies installed on your PC.
##Installation
###Ubuntu/Debian

Let's install from PPA:

```
sudo add-apt-repository ppa:maateen/battery-monitor -y
```
```
sudo apt-get update
```
```
sudo apt-get install battery-monitor -y
```
That's all. **Battery Monitor** is installed on your system. 
##Configuration
Every time, you will start/restart your PC, it will run automatically in background. But as it's your first time, let's start it by yourself. `battery-monitor` is the relevant command, you can use on Terminal to start the **Battery Monitor**. Surely, I have a different idea. Just press **alt+f2**, `battery-monitor` command in the box and press `enter`. That's all.
##Issue Tracking
If you find a bug, please open a new issue with details: [https://github.com/maateen/battery-monitor/issues](https://github.com/maateen/battery-monitor/issues)
##Screenshots
####Initial State
![Initial State](https://s20.postimg.org/6xltz5ox9/Screenshot_from_2016_07_22_20_42_29.png)
####Charging State
![Charging State](https://s20.postimg.org/qpnzyg0h9/Screenshot_from_2016_07_22_20_42_52.png)
####Discharging State
![Discharging State](https://s20.postimg.org/afxtvjpt9/Screenshot_from_2016_07_22_20_42_42.png)
####Not Charging State
![Not Charging State](https://s20.postimg.org/aihpidtgt/Screenshot_from_2016_07_22_21_11_49.png)
####Critically Low Battery State
![Critically Low Battery State](https://s20.postimg.org/ncfrbq6wd/Screenshot_from_2016_07_23_03_09_54.png)
