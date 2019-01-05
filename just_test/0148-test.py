from just_test.utils import create_linked_list, get_solution


def main():
    head = create_linked_list([9, 1, 4, 2])
    solution = get_solution("0148-sort-list")
    result = solution.sortList(head)
    print(result)


if __name__ == '__main__':
    main()
