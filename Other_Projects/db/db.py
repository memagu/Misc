import pickle


def save(object, file):
    with open(file, "wb") as f:
        pickle.dump(object, f)


def load(file):
    with open(file, "rb") as f:
        try:
            obj = pickle.load(f)
        except EOFError:
            obj = []
    return obj