import sqlite3


# В реальных проектах для таких данных нужно использовать переменные окружения (os.environ).

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
   
    # Вместо опасного форматирования строк используются параметризованные запросы с плейсхолдерами (?),
    # которые безопасно экранируют любые переданные данные.
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    result = cursor.fetchone()
    conn.close()
    
    
    # Метод возвращает True, если result не равен None, и False в противном случае.
    return result is not None


# я плохо поняла как пользоваться этим всем но как то пофиксила