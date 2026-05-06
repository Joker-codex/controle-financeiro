import streamlit as st

st.set_page_config(page_title="Chat Financeiro", layout="centered")

# Estado
if "historico" not in st.session_state:
    st.session_state.historico = []

if "saldo" not in st.session_state:
    st.session_state.saldo = 0.0

# CSS estilo WhatsApp
st.markdown("""
<style>
.chat-container {
    max-width: 600px;
    margin: auto;
}

.msg {
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px 0;
    max-width: 70%;
    display: inline-block;
}

.user {
    background-color: #DCF8C6;
    align-self: flex-end;
    float: right;
    clear: both;
}

.bot {
    background-color: #EAEAEA;
    float: left;
    clear: both;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 Chat Financeiro")

def processar(texto):
    texto = texto.lower()

    if "gastei" in texto:
        try:
            valor = float(texto.split(" ")[1])
            st.session_state.saldo -= valor
            return f"💸 Gasto: R${valor:.2f}"
        except:
            return "❌ Não entendi o valor"

    elif "recebi" in texto:
        try:
            valor = float(texto.split(" ")[1])
            st.session_state.saldo += valor
            return f"💰 Receita: R${valor:.2f}"
        except:
            return "❌ Não entendi o valor"

    elif "saldo" in texto:
        return f"📊 Saldo: R${st.session_state.saldo:.2f}"

    return "🤖 Use: gastei 50 | recebi 100 | saldo"

# Exibir mensagens
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for tipo, msg in st.session_state.historico:
    classe = "user" if tipo == "user" else "bot"
    st.markdown(f'<div class="msg {classe}">{msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input
user_input = st.text_input("Digite sua mensagem", key="input")

if user_input:
    resposta = processar(user_input)

    st.session_state.historico.append(("user", user_input))
    st.session_state.historico.append(("bot", resposta))

    st.rerun()
