def reverse_text():
    while True:
        user_input = input("Enter a Word: ")

        if user_input.isalpha():
            reversed_text = user_input[::-1]
            print("Output:", reversed_text)
            break
        else:
            print("Error Reported! Enter text only.")

if __name__ == "__main__":
    reverse_text()
