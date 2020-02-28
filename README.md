# Orchestime

Orchestime on Tietokantasovellus -harjoitustyökurssin 2020 kevät aikana muodostuva web-sovellus.

## Heroku linkki

Heroku linkki: [Orchestime](https://orchestime.herokuapp.com/)

Testitunnukset Herokuun kirjautumista varten:

username: testikayttaja

password: r5testAilija.Mpw93

## Asennusohjeet

[Asennusohjeet](https://github.com/Robustic/Orchestime/tree/master/documentation/installation.md)

## Käyttöohjeet

[Käyttöohjeet](https://github.com/Robustic/Orchestime/tree/master/documentation/user_instructions.md)

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

## Kokemuksia harjoitustyöstä

Harjoitustyötä oli mukava tehdä. Sitä tehdessä oppi Pythonin ja Flaskin perusteet. Harjoitustyön lopputulos on sellainen, minkälaiseksi sen ennakoin tulevankin. Flaskin hyödyntämisen helppous hiukan yllätti. Toisaalta Pythonin käyttö tuntui Javan ja C++:an käytön jälkeen hankalalta, vaikka sitä pidetäänkin yleisesti helpompana ohjelmointikielenä.
