# use CamelCase for classes'names
class MyFirstClass:
    pass

class Point:
    def reset(self):
        self.x =0
        self.y =0


def main():
    p1 = Point()
    p2 = Point()

    # <object>.<attribute> = <value> (dot notation)
    p1.x = 5
    p1.y = 4

    print(p1.x, p1.y)
    p1.reset()
    print(p1.x, p1.y)


# only run the code if we are running this from main, if we
# import this code, don't run this
if __name__ == "__main__":
    main()
    exit(0)


