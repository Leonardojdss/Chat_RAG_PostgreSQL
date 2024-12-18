import psycopg2
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector
import os
import json

load_dotenv()

def connection_postgreSQL(user, password, endpoint):
    conn = psycopg2.connect(user=user, password=password, host=endpoint, port=5432, database="postgres")
    cur = conn.cursor()
    register_vector(conn)
    return conn, cur

#Teste 
# USER_POSTGRESQL = os.getenv("USER_POSTGRESQL")
# PASSWORD_POSTGRESQL = os.getenv("PASSWORD_POSTGRESQL")
# ENDPOINT_POSTGRESQL = os.getenv("ENDPOINT_POSTGRESQL")

# conn, cur = connection_postgreSQL(USER_POSTGRESQL, PASSWORD_POSTGRESQL, ENDPOINT_POSTGRESQL)

# conteudo = ['123']
# conteudo_str = '[' + ','.join(conteudo) + ']'

# try:
#     cur.execute("INSERT INTO brasas_vector_db (id, titulo, conteudo, data) VALUES (%s, %s, %s::vector, %s)", (1, 'pdf', conteudo_str, '2022-01-01'))
#     conn.commit()  # Commit the transaction
#     print("Data inserted successfully")
# except Exception as e:
#     print(f"Error: {e}")
#     conn.rollback()  # Rollback the transaction in case of error
# finally:
#     cur.close()
#     conn.close()