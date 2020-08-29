from game import Pet

p1 = Pet("Kitty")
print(p1)

# let some time to pass
for i in range(5):
    p1.clock_tick()

print(p1)       # the pet is now in this state

# lets feed the pet
p1.feed()
print("After feeding " + str(p1))

# lets teach the pet some new words
p1.teach("Boo")
print("After learning new word " + str(p1))

# lets talk to the pet
p1.Hi()
