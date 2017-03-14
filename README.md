# Battery Monitor

Battery Monitor is a utility tool developed on Python3 and PyGtk3. It will notify user about charging, discharging, not charging and critically low battery state of the battery on Linux (Surely if battery is present).

 - [Dependencies](#dependencies)
 - [Installation](#installation)
	 - [Common Method](#common-method)
	 - [Ubuntu/Debian](#ubuntudebian)
 - [Configuration](#configuration)
 - [Issue Tracking](#issue-tracking)
 - [Screenshots](#screenshots)
	 - [Initial State](#initial-state)
	 - [Charging State](#charging-state)
	 - [Discharging State](#discharging-state)
	 - [Not Charging State](#not-charging-state)
	 - [Critically Low Battery State](#critically-low-battery-state)
 - [Roadmap](#roadmap)
 - [Changelog](#changelog)
 - [Contributors](#contributors)

## Dependencies

* python3
* python3-gi
* libnotify-dev
* acpi

To use **Battery Monitor** you need these dependencies installed on your PC.

## Installation

### Common Method

```
wget https://github.com/maateen/battery-monitor/archive/master.zip
```
```
unzip master.zip
```
```
cd battery-monitor-master
```
```
sudo make install
```

### Ubuntu/Debian

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

## Configuration

Every time, you will start/restart your PC, it will run automatically in background. But as it's your first time, let's start it by yourself. Please, search for **Battery Monitor** launcher in your menu entries. Then simply click on it. You will get notified that **Battery Monitor** has started. If you want to adjusr settings for **Battery Monitor**, then simply search for **Battery Monitor GUI** in your menu entries. Then click on it and you will see a new window. Now adjust your settings and save it. Your adjustment will be in action after next reboot.

## Issue Tracking

If you find a bug, please open a new issue with details: [https://github.com/maateen/battery-monitor/issues](https://github.com/maateen/battery-monitor/issues)

## Screenshots

#### Initial State

![Initial State](https://raw.githubusercontent.com/maateen/battery-monitor/master/docs/Screenshot_from_2016_07_22_20_42_29.png)

#### Charging State

![Charging State](https://raw.githubusercontent.com/maateen/battery-monitor/master/docs/Screenshot_from_2016_07_22_20_42_52.png)

#### Discharging State

![Discharging State](https://raw.githubusercontent.com/maateen/battery-monitor/master/docs/Screenshot_from_2016_07_22_20_42_42.png)

#### Not Charging State

![Not Charging State](https://raw.githubusercontent.com/maateen/battery-monitor/master/docs/Screenshot_from_2016_07_22_21_11_49.png)

#### Critically Low Battery State

![Critically Low Battery State](https://raw.githubusercontent.com/maateen/battery-monitor/master/docs/Screenshot_from_2016_07_23_03_09_54.png)

## Changelog

### v0.5

- [x] Developing a GUI to manage the custom warning easily.
- [x] Minimizing CPU consumption.
- [x] Adding Makefile for easy installation and upgradation
- [x] Re-structuring the project

### v0.4

- Reformatting the code in a new style.
- Optimizing the code in a way so that Battery Monitor consumes a little resource of your PC.

### v0.3

- Fixing [issue #7](https://github.com/maateen/battery-monitor/issues/7), decreasing CPU consuming from 40% to below 0.7%
- Fixing [issue #4](https://github.com/maateen/battery-monitor/issues/4), Adding warning at 30% battery life (temporary solution, will be replaced by a GUI in near future)
- Fixing [issue #6](https://github.com/maateen/battery-monitor/issues/6), Adding an entry in dash.

### v0.2.1

- Adding trusty support.

### v0.2

- Adding **Critically Low Battery** warning when battery is below 10%.
- Adding `ctrl+C` pressing support to stop the `battery-monitor` command on terminal.

### v0.1

- Initial release.

## Contributors

### [Safwan Rahman](https://github.com/safwanrahman)

One of the biggest contributor of **Battery Monitor**. He has reformated the code in a new style. The style represents the code easier to understand. Also he has optimized the code in a way that **Battery Monitor** consumes a little resource of your PC. Please take a minute to thank him.

### [Abdelhak Bougouffa](https://abougouffa.github.io/)

Another biggest contributor of **Battery Monitor**. He has fixed some bugs and optimized **Battery Monitor** in a way so that it consumes lower CPU and RAM than before. Please take a minute to thank him.