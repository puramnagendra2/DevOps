import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Puram Nagendra", page_icon=":material/all_inclusive:", layout="wide")

# Heading


st.title(":blue[Puram Nagendra]")
st.subheader(":material/all_inclusive: DevOps Engineer")

ln, gh, ig, emp = st.columns([1, 1, 1, 8])

with st.popover("Social Media"):
    st.link_button(label="🔗 LinkedIn", url="https://www.linkedin.com/in/puramnagendra2", type="primary")
    st.link_button(label="GitHub", url="https://www.github.com/puramnagendra2", type="primary")
    st.link_button(label="Instagram", url="https://www.instagram.com/nandu_2322", type="primary")


# Education

st.subheader(":blue[Education]")

details, lottie = st.columns([2, 1], gap="medium")


with details:
    with st.container(border=True):
        st.subheader(":rainbow[Post Graduation]")
        st.subheader("Master of Computer applications (MCA)")
        st.write("Madanapalle Institute of Technology & Science")

        st.divider()

        st.subheader(":rainbow[Under Graduation]")
        st.subheader("Bachelor of Computer Applications (BCA)")
        st.write("SJES College of Management Studies")

with lottie:
    st.header("Lottie Here")

# Technical Skills
st.subheader(":blue[Skills]")

# Projects
st.subheader(":blue[Projects]")

# Articles & Essays
st.subheader(":blue[Articles & Essays]")

# Gallery
st.subheader(":blue[Gallery]")

# Resume
st.subheader(":blue[Resume]")

# Contact
st.subheader(":blue[Contact Me]")
