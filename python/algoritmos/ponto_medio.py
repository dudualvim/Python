import math

# Coordenadas geográficas dos usuários
usuarios = [
    {"latitude":  -15.782492801396314, "longitude":  -47.89861303956294},  # Usuário 1 (Mané Garrincha)
    {"latitude":  -15.794114757123465, "longitude":  -47.9006158577204},  # Usuário 2 (nicolandia)
    {"latitude":  -15.797735531741603, "longitude":  -47.875853742319},  # Usuário 3 (Catedral)
    {"latitude":  -15.779981436967923, "longitude":  -47.8924832021719},  # Usuário 4 (Colégio Militar)
    {"latitude":  -15.828509501507893, "longitude":  -47.9125720757568}   # Usuário 5 (Ceub)
]

# Cálculo da localização média
media_latitude = sum(user["latitude"] for user in usuarios) / len(usuarios)
media_longitude = sum(user["longitude"] for user in usuarios) / len(usuarios)


print(f"\nA media da Latitude: {media_latitude}\nA media da Longitude: {media_longitude}\n")


# Base de dados de restaurantes McDonald's em Brasília (com latitudes e longitudes)
restaurantes = [
    {"nome": "McDonald's 1", "latitude": -15.768300263164063, "longitude": -47.88829549138007},
    {"nome": "McDonald's 2", "latitude": -15.785471355813618, "longitude": -47.88896309743256},
    {"nome": "McDonald's 3", "latitude":  -15.78920908799764, "longitude": -47.89120868142729},
    {"nome": "McDonald's 4", "latitude":  -15.79504915650081, "longitude": -47.89187628747978},
    {"nome": "McDonald's 5", "latitude":  -15.791603536446372, "longitude": -47.8838043233906},
    {"nome": "McDonald's 6", "latitude":  -15.789793102423637, "longitude": -47.88234772836699},
    {"nome": "McDonald's 7", "latitude":  -15.82913083333314, "longitude": -47.92111603474451},
    {"nome": "McDonald's 8", "latitude":  -15.836104655571193,"longitude": -48.015302353997455},
    {"nome": "McDonald's 9", "latitude":  -15.794862847082038, "longitude": -47.944909938621706},

]

# Cálculo da distância e seleção do restaurante mais próximo
restaurante_mais_proximo = None
distancia_mais_curta = float('inf')

for restaurante in restaurantes:
    latitude_restaurante = restaurante["latitude"]
    longitude_restaurante = restaurante["longitude"]
    
    # Cálculo da distância usando a fórmula de Haversine
    raio_terra = 6371  # Raio médio da Terra em quilômetros
    delta_lat = math.radians(latitude_restaurante - media_latitude)
    delta_lon = math.radians(longitude_restaurante - media_longitude)
    a = math.sin(delta_lat / 2) ** 2 + math.cos(math.radians(media_latitude)) * math.cos(math.radians(latitude_restaurante)) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = raio_terra * c
    
    # Verifica se a distância atual é menor do que a distância mais curta encontrada até agora
    if distancia < distancia_mais_curta:
        distancia_mais_curta = distancia
        restaurante_mais_proximo = restaurante

print(f"O McDonald's mais próximo é: {restaurante_mais_proximo['nome']} a uma distância de {distancia_mais_curta} km.\n")



"""

A fórmula de Haversine é uma equação que é usada para calcular a distância entre dois pontos 
na superfície de uma esfera, como a Terra. Ela é particularmente útil para calcular a distância 
entre duas coordenadas geográficas (latitude e longitude) em um globo, levando em consideração a curvatura da Terra. 
A fórmula é denominada "Haversine" devido ao uso da função trigonométrica "haversine" para realizar os cálculos.

"""
