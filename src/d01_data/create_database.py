#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# We import SQLite3 to create our database
import sqlite3

# We create a connector and a cursor to our database
conn = sqlite3.connect("/home/apprenant/Documents/Brief-4-Rachid-Karbiche/Data/02_intermediate/data_jobs.db")
cur = conn.cursor()

# Creation of the Responses table
cur.execute("""CREATE TABLE IF NOT EXISTS Responses (
                salary_USD VARCHAR(9),
                country VARCHAR,
                postal_code VARCHAR, 
                employment_status VARCHAR,
                job_title VARCHAR,
                same_job_years INT,
                number_of_companies VARCHAR,
                number_people_in_team VARCHAR,
                near_city_population VARCHAR, 
                career_plans VARCHAR,
                gender VARCHAR   
            )""")

# Creation of the Job_Adverts table
cur.execute("""CREATE TABLE IF NOT EXISTS Job_Adverts (
                job_title VARCHAR,
                salary_estimation VARCHAR,
                location VARCHAR
            )""")

