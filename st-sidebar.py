import streamlit as st
import pandas as pd
import time

from streamlit_tutorial1 import change_photoready, progress_bar, students

if 'photo' not in st.session_state:
    st.session_state['photo'] = 'not done'

def change_photoready():
    st.session_state['photo'] ='done'
    col1.write("Foto wurde aufgenommen: "+st.session_state.photo)

def startseite():
    st.title("Startseite")
    st.title("Das ist meine erste Web-App")
    st.write('Hello World')

    # Eingabeaufforderung
    nutzer_name = st.text_input('Gib bitte Deinen Benutzernahmen ein!')

    if nutzer_name != '':
        st.write("Der Name " + nutzer_name + " ist sehr schön!")

    col1, col2, col3 = st.columns([2, 2, 1])
    col1.write('Das ist der Text zu Spalte 1')
    col2.write('Das ist der Text zu Spalte 1')
    col3.write('Das ist der Text zu Spalte 1')

    # File Uploader
    file = col2.file_uploader('Bitte lade eine Datei hoch')

    # Markdown
    st.markdown('# Das ist die Hauptüberschrift')
    st.markdown('## Das ist die Nebenüberschrift')

    # Foto aufnehmen
    photo_shot = col1.camera_input('Nimm ein Foto auf', on_change=change_photoready)

    progress_bar = col1.progress(0)
    if st.session_state.photo == 'done':
        st.balloons()
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i)

    # Feedback-Formate
    col3.error('Das ist eine wichtige und kritische Nachricht')
    col3.warning('for warning messages')
    col3.info(' for information messages')
    col3.success('for showing success messages')

    # Metrische Angaben
    col1.metric(label='Temperatur', value='14,8°C', delta='-1,7°C')

    # Arbeiten mit Expanders
    with st.expander('Click to expand'):
        st.write(
            'oiuAOI doias oidoadoiqwud  kqpodwkq kdpqwjdpoi qojsdlalkjkdäöksüp üsskaölky ölxkqp j 0xjqijw sjwqksq pqjxpjpqjak  ükäökkl,a ö,x nal skohasohoqjwps axjqöljaöljxö  köa kxölajlskjc lkajc')
        if photo_shot is not None:
            st.image(photo_shot)

    # Tabellen darstellen
    students = ['Anna', 'Lydia', 'Tim', 'Peter', 'Kim']
    marks = [82, 73, 45, 23, 45]
    df = pd.DataFrame()
    df['StudentNames'] = students
    df['Marks'] = marks
    st.dataframe(df)

    # diagramme einbinden
    import plotly.express as px

    df = px.data.iris()
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length', color='species')
    st.plotly_chart(fig, use_container_width=True)

def daten():
    st.title("Datenanalyse")
    st.write("Hier kommt die Datenanalyse hin.")

def kontakt():
    st.title("Kontakt")
    st.write("Hier stehen Kontaktdaten.")

# Navigation über die Sidebar
seiten = {
    "Startseite": startseite,
    "Daten": daten,
    "Kontakt": kontakt
}

auswahl = st.sidebar.radio("Seite auswählen", list(seiten.keys()))
seiten[auswahl]()  # ruft die passende Funktion auf