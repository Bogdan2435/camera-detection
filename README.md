# Object Detection using two diffrent models

## Cerinta

1.  Identifica o camera web publica de la care poti prelua un stream video (minimum 720p/20fps) prin rtsp/webrtc – de preferat imaginile sa fie dintr-un spatiu deschis in aer liber cu persoane sau masini
2. Creeaza o aplicatie prin care:
    - Sa te conectezi la camera pentru preluare de imagini (opencv sau alternativa)
    - Aplica doua modele pentru detectie de obiecte pe acest stream video (modelele trebuie sa fie diferite din perspectiva capacitatii de procesare (ex effDet5 vs YoloV2)
    - Afiseaza in paralel doua imagini de la stream-ul procesat (una pentru fiecare model) – cu un overlay care sa contina box-uri care incadreaza obiectele detectate
    - Cele doua ferestre/imagini trebuie sa fie sincronizate (atentie: modelul mai rapid va procesa mai multe frame-uri decat cel mai incet)
3. Codul trebuie structurat pe o arhitectura OOP

## Tools

The two models that I've used are YoloV5 and YoloV8. For the live stream i've set up a RTMP server on my laptop (tool: Local RTMP Server) and I live streamed from my GoPro.

## Demo

I've uploaded a video on YouTube to show how it works. 
Link: https://www.youtube.com/watch?v=tBWciIwvjxo