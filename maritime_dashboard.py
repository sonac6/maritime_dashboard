import requests
import streamlit as st

# --- CONFIG ---
api_key = "54079127880843c089a688daed764cf6"
url = "https://newsapi.org/v2/everything"
params = {
    "q": "maritime rescue OR coast guard OR search and rescue",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": api_key
}

# --- STREAMLIT UI ---
st.set_page_config(page_title="Maritime Rescue Feed", layout="wide")
st.title("🛟 Live Maritime Rescue News Dashboard")

# --- DATA FETCH ---
response = requests.get(url, params=params)

if response.status_code != 200:
    st.error(f"Error {response.status_code}: {response.text}")
else:
    articles = response.json().get("articles", [])
    for article in articles:
        st.subheader(article["title"])
        st.write(f"🕒 Published At: {article['publishedAt']}")
        st.markdown(f"[Read Full Article]({article['url']})")
        st.markdown("---")
