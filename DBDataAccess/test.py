import SqlServerAccess as sql
def caricaDati():
    dba=sql.SqlAccess("DB_LISTENER08.SRV.VAT.LOCAL","RichiestePCP")
    query="SELECT Cognome + ' ' + Nome FROM [Richieste]"
    lista=dba.ExecuteSql(query)
    return lista


''''
import guizero

app = guizero.App(title="Mostra richieste")
message = guizero.Text(app, text="Richieste")
lista=caricaDati()
combo=guizero.Combo(app,width=200, options=lista)
button = guizero.PushButton(app, text="Carica Dati",width=10,height=1)

app.display()'
'''
lista=caricaDati()
print(lista)
