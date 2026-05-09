import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

producto_punto = np.dot(v1, v2)
producto_cruz = np.cross(v1, v2)

magnitud_v1 = np.linalg.norm(v1)
magnitud_v2 = np.linalg.norm(v2)

v1_normalizado = v1 / magnitud_v1
v2_normalizado = v2 / magnitud_v2

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"Producto punto: {producto_punto}")
print(f"Producto cruz: {producto_cruz}")
print(f"Magnitud de v1: {magnitud_v1}")
print(f"Magnitud de v2: {magnitud_v2}")
print(f"v1 normalizado: {v1_normalizado}")
print(f"v2 normalizado: {v2_normalizado}")
