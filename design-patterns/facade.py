"""
The façade design pattern helps us to hide the internal complexity of our systems and expose only what is necessary to the client through a simplified interface.
In essence, façade is an abstraction layer implemented over an existing complex system.

Façade is also useful if you have more than one layer in your system. You can introduce one façade entry point per layer, and let all layers communicate with each other through their façades. That promotes loose coupling and keeps the layers as independent as possible.
"""

from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')

class Server(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self):
		pass

	def __str__(self):
		return self.name

	@abstractmethod
	def boot(self):
		pass

	@abstractmethod
	def kill(self, restart=True):
		pass


class FileServer(Server):
	def __init__(self):
	   '''actions required for initializing the file server'''
	   self.name = 'FileServer'
	   self.state = State.new
	def boot(self):
	   print(f'booting the {self}')
	   '''actions required for booting the file server'''
	   self.state = State.running
	def kill(self, restart=True):
	   print(f'Killing {self}')
	   '''actions required for killing the file server'''
	   self.state = State.restart if restart else State.zombie
	def create_file(self, user, name, permissions):
	   '''check validity of permissions, user rights, etc.'''
	   print(f"trying to create the file '{name}' for user '{user}' with permissions {permissions}")

class ProcessServer(Server):
	def __init__(self):
	   '''actions required for initializing the process server'''
	   self.name = 'ProcessServer'
	   self.state = State.new
	def boot(self):
	   print(f'booting the {self}')
	   '''actions required for booting the process server'''
	   self.state = State.running

	def kill(self, restart=True):
           print(f'Killing {self}')
           '''actions required for killing the process server'''
           self.state = State.restart if restart else State.zombie
       def create_process(self, user, name):
           '''check user rights, generate PID, etc.'''
           print(f"trying to create the process '{name}' for user '{user}'")



class OperatingSystem:
	'''The Facade'''
	def __init__(self):
	   self.fs = FileServer()
	   self.ps = ProcessServer()
	def start(self):
	   [i.boot() for i in (self.fs, self.ps)]
	def create_file(self, user, name, permissions):
	   return self.fs.create_file(user, name, permissions)
	def create_process(self, user, name):
	   return self.ps.create_process(user, name)




