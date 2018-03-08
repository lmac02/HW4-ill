from employee import *

class teller(employee):
	def __init__(self):
		employee.__init__(self)
		
	def serveCustomer(self, other):
		print('\n\n    Hello there, {}! Hope you are doing well!\n    How can I help you today?'.format(other.first_name))
		
		done = False
		while not done:
			choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal  \n\nEnter (4) to say goodbye \n\nEntry: ')
			if choice == '1':
				other._customer__check_balance()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '2':
				other._customer__deposit()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '3':
				other._customer__withdrawal()
				y_n = input('\nIs that all for today? (yes/no): ')
				if y_n.lower() in ['no', 'n']:
					continue
				else:
					done = True
			elif choice == '4':
				done = True
			else:
				choice = input('\nEnter (1) to check balance  \n\nEnter (2) to make a deposit  \n\nEnter (3) to make a withdrawal  \n\nEnter (4) to say goodbye \n\nEntry: ')
			print('Have a nice day!')