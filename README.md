echo "# Weibull Analyzer: Visualización Dinámica de Distribución Weibull

## Descripción
Esta aplicación interactiva desarrollada en Streamlit permite explorar y comprender la distribución de Weibull de manera dinámica. Permite a los usuarios modificar los parámetros β (beta) y η (eta) en tiempo real para visualizar cómo estos afectan diferentes curvas de confiabilidad.

## Características Principales
- Visualización interactiva de curvas de Weibull
- Gráficas dinámicas:
  - Curva de Confiabilidad R(t)
  - Función de Densidad de Probabilidad (PDF)
  - Función de Distribución Acumulativa (CDF)
  - Tasa de Fallo h(t)
- Interpretación del modo de falla según el parámetro β
- Cálculo de Tiempo Medio Hasta el Fallo (MTTF)

## Tecnologías Utilizadas
- Streamlit
- NumPy
- Matplotlib
- SciPy

## Requisitos
- Python 3.8+
- Bibliotecas listadas en requirements.txt

## Instalación
1. Clonar el repositorio
\`\`\`bash
git clone https://github.com/Jaramillo07/Weibull-Analyzer.git
cd Weibull-Analyzer
\`\`\`

2. Instalar dependencias
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Ejecución
\`\`\`bash
streamlit run weibull_app.py
\`\`\`

## Uso
1. Ajusta los parámetros β (Beta) y η (Eta) con los controles deslizantes
2. Selecciona las gráficas que deseas visualizar
3. Observa cómo cambian las curvas en tiempo real

## Conceptos Clave
- **β (Beta)**: Parámetro de forma que define el patrón de fallo
  - β < 1: Mortalidad infantil
  - β ≈ 1: Fallos aleatorios
  - β > 1: Desgaste

- **η (Eta)**: Parámetro de escala que representa el tiempo característico

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios propuestos.

## Licencia
MIT License

## Contacto
Desarrollador: Jaramillo07" > README.md
