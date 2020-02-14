# Orchestime

Orchestime on Tietokantasovellus -harjoitustyökurssin 2020 kevät aikana muodostuva web-sovellus.

## Heroku linkki

Heroku linkki: [Orchestime](https://orchestime.herokuapp.com/)

Testitunnukset Herokuun kirjautumista varten:

username: testikayttaja

password: r5testAilija.Mpw93

## Asennusohje paikalliselle koneelle

* Tarkista, että koneellesi on asennettu Python 3

* Kloonaa tämä GitHub-repositorio koneellesi

* Siirry komentorivillä repositoriohakemiston juureen, eli hakemistoon missä näkyy mm. README.md ja requirements.txt tiedostot

* Kirjoita komentoriville `pip install -r requirements.txt`, mikä päivittää projektiin liittyvät riippuvuudet

* Aktivoi virtuaaliympäristö kirjoitamalla komentoriville `source venv/bin/activate`

* Aloita ohjelman suoritus kirjoittamalla komentoriville `python3 run.py`

* Avaa nettiselain ja mene osoitteeseen [http://localhost:5000/](http://localhost:5000/)

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

#### Rekisteröidy

Voit rekisteröityä järjestelmään valitsemalla *Register*

#### Kirjautua

Kun olet rekisteröitynyt, voit kirjautua järjestelmään valitsemalla *Log in*

### Kirjautumisen jälkeen toimivat toiminnot

#### Tietojesi päivittäminen

Voit päivittää nimesi ja instrumenttisi valitsemalla *Update name or instrument of the user*

#### Tapahtuman lisääminen

Voit lisätä uuden tapatuman valitsemalla *Add an event*

#### Poissaolon lisääminen

Voit lisätä uuden poissaolon valitsemalla *Add an absence*

#### Poissaolojesi listaaminen

Voit listata poissaolosi valitsemalla *View my absences*

#### Instrumentin lisääminen

Voit lisätä järjestelmään uuden instrumentin *Add an instrument*

#### Instrumentin päivittäminen

Voit päivittää instrumentin valitsemalla *List instruments* näkymässä *Update instrument*

## User storyt

[User storyt](https://github.com/Robustic/Orchestime/tree/master/documentation/userstories.md)

## Aihekuvaus ja tietokantakaavio

Orchestime -sovelluksen tarkoituksena on toimia orkesterin tapahtumien vuorovaikutteisena kalenterina. Sovelluksen avulla voidaan luoda, lukea, muokata ja poistaa orkesterin toimintaan liittyviä tapahtumia.

Jokaiseen tapahtumaan liittyy huone, joka puolestaan liittyy johonkin paikkaan.

Toisaalta tapahtumiin liittyy henkilöitä (soittajia), jotka voivat ilmoittaa itsensä poissaolevaksi. Jokainen henkilö soittaa jotakin instrumenttia.

Henkilö voi ilmoittautua poissa-olevaksi tietyn mittaiseksi ajaksi. Poissaolojaksolle voi sattua monta tapahtumaa. Toisaalta tapahtumilla voi olla monta poissaoloa, koska useat henkilöt voivat olla poissa.

Tietokantataulujen Event (tapahtuma) ja Absence (poissa-olo) välillä on monesta moneen yhteys, joten niiden välillä on liitostaulu EventAbsence.

Kullekin tapahtumalle voidaan suorittaa haku, jossa lasketaan kuinka monta soittajaa on poissa kyseisestä tapahtumasta.

Lisäksi tulossa on toiminto, jolla voidaan laskea kunkin soittajan läsnäoloprosentti kaikista tapahtumista tai tietyllä aikavälillä.

<img src="https://github.com/Robustic/Orchestime/blob/master/documentation/pictures/DatabaseChart.png" width="1097">

**Kuva 1.** *Tietokantakaavio.*
