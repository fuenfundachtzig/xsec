#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Example script to create a plot of cross sections from data in JSON format.
# 
# External requirements (Python modules):
# 
#   pandas (https://pandas.pydata.org/)
#   matplotlib (https://matplotlib.org/)
# 
# Run with:
# 
#   python plot_xsecs_from_json.py
# 
# (85) 
#
# $Id: plot_xsecs_from_json.py 3190 2019-05-28 17:21:31Z eis $



### imports
import os
import json

import pandas as pd
import matplotlib.pyplot as plt


### helpers
def PlotXsec(df, label):
  plt.yscale("log")
  baseline = plt.plot(df.mass_GeV, df.xsec_pb, label = label)
  # check which uncertainty type we have
  if "unc_up_pb" in df.columns:
    # asymmetric
    plt.fill_between(df.mass_GeV, df.xsec_pb - df.unc_down_pb, df.xsec_pb + df.unc_up_pb, alpha = 0.2, facecolor = baseline[0].get_color(), linewidth=0)
  else:
    # assume symmetric always present
    plt.fill_between(df.mass_GeV, df.xsec_pb - df.unc_pb     , df.xsec_pb + df.unc_pb   , alpha = 0.2, facecolor = baseline[0].get_color(), linewidth=0)
 
  
### main

# init plotting
plt.ion()
use_latex = False
if use_latex:
  plt.rc('text', usetex=True)
  plt.rc('font', size=18)
  plt.rc('legend', fontsize=14)
  plt.rc('text.latex', preamble=r'\usepackage{cmbright}')
else:
  plt.rcParams.update({'font.size': 10})

# define datasets (NOTE: files that are commented out do exist and can be used)
filenames = [
  "pp13_gluino_NNLO+NNLL.json",
  "pp13_gluinosquark_NNLO+NNLL.json",
  "pp13_squark_NNLO+NNLL.json",
  "pp13_stopsbottom_NNLO+NNLL.json",
  ##
  #"pp13_hino_NLO+NLL.json",
  #"pp13_slep_L_NLO+NLL.json",
  #"pp13_slep_R_NLO+NLL.json",
  #"pp13_wino_C1C1_NLO+NLL.json",
  #"pp13_winom_C1N2_NLO+NLL.json",
  #"pp13_winop_C1N2_NLO+NLL.json",
  #"pp13_winopm_C1N2_NLO+NLL.json",
]

# load data and plot
for filename in filenames:
  print filename
  data = json.load(open(os.path.join("json", filename)))
  df   = pd.DataFrame.from_dict(data["data"]).sort_values("mass_GeV")
  PlotXsec(df, data["process_latex"])

# draw legend and style plot
plt.xlabel("particle mass [GeV]")
plt.ylabel("cross section [pb]")
plt.grid()
plt.xlim(0, 3000)
plt.ylim(1e-7, 1e3)
plt.legend(ncol = 2, framealpha = 1)
plt.locator_params(axis = "y", base = 100) # for log-scaled axis, it's LogLocator, not MaxNLocator
#plt.title("$pp$, $\sqrt{s} = 13$ TeV, NLO+NLL - NNLO$_\mathregular{approx}$+NNLL", fontsize = 9, loc = "right")
plt.title("$pp$, $\sqrt{s} = 13$ TeV, NLO+NLL", fontsize = 9, loc = "right")
plt.savefig("SUSY_xsecs.pdf")


