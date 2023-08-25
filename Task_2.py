import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def mails():
    valid_emails = []

    while True:
        user_choice = input("Do you want to enter an email address? (Yes/No): ").strip().lower()

        if user_choice == 'no' or user_choice == 'exit':
            break
        elif user_choice == 'yes':
            email = input("Enter an email address: ").strip()
            if is_valid_email(email):
                valid_emails.append(email)
                print("Email is valid.")
            else:
                print("Email is not valid.")
        else:
            print("Invalid input. Please enter Yes or No.")

    if valid_emails:
        with open("email_list.txt", "w") as file:
            for email in valid_emails:
                file.write(email + '\n')
        print("Emails written to 'email_list.txt'.")
    else:
        print("No valid emails to write.")

    print("Valid emails entered:")
    for email in valid_emails:
        print(email)

mails()
