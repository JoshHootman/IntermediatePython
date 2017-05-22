store = []


def sort_by_last_letter(string):
    """
    Task define a function that takes a string
    as input parameter.
    Defines a local function that returns
    the last letter of the string
    your main function returns a sorted list
    based on the last letter
    :param string: a list of strings
    :return: sorted list based on last letter
    """

    # A local function

    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    # Hint: use the local function as a lambda to the sorted built-in function
    return sorted(string, key=last_letter)


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def main():
#   names = ["Josh", "Heather", "Jared", "Chris", "Lillie"]
#   print(sort_by_last_letter(names))
#   print(sort_by_last_letter(names))
#   print(sort_by_last_letter(names))
    fx = logger("program called logger")
    fx()
if __name__ == '__main__':
    main()
