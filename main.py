import sqlite3
from contextlib import closing
from function import query_executor, query_responder
import os

db_path = "test.db"

# Check if the database file needs to be initialized
db_exists = os.path.exists(db_path)

try:
    with closing(sqlite3.connect(db_path)) as db_con:
        db_con.row_factory = sqlite3.Row  # Enable dictionary-like row access
        with closing(db_con.cursor()) as cursor:
            # Create and populate the demo table if it doesn't exist
            if not db_exists:
                print("Initializing database with demo table...")
                try:
                    # Create the demo table
                    cursor.execute('''
                        CREATE TABLE demo (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER
                        )
                    ''')

                    # Insert sample data
                    sample_data = [
                        (1, "Alice", 25),
                        (2, "Bob", 30),
                        (3, "Charlie", 22),
                        (10, "David", 35),
                        (15, "Eve", 28),
                        (16, "Frank", 42),
                        (17, "Grace", 31),
                        (20, "Hannah", 29)
                    ]

                    cursor.executemany("INSERT INTO demo VALUES (?, ?, ?)", sample_data)
                    db_con.commit()
                    print("Sample data inserted successfully!")
                except Exception as e:
                    print(f"Error setting up database: {e}")

            # Task 1: String Indexing - Query rows with ID > 14
            try:
                query_q1 = "SELECT * FROM demo WHERE id > 14"
                cursor.execute(query_q1)
                rows = cursor.fetchall()
                print("\nNames of rows with id > 14:")
                for row in rows:
                    print(row["name"])  # Using string indexing to extract only names
            except Exception as e:
                print(f"Error in Task 1: {e}")

            # Task 2: Delete Row based on User Input
            try:
                print("\n--- Row Deletion ---")
                del_row = int(input("Enter the row ID threshold for deletion: "))
                query_q2 = "DELETE FROM demo WHERE id < ?"
                cursor.execute(query_q2, (del_row,))
                num_rows = cursor.rowcount
                confirmation = input(f"{num_rows} rows affected. Are you sure you want to continue? (y/n): ")

                if confirmation.lower() == 'y':
                    db_con.commit()
                    print("Deletion confirmed.")
                else:
                    db_con.rollback()
                    print("Operation canceled.")
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"Error in Task 2: {e}")

except sqlite3.Error as e:
    print(f"Database connection error: {e}")