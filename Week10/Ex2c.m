info = importdata('RadioactiveDecay');
t = info.data(:,1);
N = info.data(:,2);
figure(42)
plot(t,N,'.b')
hold on
fun = @(A,b,x) A.*exp(b.*x);
fittedmodel = fit(t,N,fun,'StartPoint',[1,1]);
plot(fittedmodel,'r-')
legend('Data','Fitted Line')
hold off