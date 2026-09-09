import sqlite3


connection = sqlite3.connect(
    "data/database/hospital_operations.db"
)


tables = connection.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table';
    """
)


print("Database Tables:")
print("----------------")


for table in tables:
    print(table[0])


connection.close()