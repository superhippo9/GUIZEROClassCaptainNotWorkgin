
"""
from guizero import *
import os
cwd = os.getcwd()


# function for writing files
def save_file():


#the app
app = App("testing")


#text box
first_name = TextBox(app, width=30, grid=[2,4])

#submit button
box = Box(app)
submitbutton = PushButton(app, command=(save_file), text="Submit")

app.display()
"""
"""
from guizero import App, TextBox, PushButton

# Create a list to store the user's input
input_list = []

def store_input():
  input_text = text_box.value
  input_list.append(input_text)
app = App()
text_box = TextBox(app)
button = PushButton(app, text="Store Input", command=store_input)
app.display()
"""

from guizero import App, Text, PushButton, Box

# Initialize variables to store candidates and their votes
candidates = []
votes = {}

# Initialize the app and create a container for the candidates
app = App(title="Class Captain Voting System")
candidate_container = Box(app, layout="grid")

# Function to add a candidate
def add_candidate():
  # Get the candidate name from the user
  name = candidate_input.value

  # Add the candidate to the list and reset the input field
  candidates.append(name)
  candidate_input.value = ""

  # Initialize the candidate's vote count to 0
  votes[name] = 0

  # Update the candidate list on the app
  update_candidates()

# Function to update the list of candidates on the app
def update_candidates():
  # Clear the candidate container
  candidate_container.clear()

  # Add a button for each candidate
  for i, candidate in enumerate(candidates):
    button = PushButton(candidate_container, text=f"{i+1}. {candidate}", command=lambda: cast_vote(candidate))
    button.width = 20

# Function to cast a vote for a candidate
def cast_vote(candidate):
  # Increment the candidate's vote count
  votes[candidate] += 1

  # Check if all votes have been cast
  if sum(votes.values()) == 30:
    # Display the results
    display_results()

# Function to display the results of the voting
def display_results():
  # Sort the candidates by their vote count in descending order
  sorted_candidates = sorted(candidates, key=lambda x: votes[x], reverse=True)

  # Check if there is a clear winner
  if votes[sorted_candidates[0]] > votes[sorted_candidates[1]]:
    # If there is a clear winner, display the winner and the vote counts
    result_text.value = f"NEW CLASS CAPTAIN: {sorted_candidates[0]} ({votes[sorted_candidates[0]]} votes)"
  else:
    # If there is no clear winner, display all candidates and their vote counts
    result_text.value = "NO OVERALL WINNER\n"
    for candidate in sorted_candidates:
      result_text.value += f"{candidate}: {votes[candidate]} votes\n"

# Create a text input field for the user to enter the candidate's name
candidate_input = Text(app, text="Enter candidate's name:")

# Create a button for the user to submit the candidate's name
add_button = PushButton(app, text="Add", command=add_candidate)

# Create a text box to display the results of the voting
result_text = Text(app, text="")

app.display()
