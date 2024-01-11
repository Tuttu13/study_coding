import random

class binary_game():
 
    def main():
        n = 0 
        num = random.randint(1, 100)

        print("looking for correct number")

        while True:

            n += 1

            print(" {0} times".format(n))

            if n == 1:
                ans = input("choose number from 1 to 100")
            else:
                ans = input("choose correct number")

            if num == int(ans):
                print(str(ans) + " is correct")
                break

            if num > int(ans):
                print("{0} is bigger than answer".format(ans))

            else:
                print("{0} is lower than answer".format(ans))

binary_game.main()