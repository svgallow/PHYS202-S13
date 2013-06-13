function [ m,b,slerr,interr ] = weightedLSQFit(x, y,weight )
%Take in arrays of (x,y) values for linearly varying data and an array of weights w.
%Uses a weighted linear least squares regression. Returns resulting slope
%and intercept parameters and uncertainties of the function
%if the weights are all equal to one, the uncertainties on the parameters are calculated using the
%non-weighted least squares equations.
w = sum(weight);
wX = sum(weight.*X);
wXSQ = sum(weight.*.^2);
wY = sum(weight.*y);
wXY = sum(weight.*x.*y);
b = (wXSP.*wY-wX.*wXY)/(w.*wXSQ-wX.^2);
m = (w.*wXY-wX.*wY)/(w.*wXSQ-wX.^2);
slerr = (w/(w.*wxsq-wX.^2)).^0.5;
interr = (wWSP/(w.*wXSQ-wX.^2)).^0.5;
end
