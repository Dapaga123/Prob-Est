import seaborn as sns

import matplotlib.pyplot as plt

df = sns.load_dataset("tips")


print("Estadísticas descriptivas generales:")
print(df.describe(), "\n")


group_stats = df.groupby("sex")["tip"].agg(["mean", "std", "count"])
print("Propina por sexo (media, desviación estándar, cantidad):")
print(group_stats, "\n")

sns.violinplot(data=df, x="sex", y="tip", palette="pastel")


plt.title("Distribución de Propinas por Sexo")


plt.show()

