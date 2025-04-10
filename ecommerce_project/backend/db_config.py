import cx_Oracle

def get_connection():
    dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XE')
    connection = cx_Oracle.connect(user='SYSTEM', password='Pr16189@', dsn=dsn_tns)
    return connection
