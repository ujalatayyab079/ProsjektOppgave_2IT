#  Risikovurdering Skjema


<img width="1280" height="744" alt="image" src="https://github.com/user-attachments/assets/cd528232-4252-4a55-94ba-da556be079ce" />

<p align="right">
Pixabay.com
</p>




## Prosjekt
### Nettbutikk: Shinystar Stickers

**Beskrivelse:** Prosjektet mitt er en nettbutikk for klistremerker kalt **Shinystar Stickers**. Nettsiden er laget som et skoleprosjekt, der målet er å lære hvordan man planlegger, bygger og tenker rundt en ekte nettbutikk.

Selv om dette er et skoleprosjekt, er det laget med tanke på at det senere kan utvikles videre og faktisk brukes som en ekte nettbutikk for salg av klistremerker. Dette gjør at prosjektet blir mer realistisk og gir en bedre forståelse av hvordan webutvikling fungerer i praksis.

Nettsiden er enkel og inneholder hovedsakelig informasjon om produkter og konseptet bak bedriften. Den har ikke avanserte funksjoner som innlogging eller betaling enda, men kan bygges videre med slike funksjoner senere.

Siden nettsiden potensielt kan publiseres på internett, er det viktig å tenke på sikkerhet. Dette inkluderer hvordan man beskytter nettsiden mot angrep, hvordan data håndteres, og hvilke tiltak som må være på plass for å sikre brukere og innhold.

**Forberedt av:** Ujala Tayyab Hussain Kanwal

---

##  Hva er en risikovudering?

En risikovurdering betyr at jeg ser på hva som kan gå galt med nettsiden, hvor alvorlig det er, og hva man kan gjøre for å beskytte den. Dette er viktig i cybersikkerhet fordi man prøver å stoppe problemer før de skjer.
Risikovudering er en systematisk prossess for å identifisere uønsekede hendelser, vudere sannsynligheten for at de skjer, og konsekvensene hvis de inntreffer. Hensikten er å implementere tiltak som reduserer risikoen til et akseptabelt nivå. Det er et lovkrav (HMS) for alle virksomheter for å forebygge skader og sykdom på arbeidsplassen.
<p align="right">
  arbeidstilsynet.no
</p>

<img width="633" height="376" alt="image" src="https://github.com/user-attachments/assets/d88f5f9d-199b-42e0-bffc-00e3f324809c" />

---
<img width="2560" height="1280" alt="image" src="https://github.com/user-attachments/assets/5c678b56-b97a-4aec-be27-8bb904cfb47f" />

## Identifiserte risikoer med risikovudering og tiltak



### ⚠️ 1. Manglende HTTPS (sikker forbindelse)

**Hva betyr dette:**
HTTPS er en sikker måte å sende data mellom brukeren og nettsiden på. Det betyr at informasjon blir kryptert slik at andre ikke kan lese den.

**Hva kan skje:**
Hvis nettsiden ikke bruker HTTPS, kan data som sendes mellom bruker og nettside i noen tilfeller bli avlyttet. Dette kan være brukernavn, kontaktinformasjon eller annen sensitiv data. Uten HTTPS kan også brukere miste tillit til nettsiden fordi den ikke virker sikker.

**Risiko:** Medium  

**Tiltak:**
- Aktivere SSL/TLS-sertifikat slik at nettsiden bruker HTTPS i stedet for HTTP  
- Sørge for at hele nettsiden automatisk videresender brukere til HTTPS  
- Bruke hosting-tjenester som tilbyr gratis eller automatisk HTTPS (for eksempel Let’s Encrypt)  
- Kontrollere at alle bilder, skript og ressurser lastes inn via sikre (HTTPS) kilder  


---

### ⚠️ 2. DDoS-angrep

**Hva betyr dette:**
DDoS er et angrep der mange datamaskiner sender trafikk til nettsiden samtidig for å overbelaste den.

**Hva kan skje:**
Nettsiden kan bli veldig treg eller helt utilgjengelig. Dette betyr at ekte brukere ikke får tilgang til nettsiden. For en nettbutikk kan dette føre til tap av kunder og salg.

**Risiko:** Medium  

**Tiltak:**
- Bruke hosting-leverandør som har innebygd DDos-beskyttelse
- Bruke tjenester som filterer og blokkerer mistenkelig trafikk
- Begrense unnormal trafikk fra samme IP-addresse der det er mulig
- Overvåke trafikk for å oppdage angrep tidlig

---

### ⚠️ 3. Malware (skadelig programvare)

**Hva betyr dette:**
Malware er skadelig programvare som er laget for å ødelegge, stjele eller manipulere data.

**Hva kan skje:**
Hvis nettsiden eller serveren blir infisert, kan filer bli ødelagt eller stjålet. Hackere kan også bruke malware til å få kontroll over systemet eller endre innholdet på nettsiden.

**Risiko:** Medium  

**Tiltak:**
- Installere anti-malware som skanner nettsiden og filer regelmessig
- Bruke brannmur (firewall) for å stoppe mistenkelig aktivitet
- Holde CMS, plugins og systemer oppdatert til nyeste versjon
- Kun bruke plugins og filer fra pålitelige kilder


---

### ⚠️ 4. Kopiering av nettside

**Hva betyr dette:**
Andre personer kan kopiere design, bilder eller tekst fra nettsiden.

**Hva kan skje:**
Innholdet mitt kan bli brukt av andre uten tillatelse. Dette kan føre til at mitt arbeid blir kopiert eller misbrukt, og det kan skape problemer med eierskap til design og innhold.

**Risiko:** Lav  

**Tiltak:**
- Være bevisst på hva som publiseres offentlig
- Legge inn logo/navn på design og innhold for å vise eierskap
- Strukturere innhold slik at det er mindre enkelt å kopiere direkte
- Vudere opphavsrett eller lisens hvis prosjektet blir kommersielt


---

### ⚠️ 5. Utdaterte systemer eller plugins

**Hva betyr dette:**
Nettsider bruker ofte CMS (som WordPress), plugins og temaer. Dette er programvare som kan oppdateres for å fikse feil.

**Hva kan skje:**
Hvis systemet ikke oppdateres, kan hackere utnytte kjente sikkerhetshull i gamle versjoner. Dette kan føre til at nettsiden blir hacket eller ødelagt.

**Risiko:** Høy  

**Tiltak:**
- Oppdatere CMS (f.eks. WordPress) jevnlig
- Oppdatere plugins og temaer så snart nye versjoner kommer
- Fjerne plugins som ikke brukes lenger
- Bruke kun sikre og godt vedlikeholdte plugins

---

### ⚠️ 6. Svake tilgangsrettigheter

**Hva betyr dette:**
Tilgangsrettigheter bestemmer hvem som kan gjøre endringer på nettsiden.

**Hva kan skje:**
Hvis for mange personer har tilgang, eller hvis passord er svake, kan uvedkommende få tilgang til å endre eller slette innhold. Dette kan føre til at nettsiden blir ødelagt eller misbrukt.

**Risiko:** Høy  

**Tiltak:**
- Gi kun nødevendige tilganger til brukere (minste privilegium-prinsippet )
- Bruke sterke og unike passorrd
- Aktivere to-faktor autentisering (2FA) for admin-tilgang
- Endre standard brukernavn dersom systemet tillater det


---

### ⚠️ 7. Manglende backup

**Hva betyr dette:**
Backup er en kopi av nettsiden som kan brukes hvis noe går galt.

**Hva kan skje:**
Hvis nettsiden blir hacket, slettet eller får feil, kan all data gå tapt hvis man ikke har backup. Dette kan bety at hele nettsiden må bygges på nytt.

**Risiko:** Høy  

**Tiltak:**
- Lage automatiske backups av hele nettsiden jevnlig
- Lagre backup både lokalt og i sky (for ekstra sikkerhet)
- Teste backup for å sikre at den kan gjenopprettes
- Ta ekstra backup før større endringer i nettsiden


### ⚠️ 8.  Identifisere hvilken informasjon som finnes på nettsiden

**Hva betyr dette:**
Dette handler om å finne ut hvilken type informasjon nettsiden inneholder og håndterer. Eksempler kan være personopplysninger, kundedata, eller innloggingsinformasjon. Dette er viktig fordi ulike typer data krever ulik grad av sikkerhet.

**Hva kan skje:**
Hvis sensitiv informasjon ikke er godt beskyttet, kan den bli misbrukt eller komme på avveie. For eksempel kan personopplysninger bli lekket, eller innloggingsinformasjon kan bli stjålet og brukt til å få uautorisert tilgang til systemet.
Dette kan føre til alvorlige konsekvenser som tap av tillit fra kunder, skade på bedriftens omdømme, og i verste fall økonomisk tap. Kundedata som navn, adresse eller betalingsinformasjon kan også bli stjålet og misbrukt.
Dersom nettsiden ikke er sikker nok, kan den også bli kompromittert (hacket), noe som kan føre til at man mister kontroll over nettsiden eller må ta den ned.

**Risiko:** Høy  

**Tiltak:**
- Kartlegge hvilken data nettsiden faktisk lagrer og behandler  
- Unngå å lagre unødvendig sensitiv informasjon  
- Kryptere sensitive data (for eksempel passord og personopplysninger)  
- Bruke sikre innloggingsmetoder og god tilgangskontroll
  
---

## Risikovurderingstabell


<img src="https://github.com/user-attachments/assets/be56aae2-eead-414f-9f7b-6d40a79c1f6c" width="1100">
<p align="right">
Freepik.com
</p>


| Risiko | Forklaring | Alvorlighet | Tiltak |
|--------|-------------|-------------|--------|
| Manglende HTTPS | Data kan bli avlyttet uten kryptering | Medium | Aktivere SSL/TLS |
| DDoS-angrep | Nettsiden kan bli overbelastet og krasje | Medium | Bruke stabil hosting |
| Malware | Skadelig programvare kan skade systemet | Medium | Brannmur og anti-malware |
| Kopiering | Andre kan kopiere nettsiden | Lav | Være bevisst på publisering |
| Utdaterte systemer | Sikkerhetshull kan utnyttes | Høy | Jevnlig oppdatering |
| Svake tilganger | Uautoriserte kan endre nettsiden | Høy | Begrense tilgang |
| Manglende backup | Data kan gå tapt | Høy | Regelmessig backup |
| Manglende beskyttelse av sensitiv informasjon (personopplysninger, kundedata, innlogginger) | Sensitive data kan bli stjålet eller misbrukt dersom de ikke er godt nok beskyttet. Dette kan føre til hacking, datalekkasjer og tap av tillit fra brukere | Høy | Kryptere sensitive data, bruke sikre innloggingssystemer, og unngå å lagre unødvendig informasjon |

---

<p align="right">
Freepik.com
</p>


<img src="https://github.com/user-attachments/assets/8c7382bb-a80b-4cbe-9b93-c17e8342bece" width="1100">


##  Refleksjon

Gjennom dette prosjektet har jeg lært at cybersikkerhet handler om å beskytte systemer mot mange ulike typer risikoer, og ikke bare én type trussel. Det er viktig å se nettsikkerhet fra flere perspektiver, som teknisk sikkerhet, brukerdata og hvordan systemet kan bli utnyttet av andre.

Selv en enkel nettside kan ha mange sårbarheter dersom den ikke er godt sikret. Derfor har jeg forstått hvor viktig det er å tenke forebyggende, og bruke grunnleggende sikkerhetstiltak som oppdateringer, backup, tilgangskontroll og kryptering.

Jeg har også fått en bedre forståelse av hvordan nettsider faktisk kan bli angrepet eller kompromittert, og hvorfor sikkerhet må bygges inn helt fra starten av et prosjekt, ikke legges til etterpå.

I løpet av arbeidet har jeg utforsket temaet mer aktivt gjennom TryHackMe, som har gitt meg en mer praktisk forståelse av cybersikkerhet. Dette har hjulpet meg å se sammenhengen mellom teori og praksis, og gjort det lettere å forstå hvordan ekte sikkerhetsproblemer fungerer.

Alt i alt føler jeg at jeg har fått en mye bedre forståelse av cybersikkerhet, og jeg ser nå mer helhetlig på hvordan systemer, brukere og data henger sammen i et sikkert digitalt miljø.


##  Konklusjon

Gjennom denne risikovurderingen har jeg fått en bedre forståelse av hvilke sikkerhetsutfordringer en nettside kan ha, selv om det er en enkel nettbutikk for et skoleprosjekt.

Jeg har lært at cybersikkerhet handler om mer enn bare å beskytte mot hacking. Det handler også om å sikre data, holde systemer oppdatert, kontrollere tilgang og ha gode rutiner for backup og vedlikehold. Selv små nettsider kan være utsatt for risikoer dersom de ikke er godt sikret.

Jeg har også forstått at det er viktig å tenke sikkerhet fra starten av et prosjekt, og ikke bare som noe man legger til etterpå. Tiltak som HTTPS, oppdateringer, tilgangskontroll og backup er grunnleggende, men veldig viktige for å beskytte både nettsiden og brukerne.

Alt i alt har dette prosjektet gitt meg en mer praktisk forståelse av cybersikkerhet, og hvordan man kan tenke som en utvikler som tar ansvar for sikkerheten i et system.


##  Bekreftelse

Jeg bekrefter at denne risikovurderingen er gjennomført basert på mitt nettsideprosjekt (**Shinystar Stickers**). Jeg har identifisert relevante risikoer, vurdert hvor alvorlige de er, og foreslått tiltak for å redusere eller forhindre dem.

Denne oppgaven viser min forståelse av grunnleggende cybersikkerhet og hvordan man kan tenke forebyggende når man utvikler og publiserer en nettside.

---



<p align="right">
Ujala Tayyab Hussain Kanwal<br>
22.04.2026
</p>




