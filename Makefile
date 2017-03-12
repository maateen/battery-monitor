SHELL := /bin/bash
OUT_DIR = /usr/share/battery-monitor

all: install
	@:

install: all
	@echo You must be root to install.
	@mkdir -p $(OUT_DIR)
	@cp battery-monitor.py $(OUT_DIR)/battery-monitor.py
	@cp config.py $(OUT_DIR)/config.py
	@cp -r icons $(OUT_DIR)/icons
	@cp sound.wav $(OUT_DIR)/sound.wav
	@cp battery-monitor /usr/bin/battery-monitor
	@chmod +x /usr/bin/battery-monitor
	@cp battery-monitor.desktop ~/.config/autostart/battery-monitor.desktop
	@echo Installation completed!

uninstall:
	@echo You must be root to uninstall.
	@rm -rf $(OUT_DIR)
	@rm -f /usr/bin/battery-monitor
	@rm -f ~/.config/autostart/battery-monitor.desktop
	@echo Uninstallation completed!