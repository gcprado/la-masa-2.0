# 📊 LA MASA 2.0 — TRACKER

Sistema de seguimiento del pipeline de documentación del proyecto LA MASA 2.0. Registra el estado de cada vídeo a través de las fases T1–T4, desde la transcripción bruta hasta su integración final.

---

## 🟢 INTEGRACIÓN FINAL (T4)

- Informe la masa 1 y 2

---

## 🔵 EDICIÓN FINAL (T3)

- Informe la masa 1,2 y 3

---

## 🟡 ESTRUCTURACIÓN (T2)

- [20120623 - Informes LA MASA ｜ Nº1 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=vJ0p7iAndXU): OK
- [20120625 - Informes LA MASA ｜ Nº2 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=wxnOS1WXNsc): OK
---

## 🟠 TRANSCRIPCIÓN BRUTA (T1)

- [20240512 - TOP 5 DE MI VIDA, Parte 2: Family Game](https://www.youtube.com/watch?v=xtyfwhRCEgY): ~0%
- [20240412 - TOP 5 DE MI VIDA, Parte 1： Colecovision](https://www.youtube.com/watch?v=HEJUk9C1TnU): ~0%
- [20120815 - Informes LA MASA ｜ Nº4 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=POLYmWpNFZ4): ~100%
- [20120711 - Informes LA MASA ｜ Nº3 ｜ Historia de los Videojuegos](https://www.youtube.com/watch?v=er3JOh96jPY): ~100%

---

## 🔴 PENDIENTES

- lo mejor que jugue
- evolucion del videjuego por decadas
- evolucion del juego del año
- top 5 de mi vida
- Informe la masa 5 y 6
- debut de tdv

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