import time
from github import Github, Auth
import streamlit as st

st.title("CodieAI") 
st.image("Magnifying_glass_icon.svg", width=30)
st.subheader("The WEBSEARCH 1.2")

tab1, tab2, tab3 = st.tabs(["WEBSEARCH 1.2", "REPORT", "About"])

#if you continue this project, expand these lists into Databases, and ofcourse improve the code
safe_websites = [("https://amazon.com"), ("https://google.com"), ("https://codieai.weebly.com"), ("https://grps.org"), ("https://wikipidea.org"), ("https://github.com"), ("https://stackoverflow.com")]
scary_websites = [("https://scamsite.com"), ("https://badwebsite.com"), ("https://free-robux.com")]
Threats_possible = [("https://youtube.com"),("https://twitter.com"),("https://facebook.com"),("https://instagram.com"),("https://tiktok.com"),("https://reddit.com")]
with tab1:
    WEBSEARCH = st.text_input("Search websites")
    if __name__=="__main__":
        if WEBSEARCH == "":
            st.write("Please enter a website to search")
        if WEBSEARCH != "":
            if "https://" not in WEBSEARCH:
                st.write("Please add 'https://' to the beginning of the link")
            if "https://" in WEBSEARCH:
                if WEBSEARCH in safe_websites:
                    st.write(f"{WEBSEARCH}  is a SAFE website, thanks for using our service :3")
                if WEBSEARCH in Threats_possible:
                    st.write(f"{WEBSEARCH}  itself is a safe website, but media hosted on this website may be unsafe.")
                if WEBSEARCH in scary_websites:
                    st.write("This website is NOT SAFE, proceed at your own risk.")
                if WEBSEARCH not in safe_websites and WEBSEARCH not in scary_websites:
                   st.write("Website is not registered in our database, please proceed with caution, and report the site to our company")
    st.write("Questions? Contact us at zacarias-d@students.grps.org or williams-l@students.grps.org")

with tab3:
    st.write("CodieAI is just a concept until now, and yet to be really worked on. And in a near future, we might be bringing this idea to life!")
    st.write("WEBSEARCH programmed by Danny Z. , concept by Levi W. As of right now,  this project is open source, and it's repository can be found here https://github.com/kumi774/CODiE-AI, if you must use, modify, remix, copy, or re-destribute this project, please credit our original work."
    "This project is under the CC BY-NC 4.0 license, learn more here https://creativecommons.org/licenses/by-nc/4.0/.")
    st.write("'magnifying_glass_icon.svg' is a copyright free work, available at https://commons.wikimedia.org/wiki/File:Magnifying_glass_icon.svg")

COOLDOWN = 0

with tab2:
        st.write("If you want to report a website, please don't hesitate, report it when you feel like you need.")
        WEBREPORT = st.text_input("Report a website here")
        st.write("If you want to report more than one site, please seperate them with a comma (,)")
        if "https://" not in WEBREPORT:
            st.write("please add 'https://' to the beginning of the link")
        if "https://" in WEBREPORT:
            if WEBREPORT != "":
                if WEBREPORT in safe_websites and WEBREPORT in scary_websites and WEBREPORT in Threats_possible:
                    st.write("this website has been registered already")
                if WEBREPORT not in safe_websites and WEBREPORT not in scary_websites and WEBREPORT not in Threats_possible:
                    if "," not in WEBREPORT:
                        st.write(f"Thank you for reporting {WEBREPORT}, we will look into it as soon as possible.")
                        with open("reported_sites.txt", "a") as f:
                            f.write(f"{WEBREPORT} is to be reviewed\n")
                    if "," in WEBREPORT:
                        st.write("These website will probably be reviewed soon :3")
                        with open("reported_sites.txt", "a") as f:
                            for site in WEBREPORT.split(", "):
                                f.write(f"{site} is to be reviewed\n")


auth = Auth.Token("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")
g = Github(auth=auth)

repo = g.get_repo("kumi774/CODiE-AI")
file = repo.get_contents("CODiE-AI/reported_sites.txt", ref="main")

current_text = file.decoded_content.decode("utf-8")
updated_text = current_text + f"{WEBREPORT} is to be revised\n"

repo.update_file(
    path=file.path,
    message="Automated site report update",
    content=updated_text,
    sha=file.sha,
    branch="main"
)
