def breakout(Sv, Pp, mu, Pm, T0, C0, Wbo):
  import numpy as np
  import matplotlib.pyplot as plt

  # plot zobackogram
  p1, p2, nf, ss, rf = zobackogram(Sv, Pp, mu)

  # ratio of S1-Pp to S3-Pp
  ratio = (np.sqrt((mu**2) + 1) + mu)**2

  # lower limit of Shmin, from Sv
  Sh = ((Sv - Pp) / ratio) + Pp

  # upper limit of SHmax, from Sv and Pp
  SH = (ratio * (Sv - Pp)) + Pp

  # axes of plot
  Sv_x = np.arange(0, (SH + 10000), 10)
  Sv_y = Sv_x

  "Tensile fracture line"
  Sh_line = Sv_x
  SH_tensile = T0 + (3 * Sh_line) - ((2 * Pp) + (Pm - Pp))
  tensile = plt.plot(Sh_line, SH_tensile, '--')

  "Wellbore breakout line"
  SH_breakout = (C0 + (2 * Pp) + (Pm - Pp) - (Sh_line *  (1 + 2 * np.cos(np.deg2rad(180 - Wbo))))) / (1 - 2 * np.cos(np.deg2rad(180 - Wbo)))
  breakout = plt.plot(Sh_line, SH_breakout, '--') 

  plt.legend((p1[0], p2[0], nf[0], ss[0], rf[0], tensile[0], breakout[0]), 
            ['Sv line', 'Sv data', 'Normal Faulting (NF) Polygon', 
              'Strike Slip (SS) Polygon', 'Reverse Faulting (RF) Polygon',
              'Tensile fracture line', 'Wellbore breakout line'])
