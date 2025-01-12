%   This script defines three observation planes and plots cross-sections and
%   NIfTI data when availble
%
%   Copyright SNM/WAW 2017-2020

%%  Define all three planes (mm)
X       = 0.0;                  %   YZ Cross-section position, mm
Y       = -20;                %   XZ Cross-section position, mm
Z       = 16;                 %   XY Cross-section position, mm
delta   = 15;                       %   half plane window, mm      
xmin = X - delta;                   % Cross-section left edge 
xmax = X + delta;                   % Cross-section right edge
ymin = Y - delta;                   % Cross-section posterior edge
ymax = Y + delta;                   % Cross-section anterior edge
zmin = Z - delta;                   % Cross-section inferior edge
zmax = Z + delta;                   % Cross-section superior edge

%%   Process cross-section data to enable fast (real time) display 
%   This block finds all edges and attached triangles for separate brain
%   compartments. This script is required for subsequent visualizations.
%   Process surface model data
tic
%   Preallocate cell arrays
m_max = length(tissue);
tS = cell(m_max, 1);
nS = tS; %  Reuse this empty cell array for other initialization
eS = tS;
TriPS = tS;
TriMS = tS;
PS = P * 1e3; % Convert to mm
for m = 1:m_max
    tS{m} = t(Indicator == m, :);
    nS{m} = normals(Indicator == m, :);
    [eS{m}, TriPS{m}, TriMS{m}] = mt(tS{m}); 
end
SurfaceDataProcessTime = toc

%   Process observation surface - optional
if exist('roi.mat', 'file')
    ROI         = load('roi.mat');      %   must be in mm
    m_max       = m_max + 1;            %   one more "tissue" added
    tS{m_max}   = ROI.t + size(P, 1);
    PS          = [PS; ROI.P];
    nS{m_max}   = ROI.normals;
    [eS{m_max}, TriPS{m_max}, TriMS{m_max}] = mt(tS{m_max});   
end

%%   Process NIfTI data
%   This block is optional (only if NIfTI data are available)
nifti_filepath = 'Model/T1w.nii';
if exist(nifti_filepath, 'file')
    tic
    V           = niftiread(nifti_filepath);
    info        = niftiinfo(nifti_filepath);
    N1N2N3      = info.ImageSize
    d1d2d3      = info.PixelDimensions
    DimensionX  = d1d2d3(1)*N1N2N3(1);
    DimensionY  = d1d2d3(2)*N1N2N3(2);
    DimensionZ  = d1d2d3(3)*N1N2N3(3);
    NIFTILoadTime = toc
else
    disp('No NIfTI data are available');
end

%%  Figure with planes
figure;
%%  Plot the planes
patch(1e-3*[xmin xmin xmax xmax],1e-3*[ymin ymax ymax ymin], 1e-3*[Z Z Z Z], 'c', 'FaceAlpha', 0.35);
patch(1e-3*[xmin xmin xmax xmax],1e-3*[Y Y Y Y], 1e-3*[zmin zmax zmax zmin], 'c', 'FaceAlpha', 0.35);
patch(1e-3*[X X X X], 1e-3*[ymin ymin ymax ymax], 1e-3*[zmin zmax zmax zmin], 'c', 'FaceAlpha', 0.35);

%%  Head graphics
tissue_to_plot = 'Skin';
t0 = t(Indicator==find(strcmp(tissue, tissue_to_plot)), :);    % (change indicator if necessary: 1-skin, 2-skull, etc.)
str.EdgeColor = 'none'; str.FaceColor = [1 0.75 0.65]; str.FaceAlpha = 1.0; 
bemf2_graphics_base(P, t0, str);

%%  Line graphics
bemf1_graphics_lines(Nx, Ny, Nz, MoveX, MoveY, MoveZ, Target, handle, 'xyz');

%%  General settings
axis 'equal';  axis 'tight';   
daspect([1 1 1]);
set(gcf,'Color','White');
camlight; lighting phong;
view(160, 60);

%%  XY plane
figure;
if exist(nifti_filepath, 'file')
    I = round(Z/d1d2d3(3) + N1N2N3(3)/2);
    S = V(:, :, I)';      %   choose the Z cross-section
    S = S(:, end:-1:1);    
    image([-DimensionX/2 +DimensionX/2], [-DimensionY/2 +DimensionY/2], S, 'CDataMapping', 'scaled');
    colormap gray;
    set(gca, 'YDir', 'normal');    
end
PofXY = cell(m_max, 1);   %   intersection nodes for a tissue
EofXY = cell(m_max, 1);   %   edges formed by intersection nodes for a tissue
TofXY = cell(m_max, 1);   %   intersected triangles
NofXY = cell(m_max, 1);   %   normal vectors of intersected triangles
countXY = [];   %   number of every tissue present in the slice
for m = 1:m_max 
    [Pi, ti, polymask, flag] = meshplaneintXY(PS, tS{m}, eS{m}, TriPS{m}, TriMS{m}, Z);
    if flag % intersection found                
        countXY               = [countXY m];
        PofXY{m}            = Pi;               %   intersection nodes
        EofXY{m}            = polymask;         %   edges formed by intersection nodes
        TofXY{m}            = ti;               %   intersected triangles
        NofXY{m}            = nS{m}(ti, :);     %   normal vectors of intersected triangles        
    end
end
color   = prism(m_max); color(3, :) = [0 1 1];
for m = countXY
    edges           = EofXY{m};             %   this is for the contour
    points          = [];
    points(:, 1)    = +PofXY{m}(:, 1);       %   this is for the contour  
    points(:, 2)    = +PofXY{m}(:, 2);       %   this is for the contour
    patch('Faces', edges, 'Vertices', points, 'EdgeColor', color(m, :), 'LineWidth', 2.0);    %   this is contour plot
end
patch([xmin xmin xmax xmax],[ymin ymax ymax ymin], 'c', 'FaceAlpha', 0.35);
line(X, Y, 'Marker', 'o', 'MarkerFaceColor', 'm', 'MarkerSize', 12);
bemf1_graphics_lines(Nx, Ny, Nz, MoveX, MoveY, MoveZ, Target, handle, 'xy');
xlabel('x, mm'); ylabel('y, mm');
axis 'equal';  axis 'tight'; 
set(gcf,'Color','White');   

%%  XZ plane
figure;
if exist(nifti_filepath, 'file')
    I = round(Y/d1d2d3(2) + N1N2N3(2)/2);
    S = squeeze(V(end:-1:1, I, :))';      %   choose the Y cross-section
    S = S(:, :);
    image([-DimensionX/2 +DimensionX/2], [-DimensionZ/2 +DimensionZ/2], S, 'CDataMapping', 'scaled');
    colormap gray;
    set(gca, 'YDir', 'normal');
end
PofXZ = cell(m_max, 1);   %   intersection nodes for a tissue
EofXZ = cell(m_max, 1);   %   edges formed by intersection nodes for a tissue
TofXZ = cell(m_max, 1);   %   intersected triangles
NofXZ = cell(m_max, 1);   %   normal vectors of intersected triangles
countXZ = [];   %   number of every tissue present in the slice
for m = 1:m_max 
    [Pi, ti, polymask, flag] = meshplaneintXZ(PS, tS{m}, eS{m}, TriPS{m}, TriMS{m}, Y);
    if flag % intersection found                
        countXZ               = [countXZ m];
        PofXZ{m}            = Pi;               %   intersection nodes
        EofXZ{m}            = polymask;         %   edges formed by intersection nodes
        TofXZ{m}            = ti;               %   intersected triangles
        NofXZ{m}            = nS{m}(ti, :);     %   normal vectors of intersected triangles        
    end
end
color   = prism(m_max); color(3, :) = [0 1 1];
for m = countXZ
    edges           = EofXZ{m};              %   this is for the contour
    points          = [];
    points(:, 1)    = +PofXZ{m}(:, 1);       %   this is for the contour  
    points(:, 2)    = +PofXZ{m}(:, 3);       %   this is for the contour
    patch('Faces', edges, 'Vertices', points, 'EdgeColor', color(m, :), 'LineWidth', 2.0);    %   this is contour plot
end
patch([xmin xmin xmax xmax], [zmin zmax zmax zmin], 'c', 'FaceAlpha', 0.35);
line(X, Z, 'Marker', 'o', 'MarkerFaceColor', 'm', 'MarkerSize', 12);
bemf1_graphics_lines(Nx, Ny, Nz, MoveX, MoveY, MoveZ, Target, handle, 'xz');
xlabel('x, mm'); ylabel('z, mm');
axis 'equal';  axis 'tight'; 
set(gcf,'Color','White');

%%  YZ plane
figure;
if exist(nifti_filepath, 'file')
    I = round(-X/d1d2d3(1) + N1N2N3(1)/2); %    minus here!
    S = squeeze(V(I, :, :))';      %   choose the X cross-section
    S = S(:, :);
    image([-DimensionY/2 +DimensionY/2], [-DimensionZ/2 +DimensionZ/2], S, 'CDataMapping', 'scaled');
    colormap gray;
    set(gca, 'YDir', 'normal');
end
PofYZ = cell(m_max, 1);   %   intersection nodes for a tissue
EofYZ = cell(m_max, 1);   %   edges formed by intersection nodes for a tissue
TofYZ = cell(m_max, 1);   %   intersected triangles
NofYZ = cell(m_max, 1);   %   normal vectors of intersected triangles
countYZ = [];   %   number of every tissue present in the slice
for m = 1:m_max 
    [Pi, ti, polymask, flag] = meshplaneintYZ(PS, tS{m}, eS{m}, TriPS{m}, TriMS{m}, X);
    if flag % intersection found                
        countYZ               = [countYZ m];
        PofYZ{m}            = Pi;               %   intersection nodes
        EofYZ{m}            = polymask;         %   edges formed by intersection nodes
        TofYZ{m}            = ti;               %   intersected triangles
        NofYZ{m}            = nS{m}(ti, :);     %   normal vectors of intersected triangles        
    end
end
color   = prism(m_max); color(3, :) = [0 1 1];
for m = countYZ
    edges           = EofYZ{m};              %   this is for the contour
    points          = [];
    points(:, 1)    = +PofYZ{m}(:, 2);       %   this is for the contour  
    points(:, 2)    = +PofYZ{m}(:, 3);       %   this is for the contour
    patch('Faces', edges, 'Vertices', points, 'EdgeColor', color(m, :), 'LineWidth', 2.0);    %   this is contour plot
end
patch([ymin ymin ymax ymax], [zmin zmax zmax zmin], 'c', 'FaceAlpha', 0.35);
line(Y, Z, 'Marker', 'o', 'MarkerFaceColor', 'm', 'MarkerSize', 12);
bemf1_graphics_lines(Nx, Ny, Nz, MoveX, MoveY, MoveZ, Target, handle, 'yz');
xlabel('y, mm'); ylabel('z, mm');
axis 'equal';  axis 'tight'; 
set(gcf,'Color','White');

