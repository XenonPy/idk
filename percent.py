# I need extra credit on this so I am going to procedurally generate the data with random and then perform the challenge. Rich for looking good, time for benchmarks
import random
import json
import time
from rich.prompt import IntPrompt
from rich.console import Console
console = Console()
import os

seeds = [1, 2, 3, 4, 5] # seed 1: 20-50 seed 2: 50-65 seed 3: 65-80 seed 4: 80-100. seed 5: 0-30 Seeds assert academic competence 

benchmark_level = int(IntPrompt.ask("Please enter the number of students to benchmark", default="10")) # You can benchmark the script by choosing a custom or preset benchmark level
gradebook = {

}

start = time.time()

for i in range(1, benchmark_level + 1):
    gradebook.update({str(i): {}})

def generate_dataset(): # ngl snake case is kind of ugly
    for student in range(1,benchmark_level + 1):
        seed = random.choice(seeds)
        for grades in range (1, 6):
            if seed == 1:
                grade = random.randint(20, 50)
            elif seed == 2:
                grade = random.randint(50, 65)
            elif seed == 3:
                grade = random.randint(65, 80)
            elif seed == 4:
                grade = random.randint(80, 100)
            elif seed == 5:
                grade = random.randint(0, 30)
            else:
                print("ERROR! Determining grade using seed")
                exit()
            gradebook[f"{student}"][str(grades)] = grade # Here, we are setting each student a random grade that we previously determined using their random seed.

generate_dataset() # calling function to populate our gradebook dict

average_grades = {

}
# Now we determine the averages by using basic math
total_avg = 0
total_div = 0
for student in gradebook: # var name should be ok because of local function scope right?
    avg = 0
    for grade in gradebook[student]:
        avg = avg + int(gradebook[student][grade]) # avg += grade?
        total_avg += int(gradebook[student][grade])
        total_div += 1
    average_grades[student] = avg / 5

end = time.time()

console.print(average_grades)
os.system("clear")
filen = 0
def writejson():
    with open(f"gradebook{filen}.json", "x") as book:
        book.write(json.dumps(gradebook))
while True:
    try:
        writejson()
        break
    except FileExistsError:
        filen += 1
        continue
    

console.print(f"\nSummary | Time to run: {end-start} | Overall average grade: {total_avg / total_div}\n")
console.print(f"\nBenchmarked Data: [red bold]gradebook{filen}.json\n")
