
# Projeto Backend em Python

Este projeto de backend em Python utiliza a biblioteca Matplotlib para visualização de dados e pandas para tratamento de dados a partir de arquivos CSV. O objetivo é analisar e filtrar dados relacionados à COVID-19.

## Funcionalidades

- **Gráfico de Pizza**: Criação de um gráfico de pizza para visualização dos dados.
### grafico

![image](https://user-images.githubusercontent.com/99447073/203872518-52a5e395-dc3f-4687-a013-d18fcadb7205.png)

### Código

![image](https://user-images.githubusercontent.com/99447073/203873093-08cb5174-f51f-4d03-a84f-a84df9e5a14d.png)

- **Tratamento de Dados CSV**: Filtragem dos dados do CSV fornecido para analisar casos e óbitos de COVID-19.
  - Dados filtrados a partir do arquivo: [Dados-covid-19-municipios.csv](https://github.com/Lucasgarcc/---kick-backend---python/blob/main/desafio_final/Dados-covid-19-municipios.csv)
  - Análise dos óbitos mínimos e casos máximos.
![grafico](https://github.com/user-attachments/assets/b00b3d9c-ea2f-4c27-9810-eb4229cb95b4)

#### Link : https://github.com/Lucasgarcc/---kick-backend---python/tree/main/desafio_final

## Exemplo de Código

Aqui está um exemplo de como criar um gráfico de pizza com Matplotlib:

```python
import matplotlib.pyplot as plt

# Exemplo de dados para o gráfico de pizza
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()






