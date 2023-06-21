import time


def add_google_search_term(search, type_):
    with open("data.txt") as file:
        file2 = file.read().split("\n")
        file2.append(f"GOOGLE SEARCH|search:{search}|type:{type_}")

    with open("data.txt", "w") as file:
        file.write('\n'.join(file2))


def add_website(url: str, type_):
    with open("data.txt") as file:
        file2 = file.read().split("\n")
        website = url.split("/")[2]
        file2.append(f"WEBSITE|url:{url}|type:{type_}|website:{website}")

    with open("data.txt", "w") as file:
        file.write('\n'.join(file2))


def search_google_search_terms(type_, term=None):
    if term is None:
        with open("data.txt") as file:
            file = file.read().split("\n")
            for i in range(0, len(file)):
                data = file[i].split("|")
                if type_ in data[2] and data[0] == "GOOGLE SEARCH":
                    print(f"\t\t\t(FOUND) [SEARCH:{data[1].split(':')[1]}]")


def search_websites(type_, website=None, url=None):  # TYPE: type of website | WEBSITE: the domain of the website | URL: the url of the website (not perfect)
    if website is None and url is None:
        with open("data.txt") as file:
            file = file.read().split("\n")
            for i in range(0, len(file)):
                data = file[i].split("|")
                if type_ in data[2] and data[0] == "WEBSITE":
                    print(f"\t\t\t(FOUND) [URL:{data[1].split(':')[1]}{data[1].split(':')[2]}|WEBSITE:{data[2].split(':')[1]}]")


if __name__ == '__main__':
    print("Database Initializing...")
    time.sleep(1.43)
    print("Database Initialized")
    time.sleep(0.63)
    print("\nConsole Open")
    while True:
        command = input("\t> ")
        if command == "add website":
            data1 = input("\t\t> Enter Website URL: ")
            data2 = input("\t\t> Enter Website Type (Webcam, Vulnerable Files, etc): ")
            if data1 == "" or data2 == "":
                print("\t\t> Invalid Website or Type")
            else:
                add_website(data1, data2)
                print("\t\t> Website Added")
        elif command == "add search":
            data1 = input("\t\t> Enter Search Term: ")
            data2 = input("\t\t> Enter Search Type (Webcam, Vulnerable Files, etc): ")
            if data1 == "" or data2 == "":
                print("\t\t> Invalid Type or Search")
            else:
                add_google_search_term(data1, data2)
                print("\t\t> Search Added")
        elif command == "search website" or command == "search websites":
            data1 = input("\t\t> Enter Website Type: ")
            search_websites(data1)
        elif command == "search terms" or command == "search term":
            data1 = input("\t\t> Enter Search Type: ")
            search_google_search_terms(data1)
