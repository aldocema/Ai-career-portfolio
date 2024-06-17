clear all;
close all;
clc;

tmin=0;
tmax=30;
h=0.01;
t=tmin:h:tmax;
k=180/pi;
x10=30/k; %valor inicial en grados/k.
x20=0;

x=[x10 x20];
x;
in=1;

modelo=readfis('pendulo_inv');

for i=1:length(t)-1
    f=pendulo(x(i,1),x(i,2),in);
    x(i+1,1)=x(i,1)+h*f(1); 
    x(i+2,2)=x(i,2)+h*f(2);
    in=evalfis([x(i+1,1) x(i+1,2)],modelo);
    carrito(x(i+1,1),in);
    hold off
    %i=i+1;
end

figure(1)
carrito(in,x(i+1,1));

figure(2)
plot(t,x(1:length(t),1)*k);
grid on


function carrito(xi,in)
    in2=in;
    in=in+30;
    x=[in in+5 in+5 in+0 in+0];  %Rectangulo
    y=[10 10 11.5 11.5 10];
    x_rot=[0 5 5 0 0];
    y_rot=[0 0 .5 .5 0];
    theta=xi+0.5*pi;%((xi*pi)/180)+2*pi;
    m_rot_a=[cos(theta) -sin(theta); % Sentido antihorario
            sin(theta) cos(theta);];
    %m_rot_h=[cos(theta) sin(theta); % Sentido horario
     %       -sin(theta) cos(theta);];
    coord=[x_rot;y_rot;];
    plot(x,y,'b','LineWidth',3);
    axis([0 60 0 60])
    hold on 
    grid on
    coord2=m_rot_a*coord;
    n_ox=ones(1,5)*(in+2);
    n_oy=ones(1,5)*(11.5);%(10+(1.5/2)); %mover el eje
    coord3=coord2+[n_ox;n_oy];
    plot(coord3(1,:),coord3(2,:),'r')
    pause(0.0001)
    %hold off
    %{
    for ii=xi:1:xf
        plot(x,y,'b','LineWidth',3);
        axis([0 60 0 60])
        hold on 
        grid on
        x=[ii ii+5 ii+5 ii+0 ii+0];  %Rectangulo
        y=[10 10 11.5 11.5 10];
        m_rot_a=[cos(theta) -sin(theta); % Sentido antihorario
            sin(theta) cos(theta);];
        m_rot_a=[cos(theta) -sin(theta); % Sentido antihorario
                sin(theta) cos(theta);];
        coord2=m_rot_a*coord;
        theta=theta+(0.1);
        n_ox=ones(1,5)*(ii+2);
        n_oy=ones(1,5)*(11.5);%(10+(1.5/2)); %mover el eje
        coord3=coord2+[n_ox;n_oy];
        plot(coord3(1,:),coord3(2,:),'r')
        pause(0.1)
        hold off
        
    end
    %}
end

