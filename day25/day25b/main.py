import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


state_data = pandas.read_csv('50_states.csv')
state_data.set_index('state',inplace=True)
all_states = state_data.index.to_list()

def generate_missed_state():

    #not_gussed_state = []
    #for state in all_states:
    #    if state not in gussed_state:
    #        not_guessed.append(state)
    not_guessed = [state for state in all_states if state not in gussed_state ]
    new_data = pandas.DataFrame(not_guessed)


    #making a dict of not guessed..
    #missed_state = {'not_guessed':not_guessed}
    #data = pandas.DataFrame(missed_state)
    new_data.to_csv('states_to_learn.csv')
    
gussed_state =[]

while len(gussed_state) <50:

    answer_state = screen.textinput(title = f'{len(gussed_state)}/50 States Correct.', prompt ="What's another state name?").title()
    if answer_state == 'Exit':
        generate_missed_state()
        break
        
    if answer_state in all_states:
        gussed_state.append(answer_state)

        #write the name of turtle in map..
        data_of_state = state_data[state_data.index == answer_state].to_dict()
        x = data_of_state['x'][answer_state]
        y = data_of_state['y'][answer_state]

        #write the name of state in map..
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(x,y)
        tim.write(answer_state)

