from movies import Movies

movies = Movies('./movies.txt')

def displayMenu():
    print()
    print("Menu")
    print("* enter q for exit")
    print("* enter list for listing all the movie names")
    print("* enter search for searching movies")
    print("* enter cast for searching cast")
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
        elif(inVar.lower() == "search"):
            searchingFor = input("Please enter the search term: ")
            found = False
            for movie in movies._movies:
                if (searchingFor.lower() in movie["name"].lower() ):
                    print(movie["name"])
                    found = True
            if (not found):
                print("No Results.")
        elif(inVar.lower() == "cast"):
            searchingFor = input("Please enter the search term: ")
            hasResults = False
            for movie in movies._movies:
                found = False
                first = True
                for actor in movie["cast"]:
                    if (searchingFor.lower() in actor.lower()):
                        found = True
                        hasResults = True
                        break
                if (not found):
                    continue
                print(movie["name"])
                for actor in movie["cast"]:
                    if (searchingFor.lower() in actor.lower()):
                        if (first):
                            print("['", end="")
                            first = False
                        else:
                            print(", '", end ="")
                        print(actor, end="'")
                print("]")
            if (not hasResults):
                print("No Result.")



if __name__ == "__main__":
    main()