from rich.console import Console
from rich.prompt import Prompt

def captitalize_firsts(s):
    sl = s.split()  # returns something like ["hello", "world"]
    for i in range(len(sl)):
        sl[i] = sl[i].capitalize()  # update the list with the capitalized word
    return ' '.join(sl)

console = Console()  # defining the Rich console object
s = Prompt.ask("[blue bold]Please enter a string")
console.print(f"[bold]The string [green]{s}[white] is [green]{captitalize_firsts(s)}")



    