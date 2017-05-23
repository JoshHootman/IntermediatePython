from random import randrange

def test_random():
    # Random number between 0 - 99'
    number = randrange(100)

    while True:
        guess = int(input("? : "))
        if guess == number:
            print("You Guessed the magic number!")
            break


def expt_hierarchy():
    s = [1, 4, 6]
    # print(s[28])
    d = dict (a=56, b=66, c =67)
    # print(d['g'])


def lookups():
    s = [1, 2, 3]
    try:
        item = s[5]
    # except IndexError:
    except LookupError:
        print("Got an IndexError")

    d = dict (a=56, b=66, c =67)
    try:
        value = d['x']
    # except KeyError:
    except LookupError:
        print("Got a KeyError")


def main():
    # test_random()
    # expt_hierarchy()
    lookups()

if __name__ == '__main__':
    main()
