names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Filter names starting with 'A'
filtered_names = list(filter(lambda each: each.startswith('A'), names))

print(filtered_names)