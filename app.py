import streamlit as st

# Inicializar estado
if "historico" not in st.session_state:
    st.session_state.historico = []

if "saldo" not in st.session_state:
    st.session_state.saldo = 0.0

st.title("💬 Controle Financeiro Chat")

# Mostrar histórico
for msg in st.session_state.historico:
    st.write(msg)

# Entrada do usuário
user_input = st.text_input("Digite sua mensagem:")

def processar_input(texto):
    texto = texto.lower()

    if "gastei" in texto:
        try:
            valor = float(texto.split(" ")[1])
            st.session_state.saldo -= valor
            return f"💸 Gasto registrado: R${valor:.2f}"
        except:
            return "❌ Não entendi o valor."

    elif "recebi" in texto:
        try:
            valor = float(texto.split(" ")[1])
            st.session_state.saldo += valor
            return f"💰 Receita registrada: R${valor:.2f}"
        except:
            return "❌ Não entendi o valor."

    elif "saldo" in texto:
        return f"📊 Seu saldo é: R${st.session_state.saldo:.2f}"

    else:
        return "🤖 Não entendi. Tente: 'gastei 50' ou 'recebi 100'"

# Processar mensagem
if user_input:
    resposta = processar_input(user_input)

    st.session_state.historico.append(f"Você: {user_input}")
    st.session_state.historico.append(f"Bot: {resposta}")

    st.rerun()