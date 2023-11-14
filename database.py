import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Database source code
def createDatabase ():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Request_reason
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description varchar(32)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS User_status
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description varchar(32)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Trouble_ticket_state
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description varchar(16)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Trouble_ticket_type
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description varchar(32)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Document
    (         
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_link varchar(128),
        send_date
        date
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS System_user
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name varchar(16),
        surname varchar(16),
        unit varchar(32),
        job_title varchar(32),
        phone_number varchar(16),
        telegram_link varchar(64),
        is_worker blob,
        fk_status integer,
        FOREIGN KEY(fk_status) REFERENCES User_status(id)
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Trouble_ticket
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creation_date date,
        fk_client integer,
        fk_worker integer,
        fk_trouble_ticket_type integer,
        fk_trouble_ticket_state integer,
        short_description varchar(256),
        FOREIGN KEY(fk_client) REFERENCES System_user(id),
        FOREIGN KEY(fk_worker) REFERENCES System_user(id),
        FOREIGN KEY(fk_trouble_ticket_type) REFERENCES Trouble_ticket_type(id),
        FOREIGN KEY(fk_trouble_ticket_state) REFERENCES Trouble_ticket_state(id)
    );''')
