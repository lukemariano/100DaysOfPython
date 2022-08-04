import random


def rock_paper_scissors():

    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    #seed
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    # list
    list_choice = [rock, paper, scissors]

    # 1º passo: pedir um input de um numero para cada opção
    index_human = int(
        input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
    # 2º passo: usar input como indice na lista para minha escolha
    human_choice = None
    # 3º passo: gerar uma escolha aleatória para o computador
    index_computer = None
    computer_choice = None

    if index_human < 0 or index_human > 2:
        return 'Invalid choice, YOU LOSE!'
    else:
        # var
        human_choice = list_choice[index_human]
        index_computer = random.randint(0, 2)
        computer_choice = list_choice[index_computer]

        # 4º passo: mostrar escolhas
        print(human_choice)
        print(f'Computer chose: \n {computer_choice}')

        # 5º passo: definir condições de vitória e derrota
        if human_choice == computer_choice:
            return 'draw'
        else:
            if human_choice == rock and computer_choice == scissors:
                return 'You win'
            elif human_choice == paper and computer_choice == rock:
                return 'You win'
            elif human_choice == scissors and computer_choice == paper:
                return 'You win'
            else:
                return 'You lose'
