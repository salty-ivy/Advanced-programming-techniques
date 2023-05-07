# one builder that builds and one director that directs the building process
# used to create a complext objects, which are created in steps

from enum import Enum
import  time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')

