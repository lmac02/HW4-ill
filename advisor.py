from employee import employee

class advisor(employee):

	def __init__(self):
		employee.__init__(self)
		self.advisor_permissions = True

	def __offer_loan(self, other):
		done1 = False
		amount = input("\n    You've chosen a great lender in I.L.L & Sons. How much would you like to borrow? The least amount you can borrow is $50\n\nAmount: ")

		while not done1:
			try:
				amount = float(amount)
				if amount >= 50:
					done1 = True
				else:
					amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')
			except:
				amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')


		period = input('\n    Over how long would you like to pay back the loan?\n    We can offer 1-year, 5-year, or 25-year loans.\n\nNumber of years: ')
		while not period.isnumeric() or period not in ['1', '5', '25']:
			period = input('\nWe can offer 1-year, 5-year, or 25-year loans only.\n\nWhich best suits you?\nNumber of years: ')
		period = int(period)

		interest_rate = 4 + r.randint(10, 70)/100

		accept = input('\n\n{}, we can offer you a {}-year loan of ${} at an interest rate of {}%. Would you like to accept this loan? (yes/no):  '.format(other.first_name, period, format(amount, '.2f'), interest_rate))
		if accept.lower() in ['yes', 'y']:
			other.balance += amount
			other.outstanding_balance += float(str(format((((1 + interest_rate / 100) ** period) * amount) - amount, '.2f')))
			other.check_outstanding_balance()
			print('\n    Each year you will owe {} / {} = ${} on this loan'.format(format(other.outstanding_balance, '.2f'), period, format(other.outstanding_balance/period), '.2f'))
		else:
			print('\n    Okay. If you reconsider, please come back and we can talk again.')

	def __open_investment_account(self, other):
		print('Have not yet enabled this function.')

	def give_advice(self, other):
		print('\n    Hello, {}. I am your advisor {} {}'.format(other.first_name, self.first_name, self.last_name))
		entry = input('\n\n     I am here to advise you on your financial options and goals. What would you like to discuss today?\n\nEnter (1) to discuss a loan.\nEnter (2) to open an investment account.\n\nEntry: ')

		done = False
		while not done:
			if entry == '1':
				self.__offer_loan(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				if y_n.lower() in ['yes', 'y']:
					done = True
				elif y_n.lower() in ['no', 'n']:
					open_invstmnt_acct = input('\n    Okay, so you would like to open an investment account then? (yes/no): ')
					if open_invstmnt_acct.lower() in ['yes', 'y']:
						self.__open_investment_account
						done = True
					else:
						print('\n    Nice seeing you today, {}.'.format(other.first_name))
						done = True
				
			elif entry == '2':
				self.__open_investment_account(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				if y_n.lower() in ['yes', 'y']:
					done = True
				elif y_n.lower() in ['no', 'n']:
					discuss_loan = input('\n    Okay, so you would like to discuss a loan then? (yes/no): ')
					if discuss_loan.lower() in ['yes', 'y']:
						self.__offer_loan(other)
						done = True
					else:
						print('\n    Nice seeing you today, {}.'.format(other.first_name))
						done = True
				
			else:
				entry = input('\nEnter(1) to discuss a loan.\nEnter (2) to open an investment account.\nEnter (3) to exit.\n\nEntry: ')
				if entry == '3':
					done = True
