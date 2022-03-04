class Magic(object, metaclass=type):

    sentence = 'Hello bro'

    def __new__(cls, *args, **kwargs):
        cls.awesome = lambda x: 420

        obj = super().__new__(cls, *args, **kwargs)
        obj.magic = 420

        return obj

    def __init__(self):
        self.title = 'Ala'

    @classmethod
    def custom_constructor(cls, *args, **kwargs):

        obj = super().__new__(cls, *args, **kwargs)
        obj.magic = 666

        return obj

    def do_smth(self):
        return self.sentence

# m = Magic()
# print(type(m))
# print(m.__dict__)
# print(m.awesome())

# new_obj = Magic.custom_constructor()
# print(new_obj, type(new_obj), new_obj.__dict__)
m = Magic()
print(m.sentence)