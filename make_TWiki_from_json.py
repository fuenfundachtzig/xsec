#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Make TWiki table from cross section as JSON.
# 
# (85) 
#
# $Id$



### imports
from __future__ import print_function # for compatibility with Python 2
import os
import json

import pandas as pd


### helpers
 
  
### main


# define datasets (NOTE: files that are commented out do exist and can be used)
filenames = [
  #"pp13_gluino_NNLO+NNLL.json",
  #"pp13_gluinosquark_NNLO+NNLL.json",
  #"pp13_squark_NNLO+NNLL.json",
  #"pp13_stopsbottom_NNLO+NNLL.json",
  ##
  #"pp13_hino_NLO+NLL.json",
  #"pp13_slep_L_NLO+NLL.json",
  #"pp13_slep_R_NLO+NLL.json",
  #"pp13_stau_L_NLO+NLL.json",
  #"pp13_stau_R_NLO+NLL.json",
  #"pp13_wino_C1C1_NLO+NLL.json",
  #"pp13_winom_C1N2_NLO+NLL.json",
  #"pp13_winop_C1N2_NLO+NLL.json",
  #"pp13_winopm_C1N2_NLO+NLL.json",
  ##
  #"pp13_stau_L_NLO+NLL.json",
  #"pp13_stau_R_NLO+NLL.json",
  "pp13_stau_L_NLO+NLL_PDF4LHC.json",
  "pp13_stau_R_NLO+NLL_PDF4LHC.json",
  "pp13_stau_LR_NLO+NLL_PDF4LHC.json",
]


for filename in filenames:
  
  # load
  data = json.load(open(os.path.join("json", filename)))
  df   = pd.DataFrame.from_dict(data["data"], orient = "index")
  # restore mass as column and sort 
  df["mass_GeV"] = df.index.astype(int)
  df = df.sort_values("mass_GeV")
  df.reset_index(inplace = True, drop = True)
  
  # compute fields with percentage uncertainties
  for v in ["", "down_", "up_"]:
    if ('unc_%spb' % v) in df.columns:
      df['unc_%s%%' % v] = df['unc_%spb' % v] / df['xsec_pb']
  
  # write output
  path_out = filename.replace("json", "txt")
  fields = [f for f in ['unc_%', 'unc_down_%', 'unc_up_%'] if f in df.columns]
  
  with open(path_out, "w") as outf:
    #header = " | ".join([field.replace("_pb", " [pb]") for field in fields])
    #print >>outf, "| mass [GeV] | xsec [pb] | %s |" % header
    print("| mass [GeV] | xsec [pb] |", file=outf)
    
    for idx, row in df.iterrows():
      s = " | ".join([("%.1f %%" % (row[field] * 100)) for field in fields]) # FIXME: actually we should round up uncertainties (but then we'd need to treat up and down separately)
      print("| %d | %.4g | %s |" % (row.mass_GeV, row.xsec_pb, s), file=outf)
      
  print("Wrote %s" % path_out)

