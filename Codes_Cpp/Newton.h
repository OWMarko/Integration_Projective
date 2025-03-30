#include <iostream>
#include <cmath>
#include <functional>

// Définition de la fonction f
double f(double t, double x) {
    return -3 * x;
}

// Définition de sa dérivée
double derivef(double t, double x) {
    return -3;
}

// Fonction Newton
double Newton(double x0, double dt, double t, double x, int itermax = 100, 
              double epsabs = 1e-6, double epsrel = 1e-6) {
    double y = x0;
    double normeres0, normeres;

    auto fonctionG = [&](double y) {
        return y - x - dt * f(t, y);
    };

    normeres0 = normeres = std::fabs(fonctionG(y));

    for (int iter = 0; iter < itermax && normeres > epsrel * normeres0 + epsabs; ++iter) {
        double deriveG = 1 - dt * derivef(t, y);

        if (std::abs(deriveG) < 1e-10) {
            std::cout << "La dérivée est trop proche de zéro, méthode arrêtée." << std::endl;
            break;
        }

        y -= fonctionG(y) / deriveG;
        normeres = std::fabs(fonctionG(y));
    }

    return y;
}
