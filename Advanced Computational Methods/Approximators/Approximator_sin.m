clear all;
close all;
clc;
tic
%{
n=80;
x=37;
vv=sin(x);
aant=0;
aact=0;
res=zeros(3,n);
serie_sin=0;
suma=0;
ea=0;
for a=0:n-1
    suma=(x^((2*a)+1))/(factorial((2*a)+1));
    if mod(a,2)~=0
        suma=-suma;
    end
    serie_sin=serie_sin+suma;
    res(1,a+1)=a+1;
    aant=aact;
    aact=serie_sin;
    l_ev=abs((vv-serie_sin)/vv)*100;
    res(2,a+1)=l_ev;
    ea=abs((aact-aant)/aact)*100;
    res(3,a+1)=ea;
end
toc
figure;
plot(res(1,:),res(2,:),'-x','LineWidth',2);
title('Grafica del error');
xlabel('Numero de terminos de la serie (n)');
ylabel('Porcentaje del error (%)');
grid on;
hold on;
plot(res(1,:),res(3,:),'-x','LineWidth',2);
legend('Error verdadero', 'Error aproximado')
%}

n=5;
x=30;
vv=sin(x);
aant=0;
aact=0;
it=[];
lista_ev=[];
lista_ea=[];
serie_cos=0;
suma=0;
ea=100;
l_ev=100;
a=0;
sigma=(0.5*10^(2-n)); %cifras significativas
while sigma<ea && sigma<l_ev || a==100
    suma=(x^((2*a)+1))/(factorial((2*a)+1));
    if mod(a,2)~=0
        suma=-suma;
    end
    serie_cos=serie_cos+suma;
    it=[it,a+1];
    aant=aact;
    aact=serie_cos;
    l_ev=abs((vv-serie_cos)/vv)*100;
    lista_ev=[lista_ev,l_ev];
    ea=abs((aact-aant)/aact)*100;
    lista_ea=[lista_ea,ea];
    a=a+1;
end
toc
figure;
plot(it(1,:),lista_ev(1,:),'-x','LineWidth',2);
title('Grafica del error');
xlabel('Numero de terminos de la serie (n)');
ylabel('Porcentaje del error (%)');
grid on;
hold on;
plot(it(1,:),lista_ea(1,:),'-x','LineWidth',2);
legend('Error verdadero', 'Error aproximado')