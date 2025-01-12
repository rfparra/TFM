%   This script creates the mesh (both CAD surface mesh and a volumetric
%   mesh) for a rectangular column. The output is saved in the binary file
%   core.mat and includes arrays P, t, normals (surface) and P, T (volume)
%
%   Copyright SNM 2018-2021

clear all; %#ok<CLALL>
if ~isunix
    s = pwd; addpath(strcat(s(1:end-13), '\CoilEngine'));   
else
    s = pwd; addpath(strcat(s(1:end-13), '/CoilEngine'));  
end

%   The brick centerline is given first
par = linspace(0, 1, 100);
L   = 0.019;                         %   cylinder height in m
x = L*par;                          %   segment
y = 0*par;                          %   segment

%   Other parameters
d    = 0.016;      %   conductor diameter in m
M    = 32;          %   number of cross-section subdivisions 
flag = 1;           %   circular cross-section    

%   Create surface CAD model
Pcenter(:, 1) = x';
Pcenter(:, 2) = y';
Pcenter(:, 3) = 0;
[P, t, normals]     = meshsurface(Pcenter, d, d, M, flag, 0);  % CAD mesh
P                   = meshrotate2(P, [0 1 0], pi/2);
normals             = meshrotate2(normals, [0 1 0], pi/2);
P(:, 3)             = P(:, 3) - mean(P(:, 3));

%   Create volume CAD model (overwrite the previous surface CAD model)
%   Important: nodes of surface facets are automatically placed up front
grade = 1.0e-3;  %   mesh resolution in meters
[P, t, normals, T] = meshvolume(P, t, grade);

%   Create expanded volume SWG basis function CAD model (overwrite
%   the previous volume CAD model)
GEOM = meshvolumeswg(P, T); %   Creates structure GEOM with all necessary parameters

%   Display CAD model (surface only)
figure;
bemf1_graphics_coil_CAD(GEOM.P, GEOM.t, 1);
camlight; lighting phong;
view(-140, 40);
axis off

save('core.mat', 'GEOM');
