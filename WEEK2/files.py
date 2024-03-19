with open ("emails.txt", "r") as emails:
   results = emails.read()
   list_of_emails = results.split()

   for i in range(len(list_of_emails)) :
      if list_of_emails[i] == "WalobwaDan@gmail.com" :
          print('Found Walobwa at position', i+1)