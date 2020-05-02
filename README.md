
# Battery Monitor [Deprecated]

Battery Monitor is a utility tool developed on Python3 and PyGtk3. It will notify the user about charging, discharging, not charging and critically low battery state of the battery on Linux (surely if the battery is present).

 - [Dependencies](#dependencies)
 - [Installation](#installation)
     - [Common Method](#common-method)
     - [For Ubuntu and its derivatives](#for-ubuntu-and-its-derivatives)
     - [For Arch Linux and its derivatives](#for-arch-linux-and-its-derivatives)
     - [For Beta Testers](#for-beta-testers)
     - [For Developers](#for-developers)
 - [User Manual](#user-manual)
     - [Auto Start](#auto-start)
     - [Settings](#settings)
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

* acpi
* python3
* python3-gi
* python3-setuptools
* libnotify4
* libappindicator3-1
* gir1.2-appindicator3-0.1

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
That's all. **Battery Monitor (Stable)** is installed on your system.

### For Ubuntu and its derivatives

Let's install from PPA (currently supported: **14.04**, **17.10** & **18.04**; we're struggling with Ubuntu 16.04 right now):

```
sudo add-apt-repository ppa:maateen/battery-monitor -y
```
```
sudo apt-get update
```
```
sudo apt-get install battery-monitor -y
```
That's all. **Battery Monitor (Stable)** is installed on your system.

### For Arch Linux and its derivatives

The stable version, git version and the beta version are available in the [Arch User Repository](https://aur.archlinux.org/):

Stable: [`battery-monitor`](https://aur.archlinux.org/packages/battery-monitor)
Git: [`battery-monitor-git`](https://aur.archlinux.org/packages/battery-monitor-git)
Beta: [`battery-monitor-devel-git`](https://aur.archlinux.org/packages/battery-monitor-devel-git)

If you're not sure how to use the AUR, please see the [Manjaro](https://wiki.manjaro.org/index.php/Arch_User_Repository) and [Arch](https://wiki.archlinux.org/index.php/Arch_User_Repository#What_is_the_AUR.3F) wiki entries about it. You will need an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers) to install packages.

### For Beta Testers

```
wget https://github.com/maateen/battery-monitor/archive/devel.zip
```
```
unzip devel.zip
```
```
cd battery-monitor-devel
```
```
sudo make install
```
That's all. **Battery Monitor (Beta)** is installed on your system.

### For Developers
Now you can automatically test **Battery Monitor** from Terminal:

```
python3 run.py --test
```
Or, if you've already installed:

```
battery-monitor --test
```

## User Manual

### Auto Start
Every time Battery Monitor starts automatically after PC boots up. It pops up notifications and you see its **Icon** in the system tray. To reveal the other beauties, you can click on the icon. Currently, there are three menus: Settings, About and Quit.

You can also start battery monitor from the menu entries. Please, search for Battery Monitor launcher in the menu entries and simply click on it. In case, if Battery Monitor doesn't start automatically, please open an issue. We would like to debug the issue and help you.

### Settings
In Settings menu, you can configure and adjust settings for Battery Monitor.

#### Configuration
Here, you can set the battery percentage levels at which you want to get notifications. The warning levels are listed in ascending order. **Critical Battery Warning** refers to the lowest level while **First Custom Warning** refers to the highest level. Custom warning levels are optional.

If you change any configuration, it will be in action only after next reboot.

![Battery Monitor GUI](https://github.com/maateen/battery-monitor/raw/gh-pages/battery-monitor-gui.png)

## Issue Tracking

If you find a bug, please open a new issue with details: [https://github.com/maateen/battery-monitor/issues](https://github.com/maateen/battery-monitor/issues)

## Screenshots

#### Initial State

![Initial State](https://github.com/maateen/battery-monitor/raw/gh-pages/Screenshot_from_2016_07_22_20_42_29.png)

#### Charging State

![Charging State](https://github.com/maateen/battery-monitor/raw/gh-pages/Screenshot_from_2016_07_22_20_42_52.png)

#### Discharging State

![Discharging State](https://github.com/maateen/battery-monitor/raw/gh-pages/Screenshot_from_2016_07_22_20_42_42.png)

#### Not Charging State

![Not Charging State](https://github.com/maateen/battery-monitor/raw/gh-pages/Screenshot_from_2016_07_22_21_11_49.png)

#### Critically Low Battery State

![Critically Low Battery State](https://github.com/maateen/battery-monitor/raw/gh-pages/Screenshot_from_2016_07_23_03_09_54.png)

## Roadmap

Please take a look at our [milestones](https://github.com/maateen/battery-monitor/milestones) to get a clear idea about our roadmap. They are dynamic and they can change frequently on user requests.

## Changelog

### v0.6

- [x] Restructured and reformatted the whole project.
- [x] Added system tray icon ([Issue #46](https://github.com/maateen/battery-monitor/issues/46))
- [x] Fixed [issue #51](https://github.com/maateen/battery-monitor/issues/51)
- [x] Added some new icons ([Issue #53](https://github.com/maateen/battery-monitor/issues/53))
- [x] Added Ubuntu 18.04 LTS support ([Issue #55](https://github.com/maateen/battery-monitor/issues/55))
- [x] Fixed [issue #61](https://github.com/maateen/battery-monitor/issues/61)

### v0.5.4

- [x] Fixed [issue #48](https://github.com/maateen/battery-monitor/issues/48)

### v0.5.3

- [x] Fixed [issue #45](https://github.com/maateen/battery-monitor/issues/45)
- [x] Support for Ubuntu 17.10 has been added.

### v0.5.2

- [x] Fixed [issue #41](https://github.com/maateen/battery-monitor/issues/41)
- [x] Fixed [issue #42](https://github.com/maateen/battery-monitor/issues/42)
- [x] Introduced a Test feature for developers.

### v0.5.1

- [x] Fixed [issue #35](https://github.com/maateen/battery-monitor/issues/35)
- [x] Fixed [issue #39](https://github.com/maateen/battery-monitor/issues/39)

### v0.5

- [x] Developed a GUI to manage the custom warning easily.
- [x] Minimized CPU consumption.
- [x] Added Makefile for easy installation and up-gradation.
- [x] Re-structured the project.
-  [x] Support for Ubuntu 14.04, 16.04, 16.10 and 17.04 has been added.

### v0.4

- [x] Reformatted the code in a new style.
- [x] Optimized the code in a way so that Battery Monitor consumes a little resource of your PC.

### v0.3

- [x] Fixed [issue #7](https://github.com/maateen/battery-monitor/issues/7), decreased CPU consuming from 40% to below 0.7%
- [x] Fixed [issue #4](https://github.com/maateen/battery-monitor/issues/4), Added warning at 30% battery life (temporary solution, will be replaced by a GUI in near future).
- [x] Fixed [issue #6](https://github.com/maateen/battery-monitor/issues/6), Added an entry in dash.

### v0.2.1

- [x] Added trusty support.

### v0.2

- [x] Added **Critically Low Battery** warning when the battery is below 10%.
- [x] Added `ctrl+C` pressing support to stop the `battery-monitor` command on terminal.

### v0.1

- [x] Initial release.

## Contributors

### [Safwan Rahman](https://github.com/safwanrahman)

He has reformatted the code in a new style. The style represents the code easier to understand. Also, he has optimized the code in a way that **Battery Monitor** consumes a little resource of your PC. Please take a minute to thank him.

### [Abdelhak Bougouffa](https://abougouffa.github.io/)

He has fixed some bugs and optimized **Battery Monitor** in a way so that it consumes lower CPU and RAM than before. Please take a minute to thank him.

### [Yochanan Marqos](https://github.com/yochananmarqos)

He is our official package maintainer in AUR. He has put Arch users' life at ease. Please take a minute to thank him.

### [Benjamin Staffin](https://github.com/benley)

He has improved the build process and added modern Python setuptools packaging. Please take a minute to thank him.
