import pickle

def save_object(object, file):
    with open(file, "wb") as f:
        pickle.dump(object, f)


def load_object(file):
    with open(file, "rb") as f:
        try:
            obj = pickle.load(f)
        except EOFError:
            obj = []
    return obj


class Account:
    def __init__(self, u_name, p_word):
        self.u_name = u_name
        self.p_word = p_word
        self.things = {}

    def credentials(self):
        return {self.u_name: self.p_word}

    def addThing(self, k, v):
        self.things[k] = v

    def getThing(self, k):
        return self.things[k]


def encrypt(string):
    password_length = 64
    password = [ord(char) for char in string]
    printable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    interstage = 0
    for i in range(len(password)):
        password[i] += sum(password[:i])
        password[i] *= sum(password)
        interstage += password[i]
        while len(str(interstage + password_length)) < 2 * password_length:
            interstage *= interstage

    interstage = [char for char in str(interstage)[:2*password_length]]

    password = []
    for i in range(0, password_length * 2, 2):
        password.append(int(interstage[i] + interstage[i+1]) % len(printable))

    password = [printable[num] for num in password]
    return "".join(password)


def register_account():
    check_if_name_available = True
    while check_if_name_available:
        u_name = input("Enter username: ")
        accounts = load_object("accounts.pkl")
        if accounts != []:
            if u_name in [acc.u_name for acc in accounts]:
                print("Username already in use, try another one.")
                continue

        check_if_name_available = False

    p_word = encrypt(input("Enter password: "))

    accounts = load_object("accounts.pkl")
    account = Account(u_name, p_word)
    accounts.append(account)
    save_object(accounts, "accounts.pkl")
    return account


def login():
    u_name = input("Enter username: ")
    p_word = encrypt(input("Enter password: "))
    accounts = load_object("accounts.pkl")

    if accounts != []:
        for account in accounts:
            if u_name == account.u_name and p_word == account.p_word:
                return account
        print("Username or password entered incorrectly!")
    else:
        print("No accounts registered.")

    return None


def remove_account(u_name, p_word):
    accounts = load_object("accounts.pkl")
    accounts.remove(Account(u_name, p_word))
    save_object(accounts, "accounts.pkl")


def start():
    selecting = True
    r = ["r", "reg", "register"]
    l = ["l", "login, sign in"]

    while selecting:
        select = input("\nRegister account or login?: ").lower()
        if select not in r + l:
            print("Invalid input, try again.")
        else:
            selecting = False


    if select in r:
        return register_account()
    else:
        return login()


def modify(account):
    selecting = True
    a = ["a", "add"]
    d = ["d", "del", "delete"]
    g = ["g", "get"]
    r = ["r", "remove"]


    while selecting:
        select = input("\nRegister account or login?: ").lower()
        if select not in a + d + g + r:
            print("Invalid input, try again.")
        else:
            selecting = False

    if select in a:
        account.addThing(input("Enter key and value separeted by a space").split())

run = True
while run:
    account = start()
    while modify(account):
        None

