"""
You also want to invite a bear to the party. To make sure the bear
receives the invitation, you decide to hand it over personally.

Adjust the function definition of visit_woods() to accept a string as
an argument:

Then, update the function call of visit_woods() so the program
prints the value of my_invitation.
"""

def visit_woods(my_invitation):
    """🐻"""
    if "my_invitation" in locals():
        print(my_invitation)

invitation = "Let's have a party!"
visit_woods(invitation)