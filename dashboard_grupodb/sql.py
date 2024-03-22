import pyodbc
import datetime
# Banco de dados: Microsoft Sql Server
# DB_HOST=172.50.10.5
# DB_PORT=1433
# DB_DATABASE=DB
# DB_USERNAME=DBCONSULTA
# DB_PASSWORD=DB@@2023**

# dados_conxeao = (
#     "Driver={SQL Server};"
#     "Server=172.50.10.5,1433;"
#     "Database=DB;"
#     "Username=DBCONSULTA"
#     "Password=DB@@2023**"
#     "Integrated_Security=false;"
#     "Trusted_Connection=no;"
    

# )

# conexao = pyodbc.connect(dados_conxeao)
# print("Conexão bem sucedida!!!")

server = '172.50.10.5'
database = 'DB'
username = 'DBCONSULTA'
password = 'DB@@2023**'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
connection = pyodbc.connect(connection_string)

print("Conxão ok")



data_prod =datetime.date(2024, 3 ,6)
query = f"""

SELECT 1 SEQ, DTRREF DIARIA, DTRDATA1 INICIO, DTRDATA2 FIM,

'MINA' ORIGEM, 'BRITADOR' DESTINO, IDTRNUMVIA VIAGEM, IDTRPESOTOT PESO

FROM ITEMDIARIATRANSP IDTR
JOIN DIARIATRANSP ON DTRCOD = IDTRDTR

WHERE DTRSIT = 1
AND DTREMP = 1
AND DTRFIL = 0
AND CAST (DTRDATA1 as DATE)  = {data_prod}

AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) LIKE '%+1+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+100+%'
AND (SELECT ISNULL('+' + CAST(L5.LOCCOD AS VARCHAR(MAX)), '+') + ISNULL(CAST(L4.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L3.LOCCOD AS VARCHAR(MAX)) + '+', '+') + ISNULL(CAST(L2.LOCCOD AS VARCHAR(MAX)) + '+', '+') + 
            ISNULL(CAST(L1.LOCCOD AS VARCHAR(MAX)) + '+', '') 
     FROM LOCAL L1
     LEFT OUTER JOIN LOCAL L2 ON L2.LOCCOD = L1.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L3 ON L3.LOCCOD = L2.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L4 ON L4.LOCCOD = L3.LOCLOCPAI
     LEFT OUTER JOIN LOCAL L5 ON L5.LOCCOD = L4.LOCLOCPAI
     WHERE L1.LOCCOD = IDTR.IDTRLOCORIG) NOT LIKE '%+101+%'
AND IDTRTIPODEST = 1
AND IDTRDESTINO = 66



"""



cursor = connection.cursor()

cursor.execute(query)

for row in cursor.fetchall():
    print(row)


connection.close()