%   This script accurately computes and displays electric fields sampled on
%   a cross-section (sagittal plane) via the FMM method with accurate neighbor integration
%
%   Copyright SNM/WAW 2017-2020

%%  Post processing parameters
component   = 4;        %   field component to be plotted (1, 2, 3 or x, y, z, or 4 - total) 
temp        = ['x' 'y' 'z' 't'];
label       = temp(component);

%%  Define dimensionless radius of the integration sphere (for precise integration near boundaries)
R = 4;

%%  Define observation points in the cross-section (MsxMs observation points)    
Ms = 500;
%   sagittal plane
y = linspace(ymin, ymax, Ms);
z = linspace(zmin, zmax, Ms);
[Y0, Z0]  = meshgrid(y, z);
clear pointsYZ;
pointsYZ(:, 1) = X*ones(1, Ms^2);
pointsYZ(:, 2) = reshape(Y0, 1, Ms^2);
pointsYZ(:, 3) = reshape(Z0, 1, Ms^2);
pointsYZ       = 1e-3*pointsYZ;  %  Convert back to m
%  Assign tissue types to observation points
obsPointTissues = assign_tissue_type_volume(pointsYZ, normals, Center, Indicator);
in              = obsPointTissues > 2;    % skin, skull excluded

%% Find the E-feld at each observation point in the cross-section         
tic  
Epri           = zeros(Ms*Ms, 3);
Esec           = zeros(Ms*Ms, 3);
Epri(in, :)    = bemf3_inc_field_electric_core(strcoil, pointsYZ(in, :), mu0, prec);        %  Incident coil field
Esec(in, :)    = bemf5_volume_field_electric(pointsYZ(in, :), c, P, t, Center, Area, normals, R, prec);
Etotal         = Epri + Esec;   
fieldPlaneTime = toc  

%% Calculate current density at each observation point
% Observation points in free space were originally assigned tissue code 0, 
% so provide an extra "Free Space" conductivity entry and point free space obs pts to that entry.
condTemp = [cond 0];                                        
obsPointTissues(obsPointTissues == 0) = length(condTemp);

% Calculate current density J = sigma * E
condTempExpanded = transpose(condTemp(obsPointTissues));
Jtotal = repmat(condTempExpanded, 1, 3).*Etotal;

%%  Plot the E-field in the cross-section
figure;
%  E-field plot: contour plot
if component == 4
    temp      = abs(sqrt(dot(Etotal, Etotal, 2)));
else
    temp      = abs(Etotal(:, component));
end
th1 = 0.7*max(temp);          %   in V/m
th2 = 0;            %   in V/m
levels      = 20;
bemf2_graphics_vol_field(temp, th1, th2, levels, y, z);

%%  Line graphics
bemf1_graphics_lines(Nx, Ny, Nz, MoveX, MoveY, MoveZ, Target, handle, 'yz');

xlabel('Distance y, mm');
ylabel('Distance z, mm');
title(['E-field (V/m), ', label, '-component in the sagittal plane.']);
 
% E-field plot: tissue boundaries
color   = prism(length(tissue)); color(4, :) = [1 1 1];
for m = countYZ
    edges           = EofYZ{m};              %   this is for the contour
    points          = [];
    points(:, 1)    = +PofYZ{m}(:, 2);       %   this is for the contour  
    points(:, 2)    = +PofYZ{m}(:, 3);       %   this is for the contour
    patch('Faces', edges, 'Vertices', points, 'EdgeColor', color(m, :), 'LineWidth', 2.0);    %   this is contour plot
end
% E-field plot: general settings 
axis 'equal';  axis 'tight';     
colormap jet; colorbar;
axis([ymin ymax zmin zmax]);
line(mean([ymin ymax]), mean([zmin, zmax]), 'Marker', 'o', 'MarkerFaceColor', 'm', 'MarkerSize', 12); 
grid off; set(gcf,'Color','White');

