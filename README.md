# ProsjektOppgave_2IT

Jeg skal lage en **ekte nettbutikk** for min egen business “ShinystaR Stickers”.  
Nettbutikken skal vise produktene mine (klistremerker), med bilder, navn, pris og beskrivelse.  

Jeg bruker:  
- **Raspberry Pi** som webserver for å kjøre nettsiden  
- **MariaDB** for å lagre produkter, brukere og handlekurv  
- **Flask (Python)** til å lage nettsiden og koble den til databasen/Backend 
- **HTML og CSS** for design, layout og strukturen av nettsiden

## Prototype / MVP
Første versjon (MVP) viser noen produkter på forsiden med bilde, navn og pris.(Jeg begynner enkelt først, bare med å lage 2-3 produkt først)  
Handlekurv og innlogging legges til senere når nettsiden fungerer.  

## Kompetanse vist i prosjektet
- **Drift:** Raspberry Pi, Flask, MariaDB, konfigurering av server  
- **Utvikling:** Python, HTML/CSS, datastrukturer, database , Backend 
- **Brukerstøtte:** Brukerveiledning, dokumentasjon på GitHub, testing

## **PROCESS**
### 1. Server og webapplikasjon
- **Raspberry Pi** brukes som webserver for å kjøre nettsiden.  
- **Flask (Python)** brukes til å lage webapplikasjonen, som håndterer **HTTP-forespørsler** fra nettlesere (f.eks. når en bruker åpner nettsiden eller klikker på et produkt).  
- Flask kobles til **MariaDB** for å hente og lagre data. Flask fungerer som **Backend**, mens HTML/CSS fungerer som **Frontend**.  

### 2. Database
- **MariaDB** lagrer alle data for nettbutikken:  
  - Produkter (navn, beskrivelse, pris, bilde)  
  - Brukere (for fremtidig innlogging)  
  - Handlekurv og favoritter  
- Flask sender SQL-spørringer til databasen for å hente, legge til eller oppdatere data.  
- Produktene som legges til i databasen vises automatisk på nettsiden gjennom **Jinja-templating**.

### 3. Frontend og visning av data
- **HTML** lager strukturen på nettsiden, som seksjoner for produkter, hero-bilder, FAQ-seksjon og knappene for handlekurv og favoritter.  
- **CSS** brukes for layout, styling, farger og responsiv design.  
- **Jinja** brukes til å sette inn data fra databasen direkte i HTML, slik at produktene vises dynamisk.  

### 4. Dynamisk innhold
- Forsiden viser et begrenset antall produkter (f.eks. 4) ved hjelp av SQL-spørring med `LIMIT`.  
- Produktsiden viser alle produkter.  
- Når nye produkter legges til databasen, blir de automatisk synlige på nettsiden uten å endre koden.  

### 5. Interaktivitet
- Brukere kan legge produkter i **favoritter** eller **handlekurv**.  
- Dette håndteres gjennom Flask og databasen, og brukergrensesnittet oppdateres dynamisk via HTML, CSS og JavaScript (knapper, ikoner).  
- **Fremtidig funksjonalitet:**  
  - Fungerende favoritt-knapp som legger til/fjerner produkter i favoritter.  
  - Fungerende handlekurv-knapp som legger til/fjerner produkter i handlekurv.  
  - Mulighet for å slette produkter direkte fra handlekurven.  

### 6. FAQ-side
- FAQ-siden viser ofte stilte spørsmål delt inn i kategorier.  
- Spørsmålene vises som foldbare elementer (accordion), slik at brukeren kan klikke for å se svaret.  
- FAQ-data hentes fra MariaDB via Flask, og nye spørsmål vises automatisk.  

### 7. Prosessflyt
1. Bruker åpner nettsiden i nettleser.  
2. Nettleseren sender en **HTTP-forespørsel** til Flask-serveren.  
3. Flask sjekker databasen via SQL og henter produktene eller FAQ-data.  
4. Flask sender dataene til HTML-sidene med **Jinja**.  
5. Nettleseren viser nettsiden med produkter, bilder og priser, eller FAQ-seksjonen.  
6. Bruker kan trykke på hjerte-knappen for favoritter, handlekurv-knappen, eller åpne FAQ-spørsmål. Flask oppdaterer session/data, og siden viser endringen dynamisk.  

## 8. Teknologier og verktøy brukt
- **Backend:** Flask, Python, SQL, databasetilkobling  
- **Frontend:** HTML, CSS, Jinja, JavaScript  
- **Database:** Opprette tabeller, hente og oppdatere produkter og FAQ  
- **Drift:** Raspberry Pi, serverkonfigurasjon  
- **Interaktivitet:** Dynamiske sider, bruk av knapper, ikoner og foldbare FAQ-elementer


