import SqlServerAccess as sql
def caricaDati():
    dba=sql.SqlAccess("DB_LISTENER08.SRV.VAT.LOCAL","RichiestePCP")
    query="SELECT Cognome + ' ' + Nome FROM [Richieste]"
    lista=dba.ExecuteSql(query)
    return lista

lista=caricaDati()
print(lista)
