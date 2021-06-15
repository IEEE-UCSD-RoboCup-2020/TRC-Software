import numpy as np
from scipy import linalg



theta = np.radians(110/2)
phi = np.radians(110/2)
R = 0.09

WtoB = np.array([[np.cos(theta)/2, -np.cos(phi)/2, -np.cos(phi)/2, np.cos(theta)/2],
				 [np.sin(theta)/2, np.sin(phi)/2, -np.sin(phi)/2, -np.sin(theta)/2],
				 [-1/(4*R), -1/(4*R), -1/(4*R), -1/(4*R)]])

w_n = np.array([100, 100, -100, -100])
w_w = np.array([-100, 100, 100, -100])
w_s = np.array([-100, -100, 100, 100])
w_e = np.array([100, -100, -100, 100])
w_cc = np.array([-6.28, -6.28, -6.28, -6.28])
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

print()

MaxVerticalSpeed = WtoB.dot(w_n)[1]
MaxHorizontalSpeed = WtoB.dot(w_e)[0]
print("MaxVerticalSpeed: ", MaxVerticalSpeed)
print("MaxHorizontalSpeed: ",MaxHorizontalSpeed)
NormB = np.array([[MaxHorizontalSpeed/100, 0, 0],
				 [0, MaxVerticalSpeed/100, 0],
				 [0, 0, 1]])

print("BodyToWheel_Normalized: North = ", BtoW.dot(NormB).dot(b_n))
print("BodyToWheel_Normalized: West = ", BtoW.dot(NormB).dot(b_w))
print("BodyToWheel_Normalized: South = ", BtoW.dot(NormB).dot(b_s))
print("BodyToWheel_Normalized: East = ", BtoW.dot(NormB).dot(b_e))
print("BodyToWheel_Normalized: CounterClockWise(positive omega) = ", BtoW.dot(NormB).dot(b_cc))
print("BodyToWheel_Normalized: ClockWise = ", BtoW.dot(NormB).dot(b_c))