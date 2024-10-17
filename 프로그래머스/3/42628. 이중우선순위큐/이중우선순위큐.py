def solution(operations):
    val_list = []
    for operation in operations:
        if operation[0] == 'I':
            number = int(operation[2:])
            val_list.append(number)
        elif operation == 'D 1':
            if val_list:
                val_list.remove(max(val_list))
        elif operation == 'D -1':
            if val_list:
                val_list.remove(min(val_list))

    if not val_list:
        return [0, 0]
    else:
        return [max(val_list), min(val_list)]