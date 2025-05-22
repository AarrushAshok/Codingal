#Shutdown
def shutdown(com):
    if com == "yes":
        return "Shutdown"
    elif com == "no":
        return "Abort shutdown"
    else:
        return "Sorry"

user_input = input("Do you want to shutdown?:").lower()
print(shutdown(user_input))