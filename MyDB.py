import mysql.connector

# Connection parameters
host = "localhost"
user = "root"
password = "Kyanaz25"
database = "WebDB"

# Create a connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL server")
            return connection

    except Exception as e:
        print(f"Error: {str(e)}")
        return None
#_______________________________________________________________________

# Define a function to delete a user by name
def delete_user_by_name(connection, cursor, name):
    try:
        delete_query_name = "DELETE FROM Users WHERE Name = %s"
        cursor.execute(delete_query_name, (name,))
        connection.commit()
        print("Changes saved successfully")

    except Exception as e:
        print(f"Error: {str(e)}")
#_______________________________________________________________________

# Define a function to delete a user by ID
def delete_user_by_id(connection, cursor, id):
    try:
        delete_query_id = "DELETE FROM Users WHERE ID = %s"
        cursor.execute(delete_query_id, (id,))
        connection.commit()
        print("Changes saved successfully")

    except Exception as e:
        print(f"Error: {str(e)}")
#_______________________________________________________________________

# Define a function to print the contents of a table
def print_table(connection, cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")

        # Get column names from the cursor's description
        column_names = [desc[0] for desc in cursor.description]

        # Print the column names (header)
        print("Table Header:")
        for column_name in column_names:
            print(column_name, end=" ")
        print()

        # Fetch and print results
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(f"Error: {str(e)}")
#_______________________________________________________________________

# Define a function to add a new user
def add_user(connection, cursor, name, email):
    try:
        # Insert a new user into the Users table
        insert_query = "INSERT INTO Users (Name, Email) VALUES (%s, %s)"
        user_data = (name, email)
        cursor.execute(insert_query, user_data)
        connection.commit()
        print(f"User {name} added successfully")

    except Exception as e:
        print(f"Error: {str(e)}")
#_______________________________________________________________________

# Define a function to authenticate a user
def authenticate_user(connection, cursor, username, password):
    try:
        # Query the database for the user's credentials
        select_query = "SELECT * FROM Users WHERE Name = %s AND Password = %s"
        user_data = (username, password)
        cursor.execute(select_query, user_data)

        # Fetch the user data (if found)
        user = cursor.fetchone()

        if user:
            print(f"Authentication successful for user: {user[1]}")
            return True
        else:
            print("Authentication failed. Invalid username or password.")
            return False

    except Exception as e:
        print(f"Error: {str(e)}")
        return False
#_______________________________________________________________________

# Create a connection and cursor
connection = create_connection()
if connection:
    cursor = connection.cursor()

    # Example usage of functions
    delete_user_by_name(connection, cursor, 'John Doe')
    delete_user_by_id(connection, cursor, 123)
    print_table(connection, cursor, 'Users')

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed")
#_______________________________________________________________________

