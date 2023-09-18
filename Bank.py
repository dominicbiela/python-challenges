# """
# Basic Object-Oriented Programming scenario of a bank
# """
# from datetime import date
# import uuid
# class User:
#     def __init__(self, name: str, dob: date, postcode: str):
#         self.name = name
#         self.dob = dob
#         self.postcode = postcode
#         self.age = int((date.today() - self.dob).days/365.25)
#
# class Bank(User):
#     def __init__(self, name: str, dob: date, postcode: str):
#         super().__init__(name, dob, postcode)
#         self.account = dict()
#
#     @staticmethod
#     def _get_acct_number() -> int:
#         acct_number = int(str(uuid.uuid4().int)[:10])
#         return acct_number
#
#     @staticmethod
#     def _generate_pin() -> int:
#         pin_number = int(str(uuid.uuid4().int)[:4])
#         return pin_number
#
#     def create_acct(self):
#         acct_num = self._get_acct_number()
#         pin = self._generate_pin()
#         self.account[acct_num] = pin
#         print('Welcome to Biela Bank')
#         print(f'Your Account Number is {acct_num}')
#         print(f'With PIN number {pin}')
#
#
#     def __repr__(self):
#         class_name = type(self).__name__
#         return f'{class_name}({self.name}, {self.age}, {self.postcode})'
#
# bank = Bank('Adam Bond',date(1992,1,4),'TS6 8TD')
# print(bank.create_acct())
import uuid
from dataclasses import dataclass, field
from getpass import getpass
from secrets import randbelow
from time import sleep
from typing import Dict, Tuple, Callable, ClassVar


class Menu:
    MENU: ClassVar[Tuple[Tuple[str, Callable[['Menu'], bool]], ...]]

    def screen(self):
        prompt = '\n'.join(f'{i}. {name}' for i, (name, fun) in enumerate(self.MENU)) + '\n'

        while True:
            choice = input(prompt)

            try:
                name, fun = self.MENU[int(choice)]
            except ValueError:
                print('Invalid integer entered')
            except IndexError:
                print('Choice out of range')
            else:
                if fun(self):
                    break


@dataclass(kw_only=True)
class Account(Menu):
    email: str
    pwd: str

    @classmethod
    def acct_details(cls):
        # Needs to return tuple
        cls.email = input('Email Address: ')
        cls.pwd = input('Password: ')


@dataclass(kw_only=True)
class BankDetails(Account):
    acct: str | None
    card: str | None
    pin: str | None

    @staticmethod
    def _generate_acct_number() -> str:
        acct_number = str(uuid.uuid4().int)[:8]
        return acct_number

    @staticmethod
    def _generate_card_number() -> str:
        card_number = f'4000{str(uuid.uuid4().int)[:12]}'
        return card_number

    @staticmethod
    def _generate_pin() -> str:
        pin_number = str(uuid.uuid4().int)[:4]
        return pin_number

    @classmethod
    def generate(cls):
        return cls(
            email=cls.email,
            pwd=cls.pwd,
            acct=cls._generate_acct_number(),
            card=cls._generate_card_number(),
            pin=cls._generate_pin()
        )

    def show_details(self):
        print(
            f"Your username: {self.email}\n"
            f"Your account number: {self.acct}\n"
            f"Your card number: {self.card}\n"
            f"Your PIN: {self.pin}"
        )

    def balance(self):
        print('Balance: 0')

    def logout(self) -> bool:
        print('You have successfully logged out!')
        return True

    def exit(self):
        print('Bye!')
        exit()

    MENU = (
        ('Exit', exit),
        ('Balance', balance),
        ('Log out', logout),
    )


@dataclass(kw_only=True)
class BankingSystem(Menu):
    # def __init__(self):
    #     self.accounts: Dict[str, Account] = dict()
    accounts: Dict[str, Account] = field(default_factory=dict)

    def create_account(self):
        print('Please enter a valid email address and password')
        Account.acct_details()
        if Account.email:
            account = BankDetails.generate()
            print('Your account has been created')
            account.show_details()
            self.accounts[account.card] = account

    def log_in(self):
        for _ in range(3):
            email = input('Enter your Email Address: ')
            if email != self.accounts.get(email):
                print('Wrong email address')
                break

            pwd = input('Enter your Password: ')
            if pwd != self.accounts.get(pwd):
                print('Wrong Password')
                sleep(2)
                break
            else:
                print('You have successfully logged in!')
                Account.screen(self)
                break

    def exit(self) -> bool:
        print('Bye!')
        return True

    MENU = (
        ('Exit', exit),
        ('Create an account', create_account),
        ('Log into an account', log_in),
    )


BankingSystem().screen()
