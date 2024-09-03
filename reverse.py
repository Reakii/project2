class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


user_input = input("Enter a word: ")


reverse_instance = Reverse(user_input)


print("Reversed string:", reverse_instance.reverse_string())
