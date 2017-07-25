SHELL := /bin/bash
OUT_DIR = /usr/share/battery-monitor

all: install
	@:

install:
	@echo You must be root to install.
	@mkdir -p $(OUT_DIR)
	@cp battery-monitor.py $(OUT_DIR)/battery-monitor.py
	@cp battery-monitor-gui.py $(OUT_DIR)/battery-monitor-gui.py
	@cp config.py $(OUT_DIR)/config.py
	@cp -r icons $(OUT_DIR)/icons
	@cp battery-monitor /usr/bin/battery-monitor
	@chmod +x /usr/bin/battery-monitor
	@cp battery-monitor-autostart.desktop /etc/xdg/autostart/battery-monitor-autostart.desktop
	@cp battery-monitor.desktop /usr/share/applications/battery-monitor.desktop
	@cp battery-monitor-gui.desktop /usr/share/applications/battery-monitor-gui.desktop
	@rm -f ~/.config/autostart/battery-monitor.desktop
	@echo Installation completed!

uninstall:
	@echo You must be root to uninstall.
	@rm -rf $(OUT_DIR)
	@rm -f /usr/bin/battery-monitor
	@rm -f ~/.config/autostart/battery-monitor.desktop
	@rm -f /etc/xdg/autostart/battery-monitor-autostart.desktop
	@rm -f /usr/share/applications/battery-monitor.desktop
	@rm -f /usr/share/applications/battery-monitor-gui.desktop
	@echo Uninstallation completed!
