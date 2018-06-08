SHELL := /bin/bash
PREFIX ?= /usr/share

all: install
	@:

install:
	@echo You must be root to install.
	install -d $(DESTDIR)$(PREFIX)/battery-monitor
	cp -a src/. $(DESTDIR)$(PREFIX)/battery-monitor
	install -Dm755 battery-monitor /usr/local/bin/battery-monitor
	install -Dm755 battery-monitor-autostart.desktop /etc/xdg/autostart/battery-monitor-autostart.desktop
	install -Dm755 battery-monitor.desktop /usr/share/applications/battery-monitor.desktop
	@echo Installation completed!

uninstall:
	@echo You must be root to uninstall.
	@rm -rf $(DESTDIR)$(PREFIX)/battery-monitor
	@rm -f /usr/local/bin/battery-monitor
	@rm -f /etc/xdg/autostart/battery-monitor-autostart.desktop
	@rm -f /usr/share/applications/battery-monitor.desktop
	@echo Uninstallation completed!
