with open('emails.txt', 'r') as emails:
    emails = emails.readlines()
    print(emails)
    for email in emails:
        if "hotmail" in email:
            print(email)
        else:
            print("email not found")
