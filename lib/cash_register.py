#!/usr/bin/env python3

class CashRegister: 

  def __init__(self, discount=0, total=0, previous_transactions=None):
    self.discount = discount
    self.total = total
    self.items = []

    if previous_transactions is None:
        self.previous_transactions = []
    else:
        self.previous_transactions = previous_transactions

  def add_item(self, item, price, quantity=1):
      amount = price * quantity
      self.total += amount
      self.previous_transactions.append(amount)

      if isinstance(item, list):
        self.items.extend(item * quantity)
      else:
        self.items.extend([item] * quantity)


  def void_last_transaction(self):
      if self.previous_transactions:
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction

      return self.total
  
  def apply_discount(self):
    if self.discount:
      self.total = self.total * (1 - self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

    else:
      print("There is no discount to apply.")
      return self.total


