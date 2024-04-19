import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
game_is_on = True
data = pandas.read_csv("50_states.csv")
counter = 0
all_states_list = data.state.to_list()
correct_list = []
while counter <= 50:
    answer = screen.textinput(
        title=f"Score: {counter}/50 States",
        prompt="Name a State's name!",
    )
    if (
        answer.title() in data["state"].values and answer not in correct_list
    ):  ### Можна перевести столбец в формат списка с помощью .tolist()
        correct_list.append(answer.title())
        state_data = data[data["state"] == answer.title()]
        counter += 1
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data.x), int(state_data.y))
        t.pendown()
        t.write(answer.title())
    if answer.lower() == "exit":
        states_to_learn = [
            state for state in all_states_list if state not in correct_list
        ]

        # for state in all_states_list:
        #     if state not in correct_list:
        #         states_to_learn.append(state)
        states_to_learn_table = pandas.DataFrame(states_to_learn)
        states_to_learn_table.to_csv("states_to_learn.csv")

        break
turtle.mainloop()
# Learning the missed states
