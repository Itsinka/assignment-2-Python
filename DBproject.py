import psycopg2 as pg
import json


# Connection to DB
try:
    conn = pg.connect(
        host="localhost",
        database="ass2",
        port=5432,
        user="postgres",
        password="Kominam19 "
    )
    cursor = conn.cursor()
    print("Connection established")
    cursor.execute("SELECT VERSION();")
    print(cursor.fetchone())

except Exception as err:
    print("Something went wrong...")
    print(err)


# Returns tables list
def get_tables(curs):
    curs.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    return curs.fetchone()


# Returns table schema
def get_schema(table, curs):
    curs.execute(f"SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = '{table}';")
    return curs.fetchall()


# Prints table content
def display_content(table, curs):
    curs.execute(f"SELECT * FROM {table};")
    contents = curs.fetchall()
    for cont in contents:
        print(cont)


# Creates new row
def create_row(table, curs, con):
    title = input("Enter title: ")
    price = input("Enter price: ")
    address = input("Enter address: ")
    link = f"https://kolesa.kz/{link_id}"

    try:
        curs.execute(f"INSERT INTO offers (title, price, address, link) VALUES ('{title}', '{price}', '{address}', '{link}');")
        con.commit()
        print("Row inserted successfully.")

    except Exception as err:
        con.rollback()  # Rollback changes in case of an error
        print("Error inserting row:")
        print(err)


# Changes existing row by ID
def change_row(table, curs, con):
    id = int(input("Which row do you want to change? "))
    title = input("Enter title: ")
    price = input("Enter price: ")
    address = input("Enter address: ")
    link = f"https://kolesa.kz/{link_id}"

    try:
        curs.execute(f"UPDATE offers SET title = '{title}', price = '{price}', address = '{address}',  link = '{link}' WHERE id = {id};")
        con.commit()
        print("Row updated successfully.")

    except Exception as err:
        con.rollback()  # Rollback changes in case of an error
        print("Error updating row:")
        print(err)


# Deletes existing row by id
def delete_row(table, curs, con):
    id = int(input("Which row do you want to delete? "))

    try:
        curs.execute(f"DELETE FROM offers WHERE id = {id};")
        con.commit()
        print("Row deleted successfully.")

    except Exception as err:
        con.rollback()  # Rollback changes in case of an error
        print("Error deleting row:")
        print(err)


# inserting data from json to table
def load_json(table, json_file, curs, con):
    with open(json_file, 'r') as data:
        extracted_data = json.load(data)
        for item in extracted_data:
            try:
                curs.execute(f"""
                INSERT INTO offers (title, price, address, link)
                VALUES ('{item["title"]}', '{item["price"]}', '{item["address"]}', '{item["id"]}', '{item["link"]}');
                """)
                con.commit()
                print("Row inserted successfully.")

            except Exception as err:
                con.rollback()  # Rollback changes in case of an error
                print("Error inserting JSON:")
                print(err)
                break