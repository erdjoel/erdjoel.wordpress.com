class Pizza:
    """Class method Real World Usage:
    to define alternative constructors for your classes.

    These class method use the same __init__ constructor internally (python only allows one __init__
    method per class, so this can provide a shortcut for remembering all of the various ingredients.
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        # Always use cls for the first argument to class methods
        # it points to the class—and not the object instance—when the method is called.
        # it can’t modify object instance state.
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


if __name__ == '__main__':
    pizza1 = Pizza.margherita()  # create new Pizza instance with margherita's ingredients
    pizza2 = Pizza.prosciutto()  # create new Pizza instance with prosciutto's ingredients
    pizza3 = Pizza(('mozzarella', 'extra cheese'))

    print(pizza3)

