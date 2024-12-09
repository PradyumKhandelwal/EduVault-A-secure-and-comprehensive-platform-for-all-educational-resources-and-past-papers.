import csv

# Create a list of dictionaries representing users
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
    {'username': 'user3', 'password': 'password3'}
]

# Write the users list to a CSV file
with open('users.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['username', 'password'])
    writer.writeheader()
    for user in users:
        writer.writerow(user)
