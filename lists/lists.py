class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return input_list
        max_value = 0
        for value in input_list:
            if value > max_value:
                max_value = value
        output_list = []
        for i in input_list:
            if i > 0:
                output_list.append(max_value)
            else:
                output_list.append(i)
        return output_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if len(input_list) == 0 or input_list[-1] < query:
            return -1
        else:
            def binary_func(low, high):

                if low > high:
                    return -1
                middle = (low + high) // 2
                if query == input_list[middle]:
                    return middle
                elif query > input_list[middle]:
                    return binary_func(middle + 1, high)
                else:
                    return binary_func(low, middle - 1)
            return binary_func(0, len(input_list) - 1)

