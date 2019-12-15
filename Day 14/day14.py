import math
def read_input(file):
    recipes = {}
    for row in file:
        row = row.replace(" => ",", ").strip("\n").split(",")
        inputs = []
        for value in row:
            value = value.split()
            inputs.append((value[1],int(value[0])))
        recipes[inputs[-1][0]] = {"output_amount":inputs[-1][1],"inputs":inputs[:-1]}
        #print(recipes)
    return recipes

def build(recipes, output, amount_to_produce, rests):
    amount_to_produce -= rests[output]
    batches = math.ceil(amount_to_produce/recipes[output]["output_amount"])
    rests[output] = recipes[output]["output_amount"] % amount_to_produce

    add_amount = 0
    for input in recipes[output]["inputs"]:
        print("At {} Output, looking at input {}. amount_to_produce {}, add_amount {}. Batches {}, rest {}".format(output,input,amount_to_produce,add_amount,batches,rests[output]))
        if input[0] == "ORE":
            print("found ORE")
            return batches * input[1]
        else:
            add_amount += build(recipes, input[0], batches * input[1], rests)
    print("BACK: At {} Output, looking at input {}. amount_to_produce {}, add_amount {}".format(output,input,amount_to_produce,add_amount))
    return amount_to_produce + add_amount

file = open("input.txt","r")
recipes = read_input(file)
print(recipes)
rests = {}
amount = build(recipes, "FUEL", 1, rests)
print("FINAL AMOUNT")
print(amount)
