import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(
       
        page_title="Framework Calidad IA",
        page_icon="bot.png",
    )

    st.title("Framework IA Release 1.0")
    st.image("Framework.png")
    st.image("iaFramework.png" , width=140  )
    st.write("Bienvenido al Bot de IA!")



    components.iframe("https://www.chatbase.co/chatbot-iframe/1iefHFyX9Jzx6bU577Mhb")



if __name__ == "__main__":
    main()
