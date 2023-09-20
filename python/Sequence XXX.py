'''SequenceX'''
def main(num, ron):
    '''solution'''
    for i in range(num):
        for _ in range(ron):
            for j in range(num):
                if j == 0:
                    print("*", end="")
                elif i == j or i + j == num - 1:
                    print("*", end="")
                elif j == num - 1:
                    print("*", end="")
                elif i == 0:
                    print("*", end="")
                elif i == num - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print(end=" ")
        print()

main(int(input()), int(input()))
