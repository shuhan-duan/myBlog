import sqlite3
DATABASE = 'Shuhan/entries.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
sql = '''
    delete from entries
    '''
result = cursor.execute(sql).rowcount
print(result)

cursor.close()
conn.close()