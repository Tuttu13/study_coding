
class practice_fizzbuzz():
    """1から100までの数字を出力するプログラミングを書いてください。
    数字が3の倍数の時は数字の代わりにFizzと出力し、
    5の倍数の時は数字の代わりにBuzzと出力し、
    3と5の倍数のときは、FizzBuzzと出力すること。
    """

    def fizzbuzz():

        FIZZ :str = "fizz"
        BUZZ :str = "buzz"

        for i in range(1, 100):

            if i % 3 == 0 and i % 5 == 0:
                print(FIZZ + BUZZ)
            elif i % 3 == 0:
                print(FIZZ)
            elif i % 5 == 0:
                print(BUZZ)
            else:
                print(i)

        return True
    
practice_fizzbuzz.fizzbuzz()