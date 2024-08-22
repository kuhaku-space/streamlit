import streamlit as st

st.title("widget")
st.button("button")  # ボタン
st.selectbox("selectbox", ("select1", "select2"))  # セレクトボックス
st.multiselect(
    "multiselectbox", ("select1", "select2")
)  # 複数選択可能なセレクトボックス
st.radio("radiobutton", ("radio1", "radio2"))  # ラジオボタン
st.text_input("text input")  # 文字入力(1行)
st.text_area("text area")  # 文字入力(複数行)
st.slider("slider", 0, 100, 50)  # スライダー
st.file_uploader("Choose file")  # ファイルアップロード
