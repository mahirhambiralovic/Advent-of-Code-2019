import math

def get_number_position(number,position):
    return math.floor((number % (10**position)) / (10**(position-1)))
matches = 0

for i in range(510152):
    number = i + 172930

    one = get_number_position(number,1)
    two = get_number_position(number,2)
    three = get_number_position(number,3)
    four = get_number_position(number,4)
    five = get_number_position(number,5)
    six = get_number_position(number,6)

    if six<=five<=four<=three<=two<=one:
        p1 = (one == two)
        p2 = (two == three)
        p3 = (three == four)
        p4 = (four == five)
        p5 = (five == six)
        arr = [p5,p4,p3,p2,p1]
        works = False
        pairs = 0
        for j in arr:
            if j:
                pairs += 1
            elif pairs == 0:
                continue
            else:
                if pairs == 1:
                    works = True
                else:
                    pairs = 0
        # for last pair
        if pairs == 1:
            works = True

        if works == True:
            matches += 1
print(matches)
