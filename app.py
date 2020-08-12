import streamlit as st


def main():
    st.title('Minicurso Streamlit')

    st.header("UNIPE")

    st.subheader('Conhecendo o microframwork Streamlit')
    
    st.sidebar.subheader('Titulo sidebar')
    
    st.sidebar.slider('Escolha um valor')
    
    st.markdown("Calculando o quadrado de um numero")

    x = st.slider('Selecione um valor')
    
    st.write(x, 'O quadrado do valor é:', x * x)

if __name__ == '__main__':
    main()
