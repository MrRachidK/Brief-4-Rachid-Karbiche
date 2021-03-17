#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Function which save our data changes in the tables of our database
def save_to_sql(df_to_save, table_name, db_connect):
    """ Function used for Pandas in order to save our data changes from a database in a SQL Database, specifically in a table """
    df_to_save.to_sql(table_name, con=db_connect, if_exists='replace')