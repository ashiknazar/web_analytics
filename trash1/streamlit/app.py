import streamlit as st
from pyhive import hive
import pandas as pd

conn = hive.Connection(host="hive-server", port=10000)
df = pd.read_sql("SELECT * FROM daily_page_visits", conn)

st.title("User Activity Analytics")
st.bar_chart(df.set_index("page"))
