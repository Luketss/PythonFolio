import mariadb

class db_Conn:
    def __init__(self):
        self.conn = self.get_connection()
        self.cursor = self.conn.cursor()

    def get_connection(self) -> str:
        try:
            conn = mariadb.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                database="stocks",
            )
            return conn
        except mariadb.Error as e:
            print(f'Error connecting to mariadb: {e}')

    def insert_stock(self, stock_code) -> None:
        try:
            if self.check_insert(stock_code):
                query = f"INSERT INTO stock (stock_code) VALUES ('{stock_code}')"
                self.cursor.execute(query)
            else:
                print('Already exist')
            
        except mariadb.Error as e:
            print(f'Error at: {e}')

    def check_insert(self, stock_code):
        try:
            query = f"SELECT * FROM stock WHERE stock_code='{stock_code}'"
            self.cursor.execute(query)
            row = self.cursor.fetchall()

            if not row:
                return True
            return False
        except mariadb.Error as e:
            print(f'Error at: {e}')

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    conection = db_Conn()
    conection.insert_stock('TSLA')
    conection.commit_and_close()