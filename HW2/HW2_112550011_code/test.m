A = [
     4, -1,  0,  0,  0,  0;
    -1,  4, -1,  0,  0,  0;
     0, -1,  4, -1,  0,  0;
     0,  0, -1,  4, -1,  0;
     0,  0,  0, -1,  4, -1;
     0,  0,  0,  0, -1,  4
];

b = [100; 200; 200; 200; 200; 100];
W = 1;

x = gaussian_elimination_band(A, b, W);
disp('Sol x = ');
disp(x);
