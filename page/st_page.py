from utils import st_mo as stm
import streamlit as st

def app():
	st.write(' 1번을 선택했습니다')
	df = stm.get_movie()
	st.dataframe(df)
