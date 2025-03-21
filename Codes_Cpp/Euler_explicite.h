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
    
    for (int i = 0; i < N; ++i) {
        std::cout << "t[" << i << "] = " << t[i] << ", x[" << i << "] = " << x[i] << std::endl;
    }
}

int main() {
    double x0 = 1.0; // Condition initiale
    double T = 10.0; // Temps total
    int N = 10; // Nombre de points
    
    EulerExplicite(x0, T, N); // Appel de la fonction
    
    return 0;
}
