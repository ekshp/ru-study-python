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
        low = 0
        high = len(input_list) - 1
        while low <= high:
            middle = (low + high) // 2
            if query == input_list[middle]:
                return middle
            elif query > input_list[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return -1

