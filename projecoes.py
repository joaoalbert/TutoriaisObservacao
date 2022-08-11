import numpy as np

def altaz2uv(alt, az, graus=True):
	'''
	Transforma coordenadas horizontais em coordenadas UV.
	Ideal para visualizar pontos próximos do zênite (alt~90), 
	fica cada vez mais deformado para alt->0.
	Só funciona para pontos localizados em um único hemisfério.
	'''
	if graus:
		alt, az = np.radians(alt), np.radians(az)
	u = np.cos(alt) * np.cos(az)
	v = np.cos(alt) * np.sin(az)
	return u,v
