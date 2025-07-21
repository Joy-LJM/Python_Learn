import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game Start")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coordinates(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coordinates)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
STATE_COUNT=50
guessed_states=[]

while len(guessed_states) < STATE_COUNT:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/{STATE_COUNT} State Correct", prompt="What is another state's name?")
    capitalize_state=answer_state.title()

    if capitalize_state == 'Exit':
        # save the missing states to .csv
        # method 1
        # missing_states = pandas.DataFrame(state_list)
        # missing_states.to_csv("states_to_learn.csv")

        # method 2
        # missing_states=[]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # list comprehension to replace above loop
        #  loop state_list, if state is not in guessed_states, append state into missing_states
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if capitalize_state in state_list:
        guessed_states.append(answer_state)
        # save the missing states to .csv
        # method 1
        # state_list.remove(capitalize_state)
        state_data=data[data.state == capitalize_state]

        pen=turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        # get value
        # method 1
        # x_value=state_data["x"].values[0]
        # y_value=state_data["y"].values[0]
        # pen.goto(x=x_value,y=y_value)

        # method 2
        pen.goto(x=state_data.x.item(),y=state_data.y.item()) #item():Return the first element of the underlying data as a Python scalar.
        pen.write(capitalize_state)


# turtle.mainloop()
