import numpy as np
def LinearLeastSquaresFit(x,y):
    import numpy as np
    """Take in arrays representing (x,y) values for a set of linearly 
    varying data and preform a linear least squares regression.  
    Return the resulting slope and intercept parameters of the best 
    fit line with their uncertainties."""
    X = np.sum(x)/len(x) #x average
    X2 = np.sum(x**2)/len(x**2) #x^2 average
    Y = np.sum(y)/len(y) #y average
    XY = np.sum(x*y)/len(x*y) #x*y average
    m = (XY-(X*Y))/(X2-(X**2)) #slope formula
    b = (X2*Y - (X*XY))/(X2-(X**2)) #intercept formula
    dir1 = y - (m*x + b) #deviation to get deviation^2
    dir2 = np.sum(dir1**2)/len(x) #deviation^2 formula
    slerr = np.sqrt((1/(len(x)-2.))*(dir2/(X2 - (X**2)))) #slope uncertainty
    interr = np.sqrt((1/(len(x)-2.))*((dir2*X2)/(X2 - (X**2)))) #intercept uncertainty
    return m,b,slerr,interr



def WeightedLinearLeastSquaresFit(x,y,w):
    """Take in arrays representing (x,y) values for a set of linearly varying data
    and an array of weights w.  Preform a weighted linear least squares regression.
    Return the resulting slope and intercept parameters of the best fit line with
    their uncertainties."""
    wsum = sum(w)
    wx = sum(x*w)
    wx2 = sum(w*(x**2))
    wy = sum(w*y)
    wxy = sum(w*x*y)
    m = (wsum*wxy-wx*wy)/(wsum*wx2 - (wx**2))
    b = (wx2*wy-wx*wxy)/(wsum*wx2 - (wx**2))
    if sum(w)/len(w) == 1:#if this equals 1, should behave like question 2
        X = average(x)
        Y = average(y)
        X2 = average(x**2)
        XY = average(x*y)
        dir1 = y - (m*x+b)
        dir2 = average(dev**2)
        slerr = ( (1.0/(len(x)-2)) * (dev1/((averagex2 - averagex**2))) )**(0.5)
        interr = ( (1.0/(len(x)-2)) * ((dev1*averagex2)/((averagex2 - averagex**2))) )**(0.5)
    else:
        slerr = (wsum/((wsum*wx2) - (wx**2)))**0.5 #weighted slope error
        interr = (wx2/(wsum*wx2 - wx**2))**0.5 #weighted intercept error
    return m,b,slerr,interr
