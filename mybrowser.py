#!/usr/bin/env python
import gtk,webkit


def go_but(widget):
	add = addressbar.get_text()
	try:
		add.index("://")
	except Exception:
		add="http://"+add
	web.open(add)

win=gtk.Window()
win.connect('destroy',lambda w: gtk.main_quit())
box1 = gtk.VBox()
win.add(box1)
box2= gtk.HBox()
box1.pack_start(box2,False)
addressbar=gtk.Entry()
addressbar.connect('activate',go_but)
box2.pack_start(addressbar)
gobutton = gtk.Button("Go")

box2.pack_start(gobutton,False)

scroller=gtk.ScrolledWindow()
box1.pack_start(scroller)

web=webkit.WebView()
scroller.add(web)
gobutton.connect('clicked',go_but)
win.maximize()
win.show_all()
gtk.main()
