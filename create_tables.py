import sqlite3


conn = sqlite3.connect("files/db_transport_planner.db")
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS tpp_table
                                        (
                                        loading_id TEXT,
                                        year INTEGER,
                                        week INTEGER,
                                        date INTEGER,
                                        sequence_in_loading INTEGER,
                                        loading_type TEXT,
                                        loading_time INTEGER,
                                        store_number INTEGER,
                                        store_name TEXT,
                                        delivery_time INTEGER,
                                        transport_company TEXT,
                                        transport_mode TEXT
                                        )""")

curs.execute("""CREATE TABLE IF NOT EXISTS stores_list
                                        (
                                        store_number TEXT,
                                        store_name TEXT,
                                        store_name_number TEXT
                                        )""")

curs.execute("CREATE TABLE IF NOT EXISTS days (day TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS sequence_in_loading (sequence INTEGER)")
curs.execute("CREATE TABLE IF NOT EXISTS loading_types (loading_type TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS transport_modes (transport_mode TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS transport_companies (company_name TEXT)")

curs.execute("""INSERT INTO stores_list (store_name, store_number) VALUES
        ('Alexandrium', '2093'),
        ('Alkmaar', '1570'),
        ('Amsterdam Arena', '0256'),
        ('Amsterdam Noord', '2226'),
        ('Apeldoorn', '0896'),
        ('Aplerbeck', '0085'),
        ('Arnhem', '1089'),
        ('Bad Oeynhausen', '2247'),
        ('Berlin Alexanderplatz', '0980'),
        ('Berlin Eiche', '2024'),
        ('Berlin Gesundbrunnen', '2248'),
        ('Berlin Gropius Passagen', '2242'),
        ('Berlin Hauptbahnhof', '2061'),
        ('Berlin Schlossstrasse', '1168'),
        ('Berlin Schoneweide', '1068'),
        ('Berlin Wilmersdorfer Arcaden', '2244'),
        ('Bielefeld', '0645'),
        ('Bielefeld-City', '2063'),
        ('Braunschweig', '2069'),
        ('Bremen Waterfront', '2249'),
        ('Bremerhaven', '0509'),
        ('Chemnitz', '0827'),
        ('Den Haag', '1186'),
        ('Dessau', '0725'),
        ('Dodenhof Posthausen', '2065'),
        ('Dortmund Kampstrasse', '2060'),
        ('Dortmund Kley', '0056'),
        ('Dusseldorf', '1573'),
        ('Enschede', '2092'),
        ('Essen', '0728'),
        ('Groningen', '2224'),
        ('Hagen', '0726'),
        ('Hamburg Harburg', '2057'),
        ('Hamburg Langenhorn', '2091'),
        ('Hamburg Wandsbek', '1431'),
        ('Hannover Laatzen', '0776'),
        ('Herne', '0273'),
        ('Huckelhoven', '1069'),
        ('Kerkrade', '0346'),
        ('Kiel', '2258'),
        ('Kiel City', '2259'),
        ('Kinkerstraat', '2227'),
        ('Koln Chorweiler', '2240'),
        ('Koln Marsdorf', '1565'),
        ('Koln-Dumont Carre', '2071'),
        ('Leeuwarden', '0897'),
        ('Leipzig Nova Eventis', '2241'),
        ('Leipzig Paunsdorf', '1141'),
        ('Leipzig Petersbogen', '2054'),
        ('Lubeck', '1358'),
        ('Magdeburg', '2067'),
        ('Neuss', '2072'),
        ('Nijmegen', '2225'),
        ('Oldenburg', '1518'),
        ('Rheine', '1567'),
        ('Roermond', '2094'),
        ('Rotterdam', '1161'),
        ('Utrecht The Wall', '2095'),
        ('Vredenburg', '2096'),
        ('Wuppertal', '1596')
        """)

curs.execute("""INSERT INTO days (day) VALUES ('Monday'), ('Tuesday'), ('Wednesday'),
             ('Thursday'), ('Friday'), ('Saturday'), ('Sunday')""")
curs.execute("INSERT INTO sequence_in_loading (sequence) VALUES (0), (1), (2) ")
curs.execute("INSERT INTO loading_types (loading_type) VALUES ('Solo'), ('Co'), ('Tri') ")
curs.execute("INSERT INTO transport_modes (transport_mode) VALUES ('Trailer'), ('20t'), ('12t'), ('7.5t'), ('WB')")
curs.execute("""INSERT INTO transport_companies (company_name) VALUES
           ('Vehar'), ('Nosta'), ('ELS'), ('DHL Berlin'), ('DHL'),
           ('Hendricks'), ('Freight'), ('Duwensee'), ('Other')""")

conn.commit()
curs.close()
conn.close()