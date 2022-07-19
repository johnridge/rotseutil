def evalBoolArg(argument, defaultState):
    argument.upper()
    if argument == True or argument == 'TRUE':
        argument = True
    elif argument == False or argument == 'FALSE':
        argument = False
    else:
        argument = defaultState
    return argument
    