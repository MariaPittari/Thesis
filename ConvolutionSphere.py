import numpy as np
from numpy import cos, sin, arctan, arcsin, pi

# funzione per calcolare i valori di Teta_1 e Phi_1 corrispondenti
# al punto sul piano tangente x_1 e y_1


def get_TetaPhi(phi):

    # implemento le formule 5 e 6 dell'articolo
    # che mi permettono a partire da due valori di teta e di phi
    # del punto di applicazione della convoluzione sulla sfera
    # di calcolare i valori di X e Y sul piano tangente
    # X_0 è sempre 0 e di conseguenza x_1 sarà sempre -1
    y_0 = ((cos(phi) * sin(phi)) - (sin(phi) * cos(phi)) / ((sin(phi) * sin(phi)) + (cos(phi) * cos(phi))))
    x_1 = -1
    y_1 = y_0 -1
    # uso le proiezioni gnomoniche inverse per ottenere i valori
    # di teta e di phi da restituire
    rho = np.sqrt(x_1**2 + y_1**2)
    v = arctan(rho)
    phi_1 = arcsin((cos(v)*sin(phi)) + (y_1*sin(v)*cos(phi)) / rho)
    # theta_0 è sempre 0 quindi non lo metto nell'equazione
    teta_1 = arctan((x_1*sin(v)) / ((rho * cos(phi) * cos(v)) - (y_1 * sin(phi) * sin(v))))
    return [phi_1, teta_1]

# funzione per creare la struttura dati costituita da un vettore 2d di dimensione H,
# in cui vengono memorizzate le coppie Delta_Phi e Delta_Teta, per ogni riga dell'immagine


def create_structure(img):
    # calcolo i valori di h dell'immagine passata come argomento oppure lo passo direttamente
    # come parametro
    h = 32
    step = pi/h
    Delta = np.empty([h, 2])
    phi = pi/2
    for j in range(0, h, 1):
        phi_1, teta_1 = get_TetaPhi(phi)
        deltaPhi = abs(phi - phi_1)
        deltaTeta = abs(teta_1)
        print(phi, deltaPhi, deltaTeta)
        Delta = np.append(Delta, [[deltaPhi, deltaTeta]], axis=0)
        phi = phi - step
    return Delta






