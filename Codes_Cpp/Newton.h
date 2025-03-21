#include <iostream>
#include <cmath>
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
        
        if (std::abs(deriveG) < 1e-10) {
            std::cout << "La dérivée est trop proche de zéro, méthode arrêtée." << std::endl;
            break;
        }

        y = y - fG / deriveG;
        fG = fonctionG(y, x, t, dt); 
        normeres = std::abs(fG); 
    }

    return y;
}


