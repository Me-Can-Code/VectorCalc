import math 
import decimal
print ("What's your name? ")
a = input() 

print ("Welcome " + a + ". This is a Vector Calculator.") 
print("Choose if you would like to Input 1 Vector or 2 Vectors. Type 1 or 2 to choose.")

b = input()


if b == '1' :
    print ("Enter the i component: ")
    c = input()
    cc = int(c,10)
    print ("Enter the j component: ")
    d = input()
    dd = int(d,10)
    print ("Enter the k component: ")
    e = input ()
    ee = int(e,10)

    mag1 = math.sqrt(ee * ee + dd * dd + cc * cc)
    mag2 = round(mag1, 3)
    mag3 = str(mag2)

    UVi = (cc / mag1)
    UVj = (dd / mag1)
    UVk = (ee / mag1)
    
    UVii = round(UVi, 3)
    UVjj = round(UVj, 3)
    UVkk = round(UVk, 3)

    UViii = str(UVii)
    UVjjj = str(UVjj)
    UVkkk = str(UVkk)
    
    Alpha = math.acos(UVi)
    Beta = math.acos(UVj)
    Gamma = math.acos(UVk) 
    
    Alpha1 = round(math.degrees(Alpha), 1)
    Beta1 = round(math.degrees(Beta), 1)
    Gamma1 = round(math.degrees(Gamma), 1)
    
    Alpha11 = str(Alpha1)
    Beta11 = str(Beta1)
    Gamma11 = str(Gamma1)
    
    Theta = math.atan (dd / cc )
    Phi = (90 - Gamma1)
    
    Theta1 = round(math.degrees(Theta), 1)
    
    Theta11 = str(Theta1)
    Phi1 = str(Phi)
    
    print("Magnitude: " + mag3)
    print("These are the Unit Vectors: " + UViii + "  ,  " + UVjjj + " , " + UVkkk )
    print("These are the Direction Cosines: ")
    print("Alpha: " + Alpha11) 
    print("Beta: " + Beta11) 
    print("Gamma: " + Gamma11)
    print("Theta: " + Theta11)
    print("Phi: " + Phi1)

if b == "2" :

	print ("Would you like to Subtract, Add or find the Dot Product the vectors?")
	print ("Type either Sub, Add, Dot, or Cross to activate the corresponding functions.")

	c = input()
	if c == "Sub" :
		print("Enter the i component of Vector A: ")
		f = input() 
		ff = int(f,10)
		print ("Enter the j component of Vector A: ")
		g = input()
		gg = int(g,10)
		print ("Enter the k component of Vector A: ")	
		h = input ()
		hh = int(h,10)
		print ("Enter the i component of Vector B: ")
		i = input()
		ii = int(i,10) 
		print ("Enter the j component of Vector B: ")
		j = input()
		jj= int(j,10)
		print ("Enter the k component of Vector B: ")
		k = input ()
		kk = int(k,10)

		iAB = (ff-ii)	
		jAB = (gg-jj)
		kAB = (hh-kk)

		iAB1 = str(iAB)
		jAB1 = str(jAB)
		kAB1 = str(kAB)

		print ("Vector A - Vector B =" + iAB1 +"i," + jAB1 + "j," + kAB1 + "k.")

		MagAB = round(math.sqrt( iAB * iAB + jAB * jAB + kAB * kAB ), 3)
		MagAB1 = str(MagAB)

		UViAB = round( ( iAB / MagAB ), 3)
		UVjAB = round( ( jAB / MagAB ), 3)
		UVkAB = round( ( kAB / MagAB ), 3)
		UViiAB = str(UViAB)
		UVjjAB = str(UVjAB)
		UVkkAB = str(UVkAB)

		Alpha = math.acos(UViAB)
		Beta = math.acos(UVjAB)
		Gamma = math.acos(UVkAB)
    
		Alpha1 = round(math.degrees(Alpha), 1)
		Beta1 = round(math.degrees(Beta), 1)
		Gamma1 = round(math.degrees(Gamma), 1)

		Alpha11 = str(Alpha1)
		Beta11 = str(Beta1)
		Gamma11 = str(Gamma1)

		Theta = math.atan ( UVjAB / UViAB )
		Phi = (90 - Gamma1)
    
		Theta1 = round(math.degrees(Theta), 1)
    
		Theta11 = str(Theta1)
		Phi1 = str(Phi)
    
		print ("This is the Magnitude of Vector A - B: " + MagAB1)
		print ("Unit Vector of Vector A - B: " + UViiAB + "," + UVjjAB + "," + UVkkAB)
		print ("These are the Direction Cosines: ") 
		print ("Alpha (A-B) = " + Alpha11)
		print ("Beta (A-B) = " + Beta11) 
		print ("Gamma (A-B) = " + Gamma11)
		print ("Theta (A-B) = " +Theta11)
		print ("Phi (A-B) = " + Phi1)


		iBA = (ii-ff)
		jBA = (jj-gg)
		kBA = (kk-hh)

		iBA1 = str(iBA)
		jBA1 = str(jBA)
		kBA1 = str(kBA)

		print ("                                                       ")
		print ("Vector B - Vector A =" + iBA1 +"i," + jBA1 + "j," + kBA1 + "k."  )
		MagBA = round(math.sqrt( iBA * iBA + jBA * jBA + kBA * kBA ), 3)
		MagBA1 = str(MagBA)
		UViBA = round(( iBA / MagBA ), 3)
		UVjBA = round(( jBA / MagBA ), 3)
		UVkBA = round(( kBA / MagBA ), 3)
		UViiBA = str(UViBA)
		UVjjBA = str(UVjBA)
		UVkkBA = str(UVkBA)

		AlphaBA = math.acos(UViBA)
		BetaBA = math.acos(UVjBA)
		GammaBA = math.acos(UVkBA)
    
		Alpha2 = round(math.degrees(AlphaBA), 1)
		Beta2 = round(math.degrees(BetaBA), 1)
		Gamma2 = round(math.degrees(GammaBA), 1)

		Alpha22 = str(Alpha2)
		Beta22 = str(Beta2)
		Gamma22 = str(Gamma2)

		ThetaBA = math.atan ( UVjBA / UViBA )
		PhiBA = (90 - Gamma2)
    
		Theta2 = round(math.degrees(ThetaBA), 1)
    
		Theta22 = str(Theta2)
		Phi22 = str(PhiBA)

		print ("This is the Magnitude of Vector B - Vector A: " + MagBA1)
		print ("Unit Vector of Vector B - A: " + UViiBA + "," + UVjjBA + "," + UVkkBA)
		print ("These are the Direction Cosines: ") 
		print ("Alpha (B-A) = " + Alpha22)
		print ("Beta (B-A) = " + Beta22) 
		print ("Gamma (B-A) = " + Gamma22)
		print ("Theta (B-A) = " +Theta22)
		print ("Phi (B-A) = " + Phi22)

	if c == "Add" :
		print("Enter the i component of Vector A: ")
		f = input() 
		ff = int(f,10)
		print ("Enter the j component of Vector A: ")
		g = input()
		gg = int(g,10)
		print ("Enter the k component of Vector A: ")	
		h = input ()
		hh = int(h,10)
		print ("Enter the i component of Vector B: ")
		i = input()
		ii = int(i,10) 
		print ("Enter the j component of Vector B: ")
		j = input()
		jj= int(j,10)
		print ("Enter the k component of Vector B: ")
		k = input ()
		kk = int(k,10)
		
		iF = (ff+ii)	
		jF = (gg+jj)
		kF = (hh+kk)

		iFF = str(iF)
		jFF = str(jF)
		kFF = str(kF)

		print ("Vector A + Vector B =" + iFF +"i," + jFF + "j," + kFF + "k.")
		MagF = round(math.sqrt( iF * iF + jF * jF + kF * kF ), 3)
		MagFF = str(MagF)

		UVi = round(( iF / MagF ), 3)
		UVj = round(( jF / MagF ), 3)
		UVk = round(( kF / MagF ), 3)
		UVii = str(UVi)
		UVjj = str(UVj)
		UVkk = str(UVk)

		Alpha = math.acos(UVi)
		Beta = math.acos(UVj)
		Gamma = math.acos(UVk)
    
		Alpha1 = round(math.degrees(Alpha), 1)
		Beta1 = round(math.degrees(Beta), 1)
		Gamma1 = round(math.degrees(Gamma), 1)

		Alpha11 = str(Alpha1)
		Beta11 = str(Beta1)
		Gamma11 = str(Gamma1)

		Theta = math.atan ( UVj / UVi )
		Phi = round((90 - Gamma1), 1)
    
		Theta1 = round(math.degrees(Theta), 1)
    
		Theta11 = str(Theta1)
		Phi1 = str(Phi)
    
		print ("This is the Magnitude: " + MagFF)
		print ("These are the Unit Vector: " + UVii + " , " + UVjj + " , " + UVkk)
		print ("These are the Direction Cosines: ") 
		print ("Alpha = " + Alpha11)
		print ("Beta = " + Beta11) 
		print ("Gamma = " + Gamma11)
		print ("Theta = " +Theta11)
		print ("Phi = " + Phi1)

	if c == "Dot":
		print("Enter the i component of Vector A: ")
		f = input() 
		ff = int(f,10)
		print ("Enter the j component of Vector A: ")
		g = input()
		gg = int(g,10)
		print ("Enter the k component of Vector A: ")   
		h = input ()
		hh = int(h,10)
		print ("Enter the i component of Vector B: ")
		i = input()
		ii = int(i,10) 
		print ("Enter the j component of Vector B: ")
		j = input()
		jj= int(j,10)
		print ("Enter the k component of Vector B: ")
		k = input ()
		kk = int(k,10)

		dot = (ff*ii + gg*jj + hh*kk) 
		dot1 = str(dot)

		ang = (math.acos((dot)/(math.sqrt(ii*ii + jj*jj + kk*kk)*(math.sqrt(ff*ff + gg*gg + hh*hh)))))
		ang1 = round(math.degrees(ang), 1)
		ang2 = str(ang1)

		magA = (math.sqrt(ff*ff + gg*gg + hh*hh))
		magB = (math.sqrt(ii*ii + jj*jj + kk*kk))

		UViA = (ff/magA)
		UVjA = (gg/magA)
		UVkA = (hh/magA)
		UViB = (ii/magB)
		UVjB = (jj/magB)
		UVkB = (kk/magB)

		ProjAB = round((math.sqrt(ff*UViB + gg*UVjB + hh*UVkB)), 3)
		ProjBA = round((math.sqrt(ii*UViA + jj*UVjA + kk*UVkA)), 3)
		Projab = str(ProjAB)
		Projba = str(ProjBA)

		print("Vector A * Vector B: " + dot1)
		print("Angle between Vector A and B: " + ang2 + " degrees")
		print("Magnitude of Projection of A onto B = " + Projab)
		print("Magnitude of Projection of B onto A = " + Projba)

	if c == "Cross":
		print("Enter the i component of Vector A: ")
		f = input() 
		ff = int(f,10)
		print ("Enter the j component of Vector A: ")
		g = input()
		gg = int(g,10)
		print ("Enter the k component of Vector A: ")   
		h = input ()
		hh = int(h,10)
		print ("Enter the i component of Vector B: ")
		i = input()
		ii = int(i,10) 
		print ("Enter the j component of Vector B: ")
		j = input()
		jj= int(j,10)
		print ("Enter the k component of Vector B: ")
		k = input ()
		kk = int(k,10)

		a = (gg*kk + (-(hh*jj)))
		b = (hh*ii + (-(ff*kk)))
		c = (ff*jj + (-(gg*ii)))
		a1 = str(a)
		b1 = str(b)
		c1 = str(c)

		d = (jj*hh + (-(kk*gg)))
		e = (kk*ff + (-(ii*hh)))
		f = (ii*gg + (-(jj*ff)))
		d1 = str(d)
		e1 = str(e)
		f1 = str(f)

		print ("Vector A Crossed With Vector B =" + a1 +"i," + b1 + "j," + c1 + "k.")
		print ("Vector B Crossed With Vector A =" + d1 +"i," + e1 + "j," + f1 + "k.")

