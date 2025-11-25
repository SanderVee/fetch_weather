import streamlit as st
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='ubuntu',
    password=,
    database=
)
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
conn.close()

st.write("Säädata laatikkona:")
st.dataframe(df)

st.write("Lämpötilakaavio:")
st.line_chart(df["temperature"])

