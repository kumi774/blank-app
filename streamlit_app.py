import streamlit as st

st.title("CodieAI")
st.title("The WEBSEARCH 1.2")

WEBSEARCH = st.text_input("Search websites")

safe_websites = [("amazon.com"), ("youtube.com")]
scary_websites = [("scam.com"), ("67.com"), ("scammer.com")]

if __name__=="__main__":
    if WEBSEARCH in safe_websites:
        st.write(f"https://{WEBSEARCH}  is a SAFE website, thanks for using our service :3")
    if WEBSEARCH in scary_websites:
        st.write("This website is NOT SAFE, proceed at your own risk.")
    if WEBSEARCH not in safe_websites and WEBSEARCH not in scary_websites:
        st.write("Website is not registered in our database, please proceed with caution, and report the site to our company")
        st.write("Contact us at contact@codieai.com,"
        "or call us at 1-800-CODIEAI")
