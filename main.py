import json

from fastapi import FastAPI
import mysql.connector
app = FastAPI()


mydb = mysql.connector.connect(
    host="192.168.100.80",
    user="root",
    password="123asd",
    database="asteriskcdrdb"
)


@app.get("/get_registers")
async def get_registers_cdr():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM cdr LIMIT 10')
    reg = cursor.fetchall()
    print(reg)
    res = []
    for i in reg:
        dict = {"id": i[0],"caller": i[1],"callee": i[2],"duration": i[3]}
        res.append(dict)
    json_res = json.dumps(res).replace('\\', "")

    return json_res


