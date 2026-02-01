def calculate_average(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total

def get_user_name(user):
    return user["name"].upper()

