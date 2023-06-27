def main(tiles):

    raw_list = tiles.split(",")
    list_converted = []
    final_sorted_list = []
    numbers = []
    for i, y in enumerate(raw_list):
        if y.isnumeric() is True:
            list_converted.append(int(y))
        else:
            list_converted.append(y)
    for i in list_converted:
        if str(i).isnumeric() is True:
            final_sorted_list.append(int(i))
    final_sorted_list.sort()
    final_sorted_list.append("")
    list_length = len(list_converted)
    n = int(list_length ** 0.5)

    top_border = '┌' + '────┬' * (n-1) + '────┐\n'
    bottom_border = '└' + '────┴' * (n-1) + '────┘'

    cell_counter = 0
    row_counter = 0
    grid = ""
    for i in range(1, n + 1):
        line = "│"
        for h in range(1, n + 1):
            if list_converted[cell_counter] == "":
                line += f"  {list_converted[cell_counter]}  │"
            elif list_converted[cell_counter] > 9:
                line += f" {list_converted[cell_counter]} │"
            elif list_converted[cell_counter] <= 9:
                line += f"  {list_converted[cell_counter]} │"
            cell_counter += 1
        line += "\n"
        grid += line
        if row_counter < n - 1:
            grid += '├' + '────┼' * (n-1) + '────┤\n'
        row_counter += 1

    total_grid = top_border + grid + bottom_border

    print(total_grid)
    if list_converted == final_sorted_list:
        print("You won in 0 moves. Congratulations!")
        return "You won in 0 moves. Congratulations!"

    possibilities = []
    possibilities_cleaned = []
    user_text = ""
    loop_close = 0
    valid_move = 0
    blank_index = 0
    move_counter = 0

    while loop_close == 0:
        possibilities.clear()
        possibilities_cleaned.clear()
        user_text = input("Your move: ")
        if user_text == "quit":
            loop_close += 1
        elif user_text.isnumeric() is False:
            print(f"{user_text} is not valid. Try again.")
            continue
        elif user_text not in list_converted and user_text not in raw_list:
            print(f"{user_text} is not valid. Try again.")
            continue
        else:
            position = list_converted.index(int(user_text))
            if position % n != 0:
                possibilities.append(position - 1)
            if list_converted.index("") % n != 0:
                possibilities.append(position + 1)
            possibilities.append(position + n)
            possibilities.append(position - n)
            for i in possibilities:
                if 0 < len(list_converted) - i:
                    possibilities_cleaned.append(i)
            for i, y in enumerate(possibilities_cleaned):
                if list_converted[y] == "":
                    blank_index = list_converted.index("")
                    user_index = list_converted.index(int(user_text))
                    list_converted[blank_index] = int(user_text)
                    list_converted[user_index] = ""
                    valid_move += 1
                    continue
        if user_text.isnumeric() is True and valid_move == 0:
            print(f"{user_text} is not valid. Try again.")
            continue
        valid_move = 0

        top_border = '┌' + '────┬' * (n-1) + '────┐\n'
        bottom_border = '└' + '────┴' * (n-1) + '────┘'

        cell_counter = 0
        row_counter = 0
        grid = ""
        for i in range(1, n + 1):
            line = "│"
            for h in range(1, n + 1):
                if list_converted[cell_counter] == "":
                    line += f"  {list_converted[cell_counter]}  │"
                elif list_converted[cell_counter] > 9:
                    line += f" {list_converted[cell_counter]} │"
                elif list_converted[cell_counter] <= 9:
                    line += f"  {list_converted[cell_counter]} │"
                cell_counter += 1
            line += "\n"
            grid += line
            if row_counter < n - 1:
                grid += '├' + '────┼' * (n-1) + '────┤\n'
            row_counter += 1

        total_grid = top_border + grid + bottom_border
        move_counter += 1

        print(total_grid)

        if list_converted == final_sorted_list:
            print(f"You won in {move_counter} moves. Congratulations!")
            loop_close += 1


