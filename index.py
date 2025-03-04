import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import glob
import os
import fontawesome as fs

st.set_page_config(page_title="Puram Nagendra", page_icon=":material/all_inclusive:", layout="wide")

# Functions

# Lottie Function
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

edu_lottie = load_lottie(r"https://lottie.host/bf834b4a-1768-4911-9052-d36147e6880a/gCAd4tXBPT.json")

# Pages
# Function to load latest blogs
def load_latest_blogs(menu):
    """Load the latest N blog files from the BLOG_DIR"""
    blog_files = sorted(glob.glob(os.path.join(BLOG_DIR+"/"+menu, "*.md")), key=os.path.getmtime, reverse=True)
    return blog_files

# Heading
st.title(":blue[:material/all_inclusive: DevOps Discussed]")


menu = option_menu(menu_title=None,
                    orientation="horizontal",
                    options=["Ansible", "GitHub Actions", "Terraform", "Docker", "Kubernetes"],
                    icons=["ansible", "actions", "terraform", "docker", "kubernetes"],
                    menu_icon="",
                    styles={
                        "nav-link-selected": {"background-color": "#0068C9", "color": "white", "cursor": "default"}
                    })
BLOG_DIR = "blogs"
blog_files = load_latest_blogs(menu)


if not blog_files:
    st.warning("No blogs found.")
else:
    for file in blog_files:
        with open(file, "r", encoding="utf-8") as f:
            blog_content = f.read()
        
        # Extract the blog title (assuming first line is the title)
        blog_lines = blog_content.split("\n")
        title = blog_lines[0].replace("# ", "") if blog_lines[0].startswith("#") else "Untitled"

        # Display blog details
        with st.expander(f"{title}"):
            st.markdown(blog_content, unsafe_allow_html=True)