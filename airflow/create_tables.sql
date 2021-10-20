CREATE TABLE public.visa (
    admnum numeric(18,0) PRIMARY KEY,
    visapost varchar(256),
    visatype varchar(256),
    entdepa varchar(256),
    entdepd varchar(256),
    entdepu varchar(256)
);

CREATE TABLE public.flights (
    fltno varchar(256) PRIMARY KEY,
    airline varchar(256),
    i94port varchar(256),
    arrdate numeric(18,0)
);

CREATE TABLE public.newcomers (
    cicid numeric(18,0) PRIMARY KEY,
    gender varchar(32),
    biryear numeric(18,0),
    i94cit numeric(18,0),
    i94addr varchar(256),
    admnum numeric(18,0) NOT NULL,
    FOREIGN KEY (admnum) REFERENCES visa(admnum),
    fltno varchar(256) NOT NULL,
    FOREIGN KEY (fltno) REFERENCES flights(fltno)
);

CREATE TABLE public.cities (
    city varchar(256) PRIMARY KEY,
    total_population varchar(256),
    male_population varchar(256),
    female_population varchar(256),
    foreign_born varchar(256)
);

CREATE TABLE public.airports (
    ident varchar(256) PRIMARY KEY,
    type varchar(256),
    name varchar(256),
    municipality varchar(256),
    coordinates varchar(256)
);

CREATE TABLE public.entries (
    cicid numeric(18,0) NOT NULL,
    FOREIGN KEY (cicid) REFERENCES newcomers(cicid), 
    city varchar(256) NOT NULL,
    FOREIGN KEY (City) REFERENCES cities(City),
    ident varchar(256) NOT NULL,
    FOREIGN KEY (ident) REFERENCES airports(ident),
    count_immigration numeric(18,0),
    count_cities numeric(18,0)
);

CREATE TABLE public.staging_immigration (
	id numeric(18,0),
    cicid numeric(18,0),
    i94yr numeric(18,0),
    i94mon numeric(18,0),
    i94cit numeric(18,0),
    i94res numeric(18,0),
    i94port varchar(256),
    arrdate numeric(18,0),
    i94mode numeric(18,0),
    i94addr varchar(256),
    depdate numeric(18,0),
    i94bir numeric(18,0),
    i94visa numeric(18,0),
    count_immigration numeric(18,0), 
    dtadfile varchar(256),
    visapost varchar(256),
    occup varchar(256),
    entdepa varchar(256),
    entdepd varchar(256),
    entdepu varchar(256),
    matflag varchar(256),
    biryear numeric(18,0),
    dtaddto varchar(256),
    gender varchar(256),
    insnum varchar(256),
    airline varchar(256),
    admnum numeric(18,0),
    fltno varchar(256),
    visatype varchar(256)
);

CREATE TABLE public.staging_demographics (
    city varchar(256),
    state varchar(256),
    median_age varchar(256),
    male_population varchar(256),
    female_population varchar(256),
    total_population varchar(256),
    number_of_veterans varchar(256),
    foreign_born varchar(256),
    average_household_size varchar(256),
    state_code varchar(256),
    race varchar(256),
    count_cities varchar(256)
);

CREATE TABLE public.staging_airports (
	ident varchar(256),
	type varchar(256),
	name varchar(256),
	elevation_ft varchar(256),
	continent varchar(256),
	iso_country varchar(256),
	iso_region varchar(256),
	municipality varchar(256),
	gps_code varchar(256),
	iata_code varchar(256),
	local_code varchar(256),
	coordinates varchar(256)
);
