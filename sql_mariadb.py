import mariadb
try:
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="localhost",
        database="test_db")
except mariadb.Error as e:
    print(f'Connection to DB not successful! {e}')


select_mri_query = """
SELECT COUNT(*) FROM Action
INNER JOIN ActionType ON Action.action_type = ActionType.id
WHERE ActionType.name == 'МРТ' AND YEAR(Action.beg_date) == '2020' AND 
YEAR(Action.end_date) == '2020';
"""

add_column_query = """
ALTER TABLE Client ADD gender VARCHAR(1);
"""

select_gender_mri_query = """
SELECT COUNT(Client.gender) FROM Action 
INNER JOIN ActionType ON Action.action_type = ActionType.id 
INNER JOIN Event ON Action.event_id = Event.id 
INNER JOIN Client ON Event.client_id = Client.id 
WHERE ActionType.name == 'МРТ' AND 
YEAR(Action.beg_date) == '2020' AND 
YEAR(Action.end_date) == '2020' 
GROUP BY Client.gender;
"""

create_organisation_query = """
CREATE TABLE Organisation (
id INT NOT NULL,
name VARCHAR(255),
inn VARCHAR(255),
address VARCHAR(255),
phone VARCHAR(255),
insurance TINYINT(1),
PRIMARY KEY (id)
);
"""

add_foreign_key_query = """
ALTER TABLE Contracts ADD FOREIGN KEY (payer_id) REFERENCES Organisation(id);
"""
