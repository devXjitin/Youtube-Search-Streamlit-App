import streamlit as st
from youtube_search import YoutubeSearch
import json

st.set_page_config(
    page_title="Youtube Search",
    layout="wide"
)

# Embedded CSS styles
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .video-card {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .video-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .video-title {
        color: white;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .video-info {
        color: #606060;
        font-size: 14px;
        margin: 5px 0;
    }
    .video-channel {
        color: #065fd4;
        font-weight: 600;
    }
    .search-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        color: white;
        text-align: center;
    }
    .thumbnail-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%;
        margin-bottom: 15px;
        border-radius: 8px;
        overflow: hidden;
    }
    .thumbnail-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="search-header"><h1>Youtube Search</h1><p>Discover and explore YouTube videos</p></div>', unsafe_allow_html=True)

st.text_input("Search for videos on Youtube:", key="search_query", placeholder="Enter your search query...")
st.button("Search", key="search_button", type="primary")

def search_youtube(query):
    results = YoutubeSearch(query, max_results=10).to_json()
    return results

if st.session_state.get("search_button"):
    with st.spinner("Searching..."):
        query = st.session_state.get("search_query", "")
        if query:
            results = search_youtube(query)
            results = json.loads(results)
            result = results['videos']
            
            st.markdown(f"### Found {len(result)} results for '{query}'")
            
            # Display results in a grid layout
            cols = st.columns(2)
            
            for idx, item in enumerate(result):
                with cols[idx % 2]:
                    video_id = item['id']
                    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
                    
                    st.markdown(f"""
                        <div class="video-card">
                            <div class="thumbnail-container">
                                <iframe src="https://www.youtube.com/embed/{video_id}" 
                                        frameborder="0" 
                                        allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                        allowfullscreen>
                                </iframe>
                            </div>
                            <div class="video-title">{item['title']}</div>
                            <div class="video-info">
                                <span class="video-channel">{item['channel']}</span>
                            </div>
                            <div class="video-info">Duration: {item['duration']}</div>
                            <div class="video-info">Views: {item['views']}</div>
                            <div class="video-info">Published: {item.get('publish_time', 'N/A')}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
        else:
            st.warning("⚠️ Please enter a search query.")