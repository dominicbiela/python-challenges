# """
# Basic Object-Oriented Programming scenario of a bank
# """
import uuid
from dataclasses import dataclass, field
from getpass import getpass
from secrets import randbelow
from time import sleep
from typing import Dict, Tuple, Callable, ClassVar


class Menu:
    MENU: ClassVar[Tuple[Tuple[str, Callable[['Menu'], bool]], ...]]
    """
     example = (('Exit', exit),
                ('Create an account', create_account),
                ('Log into an account', log_in),
                )
     """

    def screen(self):
        prompt = '\n'.join(f'{i}. {name}' for i, (name, func) in enumerate(self.MENU)) + '\n'

        while True:
            choice = input(prompt)

            try:
                name, func = self.MENU[int(choice)]
            except ValueError:
                print('Invalid integer entered')
            except IndexError:
                print('Choice out of range')
            else:
                if func(self):
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
    def generate(cls) -> 'BankDetails':
        return cls(
            email=cls.email,
            pwd=cls.pwd,
            acct=cls._generate_acct_number(),
            card=cls._generate_card_number(),
            pin=cls._generate_pin()
        )

    def show_details(self):
        print("\n"
              f"Your username: {self.email}\n"
              f"Your account number: {self.acct}\n"
              f"Your card number: {self.card}\n"
              f"Your PIN: {self.pin}\n",
              )

    def balance(self):
        #TODO add balance as class parameter
        print('Balance: 0')

    def deposit(self):
        #TODO be able to increase balance parameter
        pass

    def withdraw(self):
        #TODO be able to decrease balance but not below 0
        pass

    def logout(self) -> bool:
        print('You have successfully logged out!')
        return True

    def exit(self):
        print('Bye!')
        exit()

    MENU = (
        ('Exit', exit),
        ('Balance', balance),
        ('Deposit', deposit),
        ('Withdraw', withdraw),
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
            if email != Account.email:
                print('Wrong email address')
                break

            pwd = input('Enter your Password: ')
            if pwd != Account.pwd:
                print('Wrong Password')
                sleep(2)
                break
            else:
                print('You have successfully logged in!')
                bank = list(self.accounts.values())[0]
                bank.screen()
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
