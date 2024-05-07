def sort_list_strings(array: list[str]) -> list:
    return sorted(
        sorted(
            array, key=lambda x: len(x), reverse=False
        ),
        key=lambda x: len(x), reverse=True
    )


print(sort_list_strings(['a', 'bbb', 'ff', 'aaaaa', 'aaaaaaa']))
