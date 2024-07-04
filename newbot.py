import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(
       
        page_title="Framework Calidad IA",
        page_icon="bot.png",
    )

    st.title("Framework IA Release 1.0")
    st.image("iaFramework.png" , width=140  )
    st.write("Bienvenido al Bot de IA!")



    with st.sidebar:
            st.title("Sistema de Calidad Bot de IA")
            st.image("Framework.png")



    components.iframe("https://www.chatbase.co/chatbot-iframe/1iefHFyX9Jzx6bU577Mhb", height=900 , width=600)



if __name__ == "__main__":
    main()
