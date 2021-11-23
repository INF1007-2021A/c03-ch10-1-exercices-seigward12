#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)

def repartir_valeur():
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(i[0]**2 + i[1]**2), np.arctan2(i[1]/i[0])) for i in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.argmin((abs(values - number)))

def graph(x_lim_L, x_lim_R, points):
    x = np.linspace(x_lim_L, x_lim_R, num=points)
    y = x**2 * np.sin(1/x**2) + x
    plt.scatter(x,y)
    plt.xlim(x_lim_L, x_lim_R)
    plt.show()


def monte_carlo():

    points = {'x_inter':[], 'x_exter':[], 'y_inter':[], 'y_exter':[]}
    for i in range(5000):
        x = np.random.random()
        y = np.random.random()
        if np.sqrt(x**2 + y**2) < 1:
            points['x_inter'].append(x)
            points['y_inter'].append(y)
        else:
            points['x_exter'].append(x)
            points['y_exter'].append(y)

    plt.scatter(points['x_inter'], points['y_inter'])
    plt.scatter(points['x_exter'], points['y_exter'])
    plt.show()
    return len(points['x_inter']) / 5000 *4



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(repartir_valeur())
    #print(coordinate_conversion(np.ndarray(1,2)))
    print(find_closest_index(np.arange(-10,10), 4.3))
    graph(-1,1,250)
    print(monte_carlo())
    
