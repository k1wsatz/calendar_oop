class Ingredient:
    def __init__(self, name, protein, carbs, fats):
        self.protein = protein
        self.name = name
        self.carbs = carbs
        self.fats = fats

    @property
    def protein(self):
        return self._protein

    @protein.setter
    def protein(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Incorrect Type')
        self._protein = value


class Meal:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient, amount=100):
        ingredient.carbs *= amount / 100
        ingredient.fats *= amount / 100
        ingredient.protein *= amount / 100

        self.ingredients.append({
            'name': ingredient,
            'amount': amount,
        })

    @staticmethod
    def calc_kcal(ingredient):
        return ingredient.protein * 4 + ingredient.carbs * 4 + ingredient.fats * 9.4

    def __str__(self):
        temp = []

        for ingredient in self.ingredients:
            text = f'- {ingredient["amount"]}g {ingredient["name"].name} ('
            text += f'{ingredient["name"].protein}g białka, {ingredient["name"].carbs}g węglowodanów,' \
                    f' {ingredient["name"].fats}g tłuszczy,' \
                    f'{self.calc_kcal(ingredient["name"])} kcal)'
            temp.append(text)

        ings = '\n'.join(temp)

        return f"""
Posiłek: {self.name}
{ings}
        
     """

    def __repr__(self):
        attrs = ", ".join([f"{k[1:] if k[0] == '_' else k}={repr(v)}" for k, v in self.__dict__.items()])
        return f"{type(self).__name__}({attrs})"


class DayPlan:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def __str__(self):
        text_meals = '\n'.join([str(meal) for meal in self.meals])
        return f"""
        {self.name}
        {text_meals}
        """


i1 = Ingredient('egg', 13, 1.1, 11)
i2 = Ingredient('tomato', 0.9, 3.9, 0.2)

m1 = Meal('Scrambled eggs')
m2 = Meal('Pomidor')

m1.add_ingredient(i1, 150)
m1.add_ingredient(i1)
m2.add_ingredient(i2, 200)
m2.add_ingredient(i2)

pd = DayPlan('Oszczędny')

print(m1.DayPlan(i2))
# print(m.calc_kcal(i2))
