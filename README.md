# Orchestime

Orchestime on Tietokantasovellus -harjoitustyökurssin 2020 kevät aikana muodostuva web-sovellus.

## Heroku linkki

Heroku linkki: [Orchestime](https://orchestime.herokuapp.com/)

Testitunnukset Herokuun kirjautumista varten:

username: testikayttaja

password: r5testAilija.Mpw93

## User storyt

[User storyt](https://github.com/Robustic/Orchestime/tree/master/documentation/userstories.md)

## Aihekuvaus ja tietokantakaavio

Orchestime -sovelluksen tarkoituksena on toimia orkesterin tapahtumien vuorovaikutteisena kalenterina. Sovelluksen avulla voidaan luoda, lukea, muokata ja poistaa orkesterin toimintaan liittyviä tapahtumia.

Jokaiseen tapahtumaan liittyy huone, joka puolestaan liittyy johonkin paikkaan.

Toisaalta tapahtumiin liittyy henkilöitä (soittajia), jotka voivat ilmoittaa itsensä poissaolevaksi. Jokainen henkilö soittaa jotakin instrumenttia.

Henkilö voi ilmoittautua poissa-olevaksi tietyn mittaiseksi ajaksi. Poissaolojaksolle voi sattua monta tapahtumaa. Toisaalta tapahtumilla voi olla monta poissaoloa, koska useat henkilöt voivat olla poissa.

Tietokantataulujen Event (tapahtuma) ja Absence (poissa-olo) välillä on monesta moneen yhteys, joten niiden välillä on liitostaulu EventAbsence.

Kullekin tapahtumalle voidaan suorittaa haku, jossa lasketaan kuinka monta kunkin instrumentin soittajaa on poissa kyseisestä tapahtumasta.

Lisäksi voidaan laskea kunkin soittajan läsnäoloprosentti kaikista tapahtumista tai tietyllä aikavälillä.

<img src="https://github.com/Robustic/Orchestime/blob/master/documentation/pictures/DatabaseChart.png" width="1097">

**Kuva 1.** *Tietokantakaavio.*
