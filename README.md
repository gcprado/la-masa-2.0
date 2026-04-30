# 📊 LA MASA 2.0 — TRACKER

Sistema de seguimiento del pipeline de documentación del proyecto LA MASA 2.0. Registra el estado de cada vídeo a través de las fases T1–T4, desde la transcripción bruta hasta su integración final.

---

## 🟢 INTEGRACIÓN FINAL (T4)

- Informe la masa 1

---

## 🔵 EDICIÓN FINAL (T3)

- Informe la masa 1 y 2

---

## 🟡 TRANSCRIPCIÓN ORDENADA (T2)

- [20240918 - TOP 5 DE MI VIDA, Parte 6： Playstation 3, Xbox 360 y Nintendo Wii](https://www.youtube.com/watch?v=ZyXF755fu4s): OK
- [20240815 - TOP 5 DE MI VIDA, Parte 5： Playstation 2 y Nintendo Gamecube](https://www.youtube.com/watch?v=Yzy8de4qR1g): OK
- [20240730 - TOP 5 DE MI VIDA, Parte 4： Nintendo 64 y Playstation 1](https://www.youtube.com/watch?v=PPWq7Ucvu0U): OK
- [20240611 - TOP 5 DE MI VIDA, Parte 3： Sega y Super Nintendo](https://www.youtube.com/watch?v=qS10MAa_glo): OK
- [20240512 - TOP 5 DE MI VIDA, Parte 2: Family Game](https://www.youtube.com/watch?v=xtyfwhRCEgY): OK
- [20240412 - TOP 5 DE MI VIDA, Parte 1： Colecovision](https://www.youtube.com/watch?v=HEJUk9C1TnU): OK
- [20120625 - Informes LA MASA ｜ Nº2 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=wxnOS1WXNsc): OK
- [20120623 - Informes LA MASA ｜ Nº1 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=vJ0p7iAndXU): OK

---

## 🟠 TRANSCRIPCIÓN BRUTA (T1)

- [20250309 - EVOLUCIÓN del TOP 10 de Videojuegos de los 2000 | Análisis de Tiempo de Videojuegos](https://www.youtube.com/watch?v=3uFkR43tHes): ~0%
- [20250223 - EVOLUCIÓN del TOP 10 de Videojuegos de los '90 | Análisis de Tiempo de Videojuegos](https://www.youtube.com/watch?v=lalKFeuOXCA): ~0%
- [20250218 - EVOLUCIÓN del TOP 10 de Videojuegos de los '80 | Análisis de Tiempo de Videojuegos](https://www.youtube.com/watch?v=PftT2SEzKVU): ~0%
- [20241127 - TOP 5 DE MI VIDA, Parte 7： Playstation 4, Xbox One y Nintendo Wii U ⧸ Switch](https://www.youtube.com/watch?v=Tv6UbtvJBWk): ~100%
- [20120815 - Informes LA MASA ｜ Nº5 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=nOV-w09tos8): ~0%
- [20120815 - Informes LA MASA ｜ Nº4 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=POLYmWpNFZ4): ~100% OP
- [20120711 - Informes LA MASA ｜ Nº3 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=er3JOh96jPY): ~100% OP

---

## 🔴 PENDIENTES

- evolucion del videjuego decada 2010
- lo mejor que jugue
- evolucion del juego del año
- Informe la masa 5 y 6
- debut de tdv
- criterio de puntajes
- puntajes por generacion

---

# 🧾 NOTAS TÉCNICAS

## 📌 Header obligatorio en cada fichero

Cada archivo debe comenzar con el siguiente formato:

```text
REGISTRO DOCUMENTAL: LA MASA 2.0
TITULO:
SERIE: ver mas abajo lo referente a SERIE
FECHA ORIGINAL: YYYY-MM-DD (*)
BACKUP: 720p@1234kbps H.264 - 4.3GB (.mp4)

DOCUMENTACIÓN:
FECHA: XXXX-XX-XX | ESTADO: T1 (TRANSCRIPCIÓN BRUTA) - 0h:00m:00s - 0.0%
FECHA: XXXX-XX-XX | ESTADO: T2 (TRANSCRIPCIÓN ORDENADA)
FECHA: XXXX-XX-XX | ESTADO: T3 (REVISIÓN / EDICIÓN FINAL)
FECHA: XXXX-XX-XX | ESTADO: T4 (INTEGRACIÓN / INFORME FINAL)

TIMESTAMPS DE INTERÉS:
- 10:30 (ejemplo)

NOTAS:
- Ejemplo 1
- Ejemplo 2

------------------------------------------------------------

[00:00]

PEGA LA TRANSCRIPCIÓN DE WHISPER AQUI!!

[FIN]
```

📄 Ver archivo base: `./header.txt`

---

## 📁 ESTRUCTURA DEL BACKUP

La **SERIE** de cada vídeo corresponde al **directorio más profundo donde se encuentra almacenado dentro del backup**.

```
├── 1.LA MASA e INFORMES
│   ├── DEBUT DE TDV
│   ├── INFORME DE CONSOLAS
│   ├── INFORME DE SAGAS
│   └── LA MASA
│
├── 2.MUNDIAL DE VIDEJUEGOS
│   └── ELIMINATORIAS
│
├── 3.LIGAS y TORNEOS
│   ├── 1.Liga de CONSOLAS RETRO
│   ├── 2.Liga de CONSOLAS 3D
│   ├── 3.Torneo de CONSOLAS PORTÁTILES
│   ├── 4.Liga de CONSOLAS CRUZADAS
│   ├── 5.Liga de CONSOLAS HD
│   ├── 6.COPA DE LAS SAGAS SIGLO XX
│   └── 7.Liga de TODOS LOS TIEMPOS
│
├── 4.EVOLUCIÓN DE VIDEOJUEGOS
│   ├── DÉCADAS
│   └── GÉNEROS
│
├── 5.TIER LIST
├── 6.TOP 5 DE MI VIDA
├── 7.PUNTAJES
├── 8.CÓMO JUGAR
├── 9.REACCIÓN
│
├── 10.CHARLAS Y ENTREVISTAS
│
├── 11.PROGRMAS Y PODCASTS
│   ├── BLENDER
│   ├── Press Over
│   └── Vorterix
│
├── 12.ANECDOTA
│
├── 13.ESPECIALES Y NIGHT FIGHT
│   └── NIGHT FIGHT
│
├── 14.SHORTS
```