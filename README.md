# ProsjektOppgave_2IT

Jeg skal lage en **ekte nettbutikk** for min egen business “ShinystaR Stickers”.  
Nettbutikken viser produktene mine (klistremerker) med bilder, navn, pris og beskrivelse.  

Jeg bruker:  
- **Raspberry Pi** som webserver  
- **MariaDB** for å lagre produkter, brukere og handlekurv  
- **Flask (Python)** til å lage nettsiden og koble til databasen  
- **HTML og CSS** for design, layout og struktur  

## DEL#01
## Prototype / MVP
Første versjon (MVP) viser noen produkter på forsiden med bilde, navn og pris (2-3 produkter).  
Handlekurv og innlogging legges til senere når nettsiden fungerer.  

## Kompetanse vist
- **Drift:** Raspberry Pi, Flask, MariaDB, serverkonfigurasjon  
- **Utvikling:** Python, HTML/CSS, datastrukturer, database, backend  
- **Brukerstøtte:** Brukerveiledning, dokumentasjon på GitHub, testing, FAQ-side  

## Teknologier og verktøy
- **Backend:** Flask, Python, SQL  
- **Frontend:** HTML, CSS, Jinja, JavaScript  
- **Database:** Opprette tabeller, hente og oppdatere produkter og FAQ  
- **Drift:** Raspberry Pi, serverkonfigurasjon  
- **Interaktivitet:** Dynamiske sider, knapper, ikoner, FAQ-elementer
  
## Prosess
### Server og webapplikasjon
- Flask håndterer **HTTP-forespørsler** og fungerer som backend.  
- Flask kobles til MariaDB for å hente og lagre data.  
- HTML/CSS utgjør frontend.  

### Database
- MariaDB lagrer:  
  - Produkter (navn, beskrivelse, pris, bilde)  
  - Brukere (for innlogging)  
  - Handlekurv og favoritter  
- Flask sender SQL-spørringer for å hente, legge til eller oppdatere data.  
- Produktene vises automatisk via **Jinja-templating**.  

### Frontend og visning
- HTML lager struktur: seksjoner for produkter, hero-bilder, FAQ, handlekurv og favoritter  
- CSS gir layout, styling og responsivt design  
- Jinja setter inn database-data dynamisk  

### Dynamisk innhold
- Forsiden viser et begrenset antall produkter med SQL `LIMIT`  
- Produktsiden viser alle produkter  
- Nye produkter i databasen vises automatisk uten å endre koden  

### Interaktivitet
- Brukere kan legge produkter til **favoritter** eller **handlekurv**  
- Flask og databasen håndterer data, mens frontend oppdateres dynamisk  
- Fremtidig funksjonalitet:  
  - Favoritt-knapp som legger til/fjerner produkter  
  - Handlekurv-knapp som legger til/fjerner produkter  
  - Slette produkter fra handlekurven  

### FAQ-side
- Spørsmål vises som foldbare elementer (accordion)  
- Data hentes fra MariaDB via Flask  
- Nye spørsmål vises automatisk  

### Prosessflyt
1. Bruker åpner nettsiden  
2. Nettleser sender HTTP-forespørsel til Flask  
3. Flask henter data fra MariaDB  
4. Flask sender data til HTML med Jinja  
5. Nettleser viser nettsiden  
6. Bruker kan interagere med favoritter, handlekurv eller FAQ, og siden oppdateres dynamisk  

## DEL#02
## Videre utvikling / fremtidige planer
### Handlekurv og favoritter
- Fullføre fungerende handlekurv  
- Fullføre fungerende favoritter  

### Søk og brukerprofiler
- Gjøre search bar funksjonell  
- Implementere innlogging og brukerprofiler  

### Tilgjengelighet og testing
- Nettsiden skal kunne åpnes på andre maskiner  
- Teste nettsiden i virtuelle maskiner eller med testbrukere  

### Brukerveiledning og dokumentasjon
- Lage brukerveiledning eller video for nettsiden  

### Utvidelser og forbedringer
- Flere produkter og kategorier  
- Forbedre design og layout (responsivt for mobil og desktop)  
- Eventuelt betalingsløsning  
- Forbedre brukeropplevelse med interaktive elementer  
