GET_ALL_ENTRIES = """
                    SELECT
                        *
                    FROM
                        entries;
                """

GET_SPECIFIC_ENTRY = """
                        SELECT 
                            image_path 
                        FROM 
                            entries 
                        WHERE 
                            body_part='{body_part}' and 
                            patient_username='{patient_username}' and 
                            date='{date}';
                    """

GET_GRAPH_DATA = """
                    SELECT 
                        date, disorder_percentage 
                    FROM
                        entries 
                    WHERE 
                        body_part='{body_part}' and 
                        patient_username='{patient_username}';
                """


INSERT_DUMMY_ENTRIES = """
                INSERT OR IGNORE INTO 
                    entries (patient_username, body_part, date, disorder_percentage)
                VALUES
                    ('Chris', 'Hand', '10-20-2018', 57),
                    ('Chris', 'Hand', '11-20-2018', 55),
                    ('Chris', 'Hand', '11-28-2018', 50),
                    ('Chris', 'Hand', '12-29-2018', 47),
                    ('Chris', 'Hand', '01-21-2019', 30),
                    ('Chris', 'Hand', '03-02-2019', 21),
                    ('Chris', 'Hand', '04-27-2019', 15),
                    ('Chris', 'Face', '09-19-2018', 38),
                    ('Chris', 'Face', '10-20-2018', 34),
                    ('Chris', 'Face', '11-20-2018', 33),
                    ('Chris', 'Face', '11-28-2018', 33),
                    ('Chris', 'Face', '12-29-2018', 33),
                    ('Chris', 'Face', '01-21-2019', 32),
                    ('Chris', 'Face', '03-02-2019', 31),
                    ('Chris', 'Face', '04-27-2019', 30),
                    ('Chris', 'Leg', '09-19-2018', 47),
                    ('Chris', 'Leg', '10-20-2018', 47),
                    ('Chris', 'Leg', '11-20-2018', 45),
                    ('Chris', 'Leg', '11-28-2018', 45),
                    ('Chris', 'Leg', '12-29-2018', 42),
                    ('Chris', 'Leg', '01-21-2019', 41),
                    ('Chris', 'Leg', '03-02-2019', 41),
                    ('Chris', 'Leg', '04-27-2019', 40)
            """
            
CREATE_TABLE = """
                CREATE TABLE IF NOT EXISTS 
                    entries
                    (
                        patient_username TEXT,
                        body_part TEXT,
                        date TEXT,
                        disorder_percentage INTEGER,
                        UNIQUE(patient_username, body_part, date, disorder_percentage)
                    );
            """
            
INSERT_DATA = """
                INSERT OR IGNORE INTO 
                    entries (patient_username, body_part, date, disorder_percentage)
                VALUES
                    ('{username}', '{body_part}', '{date}', {disorder_percentage}),
                
"""