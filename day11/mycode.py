import random
cards = [11,10,10,10,10,1,2,3,4,5,6,7,8,9]

user =[]
comp = []
u1 = random.choice(cards)
u2 = random.choice(cards)
user.extend([u1,u2])
c1 = random.choice(cards)
c2 = random.choice(cards)
comp.extend([c1,c2])
print(f"User: {user}")
print(f"Comp: {comp}")


while True:
    user_sum = sum(user)

    if user_sum ==21:
        print("BlackJack")
        break
    
    if user_sum > 21:
        if 11 in user:
            user.remove(11)
            user.append(1)
        else:
            print("YOU lose")
            break


    if not input("Do u wannna draw a card ?").lower().startswith('y'):
        break
    u3 = random.choice(cards)
    user.append(u3)
    
    print(user_sum)

#computer drawing cards..
comp_sum = sum(comp)
while comp_sum <17:
    
    c3 = random.choice(cards)
    comp.append(c3)
    
    if 11 in comp:
        comp.remove(11)
        comp.append(1)
    comp_sum = sum(comp)

if comp_sum >21:
    print("YOU win")
else:
    if user_sum >comp_sum:
        print("YOu win")
    else:
        print("YOu lose")

print(f"User: {user}")
print(f"Comp: {comp}")
print(user_sum)
print(comp_sum)



