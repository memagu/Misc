import random


class Blob:
    def __init__(self, p_spawn, p_death, p_reproduction, p_reproduction_mutation):
        self.p_spawn = p_spawn
        self.p_death = p_death
        self.p_reproduction = p_reproduction
        self.p_reproduction_mutation = p_reproduction_mutation

    def __str__(self):
        return f"Blob(p_spawn={self.p_spawn}, p_death={self.p_death}, p_reproduction={self.p_reproduction}, p_reproduction_mutation={self.p_reproduction_mutation})"

    def __repr__(self):
        return f"Blob(p_spawn={self.p_spawn}, p_death={self.p_death}, p_reproduction={self.p_reproduction}, p_reproduction_mutation={self.p_reproduction_mutation})"

    def __copy__(self):
        return Blob(self.p_spawn,
                    self.p_death,
                    self.p_reproduction,
                    self.p_reproduction_mutation)

    def reproduce(self):
        if self.p_reproduction > random.randint(0, 1_000_000) / 1_000_000:
            if not self.p_reproduction_mutation > random.randint(0, 1_000_000) / 1_000_000:
                # return self.__copy__()
                pass

            return Blob(max(0, self.p_spawn + random.choice(range(-5, 6)) / 100),
                        max(0, self.p_death + random.choice(range(-5, 6)) / 100),
                        max(0, self.p_reproduction + random.choice(range(-5, 6)) / 100),
                        max(0, self.p_reproduction_mutation + random.choice(range(-5, 6)) / 100))

    def die(self):
        return self.p_death > random.randint(0, 1_000_000) / 1_000_000


b1 = Blob(p_spawn=1, p_death=0.05, p_reproduction=0.2, p_reproduction_mutation=0.1)
blobs = {b1}
blobs_remove = []
blobs_add = []

for i in range(10):
    for blob in blobs:
        blobs_add.append(blob.reproduce())
        if blob.die():
            blobs_remove.append(blob)

    while blobs_add:
        if blobs_add[-1]:
            blobs.add(blobs_add.pop())
            continue
        blobs_add.pop()

    while blobs_remove:
        if blobs_remove[-1]:
            blobs.remove(blobs_remove.pop())
            continue
        blobs_remove.pop()

    print(blobs, "\n")