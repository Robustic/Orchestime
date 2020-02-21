## User storyt ja esimerkki SQL-lausekkeet

### Account

  * As an user, I can create a new account.

    ``` 
        INSERT INTO Account (
            date_created, 
            date_modified, 
            name, 
            username, 
            password, 
            instrument_id
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'New Name', 
            'newusername', 
            'newpassword', 
            Null
        );
    ``` 

  * As an user, I can log in with my account.

    ```
        SELECT * FROM Account 
        WHERE Account.username = 'newusername'
        LIMIT 1 OFFSET 0;
    ```

  * As a logged in user, I can change my name and instrument.

    ```
        UPDATE Account 
        SET 
            date_modified=CURRENT_TIMESTAMP, 
            name='Other Name', 
            instrument_id=2 
        WHERE Account.id = 1;
    ```

### Instrument

  * As an user, I can list all instruments as a list.

    ```
        SELECT * FROM Instrument
        ORDER BY Instrument.name
        LIMIT 5 OFFSET 0;
    ```

  * As a logged in user, I can add an instrument to the instrument list.

    ```
        INSERT INTO Instrument (
            date_created, 
            date_modified, 
            name
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'Tubaaa'
        );
    ```

  * As a logged in user, I can update an instrument name.

    ```
        UPDATE Instrument 
        SET 
            date_modified=CURRENT_TIMESTAMP, 
            name='Tuba'
        WHERE Instrument.id = 1;
    ```

  * As a logged in user, I can delete the instrument from the list.

    ```
        DELETE FROM Instrument WHERE Instrument.id = 1;
    ```

### Absence

  * As an user, I can list all absences as a list.

    ```
        SELECT * FROM Absence 
        LEFT OUTER JOIN Account ON Account.id = Absence.account_id 
        ORDER BY Account.name, Absence.date_start, Absence.date_end
        LIMIT 5 OFFSET 0;
    ```

  * As a logged in user, I can add an absence to the absence list.

    ```
        INSERT INTO Absence (
            date_created, 
            date_modified, 
            name, 
            description, 
            date_start, 
            date_end, 
            account_id
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'Header of the new absent', 
            'Description of the new absent', 
            '2020-02-23', 
            '2020-02-23', 
            1
        );
    ```

  * As a logged in user, I can list all my absences as a list which are at same time as some orchestra event.

    ```
        SELECT 
            Event.name AS event_name, 
            Event.date_start AS event_date_start, 
            Event.date_end AS event_date_end, 
            Absence.name AS absence_name, 
            Absence.description AS absence_description, 
            Absence.date_start AS absence_date_start, 
            Absence.date_end AS absence_date_end 
        FROM Account 
        JOIN Absence ON Account.id = Absence.account_id 
        JOIN absence_event ON Absence.id = absence_event.absence_id 
        JOIN Event ON Event.id = absence_event.event_id 
        WHERE (Account.id = 1) 
        ORDER BY event_date_start, event_date_end, event_name, absence_date_start, absence_date_end 
        LIMIT 5 OFFSET 0;
    ```

  * As an logged in user, I can see my participation percent.

    ```
        SELECT 
            100 - COUNT(DISTINCT Event.id) * 100 / (SELECT COUNT(*) FROM Event) AS count_events 
        FROM Account 
        LEFT JOIN Absence ON Account.id = Absence.account_id 
        LEFT JOIN absence_event ON Absence.id = absence_event.absence_id 
        LEFT JOIN Event ON Event.id = absence_event.event_id 
        WHERE (Account.id = 1) 
        GROUP BY Account.id;
    ```

### Event

  * As an user, I can list all events as a list.

    ``` 
        SELECT 
            Event.name AS event_name, 
            Event.description AS event_description, 
            Event.date_start AS event_date_start, 
            Event.date_end AS event_date_end, 
            Event.id AS event_id, 
            Room.name AS room_name, 
            Place.name AS place_name, 
            COUNT(DISTINCT Account.id) as count_names 
        FROM Event 
        LEFT JOIN absence_event ON Event.id = absence_event.event_id 
        LEFT JOIN Absence ON Absence.id = absence_event.absence_id 
        LEFT JOIN Account ON Account.id = Absence.account_id 
        LEFT JOIN Room ON Room.id = Event.room_id 
        LEFT JOIN Place ON Place.id = Room.place_id 
        GROUP BY Event.id, Room.name, Place.name 
        ORDER BY event_date_start, event_date_end, event_name 
        LIMIT 5 OFFSET 0;
    ```

  * As a logged in user, I can add an event to the event list.

    ```
        INSERT INTO Event (
            date_created, 
            date_modified, 
            name, 
            description, 
            date_start, 
            date_end, 
            room_id
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'Header of the new event', 
            'Description of the new event', 
            '2020-02-23', 
            '2020-02-23',
            1
        );
    ```

  * As an user, I can view details of the selected event.

    ```
        SELECT * FROM Event 
        LEFT OUTER JOIN Room ON Room.id = Event.room_id 
        LEFT OUTER JOIN Place ON Place.id = Room.place_id 
        WHERE Event.id = 1
        LIMIT 5 OFFSET 0;
    ```

  * As an user, I can list all absences for the selected event as a list.

    ```
        SELECT 
            Account.name AS account_name,
            Absence.name AS absence_name,
            Absence.description AS absence_description,
            Absence.date_start AS absence_date_start,
            Absence.date_end AS absence_date_end
        FROM Event
        LEFT JOIN absence_event ON Event.id = absence_event.event_id
        LEFT JOIN Absence ON Absence.id = absence_event.absence_id
        LEFT JOIN Account ON Account.id = Absence.account_id
        WHERE (Event.id = 1)
        ORDER BY account_name, absence_date_start, absence_date_end
        LIMIT 5 OFFSET 0;
    ```

### Place

  * As an user, I can list all places as a list.

    ```
        SELECT * FROM Place
        ORDER BY Place.name
        LIMIT 5 OFFSET 0;
    ```
    
  * As a logged in user, I can add a place to the place list.

    ```
        INSERT INTO Place (
            date_created, 
            date_modified, 
            name,
            address
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'Pace',
            'Paceroad 42'
        );
    ```

  * As a logged in user, I can update a place name or an address.

    ```
        UPDATE Place 
        SET 
            date_modified=CURRENT_TIMESTAMP, 
            name='Place',
            address='Placeroad 42'
        WHERE Place.id = 1;
    ```

  * As a logged in user, I can delete the place from the list.

    ```
        DELETE FROM Place WHERE Place.id = 1;
    ```

### Room

  * As an user, I can list all rooms as a list.

    ```
        SELECT * FROM Room
        LEFT OUTER JOIN Place ON Place.id = Room.place_id
        ORDER BY Place.name, Room.name
        LIMIT 5 OFFSET 0;
    ```
    
  * As a logged in user, I can add a room to the room list.

    ```
        INSERT INTO Room (
            date_created, 
            date_modified, 
            name,
            place_id
        ) VALUES (
            CURRENT_TIMESTAMP, 
            CURRENT_TIMESTAMP, 
            'Rome',
            1
        );
    ```

  * As a logged in user, I can update a room name and a place.

    ```
        UPDATE Room 
        SET 
            date_modified=CURRENT_TIMESTAMP, 
            name='Room',
            place_id=2
        WHERE Room.id = 1;
    ```

  * As a logged in user, I can delete the room from the list.

    ```
        DELETE FROM Room WHERE Room.id = 1;
    ```
    
