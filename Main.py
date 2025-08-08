# portal_app_pro.py
# -*- coding: utf-8 -*-

"""
Script Principal para el Portal de Aplicaciones Empresariales.
Este dashboard centraliza el acceso a todas las herramientas internas de la compañía,
proporcionando una interfaz de usuario limpia, profesional y fácil de usar.

Autor: [Tu Nombre]
Versión: 3.2 | Edición PRO con Audio Reubicado para Mayor Relevancia
"""

import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# ======================================================================================
# --- CONFIGURACIÓN DE LA PÁGINA ---
# ======================================================================================
st.set_page_config(
    page_title="Suite Empresarial | FERREINOX SAS BIC",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ======================================================================================
# --- URLs DE LOS AUDIOS EXPLICATIVOS (FORMATO RAW) ---
# ======================================================================================
# Nota: Las URLs de GitHub se han convertido a su formato "raw" para acceso directo.
AUDIO_INVENTARIO = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_tablero_abastecimiento_final.mp3"
AUDIO_VENTAS = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_tablero_ventas.mp3"
AUDIO_CARTERA = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_gestion_cartera.mp3"
AUDIO_COTIZADOR = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_cotizador_ferreinox.mp3"
AUDIO_DATOS = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_autorizacion_de_datos.mp3"
AUDIO_CONTEO = "https://raw.githubusercontent.com/DiegoMao201/Tablero_Ferreinox/1405301b1a2eb6702e877b3523b8d0f7ba08cfd6/explicacion_inventarios_conteo.mp3"


# ======================================================================================
# --- FUNCIÓN PARA CARGAR IMÁGENES COMO BASE64 ---
# ======================================================================================
def img_to_base64(img_path):
    """Convierte una imagen a base64 para incrustarla en CSS/HTML."""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ======================================================================================
# --- ESTILOS CSS PERSONALIZADOS AVANZADOS ---
# ======================================================================================
try:
    # Carga las imágenes de apoyo para las tarjetas
    INVENTORY_IMG = img_to_base64("img/inventory.png")
    SALES_IMG = img_to_base64("img/sales.png")
    PORTFOLIO_IMG = img_to_base64("img/portfolio.png")
    QUOTES_IMG = img_to_base64("img/quotes.png")
    PRIVACY_IMG = img_to_base64("img/privacy.png")
    COUNT_IMG = img_to_base64("img/count.png")

    st.markdown(f"""
    <style>
        /* --- Estilo General --- */
        .stApp {{
            background-color: #F0F2F6;
        }}

        /* --- Contenedores de las tarjetas --- */
        .card {{
            border-radius: 15px;
            border: 1px solid #e6e6e6;
            box-shadow: 0 4px 12px 0 rgba(0,0,0,0.08);
            transition: all 0.3s ease-in-out;
            background-color: #FFFFFF;
            padding: 2rem;
            display: flex;
            align-items: center;
        }}
        .card:hover {{
            box-shadow: 0 8px 24px 0 rgba(0,0,0,0.15);
            transform: translateY(-5px);
            border: 1px solid #FF6B6B;
        }}

        /* --- Columna derecha con botón e imagen --- */
        .cta-column {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}

        /* --- Estilo del botón principal (link) --- */
        .stLinkButton a {{
            border-radius: 50px !important;
            font-weight: bold !important;
            color: #FFFFFF !important;
            background-image: linear-gradient(45deg, #FF6B6B 0%, #FF8E53 100%);
            transition: all 0.3s ease-in-out !important;
            border: none !important;
            box-shadow: 0 4px 12px 0 rgba(255,107,107,0.4);
            padding: 12px 25px !important;
            text-align: center;
            width: 100%;
        }}
        .stLinkButton a:hover {{
            transform: scale(1.05);
            box-shadow: 0 6px 20px 0 rgba(255,107,107,0.6);
            color: #FFFFFF !important;
        }}
        
        /* --- Imágenes de apoyo debajo del botón --- */
        .support-image {{
            margin-top: 2rem;
            width: 80%;
            max-width: 200px;
            opacity: 0.8;
            transition: opacity 0.3s ease-in-out;
        }}
        .card:hover .support-image {{
            opacity: 1;
        }}

        /* --- Títulos y Encabezados --- */
        h1, h2 {{
            color: #002B49;
            font-family: 'Helvetica', 'Arial', sans-serif;
        }}
        h2 {{
            color: #0056b3;
        }}

        /* --- INICIO DE CAMBIOS: NUEVOS ESTILOS PARA AUDIO --- */
        
        /* Contenedor del botón de audio en la cabecera de la tarjeta */
        .header-audio-container {{
            text-align: right;
            margin-top: -15px; /* Ajuste para alinear verticalmente con el título */
        }}

        /* Estilo para el botón de audio normal */
        .header-audio-container .stButton > button {{
            border-radius: 50px !important;
            font-weight: bold !important;
            color: #0056b3 !important; /* Texto azul */
            background-color: #E6F2FF !important; /* Fondo azul claro */
            transition: all 0.3s ease-in-out !important;
            border: 1px solid #B3D7FF !important; /* Borde azul más claro */
            box-shadow: none !important;
            padding: 8px 18px !important;
        }}

        /* Efecto hover para el botón de audio */
        .header-audio-container .stButton > button:hover {{
            transform: scale(1.05) !important;
            background-color: #0056b3 !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 12px rgba(0, 86, 179, 0.3) !important;
            border: 1px solid #0056b3 !important;
        }}

        /* --- FIN DE CAMBIOS --- */

        /* --- Contenedor para el reproductor de audio --- */
        .stAudio {{
            margin-top: 15px;
            background-color: #FAFAFA;
            border-radius: 10px;
            padding: 5px;
        }}
    </style>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Error: No se encontró la carpeta 'img' o las imágenes de apoyo. Por favor, créala y añade las imágenes para una experiencia visual completa.")

# ======================================================================================
# --- ENCABEZADO CON LOGO ---
# ======================================================================================
col1, col2, col3 = st.columns([2,3,2])
with col2:
    try:
        logo = Image.open("LOGO FERREINOX SAS BIC 2024.png")
        st.image(logo, use_container_width=True)
    except FileNotFoundError:
        st.title("🚀 Suite Empresarial FERREINOX")

st.markdown("<h1 style='text-align: center; color: #002B49;'>Suite de Herramientas Empresariales</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: #333;'>Bienvenido al centro de operaciones. Accede de forma segura y rápida a todas nuestras aplicaciones internas.</p>", unsafe_allow_html=True)
st.divider()

# ======================================================================================
# --- FUNCIÓN PARA CREAR TARJETAS (MODIFICADA PARA REUBICAR AUDIO) ---
# ======================================================================================
def create_card(icon, title, description_md, button_text, button_url, image_base64, audio_url):
    """
    Crea una tarjeta de aplicación con un layout mejorado.
    El botón de audio se reubica en la cabecera para mayor visibilidad.
    """
    # Usamos st.session_state para controlar la visibilidad del reproductor de audio
    audio_state_key = f"play_audio_{title.replace(' ', '_')}"
    if audio_state_key not in st.session_state:
        st.session_state[audio_state_key] = False

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        col1, col2 = st.columns((2, 1))

        with col1:
            # --- INICIO DE CAMBIOS: CABECERA CON TÍTULO Y BOTÓN DE AUDIO ---
            title_col, audio_col = st.columns([3, 1])

            with title_col:
                st.header(f"{icon} {title}")
            
            with audio_col:
                st.markdown('<div class="header-audio-container">', unsafe_allow_html=True)
                # Este botón cambia el estado para mostrar/ocultar el audio
                if st.button("🎧 Audio Explicativo", key=f"audio_btn_{title}"):
                    st.session_state[audio_state_key] = not st.session_state[audio_state_key]
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown(description_md)

            # El reproductor de audio solo aparece si el estado es True
            if st.session_state[audio_state_key]:
                st.audio(audio_url, format="audio/mp3")
            # --- FIN DE CAMBIOS ---

        with col2:
            st.markdown('<div class="cta-column">', unsafe_allow_html=True)
            st.link_button(f"➡️ {button_text}", button_url, use_container_width=True)
            st.markdown(f'<img src="data:image/png;base64,{image_base64}" class="support-image">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.write("") # Espacio entre tarjetas

# ======================================================================================
# --- DEFINICIÓN DEL CONTENIDO DE LAS TARJETAS ---
# ======================================================================================
# TARJETA 1
desc1 = """
**¿Qué es?** Una plataforma centralizada para la gestión y monitoreo en tiempo real de nuestro stock.
- **Niveles de Stock:** Cantidades exactas por SKU y almacén.
- **Valoración:** Costo total del inventario actual.
- **Alertas:** Notificaciones automáticas de stock bajo o sobrestock.
<br>
**¿Cómo aprovecharla?** Optimiza las compras, evita quiebres de stock y planifica la distribución.
"""
create_card("📦", "Control de Inventario", desc1, "Acceder a Inventario", "https://rotacion-iventarios-traslados-promociones.streamlit.app/", INVENTORY_IMG, AUDIO_INVENTARIO)

# TARJETA 2
desc2 = """
**¿Qué es?** Un dashboard interactivo que muestra el rendimiento de ventas a través de KPIs y gráficos.
- **Ventas Totales:** Ingresos por día, semana, mes y año.
- **Rendimiento:** Compara resultados por vendedor/región.
- **Productos Top:** Identifica los productos más vendidos.
<br>
**¿Cómo aprovecharla?** Toma decisiones comerciales informadas y ajusta estrategias en tiempo real.
"""
create_card("📈", "Seguimiento de Ventas", desc2, "Ver Dashboard", "https://resumen-ventas-gerenciales-estadisticos.streamlit.app/", SALES_IMG, AUDIO_VENTAS)

# TARJETA 3
desc3 = """
**¿Qué es?** Herramienta para el seguimiento detallado de las cuentas por cobrar y la salud financiera.
- **Edades de Vencimiento:** Clasificación de deuda (30, 60, 90+ días).
- **Estado de Cuentas:** Visualiza facturas pagadas, pendientes y vencidas.
- **Proyecciones de Cobro:** Estima los ingresos futuros.
<br>
**¿Cómo aprovecharla?** Mejora el flujo de caja, reduce riesgos y automatiza recordatorios.
"""
create_card("💰", "Gestión de Cartera", desc3, "Administrar Cartera", "https://cartera-gestion-reporte-conclusion.streamlit.app/", PORTFOLIO_IMG, AUDIO_CARTERA)

# TARJETA 4
desc4 = """
**¿Qué es?** Solución integral para crear, enviar y seguir cotizaciones, convirtiéndolas en pedidos.
- **Plantillas Personalizables:** Genera cotizaciones con la imagen de marca.
- **Historial de Versiones:** Rastrea cambios y negociaciones.
- **Tasa de Conversión:** Mide la efectividad de tus propuestas.
<br>
**¿Cómo aprovecharla?** Agiliza el ciclo de venta y proyecta una imagen más profesional.
"""
create_card("📝", "Cotizaciones y Pedidos", desc4, "Generar Cotización", "https://cotizador-presupuesto-precios.streamlit.app/", QUOTES_IMG, AUDIO_COTIZADOR)

# TARJETA 5
desc5 = """
**¿Qué es?** Plataforma para gestionar el consentimiento informado de datos de clientes y colaboradores.
- **Registro Centralizado:** Base de datos de consentimientos otorgados.
- **Gestión de Peticiones:** Atiende solicitudes de actualización o eliminación.
- **Trazabilidad:** Audita quién, cuándo y cómo se accedió a la información.
<br>
**¿Cómo aprovecharla?** Garantiza el cumplimiento legal (Habeas Data) y genera confianza.
"""
create_card("🔐", "Portal de Consentimiento", desc5, "Gestionar Datos", "https://formulario-de-actualicion-de-datos-mas-alla-del-color.streamlit.app/", PRIVACY_IMG, AUDIO_DATOS)

# TARJETA 6
desc6 = """
**¿Qué es?** App móvil/escritorio para facilitar y digitalizar el conteo físico de inventario en bodega.
- **Carga de Datos:** Importa la lista de productos a contar.
- **Registro en Vivo:** Ingresa las cantidades contadas en la app.
- **Reporte de Discrepancias:** Compara conteo físico vs. sistema.
<br>
**¿Cómo aprovecharla?** Reduce tiempo de auditoría, minimiza errores y obtén reportes al instante.
"""
create_card("🧮", "Asistente de Conteo Físico", desc6, "Iniciar Conteo", "https://conteo-inventario-fisico-ajuste-organizacional.streamlit.app/", COUNT_IMG, AUDIO_CONTEO)

# ======================================================================================
# --- PIE DE PÁGINA ---
# ======================================================================================
st.divider()
st.caption("© 2025 FERREINOX SAS BIC. Todos los derechos reservados. Desarrollado por el equipo de TI con ❤️.")
