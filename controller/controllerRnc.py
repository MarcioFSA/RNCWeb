import models.rnc as rnc
import sqlite3
import streamlit as st
conn = sqlite3.connect('rnc.db', check_same_thread=False)
cur = conn.cursor()


def Incluir(setor_notificado,setor_notificador,tipo_nc,descricao,funcao_select,data,funcao_text,turno):
    cur.execute(f"INSERT INTO RNC(setor_notificado,setor_notificador,tipo_nc,descricao,funcao_select,data,funcao_text,turno) VALUES(?,?,?,?,?,?,?,?)",(setor_notificado,setor_notificador,tipo_nc,descricao,funcao_select,data,funcao_text,turno))
    conn.commit()
    # conn.close()




def consultarTodos():
    cur.execute("Select * from rnc")
    listagem = []
    for row in cur.fetchall():
            listagem.append(rnc.rnc(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7],row[8]))

    return listagem