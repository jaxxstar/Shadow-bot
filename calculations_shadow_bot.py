# Program to calculate the thrust and Motor Torque for various values
import pandas as pd
print('Calculations for Shadow Bot\n')

print('B = mass of the bot')
print('T = Thrust of the edf (in terms of kg)')
print('M = torque obtained from the motor')
print('x = distance of application of thrust')
print('L = total length of the bot')
print('mu = friction coefficient of the floor')
print('c =  clearance between the wall and the bot')
print('m0 = mass of 1 wheel')
print('r = radius of the wheel\n')

print('The governing equations are :')

print('It is independent of distance of com from the rear end')

print('T = W/mu for no sliding')
print('M >= B*g*R/2 B is the mass of bot')
print('T >= W*(c/x) for no toppling while stationary\n')
print('T >= W*(c/x) - M/x for no toppling while moving\n')

cols = ['Thrust(kg)','x(m)','L(m)','mu','c(m)','m0(kg)','r(m)','W_no_sliding_stationary_min(kg)','W_no_toppling_stationary_max(kg)','Motor_min(kg*m)','Motor_max(kg*m)','stationary_running_match','f<=mu*N']
result = pd.DataFrame(columns = cols)
counter = 0

while(1):

	T = float(input('Enter the Thrust of the EDF,T in kg \t'))
	result.loc[counter,['Thrust(kg)']] = T
	x = float(input('Enter the distance of application of thrust,x \t'))
	result.loc[counter,['x(m)']] = x
	L = float(input('Enter the total length of the bot,L \t'))
	result.loc[counter,['L(m)']] = L
	mu = float(input('Enter the friction coefficient of the floor,mu \t'))
	result.loc[counter,['mu']] = mu
	c = float(input('Enter the clearance between the wall and bot,c \t'))
	result.loc[counter,['c(m)']] = c
	m0 = float(input('Enter the mass of 1 wheel,m0 \t'))
	result.loc[counter,['m0(kg)']] = m0
	r = float(input('Enter the radius of the wheel,r \t'))
	result.loc[counter,['r(m)']] = r

	W_no_sliding = T * mu
	result.loc[counter,['W_no_sliding_stationary_min(kg)']] = W_no_sliding
	W_no_toppling = (T * x)/c
	result.loc[counter,['W_no_toppling_stationary_max(kg)']] = W_no_toppling
	
	Motor_min = (W_no_sliding * 9.81 * r)/2
	MOtor_max = (W_no_toppling * 9.81 * r)/2
	
	Motor_min = ( (mu*T)/2 - (mu*min(W_no_sliding,W_no_toppling)*9.81)/4 + (m0*min(W_no_sliding,W_no_toppling)*9.81)/(2*m0 + 							min(W_no_sliding,W_no_toppling)) )/( (m0/(r*(m0 + min(W_no_sliding,W_no_toppling)))) - mu/(2*L) )
	
	result.loc[counter,['Motor_min(kg*m)']] = Motor_min
	
	Motor_max = ( (mu*T)/2 - (mu*max(W_no_sliding,W_no_toppling)*9.81)/4 + (m0*max(W_no_sliding,W_no_toppling)*9.81)/(2*m0 + 							max(W_no_sliding,W_no_toppling)) )/( (m0/(r*(m0 + max(W_no_sliding,W_no_toppling)))) - mu/(2*L) )
	
	result.loc[counter,['Motor_max(kg*m)']] = Motor_max
	
	if((T - W_no_sliding * c/x + Motor_min/x) > 0 and (T - W_no_toppling * c/x + Motor_max/x) > 0 ):
		result.loc[counter,['stationary_running_match']] = 'Yes'
	else:
		result.loc[counter,['stationary_running_match']] = 'No'	
	B = min(W_no_sliding,W_no_toppling)
	g = 9.81
	if(Motor_min >= (mu*T/2 - mu*B*g/4 + m0*B*g/(B+2*m0) )/(m0/(r*(m0 + B)) - mu/(2*L))):
		result.loc[counter,['f<=mu*N']] = 'Yes'
	else:
		result.loc[counter,['f<=mu*N']] = 'No'
	
	option = input('Do you want to enter the values again y or n ? \t')
	if option == 'y':
		counter = counter + 1
		continue
	else:
		break
		
result.to_csv('result.csv',sep = ',',encoding = 'UTF-8' )

