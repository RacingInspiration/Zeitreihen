import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Daten aus der Tabelle mit korrigierten Koordinaten
data = {
    "Ort": ["Bad Windsheim", "Baudenbach", "Burgbernheim", "Burghaslach", "Dachsbach", "Diespeck", "Dietersheim", "Emskirchen", "Ergersheim", "Gallmersgarten", "Gerhardshofen", "Gollhofen", "Gutenstetten", "Hagenbüchach", "Hemmersheim", "Illesheim", "Ippesheim", "Ipsheim", "Langenfeld", "Marktbergel", "Bibart", "Erlbach", "Nordheim", "Taschendorf", "Münchsteinach", "Neuhof a.d.Zenn", "Neustadt a.d.Aisch", "Oberickelsheim", "Obernzenn", "Oberscheinfeld", "Scheinfeld", "Simmershofen", "Sugenheim", "Trautskirchen", "Uehlfeld", "Uffenheim", "Weigenheim", "Wilhelmsdorf"],
    "Einwohnerzahl": [12700, 1100, 3100, 2400, 1100, 3800, 2000, 6200, 1100, 700, 2500, 800, 1500, 1300, 600, 900, 1100, 2100, 1000, 1500, 1700, 5500, 1100, 1000, 1400, 2200, 12600, 600, 2700, 1400, 4500, 900, 2300, 1200, 3000, 6000, 1000, 1200],
    "Breitengrad": [49.5027, 49.5311, 49.4511, 49.7333, 49.6411, 49.6000, 49.5667, 49.5500, 49.5167, 49.4500, 49.6333, 49.5667, 49.6167, 49.5333, 49.5667, 49.4667, 49.6000, 49.5167, 49.6167, 49.4500, 49.6333, 49.5000, 49.5833, 49.5333, 49.6333, 49.4667, 49.5833, 49.6000, 49.4500, 49.7000, 49.6667, 49.5333, 49.6000, 49.4500, 49.6667, 49.5333, 49.5667, 49.5667],
    "Längengrad": [10.4153, 10.5358, 10.3239, 10.6000, 10.7039, 10.6333, 10.5333, 10.7167, 10.3333, 10.2667, 10.6833, 10.2000, 10.6333, 10.7667, 10.1000, 10.3833, 10.2333, 10.4833, 10.5167, 10.3667, 10.4333, 10.6500, 10.1833, 10.5333, 10.6000, 10.6500, 10.6000, 10.1333, 10.4667, 10.4333, 10.4667, 10.1333, 10.4333, 10.6000, 10.7167, 10.2333, 10.2667, 10.7333],
    "1.Stimme_2021": [13.28, 13.67, 14.17, 9.97, 8.78, 13.03, 13.55, 12.35, 11.41, 14.47, 11.27, 17.17, 14.41, 13.93, 9.53, 10.03, 17.0, 10.72, 11.52, 15.85, 11.45, 11.16, 13.19, 9.71, 11.88, 9.81, 13.72, 13.58, 11.35, 9.93, 10.71, 12.21, 10.42, 9.19, 11.14, 17.19, 23.64, 10.16],
    "2.Stimme_2021": [11.29, 12.13, 11.91, 11.17, 8.41, 12.16, 12.91, 12.94, 10.13, 11.39, 11.64, 13.62, 13.18, 15.87, 8.0, 10.87, 12.25, 11.0, 10.11, 11.63, 10.65, 11.14, 8.82, 8.46, 11.65, 11.42, 13.63, 11.76, 11.36, 9.26, 10.55, 10.03, 9.58, 10.04, 10.75, 11.05, 15.04, 10.66],
    "1.Stimme_2017": [10.4, 11.3, 10.4, 7.8, 8.2, 10.5, 10.8, 9.8, 10.8, 9.4, 9.1, 16.2, 16.0, 10.3, 12.1, 8.6, 14.3, 7.8, 8.3, 11.8, 7.2, 8.8, 12.3, 6.2, 10.4, 10.2, 11.1, 11.8, 8.8, 6.8, 9.4, 10.4, 9.6, 6.2, 9.6, 16.5, 18.2, 8.9],
    "2.Stimme_2017": [8.6, 8.9, 8.5, 9.2, 7.7, 9.5, 8.5, 9.5, 8.0, 9.6, 8.2, 9.5, 13.4, 9.7, 8.4, 8.2, 9.9, 8.1, 9.1, 8.7, 8.7, 8.1, 9.5, 6.5, 10.2, 9.7, 10.1, 5.8, 9.0, 5.5, 8.7, 5.2, 7.6, 7.4, 9.0, 9.1, 11.4, 8.7]
}

df = pd.DataFrame(data)

# Streamlit-App Layout
st.title('Wahlergebnisse auf der Karte')

# Auswahl der Stimmen
wahl_werte = st.multiselect(
    'Wählen Sie die Stimmwerte aus',
    ['1.Stimme_2021', '2.Stimme_2021', '1.Stimme_2017', '2.Stimme_2017'],
    default=['1.Stimme_2021']
)

# Summe der gewählten Stimmen berechnen
df['Summe'] = df[wahl_werte].sum(axis=1)

# Mittelwert der Summe berechnen
mittelwert = df['Summe'].mean()

# Farbe basierend auf dem Vergleich mit dem Mittelwert setzen
df['Farbe'] = df['Summe'].apply(lambda x: 'green' if x > mittelwert else 'red')

# Exponentielle Skalierung der Summe für die Kreisgröße
exponent = 3  # Exponent für die Skalierung (z. B. 2 für quadratische Skalierung)
df['Summe_skaliert'] = df['Summe'] ** exponent

# Erstellen der Karte mit Plotly
fig = px.scatter_mapbox(df, lat="Breitengrad", lon="Längengrad", size="Summe_skaliert",
                        hover_name="Ort", hover_data={"Summe": True},  # Nur die Summe wird beim Hovern angezeigt
                        color="Farbe", color_discrete_map={"green": "green", "red": "red"},
                        zoom=9, height=600, size_max=50)  # size_max steuert die maximale Kreisgröße

# Legende entfernen
fig.update_layout(showlegend=False)

# Hover-Informationen anpassen
fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>Summe: %{customdata[0]:.2f}<extra></extra>")

# Kartenstil und Layout anpassen
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Karte anzeigen
st.plotly_chart(fig)
