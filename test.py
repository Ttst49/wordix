import math
import main
import spacy
import random


def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def get_random_word():
    words = get_list_of_words('./files/words.txt')

    random_word = random.choice(words)
    print(random_word)
    return random_word


def game(random_word):
    model = spacy.load("en_core_web_lg")

    secret_word = str(random_word)
    token_secret_word = model(secret_word)

    given_word = input("Give me a word: ")
    try:
        token_given_word = model(given_word)
        if not token_given_word.has_vector:
            print("donnez un mot valide")
            game(random_word)
        else:
            similarity = token_given_word.similarity(token_secret_word)
            if similarity == 1:
                print("gagné")
                #print(similarity)

            else:
                #print(similarity)
                message = "le mot " + token_given_word.text + " est a " + str(math.floor(similarity * 100)) + " degré celsius"
                print(message)
                main.list_of_words.append(given_word + ":" + str(math.floor(similarity * 100)))
                game(random_word)
    except IOError:
        pass
    finally:
        #print(similarity)
        print(main.list_of_words)


game(get_random_word())
