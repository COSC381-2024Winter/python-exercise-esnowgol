from movies import Movies

movies = Movies('./movies.txt')

def displayMenu():
    print()
    print("Menu")
    print("* enter q for exit")
    print("* enter list for listing all the movie names")
    print()

def main():
    while (True):
        displayMenu()
        inVar = input()
        if(inVar == "q"):
            break
        elif(inVar.lower() == "list"):
            i = 1
            for movie in movies._movies:
                print(str(i) + " " + movie["name"])
                i += 1


if __name__ == "__main__":
    main()