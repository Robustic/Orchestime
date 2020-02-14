## User storyt

### Account

  * As an user, I can create a new account.

  * As an user, I can log in with my account.

  * As a logged in user, I can change my name.

### Instrument

  * As an user, I can list all instruments as a list.

  * As a logged in user, I can add an instrument to the instrument list.

  * As a logged in user, I can update an instrument name.

  * As a logged in user, I can delete the instrument from the list.

### Absence

  * As an user, I can list all absences as a list.

  * As a logged in user, I can add an absence to the absence list.

  * As a logged in user, I can list all my own absences as a list.

### Event

  * As an user, I can list all events as a list.

  ``` 
           SELECT Event.name as event_name,
             Event.description as event_description,
             Event.date_start as event_date_start,
             Event.date_end as event_date_end,
             Event.id as event_id,
             COUNT(DISTINCT Account.id) as count_names
             FROM Event
             LEFT JOIN absence_event ON Event.id = absence_event.event_id
             LEFT JOIN Absence ON Absence.id = absence_event.absence_id
             LEFT JOIN account ON account.id = Absence.account_id
             GROUP BY Event.id
             ORDER BY event_name;
  ```

  * As a logged in user, I can add an event to the event list.

  * As an user, I can view details of the selected event.

  * As an user, I can list all absences for the selected event as a list.



