# Orchestime

Orchestime on Tietokantasovellus -harjoitustyökurssin 2020 kevät aikana muodostuva web-sovellus.

## Aihekuvaus

Sovelluksen tarkoituksena on toimia orkesterin tapahtumien vuorovaikutteisena kalenterina. Sovelluksen avulla voidaan luoda, lukea, muokata ja poistaa orkesterin toimintaan liittyviä tapahtumia.

Jokaiseen tapahtumaan liittyy huone, joka puolestaan liittyy johonkin paikkaan.

Toisaalta tapahtumiin liittyy henkilöitä (soittajia), jotka voivat ilmoittaa itsensä poissaolevaksi. Jokainen henkilö soittaa jotakin instrumenttia.

Tietokantataulujen Event (tapahtuma) ja Person (henkilö) välillä on monesta moneen yhteys, joten niiden välillä on liitostaulu.

Kullekin tapahtumalle voidaan suorittaa haku, jossa lasketaan kuinka monta kunkin instrumentin soittajaa on poissa kyseisestä tapahtumasta.

Lisäksi voidaan laskea kunkin soittajan läsnäoloprosentti kaikista tapahtumista tai tietyllä aikavälillä.

<img src="https://github.com/Robustic/Orchestime/blob/master/documentation/pictures/DatabaseChart.png" width="1410">

**Kuva 1.** *Tietokantakaavio.*
