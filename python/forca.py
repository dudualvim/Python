import random

def jogar_forca():
    palavras = [
    'LionelMessi', 'CristianoRonaldo', 'NeymarJr.', 'KylianMbappé', 'RobertLewandowski', 'KevinDeBruyne',
    'SergioRamos', 'VirgilvanDijk', 'LukaModric', 'MohamedSalah', 'SadioMané', 'HarryKane',
    'EdenHazard', 'AntoineGriezmann', 'PaulPogba', 'KarimBenzema', 'ToniKroos', 'SergioAgüero', 'GarethBale',
    'PauloDybala', 'RomeluLukaku', 'RaheemSterling', 'DavidDeGea', 'ThiagoAlcântara', 'PierreEmerickAubameyang',
    'ThomasMüller', 'ManuelNeuer', 'NGoloKanté', 'JadonSancho', 'MarcoReus', 'ChristianPulisic',
    'ViniciusJunior', 'FrenkiedeJong', 'MatthijsdeLigt', 'ErlingHaaland', 'JoãoFélix', 'BernardoSilva',
    'BrunoFernandes', 'DiogoJota', 'SergioBusquets', 'LuisSuárez', 'MarâAndréterStegen', 'CiroImmobile',
    'ZlatanIbrahimovic', 'AndreaBelotti', 'PierreEmerickAubameyang', 'HakimZiyech', 'AlexandreLacazette',
    'SonHeung-min', 'JamieVardy', 'KaiHavertz', 'JoshuaKimmich', 'NabilFekir', 'OlivierGiroud',
    'ThiagoSilva', 'NemanjaMatic', 'KalidouKoulibaly', 'GiorgioChiellini', 'LeonardoBonucci', 'GianluigiDonnarumma',
    'DavidAlaba', 'MohamedElneny', 'MemphisDepay', 'DriesMertens', 'HirvingLozano', 'MarekHamsik',
    'ChristianEriksen', 'CiroImmobile', 'LorenzoInsigne', 'LautaroMartínez', 'MauroIcardi', 'RadamelFalcao',
    'AngelDiMaria', 'NicolásOtamendi', 'JavierMascherano', 'SergioRomero', 'SergioAgüero', 'RobertoFirmino',
    'GabrielJesus', 'AlissonBecker', 'Fabinho', 'PhilippeCoutinho', 'ThiagoSilva', 'LucasMoura',
    'Marquinhos', 'NeymarJr.', 'Casemiro', 'DouglasCosta', 'Allan', 'Richarlison',
    'TrentAlexanderArnold', 'JordanHenderson', 'RaheemSterling', 'MarcusRashford', 'HarryMaguire', 'MasonMount',
    'JackGrealish', 'DeclanRice', 'HarryKane', 'JadonSancho', 'KalvinPhillips', 'BukayoSaka'
]

    palavra_secreta = random.choice(palavras).upper() 
    letras_certas = []
    letras_erradas = []
    tentativas = 8

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra secreta!")

    while True:
        acertou = True

        for letra in palavra_secreta:
            if letra in letras_certas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                acertou = False

        print("\n\n")

        if tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

        if acertou:
            print("Parabéns! Você acertou a palavra secreta:", palavra_secreta)
            break

        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", letras_erradas)

        try:
            palpite = input("Digite uma letra: ").strip().upper()
        except KeyboardInterrupt:
            print("\nJogo interrompido. Até mais!")
            break

        if len(palpite) != 1 or not palpite.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra antes. Tente novamente.")
            continue

        if palpite in palavra_secreta:
            letras_certas.append(palpite)
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

        print()

jogar_forca()
