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
