import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate

# Carregar o dataset de usuários
data = {
    "user_id": [1, 2, 3, 4],
    "user_name": ['roger', 'eduardo', 'amanda', 'guilherme'],
    "user_cidade": ['Rio de Janeiro', 'São Paulo', 'Rio de Janeiro', 'São Paulo'],
    "user_interests": [['museum', 'Cachoeira', 'Natureza', 'Trilha', 'aventura'],
                        ["Praia", "futebol", "samba", "musica"],
                        ["historia", "museu", "vista panoramica", "diversão", "musica"],
                        ["natureza", "cachoeira"]],
}
userdf = pd.DataFrame(data)

# Carregar o dataset de pontos turísticos
dataset = pd.read_csv('dataset_final.csv')

# Filtrar o dataset de pontos turísticos com base na cidade do usuário
def filter_dataset_by_city(dataset, cidade):
    filtered_dataset = dataset[dataset['Cidade'] == cidade].reset_index(drop=True)
    return filtered_dataset

# Criar matriz TF-IDF para as palavras-chave do dataset de pontos turísticos filtrado
def create_tfidf_matrix(dataset):
    cv = CountVectorizer(stop_words='english')
    keyword_vector = cv.fit_transform(dataset['Keywords'].fillna('').astype(str))
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(keyword_vector)
    return tfidf_matrix, cv

# Calcular similaridade do cosseno entre usuários e pontos turísticos
def calculate_similarity(user_tfidf_matrix, dataset_tfidf_matrix):
    similarity = cosine_similarity(user_tfidf_matrix, dataset_tfidf_matrix)
    return similarity

# Função para recomendar pontos turísticos para um usuário
def recommend_by_user(user_id):
    user_keywords = userdf.loc[userdf['user_id'] == user_id, 'user_interests'].item()
    user_cidade = userdf.loc[userdf['user_id'] == user_id, 'user_cidade'].item()

    # Filtrar o dataset de pontos turísticos com base na cidade do usuário
    filtered_dataset = filter_dataset_by_city(dataset, user_cidade)

    # Criar matriz TF-IDF para as palavras-chave do dataset de pontos turísticos filtrado
    tfidf_matrix, cv = create_tfidf_matrix(filtered_dataset)

    # Criar matriz TF-IDF para as palavras-chave do usuário
    user_vector = cv.transform([', '.join(user_keywords)])
    tfidf_transformer = TfidfTransformer()
    user_tfidf_vector = tfidf_transformer.fit_transform(user_vector)

    # Calcular similaridade do cosseno entre usuário e pontos turísticos
    similarity = calculate_similarity(user_tfidf_vector, tfidf_matrix)

    # Obter os índices dos pontos turísticos mais similares
    places_indices = similarity.argsort()[0][::-1]

    # Obter os nomes dos pontos turísticos mais recomendados
    recommended_places = filtered_dataset.loc[places_indices[:5], 'name'].tolist()

    return recommended_places, user_tfidf_vector, filtered_dataset

# Exemplo de recomendação para o usuário com user_id = 2
recommendations, user_tfidf_vector, filtered_dataset = recommend_by_user(2)

# Exibir a matriz TF-IDF de forma tabular
table_data = []
table_headers = ['User'] + filtered_dataset['name'].tolist()

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

for i in range(len(keywords)):
    row = [keywords[i]]
    row.extend(['{:.2f}'.format(similarity_matrix[i, j]) for j in range(len(similarity_matrix[i]))])
    table_data.append(row)

print(tabulate(table_data, headers=table_headers, floatfmt=".2f"))
print()




# Exibir as recomendações de pontos turísticos
print(f"Recomendações para o usuário 2:")
for i, recommendation in enumerate(recommendations):
    print(f"{i+1}. {recommendation}")