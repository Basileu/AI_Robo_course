# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 0.0000000001

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 
mean1 = mu
var1 = sig
# Insert code here
for i in range (0, len(motion)):
    new_mean, new_var = update(mean1, var1, measurements[i], measurement_sig)
    # print 'update:', [new_mean, new_var]
    new_mean1, new_var2 = predict(new_mean, new_var, motion[i], motion_sig)
    # print 'predict:', [new_mean1, new_var2]
    mean1 = new_mean1
    var1 = new_var2
    # print [mean1, new_var2]
mu = mean1
sig = new_var2
print [mu, sig]
