import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.patches as mpatches

# Título de la aplicación
st.title('Generador de Diagnóstico de Evolución de los Líderes de HC')

# Ingresar el nombre del estudiante
nombre_estudiante = st.text_input('Ingresa el nombre del líder:')

# Ingresar las calificaciones de cada categoría
categorias = ['Comunicación Efectiva', 'Liderazgo Transformador', 'Negociación', 'Time Management', 'Aprendizaje constante']
calificaciones = []

for categoria in categorias:
    calificacion = st.slider(f'Calificación de {categoria}', min_value=1, max_value=5, value=3)
    calificaciones.append(calificacion)

# Convertir las calificaciones a un array de numpy
valores = np.array(calificaciones)

# Estilos
GREY12 = "#1f1f1f"
plt.rcParams.update({"font.family": "monospace"})
plt.rc("axes", unicode_minus=False)
plt.rcParams["text.color"] = GREY12

# Paleta personalizada de colores fijos para cada categoría
COLORS_PALETTE = ["#E64C6A", "#673D8E", "#F08C3C", "#F7D965", "#B4D261"]  # Un color por categoría

# Asignación de colores a cada categoría
COLORS = COLORS_PALETTE  # Cada categoría tiene su color asignado directamente

# Ángulos
ANGLES = np.linspace(0, 2 * np.pi, len(valores), endpoint=False)

# Inicializar figura
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={"projection": "polar"})
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Ajustes de gráfico
ax.set_theta_offset(np.pi / 2)  # rotación para que el primer eje esté arriba
ax.set_theta_direction(-1)      # sentido horario
ax.set_ylim(0, max(valores))  # asegurar visibilidad de todo

# Barras con los colores asignados
bars = ax.bar(ANGLES, valores, width=0.5, color=COLORS, edgecolor="white", linewidth=1, zorder=10)

# Líneas de referencia
ax.vlines(ANGLES, 0, max(valores), color=GREY12, ls=(0, (4, 4)), linewidth=0.5, zorder=5)

# Añadir los círculos radiales en 5 posiciones específicas (1, 2, 3, 4, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels([str(i) for i in range(1, 6)], fontsize=11, fontweight='bold', color=GREY12)

# Etiquetas de categorías
categorias_wrap = ["\n".join(wrap(r, 15, break_long_words=False)) for r in categorias]
ax.set_xticks(ANGLES)
ax.set_xticklabels(categorias_wrap, size=12, fontweight='bold')

# Título
ax.set_title(f"Perfil de {nombre_estudiante}", fontsize=18, pad=50)  # Ajusta el 'pad' para más espacio

# Ajustar el margen superior para mover el título más abajo
fig.subplots_adjust(top=0.80)  # Ajusta este valor para mover el gráfico hacia abajo y separar más el título

# Crear la leyenda personalizada
# Quitar etiquetas alrededor del gráfico
ax.set_xticks([])

legend_patches = [
    mpatches.Patch(color=color, label=label)
    for color, label in zip(COLORS, categorias_wrap)
]

# Añadir la leyenda fuera del gráfico
ax.legend(
    handles=legend_patches,
    loc='center left',
    bbox_to_anchor=(1.1, 0.5),
    fontsize=12,
    frameon=False
)

# Mostrar la gráfica
st.pyplot(fig)
