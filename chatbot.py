# Reading data from the files and populating dictionaries
f = open("untitled3.txt", "r")
dic1 = {}
for line in f:
    (key, value) = line.replace("\n", "").split(":", 1)
    dic1[key] = value

f1 = open("untitled4.txt", "r")
dic2 = {}
for line1 in f1:
    (key, value) = line1.replace("\n", "").split(":", 1)
    dic2[key] = value

# Response function for dic1
def respond(user_input, dic1):
    user_input = user_input.lower().strip()
    if user_input in dic1:
        return dic1[user_input]
    return "Sorry, I don't understand that."

# Response function for dic2
def respond1(user_input, dic2):
    user_input = user_input.lower().strip()
    if user_input in dic2:
        return dic2[user_input]
    return "Sorry, I don't understand that."

# Main function
def main():
    while True:
        print("Press 1 for chat bot:")
        print("Press 2 for pyt bot:")
        print("Press 3 for exit:")
        n1 = int(input("Enter your choice:"))

        if n1 == 1:
            print("Welcome to the ChatBot!")
            print("Ask me something about AI. Type 'bye' or 'exit' to exit.\n")
            while True:
                user_input = input("You: ")
                if user_input.lower().strip() == "bye":
                    print("Bot:", dic1["Bye"])
                    break
                elif user_input.lower().strip() == "exit":
                    print("Bot:", dic1["exit"])
                    break
                else:
                    reply = respond(user_input, dic1)
                    print("Bot:", reply)

        elif n1 == 2:
            print("Welcome to the PytBot!")
            print("Ask me something about AI. Type 'bye' or 'exit' to exit.\n")
            while True:
                user_input = input("You: ")
                if user_input.lower().strip() == "bye":
                    print("Bot:", dic2["Bye"])
                    break
                elif user_input.lower().strip() == "exit":
                    print("Bot:", dic2["exit"])
                    break
                else:
                    reply = respond1(user_input, dic2)
                    print("Bot:", reply)

        elif n1 == 3:
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
