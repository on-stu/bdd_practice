participants = [
    'John Doe',
    'Jane Doe',
    'Joe Doe',
    'Jill Doe',
    'Jack Doe',
    'Jen Doe',
    'Jenny Doe',
]

def convert_only_first_name(names):
    temp_names = names.copy()
    for i, temp_name in enumerate(temp_names):
        temp_names[i] = temp_name.split()[0]
    return temp_names

def convert_names_to_uppercase(names):
    temp_names = names.copy()
    for i, temp_name in enumerate(temp_names):
        temp_names[i] = temp_name.upper()
    return temp_names

participants = convert_names_to_uppercase(participants)
participants = convert_only_first_name(participants)

print(participants)

# 웹 프로그래밍에서 많이 사용함 -> 함수형 프로그래밍

    
