prompt = "Hi, my name is Josh and I will be your friendly AI today."
prompt += "\nHow may I assist you today? "

message = ""

while message != 'quit':
    message = input(prompt)

    if message!= 'quit':
        print(message)