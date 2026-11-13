import sqlite3
import hashlib

ADMIN_PASSWORD = "SuperSecretPassword123!"
ADMIN_TOKEN = "Bearer secret_api_token_xyz987"

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    if result is not None:
        return True
    else:
        return False