# portal_app.py
# -*- coding: utf-8 -*-

"""
Script Principal para el Portal de Aplicaciones Empresariales.
Este dashboard centraliza el acceso a todas las herramientas internas de la compañía,
proporcionando una interfaz de usuario limpia, profesional y fácil de usar.
Autor: [Tu Nombre]
Versión: 1.0
"""

import streamlit as st

# ======================================================================================
# --- CONFIGURACIÓN DE LA PÁGINA ---
# Esto debe ser el primer comando de Streamlit en tu script.
# ======================================================================================
st.set_page_config(
    page_title="Suite Empresarial | Portal de Aplicaciones",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ======================================================================================
# --- TÍTULO Y ENCABEZADO ---
# ======================================================================================
st.title("🚀 Suite de Herramientas Empresariales")
st.markdown("""
Bienvenido al centro de operaciones de nuestra compañía. Desde este portal puedes acceder de forma segura y rápida a todas nuestras aplicaciones internas.
Cada herramienta ha sido diseñada para optimizar nuestros procesos y potenciar la toma de decisiones basada en datos.
""")
st.divider()

# ======================================================================================
# --- TARJETA 1: CONTROL DE INVENTARIO ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1)) # Divide el contenedor en 2/3 para texto y 1/3 para el botón

    with col1:
        st.header("📦 Control de Inventario")
        st.markdown("""
        **¿Qué es?**
        Una plataforma centralizada para la gestión y monitoreo en tiempo real de todo nuestro stock. Visualiza niveles de inventario, movimientos y valoraciones.

        **Información Clave:**
        - **Niveles de Stock:** Cantidades exactas por SKU y por almacén.
        - **Valoración:** Costo total del inventario actual.
        - **Alertas:** Notificaciones automáticas de stock bajo o sobrestock.

        **¿Cómo aprovecharla?**
        Optimiza las compras, evita quiebres de stock y planifica la distribución de productos de manera eficiente.
        """)

    with col2:
        st.write(" ") # Espacio para alinear verticalmente
        st.write(" ")
        st.link_button(
            "Acceder a Inventario",
            "https://tu-link-aqui.streamlit.app/inventario", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- TARJETA 2: SEGUIMIENTO DE VENTAS ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1))

    with col1:
        st.header("📈 Seguimiento de Ventas")
        st.markdown("""
        **¿Qué es?**
        Un dashboard interactivo que muestra el rendimiento de ventas a través de KPIs (Indicadores Clave de Rendimiento) y gráficos dinámicos.

        **Información Clave:**
        - **Ventas Totales:** Ingresos por día, semana, mes y año.
        - **Rendimiento por Vendedor/Región:** Compara resultados y detecta oportunidades.
        - **Productos Top:** Identifica los productos más vendidos.

        **¿Cómo aprovecharla?**
        Toma decisiones comerciales informadas, motiva al equipo de ventas con datos transparentes y ajusta estrategias en tiempo real.
        """)
    with col2:
        st.write(" ")
        st.write(" ")
        st.link_button(
            "Ver Dashboard de Ventas",
            "https://tu-link-aqui.streamlit.app/ventas", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- TARJETA 3: GESTIÓN DE CARTERA ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1))

    with col1:
        st.header("💰 Gestión de Cartera")
        st.markdown("""
        **¿Qué es?**
        Herramienta para el seguimiento detallado de las cuentas por cobrar, gestionando la salud financiera y el flujo de caja de la empresa.

        **Información Clave:**
        - **Edades de Vencimiento:** Clasificación de la deuda por antigüedad (30, 60, 90+ días).
        - **Estado de Cuentas:** Visualiza facturas pagadas, pendientes y vencidas por cliente.
        - **Proyecciones de Cobro:** Estima los ingresos futuros basados en el historial de pagos.

        **¿Cómo aprovecharla?**
        Mejora el flujo de caja, reduce el riesgo de incobrabilidad y automatiza los recordatorios de pago a clientes.
        """)

    with col2:
        st.write(" ")
        st.write(" ")
        st.link_button(
            "Administrar Cartera",
            "https://tu-link-aqui.streamlit.app/cartera", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- TARJETA 4: COTIZACIONES Y PEDIDOS ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1))

    with col1:
        st.header("📝 Cotizaciones y Pedidos")
        st.markdown("""
        **¿Qué es?**
        Una solución integral para crear, enviar y dar seguimiento a cotizaciones profesionales, y convertirlas fácilmente en pedidos de venta.

        **Información Clave:**
        - **Plantillas Personalizables:** Genera cotizaciones con la imagen de la marca en segundos.
        - **Historial de Versiones:** Rastrea cambios y negociaciones con el cliente.
        - **Tasa de Conversión:** Mide la efectividad de tus propuestas comerciales.

        **¿Cómo aprovecharla?**
        Agiliza el ciclo de venta, proyecta una imagen más profesional y centraliza la comunicación comercial.
        """)

    with col2:
        st.write(" ")
        st.write(" ")
        st.link_button(
            "Generar Cotización",
            "https://tu-link-aqui.streamlit.app/cotizaciones", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- TARJETA 5: GESTIÓN DE PRIVACIDAD (Habeas Data) ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1))

    with col1:
        st.header("🔐 Portal de Consentimiento de Datos")
        st.markdown("""
        **¿Qué es?**
        Plataforma para gestionar el consentimiento informado de clientes y colaboradores, asegurando el cumplimiento de las normativas de protección de datos (Habeas Data).

        **Información Clave:**
        - **Registro Centralizado:** Base de datos de todos los consentimientos otorgados.
        - **Gestión de Peticiones:** Atiende solicitudes de actualización o eliminación de datos.
        - **Trazabilidad:** Audita quién, cuándo y cómo se accedió a la información personal.

        **¿Cómo aprovecharla?**
        Garantiza el cumplimiento legal, genera confianza en tus clientes y protege a la empresa de riesgos y sanciones.
        """)
    with col2:
        st.write(" ")
        st.write(" ")
        st.link_button(
            "Gestionar Consentimientos",
            "https://tu-link-aqui.streamlit.app/privacidad", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- TARJETA 6: ASISTENTE DE CONTEO FÍSICO ---
# ======================================================================================
with st.container(border=True):
    col1, col2 = st.columns((2, 1))

    with col1:
        st.header("🧮 Asistente de Conteo Físico")
        st.markdown("""
        **¿Qué es?**
        Una aplicación móvil y de escritorio diseñada para facilitar y digitalizar el proceso de conteo físico de inventario en bodega.

        **Información Clave:**
        - **Carga de Datos:** Importa la lista de productos a contar desde el sistema principal.
        - **Registro en Vivo:** Ingresa las cantidades contadas directamente en la app.
        - **Reporte de Discrepancias:** Compara automáticamente el conteo físico con el stock del sistema y resalta diferencias.

        **¿Cómo aprovecharla?**
        Reduce drásticamente el tiempo de auditoría de inventario, minimiza errores humanos y obtén un reporte de ajuste de forma inmediata.
        """)

    with col2:
        st.write(" ")
        st.write(" ")
        st.link_button(
            "Iniciar Conteo",
            "https://tu-link-aqui.streamlit.app/conteo", # <-- ¡AQUÍ VA TU LINK!
            use_container_width=True
        )

# ======================================================================================
# --- PIE DE PÁGINA ---
# ======================================================================================
st.divider()
st.caption("© 2025 [Nombre de tu Compañía]. Todos los derechos reservados. Para soporte técnico, contactar al equipo de TI.")
