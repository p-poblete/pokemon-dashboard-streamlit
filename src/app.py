import streamlit as st
import pandas as pd
import numpy as np

csv_basico = 'data/pokemon_data.csv'
equipo_df = pd.read_csv(csv_basico, index_col=False)
#equipo_df.describe()
#nombres = equipo_df['nombre'].copy()

naturalezas = ["Fuerte", "Huraña", "Audaz", "Firme", "Picara", "Osada", "Dócil",
 "Relajada", "Agitada", "Descuidada", "Miedosa", "Activa", "Seria", "Alegre",
 "Ingenua", "Modesta", "Cordial", "Apacible", "Timida", "Alocada", "Serena",
 "Amable", "Grosera", "Cauta", "Extravagante" ]

tipos = ["Acero","Agua","Bicho","Dragón","Eléctrico","Fantasma","Fuego","Hada",
"Hielo","Lucha","Normal","Planta","Psíquico","Roca","Siniestro","Tierra","Veneno",
"Volador"]

tipos2 = ["Ninguno", "Acero","Agua","Bicho","Dragón","Eléctrico","Fantasma","Fuego","Hada",
"Hielo","Lucha","Normal","Planta","Psíquico","Roca","Siniestro","Tierra","Veneno",
"Volador"]

@st.dialog("Editar Datos Generales", width="medium")
def editar_general(pokemon_data, index, df_edit):
    mote_valido = pd.notna(pokemon_data['mote']) and str(pokemon_data['mote']).strip() != ""
    if mote_valido:
        st.subheader(f"Inf. General de: {pokemon_data['mote']} ({pokemon_data['nombre']})")
    else:
        st.subheader(f"Inf. General de: {pokemon_data['nombre']}")

    e_inf_b, e_inf_p = st.columns(2, border=True)
    with e_inf_b:
        e_id = st.number_input("ID en la Pokedex", 1, 1025, value=pokemon_data['id'])
        e_nombre = st.text_input("Nombre", value=pokemon_data['nombre'])
        e_mote = st.text_input("Mote", value=pokemon_data['mote'])
        e_nivel = st.slider("Nivel", 1, 100, value=pokemon_data['nivel'])
    with e_inf_p:
        idx1 = tipos.index(pokemon_data['tipo1']) if pokemon_data['tipo1'] in tipos else 0
        e_tipo1 = st.selectbox("Tipo 1", tipos, index=idx1)
        idx2 = tipos2.index(pokemon_data['tipo2']) if pokemon_data['tipo2'] in tipos2 else 0
        e_tipo2 = st.selectbox("Tipo 2", tipos2, index=idx2)
        idx3 = naturalezas.index(pokemon_data['naturaleza']) if pokemon_data['naturaleza'] in tipos2 else 0
        e_naturaleza = st.selectbox("Naturaleza", naturalezas, index=idx3)
        e_habilidad = st.text_input("Habilidad", value=pokemon_data['habilidad'])

    ivs, evs = st.columns(2, border=True)
    with ivs: 
        e_iv_ps = st.slider("IV PS", 1, 31, int(pokemon_data['iv_ps']))
        e_iv_atq = st.slider("IV Ataque", 1, 31, int(pokemon_data['iv_atq']))
        e_iv_def = st.slider("IV Defensa", 1, 31, int(pokemon_data['iv_def']))
        e_iv_atq_esp = st.slider("IV At. Especial", 1, 31, int(pokemon_data['iv_atq_esp']))
        e_iv_def_esp = st.slider("IV def. Especial", 1, 31, int(pokemon_data['iv_def_esp']))
        e_iv_vel = st.slider("IV Velocidad", 1, 31, int(pokemon_data['iv_velo']))
    with evs:    
        e_ev_ps = st.number_input("EV PS", 1, 252, int(pokemon_data['ev_ps']))
        e_ev_atq = st.number_input("EV Ataque", 1, 252, int(pokemon_data['ev_atq']))
        e_ev_def = st.number_input("EV Defensa", 1, 252, int(pokemon_data['ev_def']))
        e_ev_atq_esp = st.number_input("EV At. Especial", 1, 252, int(pokemon_data['ev_atq_esp']))
        e_ev_def_esp = st.number_input("EV def. Especial", 1, 252, int(pokemon_data['ev_def_esp']))
        e_ev_vel = st.number_input("EV Velocidad", 1, 252, int(pokemon_data['ev_velo']))
    
    if st.button("Guardar Inf. General", type="primary", width="stretch"):
        df_edit.at[index,'id'] = e_id
        df_edit.at[index,'nombre'] = e_nombre
        df_edit.at[index, 'mote'] = e_mote
        df_edit.at[index,'nivel'] = e_nivel

        df_edit.at[index, 'tipo1'] = e_tipo1
        df_edit.at[index, 'tipo2'] = e_tipo2
        df_edit.at[index, 'naturaleza'] = e_naturaleza
        df_edit.at[index, 'habilidad'] = e_habilidad

        df_edit.at[index, 'iv_ps'] = e_iv_ps
        df_edit.at[index, 'iv_atq'] = e_iv_atq
        df_edit.at[index, 'iv_def'] = e_iv_def
        df_edit.at[index, 'iv_atq_esp'] = e_iv_atq_esp
        df_edit.at[index, 'iv_def_esp'] = e_iv_def_esp
        df_edit.at[index, 'iv_velo'] = e_iv_vel

        df_edit.at[index, 'ev_ps'] = e_ev_ps
        df_edit.at[index, 'ev_atq'] = e_ev_atq
        df_edit.at[index, 'ev_def'] = e_ev_def
        df_edit.at[index, 'ev_atq_esp'] = e_ev_atq_esp
        df_edit.at[index, 'ev_def_esp'] = e_ev_def_esp
        df_edit.at[index, 'ev_velo'] = e_ev_vel

        df_edit.to_csv(csv_basico, index=False)
        st.rerun()

@st.dialog("Editar IVs")
def editar_ivs(pokemon_data, index, df_original):
    mote_valido = pd.notna(pokemon_data['mote']) and str(pokemon_data['mote']).strip() != ""
    if mote_valido:
        st.subheader(f"IVs de: {pokemon_data['mote']} ({pokemon_data['nombre']})")
    else:
        st.subheader(f"IVS de: {pokemon_data['nombre']}")

    e_iv_ps = st.slider("IV PS", 1, 31, int(pokemon_data['iv_ps']))
    e_iv_atq = st.slider("IV Ataque", 1, 31, int(pokemon_data['iv_atq']))
    e_iv_def = st.slider("IV Defensa", 1, 31, int(pokemon_data['iv_def']))
    e_iv_atq_esp = st.slider("IV At. Especial", 1, 31, int(pokemon_data['iv_atq_esp']))
    e_iv_def_esp = st.slider("IV def. Especial", 1, 31, int(pokemon_data['iv_def_esp']))
    e_iv_vel = st.slider("IV Velocidad", 1, 31, int(pokemon_data['iv_velo']))
    
    if st.button("Guardar IVs", type="primary", width="stretch"):
        df_original.at[index, 'iv_ps'] = n_iv_ps
        df_original.to_csv('pokemon_data.csv', index=False)
        st.rerun()

@st.dialog("Editar EVs")
def editar_evs(pokemon_data, index, df_original):
    mote_valido = pd.notna(pokemon_data['mote']) and str(pokemon_data['mote']).strip() != ""
    if mote_valido:
        st.subheader(f"EVs de: {pokemon_data['mote']} ({pokemon_data['nombre']})")
    else:
        st.subheader(f"EVs de: {pokemon_data['nombre']}")

    e_ev_ps = st.number_input("EV PS", 1, 252, int(pokemon_data['ev_ps']))
    e_ev_atq = st.number_input("EV Ataque", 1, 252, int(pokemon_data['ev_atq']))
    e_ev_def = st.number_input("EV Defensa", 1, 252, int(pokemon_data['ev_def']))
    e_ev_atq_esp = st.number_input("EV At. Especial", 1, 252, int(pokemon_data['ev_atq_esp']))
    e_ev_def_esp = st.number_input("EV def. Especial", 1, 252, int(pokemon_data['ev_def_esp']))
    e_ev_vel = st.number_input("EV Velocidad", 1, 252, int(pokemon_data['ev_velo']))
    
    if st.button("Guardar EVs", type="primary", width="stretch"):
        df_original.at[index, 'ev_ps'] = n_ev_ps
        df_original.to_csv('pokemon_data.csv', index=False)
        st.rerun()

st.set_page_config(layout="wide")

st.title("Dashboard Equipo PokeMMO")

# st.write("Hola, Davis!")

# with st.container(border=True):
#     users = st.multiselect("Pokes", equipo_df['nombre'])

# tab1, tab2 = st.tabs(["Chart", "Data"])
# tab1.line_chart(equipo_df['ev_def'], height=250)
# tab2.dataframe(equipo_df['ev_def'], height=250, use_container_width=True)

menu = st.sidebar.radio("Opciones", ["Visualizar Equipo", "Añadir Pokemon"])
if menu == "Añadir Pokemon":
    st.caption("CRUD MAMALON")
    df_basico_tmp = pd.read_csv(csv_basico)
    nuevo, existentes = st.columns([3, 1], border=True)
    with nuevo:
        with st.form(key="nuevo_poke", enter_to_submit=False, border=False, width="stretch"):
            st.header(body="Registrar Nuevo Pokemon", divider="red")
            inf_b, inf_p = st.columns(2, border=True)
            with inf_b:
                #st.markdown("### Información General")
                np_id = st.number_input("ID en la Pokedex", 1, 1025)
                np_nombre = st.text_input("Nombre")
                np_mote = st.text_input("Mote")
                np_nivel = st.slider("Nivel", 1, 100)
            with inf_p:
                #st.markdown("### Información Pokemon")
                #t_1, t_2 = st.columns(2, gap="small", border=False)
                #with t_1:
                np_tipo1 = st.selectbox("Tipo 1", tipos)
                #with t_2:
                np_tipo2 = st.selectbox("Tipo 2", tipos2)
                np_naturaleza = st.selectbox("Naturaleza", naturalezas)
                np_habilidad = st.text_input("Habilidad")
                # np_habilidad_d = ...
            ivs, evs = st.columns(2, border=True)
            with ivs:  
                st.subheader("Genetica - IVs", divider="red")
                np_iv_ps = st.slider("IV PS", 1, 31)
                np_iv_atq = st.slider("IV Ataque", 1, 31)
                np_iv_def = st.slider("IV Defensa", 1, 31)
                np_iv_atq_esp = st.slider("IV At. Especial", 1, 31)
                np_iv_def_esp = st.slider("IV def. Especial", 1, 31)
                np_iv_vel = st.slider("IV Velocidad", 1, 31)
            with evs:
                st.subheader("Entrenamiento - EVs", divider="red")
                np_ev_ps = st.number_input("EV PS", 1, 252)
                np_ev_atq = st.number_input("EV Ataque", 1, 252)
                np_ev_def = st.number_input("EV Defensa", 1, 252)
                np_ev_atq_esp = st.number_input("EV At. Especial", 1, 252)
                np_ev_def_esp = st.number_input("EV def. Especial", 1, 252)
                np_ev_vel = st.number_input("EV Velocidad", 1, 252)
            np_subido = st.form_submit_button(label="Subir Nuevo Pokemon", type="primary", width="stretch")
            if np_subido:
                n_fila = {
                    'id' : np_id,
                    'nombre' : np_nombre,
                    'mote' : np_mote,
                    'nivel' : np_nivel,

                    'tipo1' : np_tipo1,
                    'tipo2' : np_tipo2,
                    'naturaleza' : np_naturaleza,
                    'habilidad' : np_habilidad,

                    'iv_ps' : np_iv_ps,
                    'iv_atq' : np_iv_atq,
                    'iv_def' : np_iv_def,
                    'iv_atq_esp' : np_iv_atq_esp,
                    'iv_def_esp' : np_iv_def_esp,
                    'iv_velo' : np_iv_vel,

                    'ev_ps' : np_ev_ps,
                    'ev_atq' : np_ev_atq,
                    'ev_def' : np_ev_def,
                    'ev_atq_esp' : np_ev_atq_esp,
                    'ev_def_esp' : np_ev_def_esp,
                    'ev_velo' : np_ev_vel,
                }
                df_nuevo = pd.DataFrame([n_fila])
                df_basico_tmp = pd.concat([df_basico_tmp, df_nuevo], ignore_index=True)
                df_basico_tmp.to_csv(csv_basico, index=False)
                st.rerun()
    with existentes:
        st.subheader(body="Pokemon's Registrados", divider="red")
        for index, row in df_basico_tmp.iterrows():
            with st.container(border=True):
                label = f"{row['mote']} ({row['nombre']})" if pd.notnull(row['mote']) else row['nombre']
                st.write(label, )

                c1, c4 = st.columns(spec=2, gap="small")

                with c1:
                    if st.button("Editar", width="stretch", key=f"btn_g_{index}"):
                        editar_general(row, index, df_basico_tmp)
                
                # with c2:
                #    if st.button("IVs", width="stretch", key=f"btn_iv_{index}"):
                #        editar_ivs(row, index, df_basico_tmp)

                # c3, c4 = st.columns(spec=2, gap="small")

                # with c3:
                #    if st.button("EVs", width="stretch", key=f"btn_ev_{index}"):
                #        editar_evs(row, index, df_basico_tmp)

                with c4:
                    if st.button("Borrar", width="stretch", key=f"btn_del_{index}"):
                        df_basico_tmp.drop(index).to_csv('pokemon_data.csv', index=False)
                        st.rerun()
