class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list
        max_value = 0
        for i in input_list:
            if i > max_value:
                max_value = i
        output_list = []
        for i in input_list:
            if i > 0:
                output_list.append(max_value)
            else:
                output_list.append(i)
        return output_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        low = 0
        high = len(input_list) - 1
        middle = (low + high) // 2
        while low <= high:
            middle = (low + high) // 2
            if query == input_list[middle]:
                return middle
            elif query > input_list[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return -1
