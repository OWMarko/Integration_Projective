#include "mainwindow.h"
#include <QPushButton>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent) {
    
    setWindowTitle("Aproksi (à reflechir)");

    QWidget *centralWidget = new QWidget(this);
    QVBoxLayout *layout = new QVBoxLayout(centralWidget);

    QPushButton *button1 = new QPushButton("Approximation numérique");
    QPushButton *button2 = new QPushButton("Représentations graphiques");
    QPushButton *button3 = new QPushButton("Cours");
    QPushButton *button4 = new QPushButton("In comming");

    QLabel *logo = new QLabel();
    logo->setPixmap(QPixmap("Application/Images/logo.png")); 
    logo->setAlignment(Qt::AlignRight);

    QLabel *copyright = new QLabel("© 2025 SINADINOVIC Marko - Tous droits réservés");
    copyright->setAlignment(Qt::AlignCenter);

    layout->addWidget(logo);
    layout->addWidget(button1);
    layout->addWidget(button2);
    layout->addWidget(button3);
    layout->addWidget(button4);
    layout->addStretch();
    layout->addWidget(copyright);

    setCentralWidget(centralWidget);
}

MainWindow::~MainWindow() {}
