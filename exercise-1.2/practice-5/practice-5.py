# Step 1: Make a list of the months in a year, and store it as months_named.
months_named = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Step 2: Make another list of numbers ranging from 1 to 12 as months_numbered.
months_numbered = list(range(1, 13))

# Step 3: Use the zip() function to merge the two lists together into a dictionary called months_dict.
months_dict = dict(zip(months_named, months_numbered))

# Step 4: Clear both initial lists (months_named and months_numbered) with the clear() method available to them.
months_named.clear()
months_numbered.clear()

# Step 5: Print the entire dictionary onto your screen.
print(months_dict)

# Step 6: Convert the keys of this dictionary back into another list, months_extracted, and then list them in alphabetical order.
months_extracted = list(months_dict.keys()) # can also do "sorted(list(months_dict.keys())"
months_extracted.sort()
print(months_extracted)
