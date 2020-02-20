## Tietokantataulujen luontilausekkeet SQL-tietokantaa varten

### Instrument

  ``` 
CREATE TABLE instrument (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)
  ``` 

### Place

  ``` 
CREATE TABLE place (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	address VARCHAR(144), 
	PRIMARY KEY (id)
)
  ``` 

### Account

  ``` 
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	instrument_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(instrument_id) REFERENCES instrument (id)
)
  ``` 

### Room

  ``` 
CREATE TABLE room (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	place_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(place_id) REFERENCES place (id)
)
  ``` 

### Absence 

  ``` 
CREATE TABLE absence (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(1000), 
	date_start DATETIME NOT NULL, 
	date_end DATETIME NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
  ``` 

### Event

  ``` 
CREATE TABLE event (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(1000), 
	date_start DATETIME NOT NULL, 
	date_end DATETIME NOT NULL, 
	room_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(room_id) REFERENCES room (id)
)
  ``` 

### absence_event -liitostaulu

  ``` 
CREATE TABLE absence_event (
	absence_id INTEGER NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (absence_id, event_id), 
	FOREIGN KEY(absence_id) REFERENCES absence (id), 
	FOREIGN KEY(event_id) REFERENCES event (id)
)
  ``` 
