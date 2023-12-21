import numpy as np
import math as mt 


#Constants

q0 = 1.6021766e-19  # C 
c = 299792458 #m/s
kB = 1.3806503e-23  # J/K
T = 298			 # K
h = 6.62607015e-34 #Js
area = 0.064 #area in cm^2 
lambda_0 = 1550e-9 #m Naional Career Constant
Rs = 100e9 # Shannon datarate
Ch_spacing = 100e9#Hz channel spacing
Mod_BW = 10e12 #Hz Total Modulated BW
Loss_coef = .2e-3 #dB/m
Gamma = 1.2e-3 #W/m 
GVD= -21.7e-3 #ps^2/m
Ls = 100e3 #m Lump Amplifier spacing
NF = 4.5 #Noise Figure dB

sig2_ASE = (mt.exp(Loss_coef*Ls)-1)*10**(NF/10)*h*c/lambda_0*Rs

NSR = lambda Ni,Leff: Ni*(2*sig2_ASE**2*Gamma**2*Loss_coef*Leff**2/mt.pi/abs(GVD)**2/Rs**2*mt.log(mt.pi**2*abs(GVD)*Mod_BW**2/Loss_coef))**(1/3)