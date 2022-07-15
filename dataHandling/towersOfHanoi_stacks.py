from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("left")
middle_stack = Stack("middle")
right_stack = Stack("right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("How many disks do you want to play with?"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for num_disk in range(num_disks,0,-1):
  left_stack.push(num_disk)

num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in {opm} moves.".format(opm=num_optimal_moves))

#Get User Input
def get_input():
  choices = {}
  while True:
    for i, stack in enumerate(stacks):
      name = stack.get_name()
      letter = name[0]
      choices[letter] = i
      print("Enter {l} for {n}".format(n=name,l=letter))
    user_input = input("")
    if user_input in choices:
      return stacks[choices[user_input]]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  _ = [stack.print_items() for stack in stacks]
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {num} moves, and the optimal number of moves is {opm}".format(num=num_user_moves, opm=num_optimal_moves))