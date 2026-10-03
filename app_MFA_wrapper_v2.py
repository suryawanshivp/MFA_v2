import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="MF Analyzer", layout="wide")

html = (Path(__file__).parent / "mf-analyzer.html").read_text(encoding="utf-8")
components.html(html, height=1400, scrolling=True)
