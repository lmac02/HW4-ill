from employee import *

class manager(employee):

	def __init__(self):
		employee.__init__(self)
		self.manager_permissions = True

	def show_customer_info(self, other):
		print('Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nSocial Security Number: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, other._person__ssn, str(other.account_number).zfill(12), other.routing_number, other.balance))

	def see_customers(self):
		for customer in person.customer_list:
			print('\nName: {}      Acct #: {}'.format(customer.name, str(customer.account_number).zfill(12)))

	def delete_customer(self, other):
		done = False
		while not done:
			y_n = input('\nDelete {}? (yes/no): '.format(other.name))
			if y_n.lower() in ['yes', 'y']:
				print('Deleting...')
				person.past_customer_list.append(person.customer_list.pop(other.customer_number))
				done = True
			elif y_n.lower() in ['no', 'n']:
				print('\nNot deleted.')
				done = True