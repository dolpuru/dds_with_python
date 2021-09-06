card_numbers = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]
answer = []
n = len(card_numbers)
odd= 0
even=0
for i,v in enumerate(card_numbers):
    if i%2 !=0:
        for j in range(16):
            if j%2 == 0:
                temp = 0
                while temp <= 9:
                    temp = str(int(v[i])*2)[0] + str(int(v[i])*2)[1]
                
            else:

print(answer)