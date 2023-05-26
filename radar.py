import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache_resource()
def radar_chart(val1, val2, val3, val4, val5):  
    r=[val1, val2, val3, val4, val5]
    theta=['processing cost','mechanical properties','chemical stability',
            'thermal stability', 'device integration']
    df = pd.DataFrame({
        'r': r,
        'theta': theta
    })
    return px.line_polar(df, r='r', theta='theta', line_close=True, template="plotly_dark")

if __name__ == '__main__':
    val1 = st.text_input('processing cost')
    val2 = st.text_input('mechanical properties')

    val3 = st.text_input('chemical stability')

    val4 = st.text_input('thermal stability')

    val5 = st.text_input('device integration')

    if st.button("Generate Chart"):
        st.write(radar_chart(val1, val2, val3, val4, val5))