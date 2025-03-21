#include <iostream>
#include <vector>


#include <iostream>
#include <cmath>
#include <functional>

double f(double t, double x) {
    return -3 * x;
}

double derivef(double t, double x) {
    return -3;
}

double fonctionG(double y, double x, double t, double dt, std::function<double(double, double)> f) {
    return y - x - dt * f(t, y);
}

double Newton(double x0, std::function<double(double, double)> f, int itermax, 
              double epsabs, double epsrel, double t, double dt, double x) {
    double y = x0;
    double fG = fonctionG(y, x, t, dt, f);
    double normeres0 = std::fabs(fG);
    double normeres = normeres0;
    int iter0 = 0;

    while (iter0 < itermax && normeres > epsrel * normeres0 + epsabs) {
        iter0++;
        double deriveG = 1 - dt * derivef(t, y);
        
        if (std::fabs(deriveG) <= std::numeric_limits<double>::epsilon()) {
            std::cout << "La dérivée est nulle" << std::endl;
            break;
        }

        fG = fonctionG(y, x, t, dt, f);
        y = y - fG / deriveG;
        fG = fonctionG(y, x, t, dt, f);
        normeres = std::fabs(fG);
    }

    return y;
}


