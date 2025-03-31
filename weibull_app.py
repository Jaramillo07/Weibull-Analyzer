# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib.gridspec import GridSpec

# Configuración de la página
st.set_page_config(
    page_title="Visualización Dinámica de Distribución Weibull",
    page_icon="📊",
    layout="wide"
)

# Título y descripción
st.title("Visualización Dinámica de Distribución Weibull")
st.markdown("""
Esta aplicación muestra cómo los parámetros de la distribución Weibull afectan las curvas de confiabilidad. 
Modifica los valores de β (beta) y η (eta) para ver cómo cambian las gráficas en tiempo real.
""")

# Crear dos columnas para los controles
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Parámetros")
    
    # Controles deslizantes para los parámetros
    beta = st.slider(
        "β (Beta) - Parámetro de Forma",
        min_value=0.1,
        max_value=5.0,
        value=1.0,
        step=0.1,
        help="β < 1: Mortalidad infantil (tasa decreciente)\nβ = 1: Fallos aleatorios (tasa constante)\nβ > 1: Desgaste (tasa creciente)"
    )
    
    eta = st.slider(
        "η (Eta) - Parámetro de Escala (horas)",
        min_value=0.1,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="Tiempo característico (63.2% de fallos)"
    )
    
    # Calculando MTTF
    mttf = eta * gamma(1 + 1/beta)
    
    # Mostrar información adicional
    st.info(f"MTTF: {mttf:.2f} horas")
    
    # Interpretar el valor de beta
    if beta < 0.95:
        st.warning("**Modo de falla: Mortalidad infantil** (β < 1)\n\nLos fallos son más probables al inicio y disminuyen con el tiempo. Comunes en componentes con defectos de fabricación.")
    elif 0.95 <= beta <= 1.05:
        st.success("**Modo de falla: Fallos aleatorios** (β ≈ 1)\n\nLos fallos ocurren al azar, independientemente del tiempo en servicio.")
    else:
        st.error("**Modo de falla: Desgaste** (β > 1)\n\nLos fallos son más probables a medida que el componente envejece. Comunes en componentes que sufren fatiga o desgaste.")
    
    # Agregar opciones para la visualización
    st.subheader("Opciones de visualización")
    tiempo_max = st.slider("Tiempo máximo a mostrar (horas)", 0.1, 20.0, 5.0, 0.1)
    
    # Checkbox para mostrar/ocultar gráficas
    show_reliability = st.checkbox("Curva de Confiabilidad R(t)", value=True)
    show_pdf = st.checkbox("Función de Densidad (PDF)", value=True)
    show_cdf = st.checkbox("Función de Distribución Acumulativa (CDF)", value=True)
    show_hazard = st.checkbox("Tasa de Fallo h(t)", value=True)
    
    # Botón para reset
    if st.button("Restaurar valores predeterminados"):
        beta = 1.0
        eta = 1.0
        tiempo_max = 5.0

# Columna para las gráficas
with col2:
    # Crear el tiempo para las gráficas
    t = np.linspace(0.001, tiempo_max, 1000)
    
    # Calcular las diferentes funciones
    R_t = np.exp(-(t / eta)**beta)  # Confiabilidad
    F_t = 1 - R_t                   # CDF (probabilidad acumulada de fallo)
    pdf = (beta / eta) * (t / eta)**(beta - 1) * np.exp(-(t / eta)**beta)  # PDF
    h_t = pdf / R_t                 # Tasa de fallo
    
    # Determinar cuántas gráficas se mostrarán
    num_plots = sum([show_reliability, show_pdf, show_cdf, show_hazard])
    
    if num_plots > 0:
        # Crear la figura para las gráficas
        fig = plt.figure(figsize=(12, 3*num_plots))
        gs = GridSpec(num_plots, 1, figure=fig)
        
        plot_idx = 0
        
        # Gráfica de confiabilidad
        if show_reliability:
            ax1 = fig.add_subplot(gs[plot_idx])
            ax1.plot(t, R_t, 'b-', linewidth=2)
            ax1.set_title('Curva de Confiabilidad R(t)')
            ax1.set_xlabel('Tiempo (horas)')
            ax1.set_ylabel('Confiabilidad')
            ax1.grid(True)
            ax1.set_xlim(0, tiempo_max)
            ax1.set_ylim(0, 1.05)
            plot_idx += 1
        
        # Gráfica de PDF
        if show_pdf:
            ax2 = fig.add_subplot(gs[plot_idx])
            ax2.plot(t, pdf, 'g-', linewidth=2)
            ax2.set_title('Función de Densidad de Probabilidad (PDF)')
            ax2.set_xlabel('Tiempo (horas)')
            ax2.set_ylabel('Densidad')
            ax2.grid(True)
            ax2.set_xlim(0, tiempo_max)
            plot_idx += 1
        
        # Gráfica de CDF
        if show_cdf:
            ax3 = fig.add_subplot(gs[plot_idx])
            ax3.plot(t, F_t, 'r-', linewidth=2)
            ax3.set_title('Función de Distribución Acumulativa (CDF)')
            ax3.set_xlabel('Tiempo (horas)')
            ax3.set_ylabel('Probabilidad Acumulada')
            ax3.grid(True)
            ax3.set_xlim(0, tiempo_max)
            ax3.set_ylim(0, 1.05)
            plot_idx += 1
        
        # Gráfica de tasa de fallo
        if show_hazard:
            ax4 = fig.add_subplot(gs[plot_idx])
            ax4.plot(t, h_t, 'm-', linewidth=2)
            ax4.set_title('Tasa de Fallo h(t)')
            ax4.set_xlabel('Tiempo (horas)')
            ax4.set_ylabel('Tasa de Fallo')
            ax4.grid(True)
            ax4.set_xlim(0, tiempo_max)
            # Limitar el eje y para mejor visualización
            if beta > 1:
                ax4.set_ylim(0, min(10, np.max(h_t[t <= tiempo_max * 0.8])))
            plot_idx += 1
        
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Selecciona al menos una gráfica para visualizar")

# Información educativa sobre la distribución Weibull
st.markdown("""
## Acerca de la Distribución Weibull

La distribución Weibull es una de las distribuciones más utilizadas en el análisis de confiabilidad y mantenimiento debido a su flexibilidad para modelar diferentes patrones de fallo.

### Interpretación de parámetros

#### Beta (β) - Parámetro de forma
- **β < 1**: Tasa de fallos decreciente (mortalidad infantil)
  - Los fallos son más probables al inicio de la vida útil
  - Común en componentes con defectos de fabricación
  - El mantenimiento preventivo puede ser contraproducente

- **β = 1**: Tasa de fallos constante (fallos aleatorios)
  - Los fallos ocurren aleatoriamente
  - La distribución Weibull se convierte en una distribución exponencial
  - Común en sistemas electrónicos o fallos causados por factores externos

- **β > 1**: Tasa de fallos creciente (desgaste)
  - Los fallos se vuelven más probables con el tiempo
  - Común en componentes mecánicos
  - El mantenimiento preventivo es muy efectivo

#### Eta (η) - Parámetro de escala
- Determina la "extensión" de la distribución
- Es la vida característica del componente (tiempo para el cual el 63.2% de los componentes habrán fallado)
- Medido en las mismas unidades que el tiempo (generalmente horas)

### Fórmulas principales

- **Función de confiabilidad**: $R(t) = e^{-(t/η)^β}$
- **Función de distribución acumulativa**: $F(t) = 1 - e^{-(t/η)^β}$
- **Función de densidad de probabilidad**: $f(t) = (β/η)(t/η)^{β-1}e^{-(t/η)^β}$
- **Tasa de fallo**: $h(t) = (β/η)(t/η)^{β-1}$
- **MTTF (Tiempo Medio Hasta el Fallo)**: $MTTF = η·Γ(1+1/β)$

donde Γ es la función gamma.
""")

# Pie de página
st.markdown("""
---
Desarrollado para presentación de análisis de confiabilidad | 2025
""")