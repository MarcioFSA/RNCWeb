import sqlite3


import streamlit as st
import pandas as pd
import controller.controllerRnc as controllerRnc

conn = sqlite3.connect("rnc.db", check_same_thread=False)
cur = conn.cursor()

st.sidebar.title('MENU')
page_rnc = st.sidebar.selectbox('Não conformidade', ['Registrar','Listar'])

if page_rnc == 'Registrar':
        st.title('Registro de Não Conformidades')

        col1, col2 = st.columns(2)
        with col1:
                setor_notificado = st.selectbox("Setor", ['', 'Ambulatorio', 'Emergencia Pediatrica', 'Oncologia',
                                                          'Clinica Cirurgica'])

        with col2:
                setor_notificador = st.selectbox("Setor_Notificador",
                                                 ['', 'Ambulatorio', 'Emergencia Pediatrica', 'Oncologia',
                                                  'Clinica Cirurgica'])
        with st.form(key='Registrar_Cao_Conformidade', clear_on_submit=True):
                tipo_rnc = st.selectbox("Não conformidade",['','Falha de comunicação','Falta de atenção','Desconhecimento de procedimento interno'])
                descricao = st.text_area(label="Descreva a não conformidade")
                funcao_select = st.selectbox("Função",['','Enfermeiro','Médico','Técnico de Enfermagem'])
                data = st.date_input(label="Data da Não conformidade")
                funcao_text = st.text_input(label='Informe sua função(Caso não tenha encontrado no menu anterior)')
                turno =st.selectbox("Turno",['SN','MT'])
                # input_button = st.form_submit_button("Enviar")
                botao = st.form_submit_button("Registrar")


        if botao == True:
        # if not setor_notificado:
        #         st.warning("Informe o setor notificado")
        # else:
                controllerRnc.Incluir(setor_notificado,setor_notificador,tipo_rnc,descricao,funcao_select,data,funcao_text,turno)
                st.success("DADOS CADASTRADOS COM SUCESSO", icon="✅")


if page_rnc == 'Listar':
                listagem = []
                st.title('Clientes Cadastrados')
                for item in controllerRnc.consultarTodos():
                        listagem.append([item.setor_notificado, item.setor_notificador, item.tipoRnc, item.descricao,item.funcaoSelect,item.data,item.funcaoText,item.turno])

                df = pd.DataFrame(
                        listagem,
                        columns=['Setor Notificado', 'setor Notificador', 'Não Conformidade','Descrição', 'Função', 'Data RNC','Função Informada','Turno Ocorrência']

                    )
                st.table(df)
                # pd.set_option('max_columns', 150)





