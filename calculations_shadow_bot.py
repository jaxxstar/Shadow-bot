# Program to calculate the thrust and Motor Torque for various values
import pandas as pd
print('Calculations for Shadow Bot\n')

print('B = mass of the bot')
print('T = Thrust of the edf (in terms of kg)')
print('M = torque obtained from the motor')
print('x = distance of application of thrust')
print('L = total length of the bot')
print('mu = friction coefficient of the floor')
print('l =  distance of the com of the bot from the rear end')
print('m0 = mass of 1 wheel')
print('r = radius of the wheel\n')

print('The governing equations are :')

print('T = W/mu for no sliding')
print('T >= W*(l/x) for no toppling\n')

cols = ['Thrust(kg)','x(m)','L(m)','mu','l(m)','m0(kg)','r(m)','min_W(kg)','max_W(kg)','M_torque']
result = pd.DataFrame(columns = cols)
counter = 0

while(1):
	T = float(input('Enter the Thrust of the motor,T in kg \t'))
	result.loc[counter,['Thrust(kg)']] = T
	x = float(input('Enter the distance of application of thrust,x \t'))
	result.loc[counter,['x(m)']] = x
	L = float(input('Enter the total length of the bot,L \t'))
	result.loc[counter,['L(m)']] = L
	mu = float(input('Enter the friction coefficient of the floor,mu \t'))
	result.loc[counter,['mu']] = mu
	l = float(input('Enter the distance of the com of the bot from the rear end,l \t'))
	result.loc[counter,['l(m)']] = l
	m0 = float(input('Enter the mass of 1 wheel,m0 \t'))
	result.loc[counter,['m0(kg)']] = m0
	r = float(input('Enter the radius of the wheel,r \t'))
	result.loc[counter,['r(m)']] = r

	W_no_sliding = T * mu
	result.loc[counter,['min_W(kg)']] = W_no_sliding
	W_no_toppling = (T * x)/l
	result.loc[counter,['max_W(kg)']] = W_no_toppling
	M = ( (mu*T)/2 - (mu*max(W_no_sliding,W_no_toppling)*9.81)/4 + (m0*max(W_no_sliding,W_no_toppling)*9.81)/(2*m0 + 							max(W_no_sliding,W_no_toppling)) )/( (m0/(r*(m0 + max(W_no_sliding,W_no_toppling)))) - mu/(2*L) )
	
	result.loc[counter,['M_torque']] = M

	print('The minimum weight of the bot is',str(1000 * max(W_no_sliding,W_no_toppling)),'g')
	print('The minimum Motor Torque required to move the bot is',str(M))
	
	
	
	option = input('Do you want to enter the values again y or n ? \t')
	if option == 'y':
		counter = counter + 1
		continue
	else:
		break
		
result.to_csv('result.csv',sep='\t')

