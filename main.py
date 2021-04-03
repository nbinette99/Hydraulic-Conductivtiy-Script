import numpy as np

"""
Fun AverageTime will allow the user to input x amounts of times from there runs in seconds and give the average time 
which is then passed as back to finish the calculation. 
"""
def AverageTime():
	InputedTimes=[]
	numTimes = 2
	FirstTime=input("Input time 1 run in seconds: ")
	print("The first run time is: " + FirstTime)

	InputedTimes.append(float(FirstTime))
	MultipleRuns=input("Is there another time Y/n: ")
	

	while MultipleRuns == "Y":
		intimerun =f'{numTimes} time'
		intimerun=input(f'Input time {numTimes} run in seconds: ')
		InputedTimes.append(float(intimerun))
		numTimes= numTimes + 1
		MultipleRuns=input("Is there another time Y/n: ")
	
	
	adder = 0

	for i in range(0, len(InputedTimes)):
		adder = adder + InputedTimes[i]

	return adder/len(InputedTimes)



"""
This is simply a time saving addition so that if a user already has the time averaged they can enter it and move on to the rest of the entry and solution
"""
AllReadyAveraged = input("Do you have an Averaged Time already? Input averaged time or type no: ")
if AllReadyAveraged == "no":
	FinalTimeAveraged = AverageTime()
	print(f"Final Averaged time is {FinalTimeAveraged}" )

else:
	FinalTimeAveraged = AllReadyAveraged
	print(FinalTimeAveraged)

"""
Gathering the nessary inforamtion to do the equation, I use centemeters but it "should" work for other units as well as long as they are consitant and on value 
i.e 10 cm or 56 inches
"""
LengthofMaterial= input("What is the lenghth of the material(L): ")
InitalHead = input("what is the start value of the head (h_0): ")
EndHead = input("What is the end value of the head reduction(h): ")
InsideDiamterofHead = input("What is the inside diameter of the falling-head(d_t): ")
InsideDiameterofSample = input("What is the inside diameter of the sample material(d_c): ")


"""
Final Darcy's Law equation which is K= (dt^2*L)/(dc^2*t)*LN(h_0/h) 
Then prints the K value
"""
div = float(InitalHead)/ float(EndHead)
K= (float(InsideDiamterofHead)**2*float(LengthofMaterial))/(float(InsideDiameterofSample)**2 * float(FinalTimeAveraged))*(np.log(div))
print(f"The K value is: {round(K,6)}")

