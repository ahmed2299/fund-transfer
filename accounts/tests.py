# accounts/tests.py

from django.test import TestCase
from .models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        # Create two accounts
        self.account1 = Account.objects.create(account_number="123456", account_name="Test Account 1", balance=1000)
        self.account2 = Account.objects.create(account_number="789012", account_name="Test Account 2", balance=2000)

    def test_account1_balance(self):
        account = Account.objects.get(account_number="123456")
        self.assertEqual(account.balance, 1000)


    def test_account2_balance(self):
        account = Account.objects.get(account_number="789012")
        self.assertEqual(account.balance, 2000)


    def test_transfer_funds(self):
        # Transfer 500 from account1 to account2
        self.account1.balance -= 500
        self.account2.balance += 500
        self.account1.save()
        self.account2.save()

        # Retrieve accounts again to check balances
        account1 = Account.objects.get(account_number="123456")
        account2 = Account.objects.get(account_number="789012")

        self.assertEqual(account1.balance, 500)
        self.assertEqual(account2.balance, 2500)
