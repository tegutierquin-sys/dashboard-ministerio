import streamlit as st

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cuadro de Mando · Operadoras",
    page_icon="📊",
    layout="centered"
)

CONTRASENA_CORRECTA = "muyfacilmuylarga"
ENLACE_POWERBI = "https://app.powerbi.com/links/8l16NEHg_E?ctid=24e38255-2c42-4538-999c-5fd53e8456d2&pbi_source=linkShare"
LOGO_B64 = "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"

# ── ESTILOS ──────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(160deg, #003366 0%, #005A9C 60%, #F2C811 100%);
        }
        header[data-testid="stHeader"] { background: transparent; }
        .tarjeta {
            background: white;
            border-radius: 12px;
            padding: 40px 48px;
            max-width: 480px;
            margin: 40px auto;
            box-shadow: 0 8px 32px rgba(0,0,0,0.25);
        }
        .logo-container { text-align: center; margin-bottom: 24px; }
        .titulo-principal {
            font-size: 1.3rem; font-weight: 700; color: #003366;
            text-align: center; line-height: 1.4; margin-bottom: 4px;
        }
        .subtitulo-principal {
            font-size: 1rem; color: #005A9C; text-align: center;
            font-weight: 600; margin-bottom: 24px;
        }
        .separador { border: none; border-top: 2px solid #F2C811; margin: 16px 0 24px 0; }
        .label-acceso { font-size: 0.85rem; color: #666; margin-bottom: 8px; text-align: center; }
        .pie { text-align: center; font-size: 0.75rem; color: #999; margin-top: 24px; }
        .stButton > button {
            background-color: #003366 !important; color: white !important;
            border: none !important; border-radius: 6px !important;
            font-weight: 600 !important; padding: 10px !important; width: 100%;
        }
        .stButton > button:hover { background-color: #005A9C !important; }
        .btn-dashboard {
            display: inline-block; background-color: #F2C811; color: #003366 !important;
            font-weight: 700; font-size: 1.05rem; padding: 14px 32px;
            border-radius: 8px; text-decoration: none; margin-top: 16px;
        }
        .btn-dashboard:hover { background-color: #e0b800; }
    </style>
""", unsafe_allow_html=True)

# ── ESTADO ───────────────────────────────────────────────────────────────────
if "acceso_ok" not in st.session_state:
    st.session_state.acceso_ok = False

# ── LOGIN ─────────────────────────────────────────────────────────────────────
if not st.session_state.acceso_ok:
    st.markdown(f"""
        <div class="tarjeta">
            <div class="logo-container">
                <img src="data:image/png;base64,{LOGO_B64}" width="320" />
            </div>
            <hr class="separador"/>
            <p class="titulo-principal">Cuadro de Mando · Operadoras</p>
            <p class="subtitulo-principal">Principales Magnitudes</p>
            <p class="label-acceso">Introduce la contraseña para acceder</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        contrasena = st.text_input("Contraseña", type="password",
                                   label_visibility="collapsed",
                                   placeholder="Contraseña...")
        if st.button("Entrar", use_container_width=True):
            if contrasena == CONTRASENA_CORRECTA:
                st.session_state.acceso_ok = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta.")

    st.markdown("""
        <p style="text-align:center; font-size:0.75rem; color:rgba(255,255,255,0.7); margin-top:16px;">
        S.G. de Análisis del Mercado y Evolución Tecnológica
        </p>
    """, unsafe_allow_html=True)

# ── TRAS LOGIN ────────────────────────────────────────────────────────────────
else:
    st.markdown(f"""
        <div class="tarjeta">
            <div class="logo-container">
                <img src="data:image/png;base64,{LOGO_B64}" width="320" />
            </div>
            <hr class="separador"/>
            <p class="titulo-principal">Cuadro de Mando · Operadoras</p>
            <p class="subtitulo-principal">Principales Magnitudes</p>
            <p class="label-acceso">Acceso verificado. Haz clic para abrir el dashboard.</p>
            <div style="text-align:center;">
                <a href="{ENLACE_POWERBI}" target="_blank" class="btn-dashboard">
                    📊 Abrir Dashboard
                </a>
            </div>
            <p class="pie">S.G. de Análisis del Mercado y Evolución Tecnológica</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Cerrar sesión", use_container_width=True):
            st.session_state.acceso_ok = False
            st.rerun()
