import pickle
import Orange
import pandas as pd
import numpy as np
import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description='Two arguments: model file and patient file')

parser.add_argument('modelFile', type=str, help='Model File *.pkcls')
parser.add_argument('patientFile', type=str, help='Patient File *.csv')

# Parse the arguments
args = parser.parse_args()

# Use the parsed arguments
#print(f"Argument 1: {args.arg1}")
#print(f"Argument 2: {args.arg2}")
# Testar se os argumentos têm os tipos adequados
if not os.path.isfile(args.modelFile):
    print(f"Error: The file '{args.modelFile}' does not exist or is not a valid file.")
    exit(1)

# Verificar se o primeiro argumento é uma string e contém o padrão de arquivo CSV
if not args.modelFile.lower().endswith('.pkcls'):
    print("Error: The first argument must be a Model File *.pkcls.")
    exit(1)

if not os.path.isfile(args.patientFile):
    print(f"Error: The file '{args.patientFile}' does not exist or is not a valid file.")
    exit(1)

# Verificar se o primeiro argumento é uma string e contém o padrão de arquivo CSV
if not args.patientFile.lower().endswith('.csv'):
    print("Error: The second argument must be a Patient File *.csv.")
    exit(1)

# Carregar o modelo
# Teste na mão: with open("naivebayesmodelMinusC75C56.pkcls", "rb") as file:
with open(args.modelFile, "rb") as file:
        model = pickle.load(file)

# Carregar o arquivo CSV com a primeira linha como cabeçalho
#csv_file_path = "umvszeroAll.csv"  # Substitua pelo caminho correto do seu arquivo CSV
csv_file_path = args.patientFile
data_frame = pd.read_csv(csv_file_path, header=0)  # `header=0` indica que a primeira linha é o cabeçalho

# Verifique se a coluna 'amostra' existe
if 'amostra' not in data_frame.columns:
    raise ValueError("O arquivo CSV deve conter uma coluna chamada 'amostra'.")
amostra_column = data_frame['amostra']

# Agora, mantenha todas as colunas e garanta que as variáveis categóricas sejam tratadas corretamente
features_data = data_frame.drop(columns=['amostra'])  # Features são as colunas, exceto 'amostra'

# Identifique colunas categóricas e converta para `DiscreteVariable`
domain_attributes = []
for column in features_data.columns:
    if features_data[column].dtype == 'object':  # Categóricas são geralmente do tipo 'object' (strings)
        # Converta para o tipo 'category' para que possamos usar o acessador .cat
        features_data[column] = features_data[column].astype('category')
        # Criar uma variável discreta para a coluna categórica
        domain_attributes.append(Orange.data.DiscreteVariable.make(column, values=list(features_data[column].cat.categories)))
    else:
        # Criar uma variável contínua para a coluna numérica
        domain_attributes.append(Orange.data.ContinuousVariable(column))

# Criar o domínio para a tabela
domain = Orange.data.Domain(domain_attributes)

# Converta os dados de entrada para uma tabela Orange
# Antes de criar a tabela, precisamos converter as variáveis categóricas para o tipo correto (discretas ou contínuas)
X = []
for index, row in features_data.iterrows():
    instance = []
    for col in features_data.columns:
        if features_data[col].dtype.name == 'category':  # Se for categórica
            # Encontrar o valor correspondente à categoria
            instance.append(features_data[col].cat.codes[index])  # Usamos .cat.codes para codificar
        else:  # Se for contínua
            instance.append(row[col])
    X.append(instance)

# Criar a tabela Orange com os dados processados
orange_table = Orange.data.Table.from_numpy(domain=domain, X=np.array(X))

# Classifique cada instância e imprima a coluna 'amostra' com a classe prevista
for amostra, instance in zip(amostra_column, orange_table):
    predicted_label = model(instance)
    print(f"Amostra: {amostra}, Predicted class: {predicted_label}")
