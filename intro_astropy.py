'''
Referêcias:
https://docs.astropy.org/en/stable/coordinates/
https://learn.astropy.org/tutorials/2-Coordinates-Transforms.html
'''

import matplotlib.pyplot as plt
import numpy as np

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, Distance, EarthLocation, AltAz, get_sun

ra1 = 30*u.deg
dec1 = 30*u.deg
print("Primeiro objeto:")
obj1 = SkyCoord(ra=ra1, dec=dec1)

print(obj1)
print("RA:")
print(obj1.ra)
print("RA em deg:")
print(obj1.ra.degree)
print("RA em horas:")
print(obj1.ra.hour)
print("Dec em string:")
print(obj1.to_string("hmsdms"))

print("\nRelacionando Referenciais")
print("FK5:")
print(obj1.transform_to("fk5"))


obj2_name = "PSR J1012+5307"
print("\nSelecionando objetos por nome. Objeto {}".format(obj2_name))
obj2 = SkyCoord.from_name(obj2_name)
print(obj2)

print("\nSelecionando localizações na Terra:")
loc1_lon = -35.908276*u.deg
loc1_lat =  -7.211803*u.deg
loc1 = EarthLocation.from_geodetic(lon=loc1_lon, lat=loc1_lat)
print(loc1)

print("\nSelecionando datas para obsevação:")
fuso_brasil = -3*u.hour
data = "2022-08-05 11:00" # Tempo deve ser dado em UTC. Lembrando que BRT = UTC-3h
data_obs = Time(data)
print("Dia e hora (UTC):")
print(data_obs)

# np.arange(start, stop, step) # nao inclui o stop
# np.linspace(start, stop, numero) # inclui o stop
print("Dia e hora (BRT):")
print(data_obs+fuso_brasil) #datetime
time_grid = data_obs + np.linspace(0,24, 24*60+1)*u.hour
time_grid_fuso = (time_grid+fuso_brasil).datetime

print("\nVerficando movimento aparente:")
alt_az = AltAz(location=loc1, obstime=time_grid)
obj2_altaz = obj2.transform_to(alt_az)
print(obj2_altaz)


plt.figure(0)
plt.title("Observação Local para {}".format(obj2_name))
plt.plot(time_grid_fuso, obj2_altaz.alt.degree, label=obj2_name)
plt.plot(time_grid_fuso, np.zeros(len(time_grid_fuso)), c="r", label="Horizonte")
plt.ylim(-90,90)
plt.xlabel("Tempo (mm-dd hh)")
plt.ylabel("Altura (deg)")
plt.legend()

plt.figure(1)
# Mudando de 0 a 360 para -180 a 180
az_max = 180
az_min = az_max-360
az_rescale = [az if az<az_max else az-360 for az in obj2_altaz.az.degree]
plt.title("Movimento Aparente Local para {}".format(obj2_name))
plt.plot(az_rescale, obj2_altaz.alt.degree, label=obj2_name)
plt.plot(np.linspace(az_min, az_max, 100), np.zeros(100), c="r", label="Horizonte")
plt.ylim(-90,90)
plt.xlim(az_min, az_max)
plt.xlabel("Azimute (deg)")
plt.ylabel("Altura (deg)")
plt.legend()

print("\nBuscando Posição do Sol:")
sun = get_sun(data_obs)
print(sun)
sun_coords = get_sun(time_grid)
sun_altaz = sun_coords.transform_to(alt_az)


print("\nEncontrando hora aproximada de culminacao superior")
# Ex.:
# alt  = [0, 10, 20, 30, 35, 30, 20, 10, 0]
# time = [8, 09, 10, 11, 12, 11, ...]
culminacao_sup_idx = np.argmax(sun_altaz.alt.degree)
culminacao_sup_hora = time_grid_fuso[culminacao_sup_idx]
print(culminacao_sup_hora)

plt.figure(2)
plt.title("Observação Local para o Sol")
plt.plot(time_grid_fuso, sun_altaz.alt.degree, label="Sol", c="orange")
plt.plot(time_grid_fuso, np.zeros(len(time_grid_fuso)), c="r", label="Horizonte")
plt.ylim(-90,90)
plt.xlabel("Tempo (mm-dd hh)")
plt.ylabel("Altura (deg)")
plt.legend()

plt.show()

