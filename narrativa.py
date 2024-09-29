class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Region:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Game:
    def __init__(self):
        self.regions = [
            Region("Infinity School", "A melhor escola de tecnologia do Brasil, cheia de mentes brilhantes."),
            Region("Trade Center do Riomar", "Sala 4, sede da Infinity School em 2024, onde surgem as primeiras escolhas."),
            Region("Metrópole Neon", "Uma cidade cheia de arranha-céus brilhantes, repleta de mercados negros."),
            Region("O Submundo Digital", "Um espaço virtual repleto de avatares e representações digitais."),
            Region("Zona de Dados", "Local perigoso onde os servidores das corporações estão localizados."),
            Region("Refúgio dos Rebeldes", "Um esconderijo clandestino de um grupo de hackers."),
        ]

        self.characters = [
            Character("Zara 'Byte' Collins", "Uma hacker lendária que tem informações cruciais."),
            Character("Dr. Aiden Kline", "Um ex-cientista que criou uma IA avançada para proteger a liberdade digital."),
            Character("CEO Magnus Voss", "O ambicioso líder da Corporação TechCore que busca controle."),
            Character("Dev Aline", "Uma desenvolvedora experiente que pode ajudar na escolha da linguagem de programação."),
            Character("Victor, o Andarilho Surpresa", "Um viajante que possui perguntas enigmáticas."),
            Character("Matheus Alves", "O temido professor conhecido como Chefão do POO.")
        ]

        self.conflict = ("Investigar os desaparecimentos de hackers e o plano maligno da Corporação TechCore.")
        self.player_points = 100  # Inicializando os pontos do jogador

    def start(self):
        print("Bem-vindo ao Cyber Nexus RPG!")
        self.narrator_intro()
        self.show_regions()
        self.show_characters()
        self.show_conflict()
        self.teleport_to_trade_center()
        self.programming_choice()

    def narrator_intro(self):
        print("\nVocê se encontra na Infinity School, a melhor escola de tecnologia do Brasil.")
        print("O narrador se aproxima e diz:")
        print('"Vocês estão prestes a embarcar em uma aventura épica transtemporal que utiliza uma magia nova chamada "tecnologia".')
        print("O objetivo desta jornada é responder enigmas e enfrentar um chefão final.")
        print("Em troca, vocês ganharão novas habilidades ao longo do tempo.")
        print("Vocês desejam embarcar nessa aventura? (Sim)")

        choice = input("Digite 'Sim' para continuar: ").strip().lower()
        if choice != "sim":
            print("O narrador sorri e diz: 'Infelizmente, essa aventura não espera por ninguém. Até a próxima!'")
            exit()

    def show_regions(self):
        print("\nRegiões disponíveis:")
        for region in self.regions:
            print(region)

    def show_characters(self):
        print("\nPersonagens disponíveis:")
        for character in self.characters:
            print(character)

    def show_conflict(self):
        print("\nConflito atual:")
        print(self.conflict)

    def teleport_to_trade_center(self):
        print("\nAssim que vocês aceitam a aventura, uma luz intensa os envolve.")
        print("Vocês são teletransportados para o ano de 2024.")
        print("Agora se encontram na sala 4 do Trade Center do Riomar, sede da Infinity School.")
        print("Aqui, as primeiras escolhas começam a surgir.")

    def programming_choice(self):
        print("\nO narrador pergunta:")
        print("Vocês acham que o correto seria começar no mundo da programação estudando:")
        print("1. Lógica de Programação")
        print("2. Front-end")

        choice = input("Digite '1' para Lógica de Programação ou '2' para Front-end: ").strip()
        
        if choice == '1':
            print("Muito bem! Você passou para a próxima fase.")
            self.scenario_three()
        elif choice == '2':
            print("Está errado, vá estudar pequeno gafanhoto.")
            print("Você voltou para a idade média haha.")
            print("Reiniciando o jogo...")
            self.restart_game()
        else:
            print("Escolha inválida. O narrador decide ignorar sua indecisão.")

    def scenario_three(self):
        print("\nEnquanto você avança, encontra Dev Aline, uma desenvolvedora experiente.")
        print("Ela lhe diz:")
        print('"Agora, você precisa escolher uma linguagem de programação para continuar sua jornada."')
        print("1. Javascript")
        print("2. Python")
        print("3. Java")

        choice = input("Digite '1' para Javascript, '2' para Python ou '3' para Java: ").strip()

        if choice == '1':
            print("Você escolheu Javascript! Prepare-se para uma aventura cheia de interatividade.")
            self.player_points += 10  # O jogador ganha 10 pontos
            print("Você ganhou 10 pontos por escolher Javascript.")
        elif choice == '2':
            print("Você escolheu Python! Uma escolha sábia para quem busca simplicidade e poder.")
            self.player_points += 10  # O jogador ganha 10 pontos
            print("Você ganhou 10 pontos por escolher Python.")
        elif choice == '3':
            print("Dev Aline olha para você com desapontamento.")
            self.player_points -= 10  # O jogador perde 10 pontos
            print("Você perdeu 10 pontos.")
            print("Dev Aline desaparece.")
            print("Você não entendeu a atitude dela, mas continua sua jornada.")
            self.encounter_victor()  # Avança para o encontro com Victor
        else:
            print("Escolha inválida. Dev Aline olha para você com desapontamento.")

        print("Você está pronto para continuar sua jornada com novas habilidades!")

    def encounter_victor(self):
        print("\nEnquanto continua sua jornada, você encontra Victor, o Andarilho Surpresa.")
        print('Ele faz a seguinte pergunta:')
        print('"O que é aquilo que tira a sua paz no código, mas de tão simples faz você se sentir burro?"')
        print("1. Um erro de sintaxe")
        print("2. A lógica de um loop")
        print("3. Variáveis não inicializadas")

        choice = input("Digite '1', '2' ou '3': ").strip()

        if choice == '1':
            print("Correto! Um erro de sintaxe pode ser frustrante e simples ao mesmo tempo.")
        elif choice == '2' or choice == '3':
            print("Errado! Esses problemas são desafiadores, mas não são o que tira sua paz de forma tão simples.")
        else:
            print("Escolha inválida. Victor olha para você com uma expressão de curiosidade.")

        # Bônus AnteFomeDev
        print("\nVictor, tendo pena de você, decidiu lhe dar um bônus AnteFomeDev.")
        print("Você precisa escolher uma opção:")
        print("1. Batata Frita")
        print("2. Pizza")

        choice = input("Digite '1' para Batata Frita ou '2' para Pizza: ").strip()

        if choice == '1':
            print("Victor sorri sarcasticamente: 'Você ganhou uma semana de intoxicação alimentar e 1 semana sem codar. Parabéns, você perdeu 2 pontos em back-end.'")
            self.player_points -= 2  # O jogador perde 2 pontos
        elif choice == '2':
            print("Ótima escolha, jogador! Vamos comer juntos.")
        else:
            print("Escolha inválida. Victor balança a cabeça desapontado.")

        print("Você continua sua jornada, aprendendo e enfrentando novos desafios!")
        
        self.encounter_matheus()  # Avança para o desafio com Matheus

    def encounter_matheus(self):
        print("\nDe repente, você se encontra em sua aula de Fullstack.")
        print("Mas algo inesperado acontece...")
        print("O temido professor Matheus Alves, também conhecido como Chefão do POO, aparece!")
        print('"Prepare-se para um desafio de Programação Orientada a Objetos!"')

        # Perguntas do chefão
        questions = {
            "O que é uma classe em POO?": ("(1) Molde ou modelo para criar objetos.", "(2) Função que executa um código automaticamente.", "1"),
            "O que é um objeto em POO?": ("(1) Um loop de repetição.", "(2) Instância de uma classe.", "2"),
            "O que é herança em POO?": ("(1) Compartilhamento de atributos e métodos entre classes.", "(2) Atributos privados de uma classe.", "1"),
            "O que é encapsulamento em POO?": ("(1) Restrição do acesso direto a atributos.", "(2) Criação de uma nova classe.", "1"),
            "O que é polimorfismo em POO?": ("(1) Permitir que várias classes usem métodos com o mesmo nome.", "(2) Permitir que uma função tenha vários loops")
            }