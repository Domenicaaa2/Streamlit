import streamlit as st
import pandas as pd
import datetime

# Seite konfigurieren
st.set_page_config(page_title="Covid-19 Fälle im Kanton Zürich")

# Daten laden und cachen
@st.cache
def load_data():
    df = pd.read_csv('fallzahlen_kanton_ZH_plz.csv')
    df['Date'] = pd.to_datetime(df['Date']).dt.date  # Konvertiere das Datum in ein Datumsformat ohne Uhrzeit
    return df

df = load_data()

# Header
st.header("Covid-19 Fallzahlen Analyse für Kanton Zürich")

# PLZ Auswahl
plz = st.selectbox("PLZ wählen", df['PLZ'].unique(), index=0)

# Datum wählen
selected_date = st.date_input("Datum auswählen", value=datetime.date(2020, 2, 27),
                              min_value=datetime.date(2020, 2, 27), max_value=datetime.date(2023, 1, 3))

# Daten filtern basierend auf der Auswahl
filtered_data = df[(df['PLZ'] == plz) & (df['Date'] == selected_date)]

# Ergebnisse anzeigen
if not filtered_data.empty:
    st.write(f"COVID-19 Fälle am {selected_date.strftime('%Y-%m-%d')} für PLZ {plz}:")
    st.dataframe(filtered_data)
else:
    st.write("Keine Daten gefunden für dieses Datum und PLZ.")

# Zusätzliche Tabelle der ersten 100 Einträge
st.subheader("Übersicht der ersten 100 Einträge im Datensatz")
st.dataframe(df.head(100))


