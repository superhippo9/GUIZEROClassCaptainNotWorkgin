from guizero import PushButton, App
# Create the guizero app
app = App(title="Class Captain Voting")

# Create a list of candidate names
candidates = ["Alice", "Bob", "Charlie", "David"]

# Create a variable to store the winning candidate
winner = None

# Create a function to cast a vote for a given candidate
def cast_vote(candidate):
    global winner
    winner = candidate
    app.info("Vote Cast", "You have successfully voted for " + candidate)

# Create a guizero grid to lay out the buttons
grid = App(app, layout="auto", align="top")

# Create a button for each candidate
for candidate in candidates:
    button = guizero.PushButton(grid, text=candidate, command=cast_vote, args=[candidate])

# Create a button to see the results
results_button = guizero.PushButton(app, text="See Results", command=show_results)

# Create a function to show the results
def show_results():
    app.clear()
    guizero.Text(app, text="The winner is: " + winner, align="top")
    app.yesno("Continue?", "Do you want to continue voting?")

# Start the app
app.display()
