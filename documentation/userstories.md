## User storyt

### Account

  * As an user, I can create a new account.

  * As an user, I can log in with my account.

  * As a logged in user, I can change my name.

### Instrument

  * As an user, I can list all instruments as a list.

  ``` SELECT * FROM  instrument;```

  * As a logged in user, I can add an instrument to the instrument list.

  * As a logged in user, I can update an instrument name.

  * As a logged in user, I can delete the instrument from the list.

### Absence

  * As an user, I can list all absences as a list.

  * As a logged in user, I can add an absence to the absence list.

### Event

  * As an user, I can list all events as a list.

  * As a logged in user, I can add an event to the event list.

  * As an user, I can view details of the selected event.

  * As an user, I can list all absences for the selected event as a list.

  ``` 
             SELECT account.name as account_name, 
             Absence.name as absence_name, 
             Absence.description as absence_description, 
             Absence.date_start as absence_date_start, 
             Absence.date_end as absence_date_end 
             FROM Event 
             LEFT JOIN absence_event ON Event.id = absence_event.event_id 
             LEFT JOIN Absence ON Absence.id = absence_event.absence_id 
             LEFT JOIN account ON account.id = Absence.account_id 
             WHERE (Event.id = 4);
  ```

