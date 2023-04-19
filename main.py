list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2) -> list:
    # Create dictionaries for each list with 'id' key as the dictionary key
    dict_1 = {item['id']: item for item in list_1}
    dict_2 = {item['id']: item for item in list_2}

    # Merge the dictionaries
    dict_3 = {}
    dict_3.update(dict_1)
    dict_3.update(dict_2)

    # Convert the merged dictionary into a list
    list_3 = list(dict_3.values())

    return list_3


list_3 = merge_lists(list_1, list_2)


print(list_3)
