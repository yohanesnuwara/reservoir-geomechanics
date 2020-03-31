def zobackogram(Sv, Pp, mu):
  import numpy as np
  import matplotlib.pyplot as plt

  # ratio of S1-Pp to S3-Pp
  ratio = (np.sqrt((mu**2) + 1) + mu)**2

  # lower limit of Shmin, from Sv
  Sh = ((Sv - Pp) / ratio) + Pp

  # upper limit of SHmax, from Sv and Pp
  SH = (ratio * (Sv - Pp)) + Pp

  # axes of plot
  Sv_x = np.arange(0, (SH + 10000), 10)
  Sv_y = Sv_x

  plt.figure(figsize=(10,10))

  # plot Sv line and Sv data
  p1 = plt.plot(Sv_x, Sv_y, color='green')
  p2 = plt.plot(Sv, Sv, 'o', color='black')

  # for Normal Faulting (NF) regime
  nf_x = np.array([Sh, Sh, Sv, Sh])
  nf_y = np.array([Sh, Sv, Sv, Sh])
  nf = plt.plot(nf_x, nf_y, color='blue')

  # for Strike Slip (SS) regime
  ss_x = np.array([Sh, Sv, Sv, Sh])
  ss_y = np.array([Sv, Sv, SH, Sv])
  ss = plt.plot(ss_x, ss_y, color='red')

  # for Reverse Faulting (RF) regime
  rf_x = np.array([Sv, Sv, SH, Sv])
  rf_y = np.array([Sv, SH, SH, Sv])
  rf = plt.plot(rf_x, rf_y, color='black')

  plt.legend((p1[0], p2[0], nf[0], ss[0], rf[0]), ['Sv line', 'Sv data', 'Normal Faulting (NF) Polygon', 'Strike Slip (SS) Polygon', 'Reverse Faulting (RF) Polygon'])
  plt.title('Stress Polygons (Zoback-o-gram)')
  plt.xlabel('Shmin (psi)'); plt.ylabel('SHmax (psi)')
  plt.xlim(xmin=0); plt.ylim(ymin=0)
  plt.gca().set_aspect('equal')

  return(p1, p2, nf, ss, rf)
