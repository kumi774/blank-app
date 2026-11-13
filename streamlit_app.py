import streamlit as st

st.title("CodieAI") 
st.image("Magnifying_glass_icon.svg", width=30)
st.subheader("The WEBSEARCH 1.2")

tab1, tab2 = st.tabs(["WEBSEARCH 1.2", "About"])

#if you continue this project, expand these lists into Databases, and ofcourse improve the code
safe_websites = [("amazon.com"), ("google.com"), ("codieai.weebly.com"), ("grps.org")]
scary_websites = [("scamsite.com"), ("badwebsite.com"), ("free-robux.com")]
Threats_possible = [("youtube.com"),("twitter.com"),("facebook.com"),("instagram.com"),("tiktok.com"),("reddit.com")]
with tab1:
    WEBSEARCH = st.text_input("Search websites")
    if __name__=="__main__":
        if WEBSEARCH == "":
            st.write("Please enter a website to search")
        if WEBSEARCH != "":
            if WEBSEARCH in safe_websites:
                st.write(f"https://{WEBSEARCH}  is a SAFE website, thanks for using our service :3")
            if WEBSEARCH in Threats_possible:
                st.write(f"https://{WEBSEARCH}  itself is a safe website, but media hosted on this website may be unsafe.")
            if WEBSEARCH in scary_websites:
                st.write("This website is NOT SAFE, proceed at your own risk.")
            if WEBSEARCH not in safe_websites and WEBSEARCH not in scary_websites and websearch not in Threats_possible:
                st.write("Website is not registered in our database, please proceed with caution, and report the site to our company")
    st.write("Questions? Contact us at zacarias-d@students.grps.org or williams-l@students.grps.org")

with tab2:
    st.write("CodieAI is just a concept until now, and yet to be really worked on. And in a near future, we might be bringing this idea to life!")
    st.write("WEBSEARCH programmed by Danny Z. , concept by Levi W.")
    st.write("In no way is CodieAI a legally trademarked name.")
    st.write("'magnifying_glass_icon.svg' is a copyright free work, available at https://commons.wikimedia.org/wiki/File:Magnifying_glass_icon.svg")

