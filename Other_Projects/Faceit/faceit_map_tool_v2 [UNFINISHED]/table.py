class Table:
    def __init__(self, columns):
        self.columns = columns
        self.rows = []

    def __str__(self):
        result = ", ".join(map(str, self.columns)) + "\n"
        for row in self.rows:
            result += ", ".join(map(str, row)) + "\n"
        return result

    def add_column(self, column):
        if column in self.columns:
            return
        self.columns.append(column)
        for row in self.rows:
            row.append(None)

    def del_column(self, column):
        if column not in self.columns:
            return
        i = self.columns.index(column)
        self.columns.remove(column)
        for row in self.rows:
            row.pop(i)

    def append_row(self, amount=1):
        for i in range(amount):
            self.rows.append([None for _ in range(len(self.columns))])

    def insert_row(self, index):
        if index in range(-len(self.rows)-1, len(self.rows)):
            self.rows.insert(i, [None for _ in range(len(self.columns))])

    def del_row(self, index):
        if index in range(-len(self.rows)-1, len(self.rows)):
            self.rows.pop(index)

    def insert_value(self, column, row, value):
        x = self.columns.index(column)
        y = row
        self.rows[y][x] = value

    def sort(self, column, reverse=False):
        index = self.columns.index(column)
        self.rows.sort(key=lambda x: (x[index] is None, x[index]), reverse=reverse)


if __name__ == "__main__":
    table = Table(["c1", "c2", "c3", "c4"])

    table.append_row(4)

    table.insert_value("c1", 2, 1)
    table.insert_value("c2", 1, 2)
    table.insert_value("c3", 0, 3)
    table.insert_value("c1", 2, 4)
    table.insert_value("c2", 3, 5)
    table.insert_value("c3", 3, 6)

    print(table)

    table.sort("c3")

    print(table)















































# class Table:
#     def __init__(self, columns):
#         self.columns = columns
#         self.rows = []
#         self.table = {column: [] for column in columns}
#
#     def __str__(self):
#         result = ""
#         for column, row in self.table.items():
#             result += f"{column}: {', '.join(map(str, row))}\n"
#         return result
#
#     def add_column(self, column):
#         self.table[column] = []
#
#     def del_column(self, column):
#         if column in self.table.keys():
#             del self.table[column]
#
#     def append_row(self, column, value):
#         self.table[column].append(value)
#
#     def insert_row(self, column, value, index=0):
#         self.table[column].insert(index, value)
#
#
# table = Table(["c1", "c2", "c3", "c4"])
#
# for i in range(1, 5):
#     for j in range(5):
#         table.append_row(f"c{i}", j)
#
# print(table)