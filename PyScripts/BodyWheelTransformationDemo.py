import numpy as np
from scipy import linalg



theta = np.radians(110/2)
phi = np.radians(110/2)
R = 0.09


WtoB = np.array([[np.cos(theta)/2, -np.cos(phi)/2, -np.cos(phi)/2, np.cos(theta)/2],
				 [np.sin(theta)/2, np.sin(phi)/2, -np.sin(phi)/2, -np.sin(theta)/2],
				 [-1/(4*R), -1/(4*R), -1/(4*R), -1/(4*R)]])

#100 is arbitary number for demo
w_n = np.array([100, 100, -100, -100])
w_w = np.array([-100, 100, 100, -100])
w_s = np.array([-100, -100, 100, 100])
w_e = np.array([100, -100, -100, 100])
w_cc = np.array([-100, -100, -100, -100]) 
w_c = np.array([100, 100, 100, 100])


print("WheelToBody: North = ", WtoB.dot(w_n))
print("WheelToBody: West = ", WtoB.dot(w_w))
print("WheelToBody: South = ", WtoB.dot(w_s))
print("WheelToBody: East = ", WtoB.dot(w_e))
print("WheelToBody: CounterClockWise(positive omega) = ", WtoB.dot(w_cc))
print("WheelToBody: ClockWise = ", WtoB.dot(w_c))
print()
b_n = np.array([0, 100, 0])
b_w = np.array([-100, 0, 0])
b_s = np.array([0, -100, 0])
b_e = np.array([100, 0, 0])
b_cc = np.array([0, 0, 100])
b_c = np.array([0, 0, -100])

try:
	BtoW = linalg.pinv2(WtoB)
except LinArgError:
	pass
print("BodyToWheel: North = ", BtoW.dot(b_n))
print("BodyToWheel: West = ", BtoW.dot(b_w))
print("BodyToWheel: South = ", BtoW.dot(b_s))
print("BodyToWheel: East = ", BtoW.dot(b_e))
print("BodyToWheel: CounterClockWise(positive omega) = ", BtoW.dot(b_cc))
print("BodyToWheel: ClockWise = ", BtoW.dot(b_c))

print("=========================================================================")

###################################################################################
#real robot scenario:
#max linear speed of a wheel
w_max = 3.5 # m/s  

w_n = np.array([w_max, w_max, -w_max, -w_max])
w_w = np.array([-w_max, w_max, w_max, -w_max])
w_s = np.array([-w_max, -w_max, w_max, w_max])
w_e = np.array([w_max, -w_max, -w_max, w_max])
w_cc = np.array([-w_max, -w_max, -w_max, -w_max]) 
w_c = np.array([w_max, w_max, w_max, w_max])
MaxVerticalSpeed = WtoB.dot(w_n)[1]
MaxHorizontalSpeed = WtoB.dot(w_e)[0]
MaxAngularSpeed = WtoB.dot(w_cc)[2]
print("MaxVerticalSpeed: ", MaxVerticalSpeed, " m/s")
print("MaxHorizontalSpeed: ",MaxHorizontalSpeed, " m/s")
print("MaxAngularSpeed: ", MaxAngularSpeed, " rad/s")
NormB = np.array([[MaxHorizontalSpeed/w_max, 0, 0],
				 [0, MaxVerticalSpeed/w_max, 0],
				 [0, 0, MaxAngularSpeed/w_max]])
print("BodyToWheel_Normalized: North = ", BtoW.dot(NormB).dot(b_n), " %")
print("BodyToWheel_Normalized: West = ", BtoW.dot(NormB).dot(b_w), " %")
print("BodyToWheel_Normalized: South = ", BtoW.dot(NormB).dot(b_s), " %")
print("BodyToWheel_Normalized: East = ", BtoW.dot(NormB).dot(b_e), " %")
print("BodyToWheel_Normalized: CounterClockWise(positive omega) = ", BtoW.dot(NormB).dot(b_cc), " %")
print("BodyToWheel_Normalized: ClockWise = ", BtoW.dot(NormB).dot(b_c), " %")


# body vec: <x, y, w> (w is angular speed omega)
# percentage representation, norm(<x, y, w>) == 100%
test_bvec0 = np.array([100, 100, 0])
test_bvec1 = np.array([100, 100, 10])
test_bvec2 = np.array([100, 200, 0])
test_bvec3 = np.array([123, 456, 0])
test_bvec4 = np.array([100, 50, 20])


zero_th = 0.0001

#ordinary vector normalization
def normalize(vec):
	norm = np.linalg.norm(vec)
	if norm < zero_th:
		return vec
	return vec / norm



def norm_bvec(bvec):
	if bvec[2] > 100.00:
		bvec[2] = 100.00
	if bvec[2] < -100.00:
		bvec[2] = -100.00
	max_mag_for_xy = np.sqrt(100**2 - bvec[2]**2)
	xy = np.array([bvec[0], bvec[1]])
	if np.linalg.norm(xy) > max_mag_for_xy:
		xy = normalize(xy) * max_mag_for_xy
	return np.array([xy[0], xy[1], bvec[2]])

print("Norm(", test_bvec0, "): ", norm_bvec(test_bvec0))
print("Norm(", test_bvec1, "): ", norm_bvec(test_bvec1))
print("Norm(", test_bvec2, "): ", norm_bvec(test_bvec2))
print("Norm(", test_bvec3, "): ", norm_bvec(test_bvec3))
print("Norm(", test_bvec4, "): ", norm_bvec(test_bvec4))

#percentage representation's MaxSpeed constraint is a circle on xy plaine for x, y 
#but the real constraint for our robot is a 2d diamond determined by the max-vertical speed and max-horizontal speed
#so a mapping is needed


def xy_constraint(xy_vec, vmax, hmax):
	#diamond top & right vertex
	p1 = np.array([0, vmax])
	p2 = np.array([hmax, 0])

	#edge cases:
	if np.fabs(xy_vec[0]) < zero_th and np.fabs(xy_vec[1]) < zero_th: # x & y ==0
		return 0.00
	if np.fabs(xy_vec[0]) < zero_th: # x == 0
		return vmax
	if np.fabs(xy_vec[1]) < 0.000001: # y == 0
		return hmax

	#line1: (top-right vertex): y= a_p1p2 * x + p1[1]
	#line2: y = a_v * x
	#intersection: a_v * x = a_p1p2 * x +p1[1]
	#				x = p1[1] / (a_v - a_p1p2)
	a_v = np.fabs(xy_vec[1]) / np.fabs(xy_vec[0])
	a_p1p2 = (p1[1] - p2[1]) / (p1[0] - p2[0])
	x = p1[1] / (a_v - a_p1p2)
	y = a_p1p2 * x + p1[1]
	mag = np.linalg.norm(np.array([x, y]))
	return mag


#print(xy_constraint(np.array([1, 1]), 100, 100))
#print(100 * np.cos(np.radians(45)))



def bvecmap(bvec):
	tvec = np.array([bvec[0], bvec[1]])
	rvec = bvec[2]
	max_mag = xy_constraint(tvec, MaxVerticalSpeed, MaxHorizontalSpeed)
	mag = (np.linalg.norm(tvec) / 100.00) * max_mag 
	tvec = normalize(tvec) * mag
	rvec = (rvec / 100.00) * MaxAngularSpeed
	return np.array([tvec[0], tvec[1], rvec])



test_bvec5 = np.array([100, 0, 0])
test_bvec6 = np.array([0, 100, 0])
test_bvec7 = np.array([0, 0, 100])
test_bvec8 = np.array([-100, 0, 0])
test_bvec9 = np.array([0, -100, 0])
test_bvec10 = np.array([0, 0, -100])
test_bvec11 = np.array([100, 100, 100])
test_bvec12 = np.array([44, 88, 0])
test_bvec13 = np.array([50, 0, 0])
test_bvec14 = np.array([0, 50, 0])
test_bvec15 = np.array([0, 0, 50])
test_bvec16 = np.array([50, 25, 0])

print("B-W Transform Mapped Norm(", test_bvec0, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec0))))
print("B-W Transform Mapped Norm(", test_bvec1, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec1))))
print("B-W Transform Mapped Norm(", test_bvec2, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec2))))
print("B-W Transform Mapped Norm(", test_bvec3, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec3))))
print("B-W Transform Mapped Norm(", test_bvec4, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec4))))
print("B-W Transform Mapped Norm(", test_bvec5, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec5))))
print("B-W Transform Mapped Norm(", test_bvec6, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec6))))
print("B-W Transform Mapped Norm(", test_bvec7, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec7))))
print("B-W Transform Mapped Norm(", test_bvec8, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec8))))
print("B-W Transform Mapped Norm(", test_bvec9, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec9))))
print("B-W Transform Mapped Norm(", test_bvec10, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec10))))
print("B-W Transform Mapped Norm(", test_bvec11, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec11))))
print("B-W Transform Mapped Norm(", test_bvec12, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec12))))
print("B-W Transform Mapped Norm(", test_bvec13, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec13))))
print("B-W Transform Mapped Norm(", test_bvec14, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec14))))
print("B-W Transform Mapped Norm(", test_bvec15, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec15))))
print("B-W Transform Mapped Norm(", test_bvec16, "): ", BtoW.dot(bvecmap(norm_bvec(test_bvec16))))


print(norm_bvec(test_bvec13))
print(norm_bvec(test_bvec16))



