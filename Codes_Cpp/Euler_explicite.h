#include <iostream>
#include <vector>
#include <functional>

#include <iostream>
#include <vector>
#include <functional>

std::pair<std::vector<double>, std::vector<double>> eulerExplicite(
    double x0, 
    std::function<double(double, double)> f, 
    double T, 
    int N
) {
    double dt = T / (N - 1);
    std::vector<double> t(N), x(N);
    t[0] = 0;
    x[0] = x0;
    
    for (int k = 1; k < N; ++k) {
        t[k] = k * dt;
        x[k] = x[k-1] + dt * f(t[k-1], x[k-1]);
    }
    
    return {t, x};
}
