import random, string

output_file = "list.txt"
amount = int(input("amount of strings: "))

for i in range(amount):
    generated = ("").join(random.choices(string.ascii_letters + string.digits, k = 2))
    print(generated)
    with open(output_file, "a") as f:
        f.write(generated + "\n")
input()
