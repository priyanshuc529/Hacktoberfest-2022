with open("./Input/Letters/starting_letter.txt",mode="r") as file:
    a = str(file.read())

import fileinput


invited_people = []
#for each name in invited_names.txt
with open(r".\Input\Names\invited_names.txt", mode="r") as f:
    for x in f:
        invited_people.append(x)


#Replace the [name] placeholder with the actual name.
for i in range(len(invited_people)):
    people = invited_people[i].rstrip()
    new_letter = a.replace("[name]",f"{people}")

    with open(f"./Output/ReadyToSend/{people}.txt",mode = "w") as f:
        f.write(new_letter)
