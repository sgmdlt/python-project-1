import prompt

TRIES = 3


def run(game):
    """Run chosen game and display dialog messages.

    game -- name of game module (in 'games' package)
    """
    print('Welcome to Brain Games!')
    username = prompt.string('May I have your name?\n')
    print(f'Hello, {username}!')

    print(game.GAME_MESSAGE)
    for _ in range(TRIES):
        question, correct_answer = game.game_task()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')  # noqa: E501
            print(f"Let's try again, {username}!")
            return

        print('Correct!')
    print(f'Congratulations, {username}')
