class SparseArray:
    def __init__(self, sparse_array):
        self.length = len(sparse_array)
        self.array = dict()
        for i, element in enumerate(sparse_array):
            if element != 0:
                self.array[i] = element

    def append(self, value):
        if value > 0:
            self.array[self.length] = value
        self.length += 1

    def __getitem__(self, item):
        if item < self.length:
            if item in self.array:
                return self.array[item]
            else:
                return 0
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key < self.length:
            if key in self.array:
                if value == 0:
                    del self.array[key]
                else:
                    self.array[key] = value
            else:
                self.array[key] = value
        else:
            raise IndexError

    def __delitem__(self, key):
        if key < self.length:
            new_array = dict()
            for dict_key, value in self.array.items():
                if dict_key < key:
                    new_array[dict_key] = self.array[dict_key]
                elif dict_key > key:
                    new_array[dict_key - 1] = self.array[dict_key]
            self.array = new_array
            self.length -= 1
        else:
            raise IndexError

    def __str__(self):
        print(f"Length: {self.length}")
        last_key = -1
        txt = "["
        for key, value in sorted(self.array.items()):
            if last_key == key - 1:
                txt += f"{value}, "
            else:
                for i in range(last_key, key - 1):
                    txt += "0, "
                txt += f"{value}, "
            last_key = key
        for i in range(last_key, self.length - 1):
            txt += "0, "
        txt = txt[0:-2] + "]"
        print(txt)
