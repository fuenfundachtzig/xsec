#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Make overview (LaTeX / PDF) of available from cross sections available as JSON.
# 
# Run with:
#   python make_overview.py && pdflatex -interaction=batchmode overview.tex
# Or with latex-make:
#   python make_overview.py && latexmk --pdf overview.tex
# 
#   
# Produces 
#   overview.pdf
# 
# (85) 
#
# $Id$



### imports
from __future__ import print_function # for compatibility with Python 2
import os
import glob
import json
import pandas as pd


### helpers
def StringToLatex(s):
  # rudimentary
  s = s.replace("_", "\\_")
  s = s.replace("%", "\%")
  s = s.replace("~", "\~")
  return s


def LoadXsecJSONAsDF(jsondata):
  
  # convert to pandas.DataFrame
  df   = pd.DataFrame.from_dict(jsondata["data"], orient = "index")
  
  # restore mass as column and sort 
  df["mass_GeV"] = df.index.astype(int)
  df = df.sort_values("mass_GeV")
  df.reset_index(inplace = True, drop = True)
  
  # compute fields with percentage uncertainties
  for v in ["", "down_", "up_"]:
    if ('unc_%spb' % v) in df.columns:
      df['unc_%s%%' % v] = df['unc_%spb' % v] / df['xsec_pb'] * 100
  
  return df

  
### main
path_out = "overview.tex"
with open(path_out, "w") as outf:
  
  # header
  print(r"""\documentclass[a4paper,10pt]{scrartcl}
    \usepackage[utf8]{inputenc}
    \usepackage{booktabs}
    \usepackage{longtable}
    \usepackage{hyperref}
    \hypersetup{
      colorlinks=true,
      linkcolor=blue
    }
    \begin{document}
    \section{Descriptions}
    """, file=outf)

  filenames = sorted(glob.glob("json/*.json"))
  print("Found %d JSON files in repository:\n\\begin{itemize}" % len(filenames), file=outf)
  
  # overview
  for idx, filename in enumerate(filenames):
    data = json.load(open(filename))
    print(r"\item %s (\texttt{%s})" % (data["process_latex"], StringToLatex(filename)), file=outf)
    print(r"\begin{itemize}", file=outf) 
    print(r"\item %s" % StringToLatex(data["comment"]), file=outf)
    print(r"\item see section \ref{tab:xsec%d}" % idx, file=outf)
    print(r"\end{itemize}", file=outf)
    
  print(r"\end{itemize}\section{Tables}", file = outf)
  
  # tables
  for idx, filename in enumerate(filenames):
    data = json.load(open(filename))
    print(r"\subsection{Cross sections for %s}\label{tab:xsec%d}" % (data["process_latex"], idx), file = outf)
    try:
      df = LoadXsecJSONAsDF(data)
    except Exception as e:
      print("Failed to convert data from %s (%s)" % (filename, str(e)))
      print(r"(Failed to read data.)", file = outf)
      continue
    
    print(r"""\begin{longtable}{ccc}
      \toprule 
      Mass [GeV] & cross section [pb] & uncertainty [\%] \\
      \midrule\endhead""", file = outf)
    for idx, row in df.iterrows():
      uncs = "[unknown]"
      if row.get("unc_%") is not None:
        uncs = "$\pm$%.1f" % row.get("unc_%")
      elif row.get("unc_down_%") is not None:
        uncs = "-%.1f / +%.1f" % (row.get("unc_down_%"), row.get("unc_up_%"))
      print(r"%s & %g & %s \\" % (row.mass_GeV, float(row.xsec_pb), uncs), file=outf)
    print(r"\bottomrule\end{longtable}", file = outf)
  
  
  # footer
  print(r"\end{document}", file=outf)
            
print("Wrote LaTeX output to %s" % path_out)

