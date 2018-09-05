import numpy as np
import matplotlib.pyplot as plt


def calculate_pi(n):
	
	x_and_y = np.random.rand(n,2)
	print("This is the array of x and y values \n",x_and_y)
	
	x=x_and_y[:,0]
	y=x_and_y[:,1]
	#np.x_and_y.shape

	r= (x_and_y[:,0]**2 + x_and_y[:,1]**2)**0.5
	

	print("This is the array of r values \n", r)


	r_gt =sum(float(gt) >= 1 for gt in r)

	r_lt=sum(float(lt) <= 1 for lt in r)
	print(r_gt,r_lt)

	pi=4*(r_lt/(r_gt+r_lt))
	print(pi)
	
	fig=plt.figure()
	plt.scatter(x[r<1],y[r<1],color='red')
	plt.scatter(x[r>=1],y[r>=1],color='blue')


	plt.show()

