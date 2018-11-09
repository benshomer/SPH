"""
This class performs a single Wigner function on a given set of
arrays. An array of horizontal and an array of vertical values
of angles.  The angles are being given in degrees.
The class is initiated on each call of the process.
It returns a 2D matrix of sum values of all the selected calculations.
"""
import numpy as np
from   math       import *
from   lmfit      import Minimizer, Parameters, report_fit

MAX_L = 4 # Maximal rank for analysis.

a0 = sqrt(2.0)
a1 = sqrt(3.0 / 2.0)
a2 = sqrt(5.0 / 8.0)
a3 = sqrt(35.0/32.0)


class wigner:
    """
       Implement Wigner functions for a matrix of phi/theta angles.
       ar_phi and ar_theta are numpy 1D arrays of angles
       The class will run on all ranks with selected order Wigner functions.
       
       K is a dictionary of all possible ranks.
              Each entry holds a list of int - user selected orders per given L
       coef - Dictionary of all possible ranks.
              Each entry holds a list of relevant coefficients.
              MUST be in the proper size for the selected list of orders!
    """
	
    def __init__(self, theta, phi, K, coef, target):
	self.K           = K
	self.init_coef   = coef
	self.matrixShape = target.shape

	print "WIGNER INITIALIZED WITH Theta: %s Phi: %s"%(theta.size, phi.size)


	# Create a 2D array of theta values (same X value in columns)
	tlst = []
	for i in theta:
	    tlst.append(np.full((theta.size),i))	    
	self.theta_ar = np.array(tlst).T # T method for transposed
	# Flatten for minimization operations
	self.theta_ar = self.theta_ar.flatten()
	del tlst

	# Create a 2D array of phi values (same Y value in rows)
	tlst = []
	for i in phi:
	    tlst.append(np.full((phi.size),i))	    
	self.phi_ar = np.array(tlst)
	# Flatten for minimization operations
	self.phi_ar = self.phi_ar.flatten()

	self.target = target.flatten()



    def mkParams(self):
	"""
	   Declare a lmfit Parameters object for the minimizer
	"""
	self.params = Parameters()
        for L in range(1,MAX_L+1):
            K     = self.K[L]
            icoef = self.init_coef[L]
            for idx in range(len(icoef)):
                if K[idx] < 0:
                    pname = "coef_%s_m%s"%(L, abs(K[idx]))
                else:
                    pname = "coef_%s_p%s"%(L, K[idx])
                #pval  = self.init_coef[idx]
		pval  = icoef[idx]
                self.params.add(pname, value=pval, min=-30.0, max=30.0)


    def optimizeFn(self, params):
	"""
	   This is the method which actually runs the optimization
	   (least square analysis).
	   params is actually self.params, but is given as an argument
	   rather than passed as self because the method must have
	   a specific signature.
	"""
	self.coef = {}
        for L in range(1,MAX_L+1):
	    self.coef[L] = []
            for K in self.K[L]:
                if K < 0:
                    sig = "m"
                else:
                    sig = "p"
                self.coef[L].append(params["coef_%s_%s%s"%(L,sig,abs(K))])

	# Call the apropriate method for a given L
	funcdir = {1:self.mkDegree1,
		   2:self.mkDegree2,
		   3:self.mkDegree3,
		   4:self.mkDegree4}
        model = []
        for L in range(1,MAX_L+1):
            model.append(funcdir[L]())
	return  sum(model) - self.target

    def runOptimization(self):
	"""
	   Initialize the Minimizer and run the analysis
	   of Least Square
	"""
	self.mkParams()
	ls_minimizer = Minimizer(self.optimizeFn, self.params)
	result       = ls_minimizer.minimize()
	trajectory   = (self.target + result.residual).reshape(self.matrixShape)

        # Check that there are no negative values in the
        # trajectory results. If there are, raise all results
        # in the delta
        rmin         = trajectory.min()
        if rmin < 0:
            trajectory += abs(rmin)

        self.stats   = report_fit(result)
        self.result  = result

	return trajectory

	
    def mkDegree1(self):
	""" Calculate 1st degree on matrices
	    Loop through selected orders
	"""
	results = []
        L       = 1
        KL      = self.K[L]
	if 1 in KL or -1 in KL:
	    st = np.sin(self.theta_ar)
	for i in range(len(KL)):
	    K    = KL[i]
	    coef = self.coef[L][i]
	    if   K == 0:
		T10 = np.cos(self.theta_ar)
		u10 = T10 * coef
		results.append(u10)
	    elif K == 1:
		T1p1 = a0 * st * np.sin(self.phi_ar) * -1.0
		u1p1 = T1p1 * coef
		results.append(u1p1)
	    elif K == -1:
		T1m1 = a0 * st * np.cos(self.phi_ar)
		u1m1 = T1m1 * coef
		results.append(u1m1)
	return sum(results)

    def mkDegree2(self):
	""" Calculate 2nd degree on matrices """
	results = []
        L       = 2
        KL      = self.K[L]
	st = np.sin(self.theta_ar)
	if 0 in KL or 1 in KL or -1 in KL:
	    ct = np.cos(self.theta_ar)
	if 0 in KL:
	    ctsq = np.square(ct)
        if 1 in KL:
            sp = np.sin(self.phi_ar)
        if -1 in KL:
            cp = np.cos(self.phi_ar)
	if 2 in KL or -2 in KL:
	    stsq = np.square(st)
	for i in range(len(KL)):
	    K    = KL[i]
	    coef = self.coef[L][i]	    
	    if K == 0:
		T20 = (3.0 * ctsq - 1.0)/2.0
		u20 = T20 * coef
		results.append(u20)
	    elif K == 1:
		T2p1 = (-2.0) * a1 * st * ct * sp
		u2p1 = T2p1 * coef
		results.append(u2p1)
	    elif K == -1:
		T2m1 = 2.0 * a1 * st * ct * cp
		u2m1 = T2m1 * coef
		results.append(u2m1)
	    elif K == 2:
		c2p  = np.cos(2*self.phi_ar)
		T2p2 = a1 * stsq * c2p
		u2p2 = T2p2 * coef
		results.append(u2p2)
	    elif K == -2:
		s2p  = np.sin(2*self.phi_ar)
		T2m2 = -1.0 * a1 * stsq * s2p
		u2m2 = T2m2 * coef
		results.append(u2m2)
	return sum(results)

    def mkDegree3(self):
	""" Calculate 3rd degree on matrices """
	results = []
        L       = 3
        KL      = self.K[L]
	st = np.sin(self.theta_ar)
        ct = np.cos(self.theta_ar)
        if 0 in KL or 1 in KL or -1 in KL:
            ctsq = np.square(ct)
        if 1 in KL:
            sp = np.sin(self.phi_ar)
        if -1 in KL:
            cp = np.cos(self.phi_ar)
        if 2 in KL or -2 in KL \
           or 3 in KL or -3 in KL:
            stsq = np.square(st)
	for i in range(len(KL)):
	    K    = KL[i]
	    coef = self.coef[L][i]	    
	    if K == 0:
                T30 = (5*ctsq*ct-3*ct)/2
                u30 = T30 * coef
                results.append(u30)
	    elif K == 1:
                T3p1 = -(a1/a0) * st * (5*ctsq-1) * sp
                u3p1 = T3p1 * coef
                results.append(u3p1)
	    elif K == -1:
                T3m1 = (a1/a0) * st * (5*ctsq-1) * cp
                u3m1 = T3m1 * coef
                results.append(u3m1)
	    elif K == 2:
                c2p = np.cos(2*self.phi_ar)
                T3p2 = (2.0)*(a0*a1*a2)*stsq*ct*c2p
                u3p2 = T3p2 * coef
                results.append(u3p2)
	    elif K == -2:
                s2p  = np.sin(2*self.phi_ar) 
                T3m2 = -2.0*(a0*a1*a2)*stsq*ct*s2p
                u3m2 = T3m2 * coef
                results.append(u3m2)
	    elif K == 3:
                s3p = np.sin(3*self.phi_ar)
                T3p3 = -(1.0) * a0 * a2 * stsq * st * s3p
                u3p3 =  T3p3 * coef
                results.append(u3p3)
	    elif K == -3:
                c3p  = np.cos(3*self.phi_ar)
                T3m3 = a0 * a2 * stsq * st * c3p
                u3m3 = T3m3 * coef
                results.append(u3m3)
	return sum(results)
        


    def mkDegree4(self):
	""" Calculate 4th degree on matrices """
	results = []
        L       = 4
        KL      = self.K[L]
	st = np.sin(self.theta_ar)
        ct = np.cos(self.theta_ar)
        if 0 in KL or 1 in KL or -1 in KL \
           or 2 in KL or -2 in KL:
            ctsq = np.square(ct)
        if 1 in KL:
            sp = np.sin(self.phi_ar)
        if -1 in KL:
            cp = np.cos(self.phi_ar)
        if 2 in KL or -2 in KL or 3 in KL \
           or -3 in KL or 4 in KL or -4 in KL:
            stsq = np.square(st)    
        if 4 in KL or -4 in KL:
            stsqsq = np.square(stsq)
	for i in range(len(KL)):
	    K    = KL[i]
	    coef = self.coef[L][i]	    
	    if K == 0:
                T40 = ((35.0*ctsq-30.0)*ctsq+3.0)/8.0
                u40 = T40 * coef
                results.append(u40)
	    elif K == 1:
                T4p1 = -2.0*a2/a0*(7.0*ctsq - 3.0)*st*ct*sp
                u4p1 = T4p1 * coef
                results.append(u4p1)
	    elif K == -1:
                T4m1 = 2*a2/a0*(7.0*ctsq - 3.0)*st*ct*cp
                u4m1 = T4m1 * coef
                results.append(u4m1)
	    elif K == 2:
                c2p = np.cos(2*self.phi_ar)
                T4p2 = a2*stsq*(7.0*ctsq-1.0)*c2p
                u4p2 = T4p2 * coef
                results.append(u4p2)
	    elif K == -2:
                s2p  = np.sin(2*self.phi_ar)
                T4m2 = -1.0*a2*stsq*(7.0*ctsq-1.0)*s2p
                u4m2 = T4m2 * coef
                results.append(u4m2)
	    elif K == 3:
                s3p  = np.sin(3*self.phi_ar)
                T4p3 = -2.0*a0*a3*stsq*st*ct*s3p
                u4p3 = T4p3 * coef
                results.append(u4p3)
	    elif K == -3:
                c3p = np.cos(3*self.phi_ar)
                T4m3 = 2.0*a0*a3*stsq*st*ct*c3p
                u4m3 = T4m3 * coef
                results.append(u4m3)
	    elif K == 4:
                c4p = np.cos(4*self.phi_ar)
                T4p4 = a3 * stsqsq * c4p
                u4p4 = T4p4 * coef
                results.append(u4p4)
	    elif K == -4:
                s4p  = np.sin(4*self.phi_ar)
                T4m4 = -1.0 * a3 * stsqsq * s4p
                u4m4 = T4m4 * coef
                results.append(u4m4)
	return sum(results)





