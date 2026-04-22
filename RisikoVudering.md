#  Risikovurdering Skjema
<img width="1280" height="744" alt="image" src="https://github.com/user-attachments/assets/cd528232-4252-4a55-94ba-da556be079ce" />

--- 

## Prosjekt
### Nettbutikk: Shinystar Stickers

**Beskrivelse:** Proskejket mitt er da en nettbutikk som jeg lager for mine klistremerker, det er skolearbeid men seinere skal brukes til min bedrift  "Shinystar stickers" og nettsiden skal publiseres når den skal bli ferdig ...

**Forberedt av:** Ujala Tayyab Hussain Kanwal

---

## Identifiserte risikoer:
- Risiko 1: [Beskriv risiko]
-  Risiko 2: [Beskriv risiko]
-  Flere risikoer: [Legg til mer hvis nødvendig]



##


## 🔐 Risikovurdeings Tabell

| Risiko | Hva kan gå galt | Alvorlighet | Tiltak |
|--------|----------------|-------------|--------|
| Manglende HTTPS | Data er ikke sikret | Medium | Aktivere HTTPS |
| Kopiering av nettside | Andre kan bruke innholdet | Lav | Være bevisst på publisering |
| Sikkerhetsproblemer ved videre utvikling | Kan bli sårbar hvis man legger til input | Medium | Validere input og skrive sikker kode |
| Dårlig hosting / konfigurasjon | Nettsiden kan bli utsatt for angrep | Medium | Bruke sikker hosting |



### Refleksjon
Jeg har lært at......



# 🔐 Risikovurdering av nettsiden

Prosjektet mitt er en nettbutikk for klistremerker kalt **Shinystar Stickers**. Nettsiden er laget som et skoleprosjekt, men planen er at den senere kan brukes som en ekte nettbutikk. Derfor er det viktig å forstå sikkerhet og risikoer.

---

## 🧠 Hva en risikovurdering er
En risikovurdering betyr at jeg ser på hva som kan gå galt med nettsiden, hvor alvorlig det er, og hva man kan gjøre for å beskytte den. Dette er viktig i cybersikkerhet fordi man prøver å stoppe problemer før de skjer.

---

## ⚠️ 1. Manglende HTTPS (sikker forbindelse)

**Hva betyr dette:**
HTTPS er en sikker forbindelse mellom brukeren og nettsiden. Det gjør at data blir kryptert (gjort om til kode) slik at andre ikke kan lese det.

**Hva kan gå galt:**
Hvis nettsiden ikke bruker HTTPS, kan informasjon som sendes mellom bruker og nettside i teorien bli avlyttet. Dette er spesielt viktig hvis nettsiden senere får betaling eller innlogging.

**Risiko:** Medium  

**Tiltak:**
- Bruke SSL/TLS sertifikat  
- Aktivere HTTPS på nettsiden  

---

## ⚠️ 2. DDoS-angrep

**Hva betyr dette:**
DDoS er et angrep der mange “falske brukere” sender trafikk til nettsiden samtidig for å overbelaste den.

**Hva kan gå galt:**
Nettsiden kan bli veldig treg eller krasje helt, slik at ekte brukere ikke får tilgang.

**Risiko:** Medium  

**Tiltak:**
- Bruke stabil hosting  
- Bruke tjenester som beskytter mot trafikkangrep  

---

## ⚠️ 3. Malware (skadelig programvare)

**Hva betyr dette:**
Malware er skadelig programvare som kan skade systemer, stjele data eller gjøre nettsiden ustabil.

**Hva kan gå galt:**
Hvis serveren eller systemet ikke er godt sikret, kan malware påvirke nettsiden og ødelegge filer eller data.

**Risiko:** Medium  

**Tiltak:**
- Bruke anti-malware program  
- Bruke brannmur som beskytter nettsiden  
- Holde system oppdatert  

---

## ⚠️ 4. Kopiering av nettside

**Hva betyr dette:**
Noen kan kopiere design, bilder eller innhold fra nettsiden og bruke det som sitt eget.

**Hva kan gå galt:**
Mitt arbeid kan bli brukt av andre uten tillatelse, og det kan skape problemer med eierskap.

**Risiko:** Lav  

**Tiltak:**
- Være bevisst på hva som publiseres  
- Eventuelt merke innhold med navn/logo  

---

## ⚠️ 5. Utdaterte systemer eller plugins

**Hva betyr dette:**
Nettsider bruker ofte systemer (CMS som WordPress) og plugins (ekstra funksjoner). Hvis disse ikke oppdateres, kan de få sikkerhetshull.

**Hva kan gå galt:**
Hackere kan bruke gamle feil i systemet til å komme inn på nettsiden eller skade den.

**Risiko:** Høy  

**Tiltak:**
- Oppdatere CMS, plugins og temaer jevnlig  
- Bruke siste versjon av programvare  

---

## ⚠️ 6. Svake tilgangsrettigheter

**Hva betyr dette:**
Tilgangsrettigheter bestemmer hvem som kan gjøre endringer på nettsiden.

**Hva kan gå galt:**
Hvis for mange har tilgang, kan noen gjøre uønskede endringer eller ødelegge innhold.

**Risiko:** Høy  

**Tiltak:**
- Begrense tilgang til kun nødvendige personer  
- Bruke sterke passord og eventuelt 2FA  

---

## ⚠️ 7. Manglende backup

**Hva betyr dette:**
Backup er en kopi av nettsiden som kan brukes hvis noe går galt.

**Hva kan gå galt:**
Hvis nettsiden blir hacket eller data forsvinner, kan alt gå tapt uten backup.

**Risiko:** Høy  

**Tiltak:**
- Ta regelmessige backups  
- Lagre kopier på trygg plass  

---

## 📊 Risikovurderingstabell

| Risiko | Forklaring | Alvorlighet | Tiltak |
|--------|-------------|-------------|--------|
| Manglende HTTPS | Data kan bli avlyttet uten kryptering | Medium | Aktivere SSL/TLS |
| DDoS-angrep | Nettsiden kan bli overbelastet og krasje | Medium | Bruke stabil hosting |
| Malware | Skadelig programvare kan skade systemet | Medium | Brannmur og anti-malware |
| Kopiering | Andre kan kopiere nettsiden | Lav | Være bevisst på publisering |
| Utdaterte systemer | Sikkerhetshull kan utnyttes | Høy | Jevnlig oppdatering |
| Svake tilganger | Uautoriserte kan endre nettsiden | Høy | Begrense tilgang |
| Manglende backup | Data kan gå tapt | Høy | Regelmessig backup |

---

## 🧠 Refleksjon

Jeg har lært at cybersikkerhet handler om å beskytte systemer mot mange typer risikoer, selv på en enkel nettside. Det viktigste er å tenke forebyggende og bruke grunnleggende sikkerhetstiltak som oppdateringer, backup og tilgangskontroll.

Jeg forstår nå bedre hvordan nettsider kan bli utsatt for angrep, og hvorfor sikkerhet er viktig allerede i starten av et prosjekt.

---

## 📌 Konklusjon
En nettside kan være enkel, men må likevel sikres godt før den publiseres på internett.


## 📌 Bekreftelse

Jeg bekrefter at denne risikovurderingen er gjennomført basert på mitt nettsideprosjekt (**Shinystar Stickers**). Jeg har identifisert relevante risikoer, vurdert hvor alvorlige de er, og foreslått tiltak for å redusere eller forhindre dem.

Denne oppgaven viser min forståelse av grunnleggende cybersikkerhet og hvordan man kan tenke forebyggende når man utvikler og publiserer en nettside.

---

**Navn:** Ujala Tayyab Hussain Kanwal  
**Dato:** 22.04.2026  


---

<p align="right">
Ujala Tayyab Hussain Kanwal<br>
22.04.2026
</p>
