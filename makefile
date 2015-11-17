###################################################################
# Installing clamTools (Linux & *BSD systems)                     #
###################################################################

PREFIX=/usr

install:
	cp clamTools/clamTools.py $(PREFIX)/bin
	cp clamToolsdbd/clamToolsdbd.py $(PREFIX)/bin
	cp clamToolsdbd/clamToolsdbd-log.py $(PREFIX)/bin
	cp clamToolsd/clamToolsd.py $(PREFIX)/bin
	cp clamToolsd/clamToolsd-log.py $(PREFIX)/bin
	cp clamToolsd/clamToolsd-config.py $(PREFIX)/bin
	cp desktop/clamav-accesories.desktop $(PREFIX)/share/applications
	cp desktop/clamav-system.desktop $(PREFIX)/share/applications
	cp icon/clamav.png $(PREFIX)/share/icons
	chmod +x $(PREFIX)/bin/clamTools.py
	chmod +x $(PREFIX)/bin/clamToolsdbd.py
	chmod +x $(PREFIX)/bin/clamToolsdbd-log.py
	chmod +x $(PREFIX)/bin/clamToolsd.py
	chmod +x $(PREFIX)/bin/clamToolsd-log.py
	chmod +x $(PREFIX)/bin/clamToolsd-config.py
	chmod +x $(PREFIX)/share/applications/clamav-accesories.desktop
	chmod +x $(PREFIX)/share/applications/clamav-system.desktop
	
uninstall:
	rm $(PREFIX)/bin/clamTools.py
	rm $(PREFIX)/bin/clamToolsdbd.py
	rm $(PREFIX)/bin/clamToolsdbd-log.py
	rm $(PREFIX)/bin/clamToolsd.py
	rm $(PREFIX)/bin/clamToolsd-log.py
	rm $(PREFIX)/bin/clamToolsd-config.py
	rm $(PREFIX)/share/applications/clamav-accesories.desktop
	rm $(PREFIX)/share/applications/clamav-system.desktop
	rm $(PREFIX)/share/icons/clamav.png

