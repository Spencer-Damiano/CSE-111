def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    reverse_list = fruit_list[::-1]
    print(f' reverse list {reverse_list}')

    fruit_list.append('orange')
    print(f'append orange {fruit_list}')

    index_replace = fruit_list.index('apple')
    fruit_list.insert(index_replace, 'cherry')
    print(f'cherr b4 apple {fruit_list}')

    index_replace = fruit_list.index('banana')
    fruit_list.pop(index_replace)
    print(f'no nana {fruit_list}')

    print(f'pop {fruit_list[-1]}: {fruit_list[:-1]}')
    fruit_list.pop(-1)

    fruit_list = sorted(fruit_list)
    print(f'sorted {fruit_list}')

    fruit_list = fruit_list.clear()
    print(f'clear {fruit_list}')








main()