from rich.console import Console
from rich.prompt import IntPrompt
console = Console() # defining the Rich console object
def get_is_weird(n):
    n = abs(n)
    if n % 2 != 0:
        return True
    elif n >= 2 and n <= 5: # don't need to check even/odd here because that's handled by the first clause
        return False
    elif n >= 6 and n <= 20: 
        return True
    elif n > 20:
        return False
    else:
        raise Exception("Something went wrong")
def bool_to_text(boolean): # parts of function reused from leapyear.py
    if boolean == True: 
        return "[blue bold]weird"
    elif boolean == False:
        return "[red bold]not weird"
    else:
        raise TypeError 
    # basically returns specific gramatical format for True and False, and raises a type error if the input isn't true or false
n = IntPrompt.ask("[blue bold]Please enter an integer")
console.print(f"The number {n} is {bool_to_text(get_is_weird(int(n)))}")


    