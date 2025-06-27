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
# --- GNEWS INTEGRATION ---
gnews_key = "ccc546ad66ec22944f00818ef829bd8b"
gnews_url = "https://gnews.io/api/v4/search"
gnews_params = {
    "q": "maritime rescue OR coast guard OR search and rescue",
    "lang": "en",
    "max": 5,
    "token": gnews_key
}

st.markdown("## 📰 Additional Articles from GNews")

gnews_response = requests.get(gnews_url, params=gnews_params)
if gnews_response.status_code == 200:
    gnews_articles = gnews_response.json().get("articles", [])
    for article in gnews_articles:
        st.subheader(article["title"])
        st.write(f"🕒 Published At: {article['publishedAt']}")
        st.markdown(f"[Read Full Article]({article['url']})")
        st.markdown("---")
else:
    st.error(f"GNews API error: {gnews_response.status_code} - {gnews_response.text}")
