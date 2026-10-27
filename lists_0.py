foods = ["Rice", "Banana", "Yam", "Bread"]

foods[1] = "Beans"

print(foods)

# Add one item to the list
foods.insert(0, "Pepper Soup")
foods.insert(3, "Moin moin")
foods.append("Corn")
foods.append("Spaghetti")

print("My list after spaghetti: ", foods)

# Remove Item
# foods.pop()  # removes the last item
# foods.pop(0)  #Removes the item at index 0

foods.remove("Spaghetti")
# foods.remove("okro") Removing an item not in the list shows a ValueError

del foods[0]

last_item = foods.pop()
print("The last food on the list is " + last_item)
# print(foods[10]) Error: Index out of range
print(foods)