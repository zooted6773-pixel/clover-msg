import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (넓게 보기)
st.set_page_config(layout="wide", page_title="클로버 학원 문자 생성기")

# HTML 파일 읽기
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# 앱 실행
html_code = load_html()

# 화면에 표시 (height는 화면 길이에 맞춰 넉넉하게 1200으로 잡음)
components.html(html_code, height=1200, scrolling=True)