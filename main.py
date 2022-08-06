from time import *
import random as r


def counting_mistakes(test_sentence,answer):
    error = 0
    for i in range(len(test_sentence)):
        try:
            if test_sentence[i]!=answer[i]:
                error+=1
        except :
            error+=1
    return error



def speed_time(start_time,end_time,user_input):
    time_taken = end_time - start_time
    time_roundoff = round(time_taken,2)
    speed = len(user_input)/time_roundoff
    a = round(speed,2)
    return a




test = ["Veermata Jijabai Technological Institute is a state funded college located in Mumbai, Maharashtra, India, and one of the oldest engineering colleges in Asia.",
        " Founded in 1887 and formerly known as the Victoria Jubilee Technical Institute.VJTI is also the Central Technical Institute of Maharashtra State.",
        "The institute trains students in engineering and technology at the certificate,[3] diploma, degree, post-graduate and doctoral levels."]


test1 = r.choice(test)
print("*** WELCOME TO PRUTHVIRAJ'S TYPING SPEED COMPETITION ***")
(input("Candidate's Name: "))
print("Test_sentence : \n",test1)
print()
print()
time_1 = time()
input_from_candidate = input("Enter your answer: ")
time_2 = time()



print("Speed: ",speed_time(time_1,time_2,input_from_candidate),"w/s")
print("Error: ",counting_mistakes(test1,input_from_candidate))


print("Thanks for participation")





