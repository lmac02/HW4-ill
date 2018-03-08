from employee import *
import random as r

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
			print('\n    Each year you will owe {} / {} = ${} on this loan'.format(format(other.outstanding_balance, '.2f'), period, format(other.outstanding_balance/period, '.2f')))
		else:
			print('\n    Okay. If you reconsider, please come back and we can talk again.')

	def __open_investment_account(self, other):
		
		if other.balance < 1000:
			print('\n    To open an investment account, you must have at least $1,000 in your account.')
			print('\n\n    Right now, it looks like you don\'t have enough to open an investment account with us. Once you accumulate more funds, please come back and we will talk more about your investment options.')
		else:
			print('\n    Okay, {}, so you would like to invest. Good idea in today\'s world. Right now, we have three investment options for you to consider. Our mutual fund is doing great these days. It is the safest investment for you to make.\nOr I could get you in on our precious metal & gem fund. Yeah, it is a little riskier, but the potential reward is even greater.\n\nYou ever heard of bitcoin? What about XRP\'s Ripple? Well if you are into cryptocurrencies, we can help you invest in those, too.\n\nThe choice is yours, {}.'.format(other.first_name, other.first_name))
			choice = input('\n\nEnter (1) to invest in our mutual fund.\nEnter (2) to invest in our precious metal & gem fund.\nEnter (3) to invest in our special blend of cryptocurrencies.\nEnter (4) if you don\'t want to invest with us anymore.\n\nEntry: ')
			while choice not in ['1', '2', '3', '4']:
				choice = input('\n(1) Mutual Fund\n\n(2)Precious metal & gem\n\n(3)Cryptocurrencies\n\n(4)Nevermind\n\nEntry: ')
			
			if choice == '1':
				print('\n    Great choice.')
			elif choice == '2':
				print('\n    You won\'t regret this.')
			elif choice == '3':
				print('\n    Rolling the dice, huh? Hopefully it pays off.')
			elif choice == '4':
				print('\n    Okay, {}. Well, feel free to come back if you change your mind.'.format(other.first_name))

			if choice != '4':
				amount = input('\n\n    How much would you like to add to your investment account right now?\n    You must deposit at least $500.\n\nDeposit: $ ')
			
			done = False

			if choice == '4':
				done = True

			while not done:
				try:
					amount = float(amount)
					if amount >= 500:
						done = True
					else:
						amount = input('\nDeposit must be at least $500.\n\nDeposit: $')
				except:
					amount = input('\nEnter a valid amount over $500 to invest.\n\nDeposit: $')

			if choice == '1':
				return_rate = r.normalvariate(1.06, 0.025)
				other.investment_acct_balance += amount

			elif choice == '2':
				return_rate = r.normalvariate(1.08, 0.04)
				other.investment_acct_balance += amount

			elif choice == '3':
				return_rate = r.normalvariate(1.14, 0.09)
				other.investment_acct_balance += amount

			elif choice == '4':
				print('\n\n    Goodbye!')

######Finish this fcn########################
############################################################



	def GiveAdvice(self, other):
		print('\n    Hello, {}. I am your advisor {} {}.'.format(other.first_name, self.first_name, self.last_name))
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
						self.__open_investment_account(other)
						done = True
					else:
						print('\n    Nice seeing you today, {}.'.format(other.first_name))
						done = True
				else:
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

