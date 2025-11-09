def move(my_list, direction):

    def move(my_list, direction):
  index_of_one = lst.index(1)

  if direction == "right" and index_of_one < len(lst) - 1:
        lst[index_of_one], lst[index_of_one + 1] = lst[index_of_one + 1], lst[index_of_one]

  elif direction == "left" and index_of_one > 0:
        lst[index_of_one], lst[index_of_one - 1] = lst[index_of_one - 1], lst[index_of_one]

  return lst
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
