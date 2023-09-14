import mysql.connector

# Connection parameters
host = "localhost"  # Replace with your MySQL server's hostname or IP address
user = "root"
password = "Kyanaz25"
database = "WebDB"

# Create a connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor
        cursor = connection.cursor()

        # Drop the Users table if it exists
        '''
        cursor.execute("DROP TABLE IF EXISTS Users")
        '''
        
        # Define the CREATE TABLE statement with an auto-incrementing UserID
        '''
        create_table_query = """
        CREATE TABLE Users (
            UserID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(25) NOT NULL,
            Password VARCHAR(25) NOT NULL
        )
        """

        # Execute the CREATE TABLE statement
        cursor.execute(create_table_query)
        print("Users table created successfully.")
        '''

        # Insert a new user into the Users table (UserID will be generated automatically)
        insert_query = "INSERT INTO Users (Name, Password) VALUES (%s, %s)"
        user_data = ("Kyan", "123")  # Replace with your user data
        cursor.execute(insert_query, user_data)

        # Commit the transaction (save the changes to the database)
        connection.commit()

        # Select and print all users in the Users table
        cursor.execute("SELECT * FROM Users")
        for user in cursor.fetchall():
            print(f"UserID: {user[0]}, Name: {user[1]}, Password: {user[2]}")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")
