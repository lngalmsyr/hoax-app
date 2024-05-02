import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from st_pages import add_page_title
import time

add_page_title(layout="wide")

colored_header(
    label="Data Berita Palsu/Hoax",
    description="",
    color_name="violet-70",
)

start_time = time.time()

# Assuming 'df' is your DataFrame containing news data
df = pd.read_csv('./assets/df.csv') # Replace with your actual file path
#ambil df yang datanya berlabelkan positive saja, hapus index
df=df[df['label']=='positive'].reset_index(drop=True)

# Select only the relevant columns (judul, tanggal, url)
relevant_columns = ["judul", "date", "url"]  # Adjust column names as needed
filtered_df = df[relevant_columns]

# Display the filtered DataFrame using dataframe_explorer for interactivity
filtered_df = dataframe_explorer(filtered_df, case=False)
st.dataframe(filtered_df, use_container_width=True)

end_time = time.time()
execution_time = end_time - start_time

st.warning(f"Memerlukan waktu {execution_time:.2f} detik untuk dieksekusi.")