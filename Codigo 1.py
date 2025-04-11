import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset
tips = sns.load_dataset("tips")

# 1. Mostrar los primeros datos
print("1. Primeras filas del dataset:")
print(tips.head(), "\n")

# 2. Scatterplot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("2. Propina vs Cuenta Total (Scatterplot)")
plt.show()

# 3. Lineplot
plt.figure(figsize=(6, 4))
sns.lineplot(data=tips.sort_values("total_bill"), x="total_bill", y="tip")
plt.title("3. Tendencia de Propinas (Lineplot)")
plt.show()

# 4. Histograma (Histplot)
plt.figure(figsize=(6, 4))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
plt.title("4. Histograma de Cuentas Totales")
plt.show()

# 5. Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("5. Caja de Cuentas por Día (Boxplot)")
plt.show()

# 6. Violinplot
plt.figure(figsize=(6, 4))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("6. Distribución por Día y Sexo (Violinplot)")
plt.show()

# 7. Barplot
plt.figure(figsize=(6, 4))
sns.barplot(data=tips, x="day", y="tip", hue="sex")
plt.title("7. Propinas Promedio por Día y Sexo (Barplot)")
plt.show()

# 8. Heatmap de correlaciones
plt.figure(figsize=(6, 4))
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("8. Mapa de Calor de Correlaciones (Heatmap)")
plt.show()

# 9. Pairplot
sns.pairplot(tips, hue="sex")
plt.suptitle("9. Matriz de Gráficos (Pairplot)", y=1.02)
plt.show()

# 10. Catplot tipo Swarm
sns.catplot(data=tips, x="day", y="total_bill", kind="swarm", hue="sex", height=5, aspect=1.5)
plt.title("10. Swarmplot por Día y Sexo (Catplot)")
plt.show()
