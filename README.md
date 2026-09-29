this is a program to use a set of temperature recorded in celcius and fahrenheit to calculate the weight.
it takes a starting guess of 1.5 to work out the actual 'weight' in the function. first it adds a small value to check the loss in the function. if the loss goes up it moves the weight down by learning rate(0.01); if it goes down it moves up instead until the loss is below 0.0001.(here, loss is distance between line's prediction and real fahrenheit value)
Before this project, I could barely write basic input/output in Python. i learned to use loop, functions, return and break, and deciding what code belongs where.
the code can only predict the weight given that we already know the bias. it is limited since i used what i already knew about the formula.
