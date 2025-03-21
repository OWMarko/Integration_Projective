#include <iostream>
#include <vector>

void EulerExplicite(double x0, double T, int N) {
    double dt = T / (N - 1); 
    std::vector<double> t(N), x(N); 
    
    t[0] = 0; 
    x[0] = x0; 
    
    for (int k = 1; k < N; ++k) {
        t[k] = t[k - 1] + dt; 
        x[k] = x[k - 1] + dt * (-x[k - 1]); 
    }
