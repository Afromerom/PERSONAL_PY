import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_axis_off()

def add_node(text, x, y, width=200, height=50, color="pink"):
    rect = mpatches.FancyBboxPatch((x - width / 2, y - height / 2),
                                   width, height,
                                   boxstyle="round,pad=0.3",
                                   edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=10)

def add_arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Nodes
add_node("Importar bibliotecas", 0, 0)
add_node("Configurar I2C", 0, -100)
add_node("Crear objeto sensor", 0, -200)
add_node("Configurar pantalla LCD", 0, -300)

# Arrows
add_arrow(0, -30, 0, -70)
add_arrow(0, -130, 0, -170)
add_arrow(0, -230, 0, -270)

plt.show()
