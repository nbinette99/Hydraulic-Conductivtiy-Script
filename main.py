
import numpy as np
import math as math


"""
Created by Noah Binette 
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
def OrginalDarcys():
	print("Final Darcy's Law equation which is K= (dt^2*L)/(dc^2*t)*LN(h_0/h) Then prints the K value")
	AllReadyAveraged = input("Do you have an Averaged Time already? Input averaged time or type no: ")
	if AllReadyAveraged == "no":
		FinalTimeAveraged = AverageTime()
		print(f"Final Averaged time is {FinalTimeAveraged}" )

	else:
		FinalTimeAveraged = AllReadyAveraged
		print(FinalTimeAveraged)

	min_to_Seconds=input("Do you want to convert your average time from mintues to seconds Y/n: ")
	if min_to_Seconds == "Y":
		FinalTimeAveraged=int(FinalTimeAveraged) * 60
		print(f"Final Averaed time is seconds is now: {FinalTimeAveraged}")
	"""
	Gathering the nessary inforamtion to do the equation, I use centemeters but it "should" work for other units as well as long as they are consitant and on value 
	i.e 10 cm or 56 inches
	"""
	LengthofMaterial= input("What is the lenghth of the material(L): ")
	InitalHead = input("what is the start value of the head (h_0): ")
	EndHead = input("What is the end value of the head reduction(h): ")
	InsideDiamterofHead = input("What is the inside diameter of the falling-head(d_t): ")
	InsideDiameterofSample = input("What is the inside diameter of the sample material(d_c): ")

	outchecker1 =['Length(L): ','Inital Head(h_0): ','End Head(h): ','Diameter of falling-head(d_t): ','Diameter of sample material(d_c): ','Averaged Time(t): ']
	outchecker2 =[LengthofMaterial,InitalHead,EndHead,InsideDiamterofHead,InsideDiameterofSample,FinalTimeAveraged]
	
	div = float(InitalHead)/ float(EndHead)
	K= (float(InsideDiamterofHead)**2*float(LengthofMaterial))/(float(InsideDiameterofSample)**2 * float(FinalTimeAveraged))*(np.log(div))
	print("************************************")
	print(f"The K value is: {round(K,6)}")
	for x, g in zip(outchecker1, outchecker2):
		print(x, g, end='\n')
	print("************************************")
	return


def ConfiedAquifer():
	print("Confied Aquifer Equation: ")
	Hydroconduct = input("What is the Hydraulic conductivity or K value: ")
	thickness = input("What is the thickness of the aquifer normally b value: ")
	slopecal = input("Is the slope already caluated Y/n: ")
	if slopecal == "Y":
		finalslope = input("what is your slope value :")
		outchecker1=['Hydraulic conductivity(k):', 'Aquifer thickenss(b): ', 'Slope of potentiometric surface(dh/dl): ']
		outchecker2=[Hydroconduct,thickness, finalslope]
	else:
		dh=input("What is the dh value: ")
		dl=input("What is the dl value: ")
		finalslope=int(dh)/int(dl)
		outchecker1=['Hydraulic conductivity(k):', 'Aquifer thickenss(b): ', 'Slope of potentiometric surface(dh/dl): ', 'dh:', 'dl:']
		outchecker2=[Hydroconduct,thickness, finalslope, dh, dl]

	q=float(Hydroconduct)*int(thickness)*int(finalslope)
	
	print("************************************")
	print(f"The q' or quanity of flow per unit width is: {round(q,6)}")
	for x, g in zip(outchecker1, outchecker2):
		print(x, g, end='\n')
	print("************************************")
	return 

def Reynoldsnum():
	print("Rynolds number equation: ")
	p=input("Input fluid density value: ")
	q=input("Input discharge velocity Value: ")
	d=input("Input diameter of the passageway of the fluid: ")
	vis=input("Input the value of viscosity: ")
	outchecker1 = ['fluid density(p):', 'discarge velocity(q):','diameter(d):', 'viscosity(vis):']
	outchecker2 = [p,q,d,vis]
	R=float(p)*float(q)*float(d)/float(vis)

	print("************************************")
	print(f"The R value or Reynolds Number is (make sure to adjust decmimal place if moved from scientific notation: {round(R,6)}")

	if R > 2000:
		print("Since the R value is above 2000 the flow is turbulent")
	else:
		print("Since the R value is under 2000 the flow is laminar")
	for x, g in zip(outchecker1, outchecker2):
		print(x, g, end='\n')
	print("***********************************")
	return 


#def DarcyRadial():


def TheisEq():
	print("first we need to compute the Transmissivity or T. This is done with T=k*b (hydro conductivity*thickness")
	yn = input("Do you already have a T value Y/n")
	if yn == "Y":
		T = input("Enter T value: ")
		# thickness=input("What is the thickness of the Aquifer(b): ")
	else:
		Hydroconduct=input("What is the hydro conductivity(K): ")
		thickness=input("What is the thickness of the Aquifer(b): ")
		T=float(Hydroconduct)*float(thickness)

	print(f"The Transmissivity value is {int(T)}")
	print("Next we need to find the value u so that we find W(u) in the chart. ")
	r=input("What is the r distance we want from the well(r): ")
	storativity=input("What is the storativity(S): ")
	t=input("What is the time(t): ")
	a=int(r)**2*float(storativity)
	b = (4*int(T)*float(t))
	print(a)
	print(b)
	u=a/b
	print(f"The u value is {float(u)}")

	W = (-np.euler_gamma) - np.log(u) + u - ((u**2)/(2*math.factorial(2))) + ((u**3)/(2*math.factorial(3))) - ((u**4)/(4*math.factorial(4))) +((u**5)/(5*math.factorial(5)))
	
	print (round(W,4))
	Q=input("What is the pumping rate/discharge (Q): ")
	a1 = 4 * math.pi * int(T)
	print(a1)
	final =(int(Q) /(4 * math.pi * int(T)))*float(W)
	print(round(final,3))
	return

def Thiem():
	print("Thiem Equation for the Confied Aquifer T Value ft^2/day" )
	Q=input("What is the total discharge(Q) ft^3/day: ")
	h1 = input("What is the head 1 value: ")	
	h2 = input("What is the head 2 value: ")
	r1 = input("What is the radius distance  1 value: ")	
	r2 = input("What is the radius distance  2 value: ")
	loged =np.log(float(r2)/float(r1))
	head = 2*math.pi*(float(h2)-float(h1))
	T= (int(Q)/head)*float(loged)
	print(f"This is the Transmissivity value: {round(T,4)} ")
	return

def Thiem_Hydro_Conductivity():
	print("Thiem Equation for the Hydro Conductivity" )
	Q=input("What is the total discharge(Q) ft^3/day: ")
	b=input("What is the thickness of the aquifer: ")
	h1 = input("What is the head 1 value: ")	
	h2 = input("What is the head 2 value: ")
	r1 = input("What is the radius distance  1 value: ")	
	r2 = input("What is the radius distance  2 value: ")

	b_1 = int(h1) - int(b) 
	b_2 = int(h2) - int(b)

	base=(b_2**2 - b_1**2)
	K=(int(Q)/math.pi*(base)) * np.log(r2/r1) 
	print(K)
	return 




"""
def ConofSoultue():
	C_o=input("Intial Solute Concentration: ")
	L=input("The flow path length: ")
	v_x=input("Average linear ground-water velocity: ")
	t=input("Time since the release of the solute: ")
	D_L=input("The longitudinal dispersion coefficent: ")

	A=math.erfc(L-(v_x*t)/2*math.sqrt(D_L*t))
	print(A)
	B=math.exp(L - (v_x*t)/D_L)
	print(B)
	C=math.erfc(L + (v_x*t)/2 * math.sqrt(D_L*t))
	print(C)

	FinalC=C_o/2(A+B*C)
	print(FinalC)
"""

def entrance():
	while True: 

		print("***Hydro Equation Calculator Script***")
		print("1 : Normal Darcy to find the K value ")
		print("2 : Equation for Steedy flow in a Confied Aquifer")
		print("3 : Reynolds number ")
		print("4 : Darcy Radial ")
		print("5 : Theis Equation ")
		print("6 : Theim Equation for a confied Aquifer finding T ")
		print("7 : Concentration of a soultue ")
		print("8 : Thiem Hydro Conductivty ")
		print("9 : EXIT")

		pickle=input("Which Hydro equation would you like to use?")


		if pickle == "1":
			OrginalDarcys()
		elif pickle == "2":
			ConfiedAquifer()
		elif pickle == "3":
			Reynoldsnum()
		elif pickle == "4":
			DarcyRadial()
		elif pickle == "5":
			TheisEq()
		elif pickle == "6":
			Thiem()
		elif pickle == "7":
			ConofSoultue()
		elif pickle == "8":
			Thiem_Hydro_Conductivity()
		elif pickle == "9":
			print("Exited Successfully kinda..")
			break


entrance()




