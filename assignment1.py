import threading
import mysql.connector

mysql_config = {
    'host': 'localhost',
    'database': 'db_1',
    'user': 'root',
    'password': 'Sandeep@9524',
    'autocommit': True  
}

num_cases = 2000

def insert_cases(thread_id, num_cases_per_thread):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()

        for i in range(num_cases_per_thread):
            insert_query = f"INSERT INTO your_table_name (column1, column2, ...) VALUES ('value1', 'value2', ...)"
            cursor.execute(insert_query)

        cursor.close()
        connection.close()
        print(f"Thread {thread_id} completed")

    except Exception as e:
        print(f"Error in thread {thread_id}: {str(e)}")

threads = []
cases_per_thread = num_cases // 10  

for i in range(10): 
    thread = threading.Thread(target=insert_cases, args=(i+1, cases_per_thread))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads completed")
