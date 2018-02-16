#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:40:50 2018

@author: cynthia
"""
########Imports##########
from aide_design.play import*
from coastal import*
from scipy import optimize

######## 1i ##########
period = 4 * u.s
height = 5 * u.m
g = 9.80665 * u.m/u.s**2

k_number = wavenumber(period, height)
wave_length = wavelength(k_number)
wave_speed = celerity(wave_length, period)

print(wave_length)
print(wave_speed)

######## 1ii ##########
z = -2 * u.m
z_crest = 1 * u.m
x = 0 * u.m
t = 0 * u.s
temp = (25 * u.degC).to(u.degK)
amp = 1 * u.m

vel_u = velocity_u(period, height, amp, t, x, z)
vel_w = velocity_w(period, height, amp, t, x, z)
pressure = pressure_wave(period, height, amp, t, x, z, temp)
pressure_crest = pressure_wave(period, height, amp, t, x, z_crest, temp)

print(vel_u, vel_w, pressure.to(u.kPa), pressure_crest.to(u.kPa))

#2a
height_design = 3 * u.m
amp_design = 0.5 * u.m
height_wall = 2 * amp_design + height_design

print(height_wall)

#2b
period_design = 10* u.s
force_max = force_max(period_design, height_design, amp_design, temp)
print(force_max.to(u.kN))
