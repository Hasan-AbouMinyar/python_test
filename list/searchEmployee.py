clients = ["John Doe", "Jane Smith",
            "Emily Davis", "Michael Brown",
            "Hasan","googlE","Hasan"]

hsan_count = clients.count("Hasan")
print(f"The name 'Hasan' appears {hsan_count} times in the list.")

index_of_googlE = clients.index("googlE")
print(f"The index of 'googlE' in the list is {index_of_googlE}.")

print("List of clients:")
for client in clients:
    print(client)