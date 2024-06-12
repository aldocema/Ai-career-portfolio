% Este programa realiza la aproximación de la funcion e^x  
%mediante su serie de Maclaurin
%chapra 
% ACM 2022-08-08

%{
clear all;
clc;
close all;

V_v=1.648721271;
x=0.5;
%Primer termino de la serie
e_x=1;
V_a=e_x;
E_v=(abs(V_v-V_a)/V_v)*100
Aact=e_x;
Aant=0;
E_a=(abs(Aact-Aant)/Aact)*100
%2do termino de la serie
e_x=1+x;
V_a=e_x;
E_v=(abs(V_v-V_a)/V_v)*100
Aact=e_x;
Aant=1;
E_a=(abs(Aact-Aant)/Aact)*100
%3er termino de la serie
e_x=1+x+((x^2)/factorial(2));
V_a=e_x;
E_v=(abs(V_v-V_a)/V_v)*100
Aact=e_x;
Aant=1.5;
E_a=(abs(Aact-Aant)/Aact)*100
%}

clear all;
close all;
clc;
tic
% Numero de terminos de la serie
n=25;
% Valor al cual se quiere aproximar la funcion exponencial
x=0.5;
% Valor verdadero
Vv=exp(x);
%Vv=1.648721270700128;
% 1a Aproximacion
Aant=0;
e_x=(x^0)/(factorial(0));
% Aproximacion del valor del termino de la serie
Va=e_x;
Aact=e_x;
Aant=0;
% Error verdadero (Et)-> t = true
Et=abs(((Vv-Va)/Vv)*100);
% Error aproximado (Ea)->  = approximate
Ea=abs(((Aact-Aant)/Aact)*100);
Es=(0.5)*10^(2-n);
for m=1:n-1
    Aant=Va;
    e_x=e_x+(x^m)/(factorial(m));
    Va=e_x;
    Aact=e_x;
    Et_new=abs((Vv-Va)/Vv)*100;
    Et=[Et,Et_new];
    Ea_new=abs((Aact-Aant)/Aact)*100;
    Ea=[Ea,Ea_new];
end
toc
figure;
plot(Ea,'LineWidth',2);
title('Grafica del error');
xlabel('Numero de terminos de la serie');
ylabel('Porcentaje del error');
grid on;
hold on;
plot(Et,'r','LineWidth',2);
 %colocar etiqueta a cada cosa hacerlo en python
e_x
Vv

