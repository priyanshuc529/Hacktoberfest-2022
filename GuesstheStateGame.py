import turtle as t
import pandas


def is_there(answer_state):
    all_states = data.state.to_list()
    if answer_state not in answer:
        for x in all_states :
            if x == answer_state:
                answer.append(x)
                return  True
    return False




my_screen = t.Screen()
my_screen.tracer(0)
my_screen.title("Guess the state")
image = "blank_states_img.gif"
my_screen.addshape(image)

mover = t.Turtle()
mover.hideturtle()
t.shape(image)
my_screen.update()
is_on = True
#
missing = []
mover2 = t.Turtle()
mover2.hideturtle()
mover2.color("red")
done_state = 0
answer= []
while is_on:


    data = pandas.read_csv("50_states.csv")
    answer_state = my_screen.textinput(title=f" total state {done_state}/50 ", prompt=" Guess a state ").title()
    if answer_state == "Exit":
        for x in data.state:
            if x not in answer:
                missing.append(x)
        study = pandas.DataFrame(missing)
        study.to_csv("go_study.csv")
        break


    elif done_state == 50:
        is_on = False
        mover2.clear()
        mover2.write("Well done",align="center",font = ("Arial", 24, "normal"))
        mover2.goto(0,0)
    elif is_there(answer_state):
        mover2.clear()
        done_state += 1
        move = data[data.state == answer_state]
        new_x = int(move.x)
        print(new_x)
        new_y = int(move.y)
        print(new_y)
        mover.penup()
        mover.color("black")
        mover.goto(new_x, new_y)
        mover.write(f"{answer_state}",align="center" , font=("Arial", 8, "normal"))
    else:
        mover2.clear()
        mover2.write("please try again",align="center",font=("Arial", 24, "normal"))
        mover2.goto(0,0)


    my_screen.update()
