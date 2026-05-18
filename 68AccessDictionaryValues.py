student = {
    "name": "Krishna",
    "age": 21,
    "branch": "CSE"
}

# Access using key
print("Name:", student["name"])
print("Age:", student.get("age"))  # get() avoids error if key not found