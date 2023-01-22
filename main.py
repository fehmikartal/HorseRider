from time import sleep
from playsound import playsound

q = 0

questions = int(input('How many question will you solve?: '))
total_time = int(input('In how many minutes?: '))*60
time_per_q = total_time/questions
print('Time per Question: ' + str(time_per_q))

while q<questions:    
    sleep(time_per_q)
    q += 1
    print(f"Question #{q}")
    print(f"Time: {round((q*time_per_q)/60,1)} Minutes")

print("IT'S DONE!")
playsound('clock.mp3')