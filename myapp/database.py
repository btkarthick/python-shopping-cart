"""
******************************************
Custom database class file
******************************************
"""
import sys
import pymysql.cursors


class Database(object):

    def __init__(self, logger):
        self.host = ""
        self.user = ""
        self.password = ""
        self.db = ""
        self.charset = 'utf8mb4'
        self.conn = None
        self.log = logger

    def init_app(self, app):

        self.host = app.config['MYSQL_HOST']
        self.user = app.config['MYSQL_USER']
        self.password = app.config['MYSQL_PASSWORD']
        self.dbName = app.config['MYSQL_DB_NAME']

    def finally_block(self):
        """ Finally Block Template """
        if self.conn:
            self.conn.close()
            self.conn = None
            self.log.info('Database connection closed')

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    db=self.dbName,
                    charset=self.charset,
                    cursorclass=pymysql.cursors.DictCursor)

        except pymysql.MySQLError as e:
            self.log.error(f"MYSQL CONNECTION ERROR - {e}")
            sys.exit()

        finally:
            self.log.info('Connection opened successfully.')

    def fetch_rows(self, query):
        """Execute SQL SELECT query and return the result"""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                records = []
                cur.execute(query)
                self.log.info(f"Executed Query - {query}")
                result = cur.fetchall()
                for row in result:
                    records.append(row)
                cur.close()
                return dict(status=True, rows=records)

        except pymysql.MySQLError as e:
            self.log.error(f"MYSQL ERROR - {e}")
            return dict(status=False, error=e)

        finally:
            self.finally_block()

    def execute_query(self, query):
        """ Execute - INSERT, UPDATE, DELETE Statements  """
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                cur.execute(query)
                self.log.info(f"Executed Query - {query}")
                row_count = cur.rowcount
                last_insert_id = cur.lastrowid if 'INSERT' in query else False

                if any(keyword in query.upper() for keyword in ('INSERT' or 'UPDATE')):
                    self.conn.commit()

                cur.close()

                result = dict(status=True, row_count=row_count)

                if last_insert_id:
                    result.update(last_insert_id=last_insert_id)

                return result

        except pymysql.MySQLError as e:
            self.log.error(f"MYSQL ERROR - {e}")
            return dict(status=False, error=e)

        finally:
            self.finally_block()
