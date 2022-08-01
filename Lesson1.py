from math import pi
from re import T
from subprocess import DETACHED_PROCESS
#Ex1
print("what do you call a bear with no teeth?")
print("A gummy bear")
#ex2
print((9.5*4.5*2.5*3)/45.5-3.5)
#Ex3
radius=5
perimeter=2*radius*pi
area=radius*radius*pi
print(perimeter)
print(area)
#ex4
d=14*1.6
t=(45/60)+(30/3600)
v=d/t 
print("The average speed is :",v)
#ex5
#set variable
sec=3600
H=24
D=365
birth= 6
death=15 
immigrate=45 
#compute a day 
Sec_y=sec*H*D 
Birth=Sec_y/birth
Dead=Sec_y/death
Im=Sec_y/immigrate
population =( (Birth+Im)-Dead) + 312032486
print("Total population in US:",population)
# #exer6
# name=input("Enter your first name:")
# print("Hello:",name)
# #exer7
# L_name=input("Enter last name:")
# F_name=input("Enter first name :")
# print("Hello:",L_name,F_name)
# #exer8
# num1=int(input("num1:"))
# num2=int(input("num2:"))
# print("The total is :",num1 ,num2)
#Exer9 
# Kg=2.204
# W=float(input("Enter weight:"))
# total=(Kg*W)

# print("The total is:",total)
#exer10
from math import pi 
radius=2
lenght=6
area=radius * radius * pi
volume=area*lenght
print(area,volume)
# Exer11
# M=input("enter amount of water in kilograms:")
# user1=input("Enter the final temerpatire of the water:")
# final_Tem=("Enter the amount of water:")
# Q=M*(final_Tem-user1)*4184
# print(Q)

