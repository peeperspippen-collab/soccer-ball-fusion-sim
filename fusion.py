  # import numpy as np import matplotlib.pyplot     
  # import matplotlib.pyplot as plt r_ball = 0.10
 # 10 cm radius (full diameter 20 cm) faces = 12 np.ones(12) + 20 np.ones(20)
 # pentagons + hexagons
 # magnet coils (4 total, curved arcs) coil_arc = np.pi / 12
 # 15° each theta = np.linspace(-coil_arc, coil_arc, 50) r_coil = 0.05
 # 50 mm wide coil_x = r_ball np.cos(theta) coil_y = r_ball np.sin(theta) np.ones_like(theta)
 # plasma ring (2 cm dia, center) r_plasma = 0.01 theta_plasma = np.linspace(0, 2 np.pi, 100) x_plasma = r_plasma np.cos(theta_plasma) y_plasma = r_plasma np.sin(theta_plasma)
# field lines (simple toroidal wrap) B = 1.0
# tesla at center omega = 1885
# 18000 RPM in rad/s field_x = [] field_y = [] for t in np.linspace(-np.pi, np.pi, 50): for r in np.linspace(r_plasma 0.9, r_plasma 1.1, 5): x = r np.cos(t) y = r np.sin(t) + r_ball np.sin(0.5 t)
 # slight bulge field_x.append(x) field_y.append(y)
# plot plt.figure(figsize=(8,8)) plt.plot(coil_x, coil_y, ‘c-’, lw=4, label=‘Coils’) plt.plot(x_plasma, y_plasma, ‘r-’, lw=3, label=‘Plasma’) plt.plot(field_x, field_y, ‘b-’, alpha=0.6, label=‘B-field’) plt.axis(‘equal’) plt.title(‘Soccer Ball Reactor - 10 kW @ 18k RPM’) plt.legend() plt.show()
