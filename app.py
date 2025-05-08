import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np

st.title("Read Google Sheet as DataFrame")

url = "https://docs.google.com/spreadsheets/d/1kT2Ly7_wYwCKTrElsCpneihHmhwGX-DpzhCPN9jpXSo/edit?usp=sharing"


conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url,)
df2 = pd.DataFrame(df)
#print(df2)

st.dataframe(df)
sql ='''
        SELECT
         "F4",
         "F8"
        FROM
          HC
        WHERE
          "F4" < 2
     ''' 
df3 = conn.query(spreadsheet=url,sql=sql)
st.dataframe(df3)

#側欄、容器測試

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [24.0, 120.5],
    columns=['lat', 'lon'])
st.sidebar.map((map_data))

with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
    st.scatter_chart(
        df2,
        x="Fp1",
        y=["Fp2","F4"],
        #color=["#FF0000"]
        color=["#FF0000", "#0000FF"],
        )

st.write("This is outside the container")