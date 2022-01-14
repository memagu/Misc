while True:
    P = int(input())

    if P == 2:
        print("Optimus Prime")
        break

    if P % 2 == 0:
        print("Even Steven")
        break

    else:
        for i in range(3, int(P ** 0.5 + 1), 2):
            if P % i == 0:
                print("Not Prime")
                print(i)
                break
            print("Optimus Prime")
            break

    print()



