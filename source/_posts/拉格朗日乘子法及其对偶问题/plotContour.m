
x = 0:0.1:4;
y = -2:0.1:2;
[X, Y] = meshgrid(x, y);
Z = (X-2).^2 + Y.^2;
contour(X, Y, Z);

hold on;

plot(2, 1, '*');
arrow([2, 1], [0, 0.2], 'r');


% x = -2:0.1:0.5;
% y = -x - sqrt(2.0)
% 
% plot(x, y);
% 
% plot(-sqrt(2) / 2, -sqrt(2) / 2, '*');
% 
% arrow([-sqrt(2) / 2, -sqrt(2) / 2], [0.2, 0.2], 'red');
% arrow([-sqrt(2) / 2, -sqrt(2) / 2], [-0.2, -0.2]);

