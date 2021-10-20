class SqlQueries:
    entries_table_insert = ("""
        SELECT
                imm.cicid,
                dem.city,
                air.ident,
                imm.count_immigration,
                dem.count_cities
            FROM staging_immigration imm, 
            staging_demographics dem, 
            staging_airports air
    """)
                
                
    newcomers_table_insert = ("""
        SELECT distinct cicid, gender, biryear, i94cit, i94addr, admnum, fltno
        FROM staging_immigration
    """)

    visa_table_insert = ("""
        SELECT distinct admnum, visapost, visatype, entdepa, entdepd, entdepu
        FROM staging_immigration
    """)

    flights_table_insert = ("""
        SELECT distinct fltno, airline, i94port, arrdate
        FROM staging_immigration
    """)

    cities_table_insert = ("""
        SELECT distinct city, total_population, male_population, female_population, foreign_born
        FROM staging_demographics
    """)

    airports_table_insert = ("""
        SELECT distinct ident, type, name, municipality, coordinates
        FROM staging_airports
    """)