import streamlit as st

# ── CONFIGURACIÓN DE LA PÁGINA ──────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Ministerio",
    page_icon="📊",
    layout="centered"
)

# ── CONTRASEÑA Y ENLACE ───────────────────────────────────────────────────────
CONTRASENA_CORRECTA = "muyfacilmuylarga"  # ← Cambia esto cuando quieras
ENLACE_POWERBI = "https://app.powerbi.com/links/4JxHThc4_P?ctid=24e38255-2c42-4538-999c-5fd53e8456d2&pbi_source=linkShare"

# ── ESTILOS ───────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .titulo {
            font-size: 2rem;
            font-weight: 700;
            color: #1a1a2e;
            margin-bottom: 0.2rem;
        }
        .subtitulo {
            color: #666;
            margin-bottom: 2rem;
            font-size: 0.95rem;
        }
        .enlace-grande {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 14px 28px;
            background-color: #F2C811;
            color: #1a1a2e !important;
            font-weight: 700;
            font-size: 1.1rem;
            border-radius: 6px;
            text-decoration: none;
        }
        .enlace-grande:hover {
            background-color: #e0b800;
        }
    </style>
""", unsafe_allow_html=True)

# ── LÓGICA DE ACCESO ──────────────────────────────────────────────────────────
if "acceso_ok" not in st.session_state:
    st.session_state.acceso_ok = False

if not st.session_state.acceso_ok:

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="titulo">📊 Dashboard Ministerio</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Introduce la contraseña para acceder</p>', unsafe_allow_html=True)

    contrasena = st.text_input("Contraseña", type="password", label_visibility="collapsed", placeholder="Contraseña...")

    if st.button("Entrar", use_container_width=True):
        if contrasena == CONTRASENA_CORRECTA:
            st.session_state.acceso_ok = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta. Inténtalo de nuevo.")

else:
    # ── PANTALLA TRAS LOGIN ───────────────────────────────────────────────────
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="titulo">Dashboard Ministerio</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Haz clic en el botón para abrir el dashboard en una nueva pestaña.</p>', unsafe_allow_html=True)

    st.markdown(
        f'<a href="{ENLACE_POWERBI}" target="_blank" class="enlace-grande">Abrir Dashboard</a>',
        unsafe_allow_html=True
    )

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    if st.button("Cerrar sesión"):
        st.session_state.acceso_ok = False
        st.rerun()
