    %   This script creates the mesh (both CAD surface mesh and a computational
%   wire grid) for a double helix with 1 A of total current using the new method.
%   The output is saved in the binary file coil.mat and includes:
%   strcoil.Pwire(:, 3) - set of nodes for all wires 
%   strcoil.Ewire(:, 2) - set of edges or current dipoles for all wires
%   (current flows from the first edge node to the second edge node)
%   strcoil.Swire{:, 1} - current strength weight for every elementary
%   dipole asssuring that the total conductor current through any
%   cross-section is 1 A.
%   For accurate inductance calculations, mesh facets must have the highest
%   triangle quality and the wire mesh parameter 'check' must be in the range
%   from 1 to 3
%
%   Copyright SNM 2018-2021

clear all; %#ok<CLALL>
if ~isunix
    s = pwd; addpath(strcat(s(1:end-13), '\CoilEngine'));   
else
    s = pwd; addpath(strcat(s(1:end-13), '/CoilEngine'));  
end

%%  Define dIdt (for electric field)

%%  Define I0 (for magnetic field)
I0 = 0.5;                    %   Amperes, for magnetic field
dIdt = 2*pi*0.5*0.5;           %   Amperes/sec (2*pi*I0/period), for electric field for 10 kHz

%%  First helix with a varying pitch - Hanbing
turns       = 3.5;                               %   number of turns 
theta0      = turns*2*pi;                       %   how many turns (one turn is 2*pi)
twist       = 0;                            %   twist per delta theta. Antes habia pi/12
N           = 600;                              %   subdivisions total
theta       = linspace(0, theta0, N);           %   running angle in radians
delta_theta = theta(2) - theta(1);              %   angle step in radians

d       = 0.00075;                                %   conductor diameter in m 
radius1 = 0.0075;                                %   helix radius, m checks
pitch1  = 0.00075;                               %   pitch amplitude
x       = radius1*cos(theta);                   %   segment
y       = radius1*sin(theta);                   %   segment
z       = zeros(1, N);
delta   = pitch1*delta_theta/pi; 
for m = 2:N
    z(m)  = z(m-1) + 0.5*(1 - sign(sin(theta(m))))*delta;
end
%       Do smooting of the path
for m = 1:1
    z = smooth(z);
end

%   Centerline
clear Pcenter; 
Pcenter(:, 1) = x';
Pcenter(:, 2) = y';
Pcenter(:, 3) = z'-0.00125; %-0.0025

%   Other parameters
M    = 16;              %   number of cross-section subdivisions 
flag = 1;               %   ellipsoidal cross-section    
sk   = 0;               %   surface current distribution (skin layer)

%   Create surface and wire meshes
[strcoil, check]        = meshwire(Pcenter, d, d, M, flag, sk, twist);  %    Wire model    
[P, t]                 = meshsurface(Pcenter, d, d, M, flag, twist);   %    CAD mesh (optional, slow) 

mu0                         = 1.25663706e-006;  %   Magnetic permeability of vacuum(~air)
prec                        = 1e-4;
Inductance1                 = bemf6_inductance_neumann_integral(strcoil, mu0, prec)


figure;
bemf1_graphics_coil_CAD(P, t, 0);
view(0, 0);
camlight; lighting phong; axis off;

strcoil.I0      = I0;
strcoil.dIdt    = dIdt;
strcoil.P       = P;
strcoil.t       = t;
save('coil', 'strcoil');

%%  Second helix with a larger radius
%turns       = 20;                               %   number of turns (shold be 19?)
%theta0      = turns*2*pi;                       %   how many turns (one turn is 2*pi)
%twist       = 0;                            %   twist per delta theta
%N           = 600;                              %   subdivisions total
%theta       = linspace(0, theta0, N);           %   running angle in radians
%delta_theta = theta(2) - theta(1);              %   angle step in radians

%d       = 0.004;                                %   conductor diameter in m (0.004 mm) 
%radius2 = 0.013;                                %   helix radius, m checks
%pitch2  = 0.0055;                               %   pitch amplitude
%x       = radius2*cos(theta);                   %   segment
%y       = radius2*sin(theta);                   %   segment
%z       = zeros(1, N);
%delta   = pitch1*delta_theta/pi; 
%for m = 2:N
%    z(m)  = z(m-1) + 0.5*(1 - sign(sin(theta(m))))*delta;
%end
%       Do smooting of the path
%for m = 1:1
%    z = smooth(z);
%end

%   Skew
%deform  = radius1*atan(pi/12);                              %   deformation scale, m
%z       = z' + deform*(x-mean(x))/max(abs(x-mean(x)));      %    deform

%   Centerline
%clear Pcenter; 
%Pcenter(:, 1) = x';
%Pcenter(:, 2) = y';
%Pcenter(:, 3) = z';

%   Other parameters
%M    = 16;              %   number of cross-section subdivisions 
%flag = 1;               %   ellipsoidal cross-section    
%sk   = 0;               %   surface current distribution (skin layer)

%   Create surface and wire meshes
%[strcoil2, check]        = meshwire(Pcenter, d, d, M, flag, sk, twist);  %    Wire model    
%[P2, t2]                 = meshsurface(Pcenter, d, d, M, flag, twist);   %    CAD mesh (optional, slow) 

%mu0                         = 1.25663706e-006;  %   Magnetic permeability of vacuum(~air)
%prec                        = 1e-4;
%Inductance3                 = bemf6_inductance_neumann_integral(strcoil2, mu0, prec)

% %   Rotate the first helix by 0 deg about the z-axis
% angle           = 0;
% P2              = meshrotate2(P2, [0 0 1], angle);
% strcoil2.Pwire  = meshrotate2(strcoil2.Pwire, [0 0 1], angle);

%figure;
%bemf1_graphics_coil_CAD(P2, t2, 0);
%view(0, 0);
%camlight; lighting phong; axis off;


%%  Third helix with a larger radius
%turns       = 6;                               %   number of turns (shold be 19?)
%theta0      = turns*2*pi;                       %   how many turns (one turn is 2*pi)
%twist       = 0;                            %   twist per delta theta
%N           = 180;                              %   subdivisions total
%theta       = linspace(0, theta0, N);           %   running angle in radians
%delta_theta = theta(2) - theta(1);              %   angle step in radians

%d       = 0.004;                                %   conductor diameter in m (0.004 mm) 
%radius2 = 0.017;                                %   helix radius, m checks
%pitch2  = 0.0055;                               %   pitch amplitude
%x       = radius2*cos(theta);                   %   segment
%y       = radius2*sin(theta);                   %   segment
%z       = zeros(1, N);
%delta   = pitch1*delta_theta/pi; 
%for m = 2:N
%    z(m)  = z(m-1) + 0.5*(1 - sign(sin(theta(m))))*delta;
%end
%       Do smooting of the path
%for m = 1:1
%    z = smooth(z);
%end

%   Skew
%deform  = radius1*atan(pi/12);                              %   deformation scale, m
%z       = z' + deform*(x-mean(x))/max(abs(x-mean(x)));      %    deform

%   Centerline
%clear Pcenter; 
%Pcenter(:, 1) = x';
%Pcenter(:, 2) = y';
%Pcenter(:, 3) = z';

%   Other parameters
%M    = 16;              %   number of cross-section subdivisions 
%flag = 1;               %   ellipsoidal cross-section    
%sk   = 0;               %   surface current distribution (skin layer)

%   Create surface and wire meshes
%[strcoil3, check]        = meshwire(Pcenter, d, d, M, flag, sk, twist);  %    Wire model    
%[P3, t3]                 = meshsurface(Pcenter, d, d, M, flag, twist);   %    CAD mesh (optional, slow) 

%mu0                         = 1.25663706e-006;  %   Magnetic permeability of vacuum(~air)
%prec                        = 1e-4;
%Inductance3                 = bemf6_inductance_neumann_integral(strcoil3, mu0, prec)

% %   Rotate the first helix by 0 deg about the z-axis
% angle           = 0;
% P3              = meshrotate2(P3, [0 0 1], angle);
% strcoil3.Pwire  = meshrotate2(strcoil3.Pwire, [0 0 1], angle);

%figure;
%bemf1_graphics_coil_CAD(P3, t3, 0);
%view(0, 0);
%camlight; lighting phong; axis off;

%%   Construct the entire coil as a combination of three parts
%t2          = t2+size(P1, 1);
%t3          = t3+size(P1, 1)+size(P2, 1);
%P           = [P1; P2; P3];
%t           = [t1; t2; t3];
%P(:, 3)     = P(:, 3) - min(P(:, 3));

%strcoil2.Ewire = strcoil2.Ewire+size(strcoil1.Pwire, 1);
%strcoil3.Ewire = strcoil3.Ewire+size(strcoil1.Pwire, 1)+size(strcoil2.Pwire, 1);
%strcoil.Pwire = [strcoil1.Pwire; strcoil2.Pwire; strcoil3.Pwire]; 
%strcoil.Ewire = [strcoil1.Ewire; strcoil2.Ewire; strcoil3.Ewire];
%strcoil.Swire = [+strcoil1.Swire; strcoil2.Swire; strcoil3.Swire;]; %  do not swap current direction for the second part
%strcoil.Pwire(:, 3)     = strcoil.Pwire(:, 3) - min(strcoil.Pwire(:, 3));

%figure;
%bemf1_graphics_coil_CAD(P, t, 0);
%view(10, 20);
%camlight; lighting phong; axis off;

%%   Inductance calculator
%clear I;
%mu0                         = 1.25663706e-006;  %   Magnetic permeability of vacuum(~air)
%prec                        = 1e-4;
%Inductance                  = bemf6_inductance_neumann_integral(strcoil, mu0, prec)
%if check > 3
%    disp('Decrease the ratio AvgSegmentLength/AvgSegmentSpacing for the wire mesh. Inductance accuracy cannot be guaranteed.')
%end

%   Save coil structure
%strcoil.I0      = I0;
%strcoil.dIdt    = dIdt;
%strcoil.P       = P;
%strcoil.t       = t;
%save('coil', 'strcoil');