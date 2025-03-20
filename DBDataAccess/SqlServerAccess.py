import pyodbc

class SqlAccess():
    dbConn=""
    
    #COSTRUTTORI    
    def __init__(self,dbconn):
        self.dbConn=dbconn
    
    def __init__(self,server,database,username="",password="",encryption="Optional"):
        driver = '{ODBC Driver 18 for SQL Server}'
        
        if (username=="" or password==""):
            self.dbConn = f'DRIVER={driver};SERVER={server};DATABASE={database};Encrypt={encryption};Trusted_Connection=yes'
        else:
            self.dbConn = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt={encryption}'
    #END COSTRUTTORI

    #ESECUZIONE QUERY
    def ExecuteSql(self,sql,*pars):
        try:
            with pyodbc.connect(self.dbConn) as conn:
                cursor=conn.cursor()
                cursor.execute(sql,*pars)
                return cursor.fetchall()
        except pyodbc.Error as err01:
            print("Errore nell'esecuzione della query: ",err01)
            return None
        return None   
         
    #ESECUZIONE STORED PROCEDURE
    def ExecuteProcedureResultset(self,procedura,*pars):
        try:
            with pyodbc.connect(self.dbConn) as conn:
                cursor=conn.cursor()
                cursor.execute(f"exec {procedura}",*pars)
                return cursor.fetchall()
        except pyodbc.Error as err01:
            print("Errore nell'esecuzione della procedura: ",err01)
            return None
        return None