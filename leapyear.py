# Criteria: Divisible by 4, except end of century, unless the end of century year
from rich.prompt import IntPrompt
from rich.console import Console
console = Console()
def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else: 
        return False
def bool_to_text(boolean):
    if boolean == True:
        return "[green bold]is"
    elif boolean == False:
        return "[red bold]isn't"
    else:
        raise TypeError
year = IntPrompt.ask("[blue bold]Enter a year")
console.print(f"[white]The year {year} {bool_to_text(is_leap_year(year))} a leap year")


