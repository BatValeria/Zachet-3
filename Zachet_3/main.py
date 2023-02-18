import hashlib
import random
import os
import re
import string


class IdCounter:  # First Task
    def __init__(self) -> None:
        self.num_ = 6
        self.numbers = string.digits

        self.__id = ''.join([random.choice(self.numbers) for _ in range(self.num_)])

    def set_id(self, num_: 6) -> None:
        self.num_ = num_
        self.__id = ''.join([random.choice(self.numbers) for _ in range(self.num_)])

    def get_id_person(self) -> str:
        return self.__id


class Password:  # Second Task
    def __init__(self, password_: str) -> None:
        self.has_digit = None
        self.has_symbol = None
        self.has_uppercase = None
        self.new_key = None
        self.pass_to_check = None
        self.key = None
        self.password_ = None
        self.salt = os.urandom(32)
        self.password_ = password_

    def set_password(self, password_) -> None:
        self.password_ = password_

    def get_password(self) -> str:
        return self.password_

    def first_check_password(self) -> bool:
        self.has_uppercase = re.search(r'[A-Z]', self.password_) is not None
        self.has_symbol = re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password_) is not None
        self.has_digit = re.search(r'\d', self.password_) is not None

        if self.has_uppercase and self.has_symbol and self.has_digit:
            return True
        else:
            raise ValueError("Password must contain at least one uppercase letter, one special symbol, and one number.")

    def get_password_one(self) -> tuple:
        self.salt = os.urandom(32)
        self.key = hashlib.pbkdf2_hmac(
            'sha256',
            self.password_.encode('utf-8'),
            self.salt,
            100000,
            dklen=128)
        return self.key, self.salt

    def check_password(self, salt_) -> None:
        self.salt = salt_
        password_to_check = self.password_
        self.new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password_to_check.encode('utf-8'),
            self.salt,
            100000,
            dklen=128)

        if self.new_key != self.key:
            print('Password is not correct')
        else:
            print('Password is correct')


if __name__ == '__main__':
    pass_ = Password("Password123")
    pass_.set_password("Password124.")
    pass_.first_check_password()
    key, salt = pass_.get_password_one()
    pass_.salt = salt
    pass_.key = key
    pass_.check_password(salt)


class Product(IdCounter):  # Third Task
    def __init__(self, price: int, rating: int) -> None:
        super().__init__()
        self.price = price
        self.rate = rating
        self.__name = None
        self.__id = super().get_id_person()

    def set_name(self, name) -> None:
        self.__name = name

    def set_price(self, price) -> None:
        self.price = price

    def set_rate(self, rating) -> None:
        self.rate = rating

    def __str__(self) -> str:
        return f"{self.__id}_{self.__name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.__id!r}, name={self.__name!r}, price={self.price!r}," \
               f" rating={self.rate!r})"


if __name__ == '__main__':
    product = Product(100, 5)
    product.set_name("Milk")

    print(product.__str__())
    print(product.__repr__())


class Cart:  # Forth Task
    def __init__(self, cart_cart: list):
        self.element = None
        self.cart_cart = cart_cart

    def __add__(self, other):
        self.cart_cart = Cart(self.cart_cart + other.cart_cart)
        return self.cart_cart

    def delete(self, element):
        self.element = element
        for self.element in self.cart_cart:
            self.cart_cart.remove(self.element)
            return self.cart_cart


if __name__ == '__main__':
    cart_ = Cart(["milk", "bread", "cheese"])
    add_cart_ = Cart(["banana", "apple"])
    full_cart = cart_ + add_cart_
    print(full_cart.cart_cart)  # add products
    _cart_ = Cart(full_cart.cart_cart)
    print(_cart_.delete(1))  # delete products


def fake_password():
    return "Password1"


class User(IdCounter, Password, Cart):  # Fifth task
    def __init__(self, username, password_) -> None:
        IdCounter.__init__(self)
        Password.__init__(self, password_)
        Cart.__init__(self, cart_cart=[])
        self.__username = username
        self.__id = super().get_id_person()
        self.__password = super().get_password_one()
        self.password_clear = super().get_password()

    def set_name(self, username):
        self.__username = username
        super().cart_cart = []  # create a cart with initializing of a name from cart class

    def check_username(self):
        if r'[!@#$%^&*(),.?":{}|<>]' == self.__username:
            raise ValueError("Username doesn't have to contain special symbols.")
        else:
            return True

    def __str__(self) -> str:
        return f"{self.__id}_{self.__username}_{fake_password()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.__id!r}, name={self.__username!r}, password={fake_password()!r}"


if __name__ == '__main__':
    user = User("Valeria", "Password123.")
    print(user.__repr__())
    print(user.__str__())


class my_shop:
    def __init__(self) -> None:
        self.item = None
        self.rate = random.choice([1, 2, 3, 4, 5])
        self.cost = random.choice([11, 33, 54, 77, 100, 44, 182, 90])
        self.list = ["Milk", "Bread", "Eggs", "Coke", "Cheese"]
        self.products = [self.item for self.item in self.list]
        print(self.item)

    def gives_back(self) -> str:
        return f'Product: {self.item}, Rating: {self.rate}, Cost: {self.cost} rub'


if __name__ == '__main__':
    my_shop = my_shop()
    print(my_shop.gives_back())