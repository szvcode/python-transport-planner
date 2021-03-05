import sqlite3


conn = sqlite3.connect("files/db_transport_planner.db")
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS transport_table
                                        (
                                        rowid INTEGER PRIMARY KEY,
                                        loading_id TEXT,
                                        year INTEGER,
                                        week INTEGER,
                                        date INTEGER,
                                        day TEXT,
                                        multi_id INTEGER,
                                        sid INTEGER,
                                        sequence INTEGER,
                                        loading_type TEXT,
                                        loading_time INTEGER,
                                        store_number INTEGER,
                                        store_name TEXT,
                                        delivery_day TEXT,
                                        delivery_time INTEGER,
                                        transport_company TEXT,
                                        transport_mode TEXT,
                                        comment TEXT
                                        )""")

                                
curs.execute("""CREATE TABLE IF NOT EXISTS days
                                        (
                                        day TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS delivery_day
                                        (
                                        d_day TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS loading_types
                                        (
                                        loading_type TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS multi_ids
                                        (
                                        multi_id TEXT,
                                        store_1 TEXT,
                                        store_2 TEXT,
                                        store_3 TEXT,
                                        store_4 TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS sequence
                                        (
                                        seq INTEGER
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS store_in_day
                                        (
                                        sid INTEGER
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS stores
                                        (
                                        store_number TEXT,
                                        store_name TEXT,
                                        default_transport_company TEXT,
                                        default_multi_id TEXT,
                                        default_loading_type TEXT,
                                        default_transport_mode TEXT,
                                        default_sequence INTEGER,
                                        default_sid INTEGER,
                                        default_loading_time TEXT,
                                        default_delivery_day TEXT,
                                        default_delivery_time TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS time_values
                                        (
                                        time_value TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS transport_companies
                                        (
                                        transport_company TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS transport_modes
                                        (
                                        transport_mode TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS weeks
                                        (
                                        week INTEGER
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS years
                                        (
                                        year INTEGER
                                        )""")

curs.execute("""INSERT INTO stores (store_name, store_number, default_transport_company, default_multi_id,
             default_loading_type, default_sequence, default_loading_time, default_sid, default_transport_mode, 
             default_delivery_day, default_delivery_time) VALUES
        ('Stuttgart', '1001', 'Company South', '201', 'Co', '1', '06:00', '1', '40t', 'AA', '12:00'),
        ('München', '1002', 'Company South', '201', 'Co', '2', '06:00', '1', '40t', 'AA', '10:00'),
        ('Berlin', '1003', 'Company East', '103', 'Solo', '1', '08:00', '1', '40t', 'AA', '12:00'),
        ('Potsdam', '1004', 'Company East', '104', 'Solo', '1', '09:00', '1', '40t', 'AA', '13:00'),
        ('Bremen', '1005', 'Company West', '301', 'Tri', '1', '10:00', '1', '40t', 'AA', '18:00'),
        ('Hamburg', '1006', 'Company North', '301', 'Tri', '2', '10:00', '1', '40t', 'AA', '16:00'),
        ('Wiesbaden', '1007', 'Company West', '107', 'Solo', '1', '12:00', '1', '40t', 'AA', '16:00'),
        ('Hannover', '1008', 'Company West', '108', 'Solo', '1', '15:00', '1', '40t', 'AB', '08:00'),
        ('Schwerin', '1009', 'Company North', '109', 'Solo', '1', '16:00', '1', '40t', 'AB', '08:00'),
        ('Düsseldorf', '1010', 'Company West', '110', 'Solo', '1', '17:00', '1', '40t', 'AB', '08:00'),
        ('Mainz', '1011', 'Company South', '202', 'Co', '1', '18:00', '1', '40t', 'AB', '12:00'),
        ('Saarbrücken', '1012', 'Company South', '202', 'Co', '2', '18:00', '1', '40t', 'AB', '08:00'),
        ('Dresden', '1013', 'Company East', '113', 'Solo', '1', '19:00', '1', '40t', 'AB', '08:00'),
        ('Magdeburg', '1014', 'Company East', '114', 'Solo', '1', '11:00', '1', '40t', 'AA', '15:00'),
        ('Kiel', '1015', 'Company North', '301', 'Tri', '3', '10:00', '1', '40t', 'AA', '14:00'),
        ('Erfurt', '1016', 'Company East', '116', 'Solo', '1', '08:00', '1', '40t', 'AA', '12:00')
        """)

curs.execute("""INSERT INTO days (day) VALUES ('Mon'), ('Tue'), ('Wed'),
             ('Thu'), ('Fri'), ('Sat'), ('Sun')""")

curs.execute("INSERT INTO sequence (seq) VALUES (1), (2), (3), (4)")

curs.execute("INSERT INTO store_in_day (sid) VALUES (1), (2), (3), (4), (5), (6)")

curs.execute("INSERT INTO loading_types (loading_type) VALUES ('Solo'), ('Co'), ('Tri'), ('Quattro')")

curs.execute("INSERT INTO transport_modes (transport_mode) VALUES ('40t'), ('20t'), ('12t'), ('7.5t'), ('WB')")

curs.execute("""INSERT INTO transport_companies (transport_company) VALUES
           ('Company East'), ('Company West'), ('Company South'), 
           ('Company North'), ('Other')""")

curs.execute("""INSERT INTO weeks (week) VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10),
             (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25), 
             (26), (27), (28), (29), (30), (31), (32), (33), (34), (35), (36), (37), (38), (39), (40), 
             (41), (42), (43), (44), (45), (46), (47), (48), (49), (50), (51), (52), (53)""")

curs.execute("INSERT INTO years (year) VALUES (2020), (2021), (2022)")

curs.execute("""INSERT INTO time_values (time_value) VALUES ('00:00'), ('00:30'), ('01:00'), ('01:30'), 
            ('02:00'), ('02:30'), ('03:00'), ('03:30'), ('04:00'), ('04:30'), ('05:00'), ('05:30'), 
            ('06:00'), ('06:30'), ('07:00'), ('07:30'), ('08:00'), ('08:30'), ('09:00'), ('09:30'), 
            ('10:00'), ('10:30'), ('11:00'), ('11:30'), ('12:00'), ('12:30'), ('13:00'), ('13:30'), 
            ('14:00'), ('14:30'), ('15:00'), ('15:30'), ('16:00'), ('16:30'), ('17:00'), ('17:30'), 
            ('18:00'), ('18:30'), ('19:00'), ('19:30'), ('20:00'), ('20:30'), ('21:00'), ('21:30'), 
            ('22:00'), ('22:30'), ('23:00'), ('23:30')""")

curs.execute("INSERT INTO delivery_day (d_day) VALUES ('AA'), ('AB')")

curs.execute("""INSERT INTO multi_ids (multi_id) VALUES 
            ('101'), ('102'), ('103'), ('104'), ('105'), ('106'), ('107'), ('108'), ('109'), ('110'),
            ('111'), ('112'), ('113'), ('114'), ('115'), ('116'), ('201'), ('202'), ('203'), ('204'), 
            ('205'), ('206'), ('207'), ('208'), ('209'), ('210'), ('301'), ('302'), ('303'), ('304'), 
            ('305'), ('306'), ('307'), ('308'), ('309'), ('310')
             """)

conn.commit()
curs.close()
conn.close()