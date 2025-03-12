# package-install
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Hello, This is Promotion Management")
st.write("これは簡単なStreamlitアプリです。")

# ユーザー入力
name = st.text_input("名前を入力してください")
if name:
    st.write(f"こんにちは、{name}さん！")

# スライダー
age = st.slider("年齢を選択", 0, 100, 25)
st.write(f"あなたの年齢: {age}")

# ボタン
if st.button("クリックしてメッセージを表示"):
    st.success("ボタンが押されました！")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# ダミーデータ
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# 折れ線グラフ
st.line_chart(df)

from st_aggrid import AgGrid, GridOptionsBuilder

# ダミーデータ
df = pd.DataFrame({
    "名前": ["田中", "佐藤", "鈴木"],
    "年齢": [25, 30, 35],
    "スコア": [80, 90, 85]
})

# Gridの設定
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_default_column(editable=True)  # 全カラムを編集可能に
builder.configure_side_bar()  # サイドバーを追加（オプション）
grid_options = builder.build()

# 編集可能なテーブルを表示
grid_response = AgGrid(df, gridOptions=grid_options, update_mode="VALUE_CHANGED")

# 変更後のデータ
updated_df = grid_response["data"]


# ダミーデータ
df = pd.DataFrame({
    "名前": ["田中", "佐藤", "鈴木"],
    "年齢": [25, 30, 35],
    "スコア": [80, 90, 85]
})

# 編集可能なテーブル
edited_df = st.data_editor(df, num_rows="dynamic")

# 変更後のデータを表示
st.write("更新後のデータ:", edited_df)
