
def run():
    #squares =[]
    #for i in range (1,101):
    #    if i % 3 != 0:
    #        squares.append(i**2)

    square=[i for i in range(1, 500) 
            if i % 4 == 0
            and i % 9 == 0
            and i % 6 ==0 
            ]

    print(square)

if __name__ =="__main__":
    run()