#Scope..

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside the function: {enemies}")

increase_enemies()
print(f"Enemies outside the function: {enemies}")
