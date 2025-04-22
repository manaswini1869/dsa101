# Create a game where the computer tries to guess the name of the person you are thinking of.

# The computer asks a series of yes or no questions to determine the person. The computer only gets a single guess about the identity.

# If the guess is correct, the game ends.

# If the guess is incorrect, the computer asks the player who they were thinking of and asks to input a
# new yes or no question to distinguish between the person it guessed and the person you where thinking of. Include the new question and person in future playthroughs.

# --------------------------------------------------------------------------------------

# Example 1: Computer guesses correctly
# New Game!
# Is the person a movie star?
# > N
# Is the person a famous athlete?
# > Y
# Is the person LeBron James?
# > Y
# I guessed it!
# Would you like to play again?
# > N

# Example 2: Computer does not guess correctly
# New Game!
# Is the person a movie star?
# > N
# Is the person a famous athlete?
# > Y
# Is the person LeBron James?
# > N
# I give up! Who is it?
# > Lionel Messi
# What is a question I can use to distinguish between Lionel Messi and LeBron James
# > Is the person a soccer (football) player?
# And what is the answer if the person is Lionel Messi?
# > Y
# Thank You!
# Would you like to play again?
# > Y

# New Game!
# Is the person a movie star?
# > N
# Is the person a famous athlete?
# > Y
# Is the person a soccer (football) player?
# > Y
# Is the person Lionel Messi?
# > Y
# I guessed it!
# Would you like to play again?



# from collections import defaultdict

# class Node:
#     def __init__(self):
#         self.category = defaultdict(list)


## I removed category and the game will be played as along as the user says Y
# instead of category, I added a new boolean to the treenode
# the boolean will keep track of as new categories come up


class TreeNode:
    def __init__(self, value, is_question=False):
        self.value = value # this will keep trck of the value
        self.is_question = is_question # new question for the answer
        self.yes = None
        self.no = None


# this function for yes or no, if no it will create a new question and yes than the program will give an answer
def ask_yes_no(question):
    while True:
        answer = input(f"{question}\n> ").strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("Please enter Y or N.")

# Since the I changed the category and the data structure, these helper functions are not that useful

# def give_up():
#     # add new category and person
#     return

# def new_node():




def play_game(root):
    current = root
    parent = None
    last_answer = None

    while current.is_question:
        parent = current
        if ask_yes_no(current.value):
            current = current.yes
            last_answer = 'yes'
        else:
            current = current.no
            last_answer = 'no'

    if ask_yes_no(f"Is the person {current.value}?"):
        print("I guessed it!")
        return root
    else:
        print("I give up! Who is it?")
        new_person = input("> ").strip()
        print(f"What is a question I can use to distinguish between {new_person} and {current.value}?")
        new_question = input("> ").strip()
        if ask_yes_no(f"And what is the answer if the person is {new_person}?"):
            # here is where the new node will accept the new question and answer for that question
            new_node = TreeNode(new_question, is_question=True)
            new_node.yes = TreeNode(new_person)
            new_node.no = current
        else:
            new_node = TreeNode(new_question, is_question=True) # creating the new treeNode
            new_node.yes = current
            new_node.no = TreeNode(new_person)

        if parent is None:
            root = new_node
        else:
            if last_answer == 'yes':
                parent.yes = new_node
            else:
                parent.no = new_node

        print("Thank you!")
        return root

if __name__ == "__main__":
    print("Welcome to the Guessing Game!") # the initial question
    root = TreeNode("Is the person a movie star?", is_question=True)
    root.yes = TreeNode("Tom Cruise") # initial values
    root.no = TreeNode("LeBron James") # initial values

    # inifinite while loop until user says no
    while True:
        print("\nNew Game!")
        root = play_game(root)
        if not ask_yes_no("Would you like to play again?"):
            break

    print("Thanks for playing!")
