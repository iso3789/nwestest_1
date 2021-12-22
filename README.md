# Webserver-Programm in Python
## Aufgabenstellung **(60 Punkte)**
Programmieren Sie bitte in Python einen einfachen Webserver `serverlein.py` mit folgender Funktionalität unter Verwendung der socket–Bibliothek:  

1. Nach dem Start mit `./serverlein.py` soll der Server auf allen Interfaces auf Port 8080 empfangsbereit sein.
2. Ablauf der Kommunikation Client-Server gemäß HTTP:
    - Client (Webbrowser) sendet eine Begrüßung:  
    `GET / HTTP/1.1\r\nHost: localhost\r\n\r\n`  
    Diese soll zwar gelesen werden, eine weitere Bearbeitung oder Überprüfung ist aber nicht notwendig. 
    - Server antwortet mit:  
    `HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>` 
3. Server schließt den Socket zum Client mit `close()` und ist danach für neue Client-Anfragen bereit.

*Tipps:*  
- *Die vom Sender erzeugte Antwort muss vor dem Versand mit `encode()` in das UTF-8 - Format konvertiert werden.*
- *Um beim Testen die Meldung `Address is already in use`  zu vermeiden, kann vor dem Aufruf von `bind` diese Zeile eingefügt werden:* 
*`s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`*
- *Test des Servers mittels Webbrowser, URL `http://<familienname>.local:8080`*

## Bonusaufgabe: **(20 Punkte)**  
Der Server liefert als Antwort nicht nur `Hi BULME`, sondern `Hi BULME an (<IP>, <Portnummer)`. IP und Portnummer sind dabei die Verbindungs-Parameter es aufrufenden Clientrechners.

## Abgabe via github: **(20 Punkte)**
Versionierung des Projektes mit git und Upload des Repositorys `nwestest_1` auf den eigenen github-Account.

### Notenschlüssel

| Punkte | Note |
|--------|------|
|100 - 89  |sehr gut |
|88 - 76|gut |
|75 - 63| befriedigend|
|62 - 50 | genügend |
|49 - 0| nicht genügend|

### *Ivan Dzido:*