from movies import Movies

movies = Movies('./movies.txt')

def displayMenu():
    print()
    print("Menu")
    print("* enter q for exit")
    print()

def main():
    while (True):
        displayMenu()
        inVar = input()
        if(inVar == "q"):
            break

if __name__ == "__main__":
    main()