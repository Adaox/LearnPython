# prints string
print("Mary had a little lamb.")
# prints formatted string
print("Its fleece was white as {}.".format("snow"))
# prints string
print("And everywhere that Mary went.")
# prints . 10 times via string replication
print("." * 10)  # what did that do?

# set variables to strings
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# end = /n is the default keyword argument for the print function
# removing it, has it fall back to it's default setting
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)
