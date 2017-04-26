Title: Der Gnome3 Shell Recorder
Date: 2011-04-23 05:58
Author: Heiko
Category: Artikel
Tags: News,Screencast-Tool,gnome3,shell-recorder,dconf-editor,gsettings
Slug: gnome3_shell_recorder

Nicht nur die Screenshot-Funktionalität (Bildschirmfotos erstellen) gehört,
wie auch schon bei Gnome2, zur Grundausstattung von Gnome3, sondern jetzt auch
neu die Bildschirmvideoaufnahme. Bisher war es um Bildschirmaktivitäten in
einem Video festzuhalten immer notwendig ein zusätzliches Tool wie z.B.
recordmydesktop zu installieren. Jetzt reicht es vollkommen aus wenn die
Tastenkombination Strg+Alt+Shift+R gedrückt wird um die Bildschirmaufnahme zu
beginnen und zu beenden. Die Aufnahme wird die ganze Zeit rechts unten durch
einen kleinen roten Kreis angezeigt.

![Shell recorder 1](https://www.openscreencast.de/pictures/shellrecorder1.png)

Die festgehaltenen Bilder werden in eine .webm-Datei geschrieben. Die Datei
mit folgendem Muster shell-yyyymmdd-#.webm befindet sich im Home-Verzeichnis
und enthält den VP8-Videocodec. Die Framerate beträgt den Wert 15, was
bedeutet das 15 Bilder pro Sekunden gespeichert werden. Audio-Daten gibt es
allerdings nicht. Die Framerate und auch das Video-Format können geändert
werden. Hier kommt das Einstellungstool dconf-editor ins Spiel. dconf-editor
gehört nicht zum Standard und muss nachinstalliert werden. Bei der
Linuxdistribution Fedora leitet man dies mit folgendem Befehl in die Wege: `su
-c "yum install dconf-editor"`.

![Shell recorder 2](https://www.openscreencast.de/pictures/shellrecorder2.png)

Nach dem Start, per Eingabe dconf-editor, findet man unter
org.gnome.shell.recorder 3 Einstellungsmöglichkeiten. Der Wert der Dateiendung
(file-extension: webm), der Framerate (framerate: 15) und der pipeline
(pipeline: '') kann verändert werden.

![Shell recorder 3](https://www.openscreencast.de/pictures/shellrecorder3.png)

Möchte man die Modifikation per Befehl bewerkstelligen so sei an dieser Stelle
der Befehl gsettings erwähnt. Folgende Kommandos sind denkbar um die gesetzten
Werte abzurufen.

`gsettings get org.gnome.shell.recorder file-extension # Dateiendung -
default: webm  
gsettings get org.gnome.shell.recorder framerate # Frames pro Sekunde -
default: 15  
gsettings get org.gnome.shell.recorder pipeline # Pipeline - default: ''
('videorate ! vp8enc quality=10 speed=2 threads=%T ! queue ! webmmux')  
`  
Da hingegen kann get durch set ersetzt werden um Werte neu zu setzen.  
`  
gsettings set org.gnome.shell.recorder file-extension ogv # Dateiendung -
default: webm  
gsettings set org.gnome.shell.recorder framerate 25 # Frames pro Sekunde -
default: 15  
gsettings set org.gnome.shell.recorder pipeline 'videorate ! theoraenc ! queue
! oggmux' # Pipeline - default: ''  
`  
Mit diesen Einstellungen ist das Ergebnis der Aufnahme nun ein Video im Format
Ogg-Theora.

