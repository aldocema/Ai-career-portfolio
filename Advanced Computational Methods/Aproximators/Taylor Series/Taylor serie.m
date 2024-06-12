%Series de Taylor con las formulas 4.1 y 4.2 de chapra
%Aldo Cervantes
%Evaluación de dos funciones, únicamente modificar derivadas, a1,a2,n 
clear all;
close all;
clc;

syms x; f1=-0.1*x^4-0.15*x^3-0.5*x^2-0.25*x+1.2; 
f2=cos(x);
f3=3^(x);
n=7;
a1=pi/4;
a2=pi/3;
h=a2-a1;
z=10; %el valor de z es variable y depende de otras cosas
aprox=0;
derivadas=f2;%f2
vv=cos(a2);
m={n,4};
for i=1:n
    m{i,1}=i-1;
    m{i,2}=string(derivadas);
    aprox=aprox+((subs(derivadas,a1)/factorial(i-1))*(h)^(i-1));
    m{i,3}=double(aprox);
    erp=((vv-aprox)/vv)*100;
    m{i,4}=double(erp);
    derivadas=diff(derivadas);
    
end
r_n=double(((subs(int(f2),z))/factorial(n+1))*(h)^(n+1)) % se debe sumar pero puede afectar el resultado si no se elije bien z
double(aprox)
m


