import datetime

import pandas as pd
import streamlit as st

def record():
    # conn = st.connection('pyri_db', type='sql')
    #
    # with conn.session as s:
    #     s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    #     s.execute('DELETE FROM pet_owners;')
    #     pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    #     for k in pet_owners:
    #         s.execute(
    #             'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
    #             params=dict(owner=k, pet=pet_owners[k])
    #         )
    #     s.commit()
    # pet_owners = conn.query('select * from pet_owners')
    # st.dataframe(pet_owners)

    date = st.date_input("Date", value="today", key="date", label_visibility="hidden")

    st.header("Traitement")
    meds = ['Plaquenil', 'Medrol', 'Bisoprolol']
    doses = [200, 4, 5]
    perdays = [1, 2, 1]
    for med, dose, perday in zip(meds, doses, perdays):
        cols = st.columns(3)
        with cols[0]:
            st.write(med)
        with cols[1]:
            st.number_input(label="mg", min_value = 0, value=dose, key=f"{med}-dose")
        with cols[2]:
            st.number_input(label="Par jour", min_value = 0,value=perday, key=f"{med}-perday")

    st.header("Symptômes")
    st.slider("Fatigue", min_value=1, max_value=10, value=None, step=1, key="fatigue")
    st.slider("Douleur", min_value=1, max_value=10, value=None, step=1, key="pain")
    st.slider("Brouillard mental", min_value=1, max_value=10, value=None, step=1, key="mental-fog")
    st.select_slider("Sommeil", options=['mauvais', 'moyen', 'bon'], value=None, key="sleep")
    st.multiselect("Articulations affectées", ['mains', 'pieds', 'genoux', 'coudes', 'hanches', 'épaules', 'dos'])
    st.time_input("Durée de dérouillage matinal", value=None, key='morning-stiffness')
    st.time_input("Heure de début des douleurs du soir", value=datetime.time(hour=19), key='evening-stiffness')

    if st.button("Enregistrer"):
        st.write(f"Résultats enregistrés pour le {date}")
