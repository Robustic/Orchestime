# Orchestime

Orchestime on Tietokantasovellus -harjoitustyökurssin 2020 kevät aikana muodostuva web-sovellus.

## Heroku linkki

Heroku linkki: [Orchestime](https://orchestime.herokuapp.com/)

Testitunnukset Herokuun kirjautumista varten:

username: testikayttaja

password: r5testAilija.Mpw93

## Asennusohjeet 

### Asennusohjeet paikalliselle koneelle

* Tarkista, että koneellesi on asennettu Python 3, mieluiten versio Python 3.6.9, jolla ohjelman toiminta on testattu. Asenna tarvittaessa tämä ehdotettu versio.

* Kloonaa tämä GitHub-repositorio koneellesi

* Siirry komentorivillä repositoriohakemiston juureen, eli hakemistoon missä näkyy mm. README.md ja requirements.txt tiedostot

* Kirjoita komentoriville `python3 -m venv venv`, joka luo kansioon virtuaaliympäristön

* Aktivoi virtuaaliympäristö kirjoitamalla komentoriville `source venv/bin/activate`

* Kirjoita komentoriville `pip3 install -r requirements.txt`, mikä päivittää projektiin liittyvät riippuvuudet

* Aloita ohjelman suoritus kirjoittamalla komentoriville `python3 run.py`

* Avaa nettiselain ja mene osoitteeseen [http://localhost:5000/](http://localhost:5000/), jolloin sovellus aukeaa nettiselaimeen

* Jos asetat projektille uusia riippuvuuksia, päivitä requirements.txt tiedosto kirjoittamalla komentoriville `pip freeze | grep -v pkg-resources > requirements.txt`, jolloin uudet riippuvuudet määrittyvät requirements.txt tiedostoon

### Asennusohjeet sovelluksen asentamisesta Herokuun

* Avaa tili [Herokuun](https://www.heroku.com)

* Siirry komentorivillä repositoriohakemiston juureen, eli hakemistoon missä näkyy mm. README.md ja requirements.txt tiedostot

* Luo uusi Heroku sovellus kirjoittamalla koneesi terminaalin komentoriville `heroku create`

* Aseta Herokuun ympäristömuuttuja kirjoittamalla koneesi terminaalin komentoriville `heroku config:set HEROKU=1`

* Tarkista, onko Herokussa jo tietokanta olemassa kirjoittamalla koneesi terminaalin komentoriville `heroku pg:psql`. Jos saat vastauksen, joka sisältää kohdan `has no databases`, voit lisätä Herokuun uuden tietokannan.

* Lisää Herokuun uusi tietokanta kirjoittamalla koneesi terminaalin komentoriville `heroku addons:add heroku-postgresql:hobby-dev`

* Varmista, että kaikki muutokset projektiin on kommitoitu ja puske sovellus Herokuun koneesi terminaalin komentoriviltä:

  `git add .`

  `git commit -m "Commitoidaan muutokset"`

  `git push heroku master`

* Voit nyt käynnistää sovelluksen Herokun ilmoittamasta osoitteesta nettiselaimella

## Käyttöohje

Voit käyttää ohjelmaa kirjautumatta tai kirjautumalla. Kirjatuminen tuo käyttäjälle enemmän toimintoja käyttöön.

### Kirjautumatta toimivat toiminnot

#### Listaa tapahtumat

Voit listata järjestelmään kirjatut tapahtumat valitsemalla *List events*

#### Listaa tapahtuman yksityiskohdat

Voit listata järjestelmään kirjatut tiedot tapahtumalle valitsemalla *List events* näkymässä *View event details*

#### Listaa poissaolot

Voit listata järjestelmään kirjatut poissaolot valitsemalla *List absences*

#### Listaa instrumentit

Voit listata järjestelmään kirjatut instrumentit valitsemalla *List instruments*

#### Listaa paikat

Voit listata järjestelmään kirjatut paikat valitsemalla *List places*

#### Listaa huoneet

Voit listata järjestelmään kirjatut huoneet valitsemalla *List rooms*

#### Rekisteröidy

Voit rekisteröityä järjestelmään valitsemalla *Register*

#### Kirjaudu sisään

Kun olet rekisteröitynyt, voit kirjautua järjestelmään valitsemalla *Log in*

### Kirjautumisen jälkeen toimivat toiminnot

#### Uloskirjautuminen

Voit kirjautua ulos järjestelmästä valitsemalla *Log out*

#### Tietojesi päivittäminen

Voit päivittää nimesi ja instrumenttisi valitsemalla *Update name or instrument of the user*

#### Tapahtuman lisääminen

Voit lisätä uuden tapatuman valitsemalla *Add an event*

#### Poissaolon lisääminen

Voit lisätä uuden poissaolon valitsemalla *Add an absence*

#### Poissaolojesi listaaminen

Voit listata poissaolosi valitsemalla *View my absences for the events*

#### Instrumentin lisääminen

Voit lisätä järjestelmään uuden instrumentin valitsemalla *Add an instrument*

#### Instrumentin päivittäminen

Voit päivittää instrumentin tiedot valitsemalla *List instruments* näkymässä *Update instrument*

#### Paikan lisääminen

Voit lisätä järjestelmään uuden paikan valitsemalla *Add a place*

#### Paikan päivittäminen

Voit päivittää paikan tiedot valitsemalla *List places* näkymässä *Update place*

#### Huoneen lisääminen

Voit lisätä järjestelmään uuden huoneen valitsemalla *Add a room*

#### Huoneen päivittäminen

Voit päivittää huoneen tiedot valitsemalla *List rooms* näkymässä *Update room*

## User storyt ja esimerkki SQL-lausekkeet

[User storyt](https://github.com/Robustic/Orchestime/tree/master/documentation/userstories.md)

## Tietokantataulujen luontilausekkeet SQL-tietokantaa varten

[Tietokantataulujen luontilausekkeet](https://github.com/Robustic/Orchestime/tree/master/documentation/create_tables.md)

## Aihekuvaus ja tietokantakaavio

Orchestime -sovelluksen tarkoituksena on toimia orkesterin tapahtumien vuorovaikutteisena kalenterina. Sovelluksen avulla voidaan luoda ja lukea orkesterin toimintaan liittyviä tapahtumia.

Jokaiseen tapahtumaan liittyy huone, joka puolestaan liittyy johonkin paikkaan.

Toisaalta tapahtumiin liittyy henkilöitä (soittajia), jotka voivat ilmoittaa itsensä poissaolevaksi. Jokainen henkilö soittaa jotakin instrumenttia.

Henkilö voi ilmoittautua poissaolevaksi tietyn mittaiseksi ajaksi. Poissaolojaksolle voi sattua monta tapahtumaa. Toisaalta tapahtumilla voi olla monta poissaoloa, koska useat henkilöt voivat olla poissa.

Tietokantataulujen Event (tapahtuma) ja Absence (poissa-olo) välillä on monesta moneen yhteys, joten niiden välillä on liitostaulu AbsenceEvent.

Kullekin tapahtumalle näytetään, kuinka monta soittajaa on poissa kyseisestä tapahtumasta.

Lisäksi jokainen soittaja voi tarkistaa läsnäoloprosenttinsa huomioiden kaikki tapahtumat.

Kurssin aikana saatiin valmiiksi kaikki tietokantataulut ja tarpeellisimmat haut.

<img src="https://github.com/Robustic/Orchestime/blob/master/documentation/pictures/DatabaseChart.png" width="1102">

**Kuva 1.** *Tietokantakaavio.*

## Jatkokehitysideat

* Sovelluksen jatkokehitystä varten tulisi kirjoittaa testit tähän mennessä luodulle toiminnallisuudelle

* Tapahtuman tietojen muokkaamismahdollisuus

* Tapahtuman poistomahdollisuus

* Poissaolon tietojen muokkaamismahdollisuus

* Poissaolon poistomahdollisuus

* Päivämäärän tarkkuudella tapahtuvan tapahtumien ja poissaolojen tarkastelun tarkentaminen minuuttitarkkuuteen
