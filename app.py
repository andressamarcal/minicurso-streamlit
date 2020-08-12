import streamlit as st


def main():
    st.title('Minicurso Streamlit')
    st.subheader('Conhecendo o microframwork Streamlit')
    st.sidebar.subheader('Titulo sidebar')
    st.sidebar.slider('Escolha um valor')


if __name__ == '__main__':
    main()
