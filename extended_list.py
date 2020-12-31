class ExtendedList(list):
    def __init__(self, lst):
        super().__init__(lst)
        self.lst = lst

    def __eq__(self, other):
        return self.average() == other.average()

    def __ne__(self, other):
        return self.average() != other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __ge__(self, other):
        return self.average() >= other.average()

    def __le__(self, other):
        return self.average() <= other.average()

    def __add__(self, other):
        new_lst = self.lst
        new_lst.extend(other.lst)
        return new_lst

    def average(self):
        return sum(self.lst) / len(self.lst)

    @staticmethod
    def next_val(lst):
        for num in lst:
            try:
                yield float(num)
            except ValueError:
                yield num


class TypeList(ExtendedList):
    def __eq__(self, other):
        if self.lst[-1] == other.lst[-1]:
            return True
        return False

    def __ne__(self, other):
        if self.lst[-1] != other.lst[-1]:
            return True
        return False


# lst1 = ExtendedList([0, 1, 2])
# lst2 = ExtendedList([0, 1, 3, 2])
# print(lst1 == lst2)
# print(lst1 < lst2)
# print(lst1 <= lst2)
#
# print(lst1 + lst2)
#
# lst3 = TypeList([1, 2])
# print(lst3 == lst2)
#
# lst2 = ExtendedList([0, 1, 3, 2])
# next_val = ExtendedList.next_val(lst2.lst)
# while True:
#     try:
#         print(next(next_val))
#     except StopIteration:
#         break
