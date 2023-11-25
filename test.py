import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
    database="dora"
)
mycursor = mydb.cursor()
# id=2
# mycursor.execute(f"SELECT * FROM good_main where id={id}")
# myresult = mycursor.fetchall()
# print(myresult)


# result = "INSERT INTO good_main (id, habits, state) VALUES (%s,%s,%s)" 
# userpass = [(1,"Reading", 0 ),
#             ]
# mycursor.executemany(result, userpass)
# mydb.commit()

# mycursor.execute("SELECT * FROM good_main")
# myresult = mycursor.fetchall()
# print(myresult)

# old_state=0
# new_state=1
# update_row="UPDATE good_main SET state = %s WHERE id = %s"
# mycursor.execute(update_row, (new_state, old_state))
# mydb.commit()


# delrow = 1
# sql = "DELETE FROM good_main WHERE id = %s"
# mycursor.execute(sql, (delrow,))
# mydb.commit()
    

id_value = 2
name_value = "bad"

# Select the row by ID and Name
select_query = "SELECT * FROM good_main WHERE id = %s AND habits = %s"
mycursor.execute(select_query, (id_value, name_value))

# Fetch the selected row
selected_row = mycursor.fetchone()

if selected_row:
    # Display the selected row
    print("Selected Row:", selected_row)

    # Update the status of the selected row
    if selected_row[2] == 0:
        status = 1
    else:
        status = 0
    update_query = f"UPDATE good_main SET state = {status} WHERE id = %s AND habits = %s"
    mycursor.execute(update_query, (id_value, name_value))

    # Commit the changes
    mydb.commit()

    print("Row updated successfully.")
else:
    print("Row not found.")

