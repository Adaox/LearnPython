# cars equals int
cars = 100
# space_in_a_car equals float
space_in_a_car = 4.0
# drivers equals int
drivers = 30
# passengers equals int
passengers = 90
# cars_not_driven equals 100 - 30
cars_not_driven = cars - drivers
# cars_driven equals 30
cars_driven = drivers
# carpool_capacity equals 30 multiplied by 4.0
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car equals 90 divided by 30
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
