SHELL := /bin/bash
OUT_DIR = /usr/share/battery-monitor

all: install
	@:

install:
	@echo You must be root to install.
	@mkdir -p $(OUT_DIR)
	@cp -r src/icons $(OUT_DIR)/icons
	@cp src/__init__.py $(OUT_DIR)/__init__.py
	@cp src/BatteryMonitor.py $(OUT_DIR)/BatteryMonitor.py
	@cp src/config.py $(OUT_DIR)/config.py
	@cp src/gui.py $(OUT_DIR)/gui.py
	@cp src/MainWindow.py $(OUT_DIR)/MainWindow.py
	@cp src/Notification.py $(OUT_DIR)/Notification.py
	@cp src/run.py $(OUT_DIR)/run.py
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
	@rm -f /usr/share/applications/battery-monitor.desktop
	@rm -f /usr/share/applications/battery-monitor-gui.desktop
	@echo Uninstallation completed!
