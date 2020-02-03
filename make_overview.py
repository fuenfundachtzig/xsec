#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Make overview (LaTeX / PDF) of available from cross sections available as JSON.
# 
# Run with:
#   python make_overview.py && pdflatex -interaction=batchmode overview.tex 
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


### helpers
def StringToLatex(s):
  # rudimentary
  s = s.replace("_", "\\_")
  s = s.replace("%", "\%")
  s = s.replace("~", "\~")
  return s

  
### main
path_out = "overview.tex"
with open(path_out, "w") as outf:
  
  print(r"""\documentclass[a4paper,10pt]{scrartcl} 
  \usepackage[utf8]{inputenc}
  \begin{document}""", file=outf)

  filenames = sorted(glob.glob("json/*.json"))
  print("Found %d JSON files in repository:\n\\begin{itemize}" % len(filenames), file=outf)
  for filename in filenames:
    data = json.load(open(filename))
    print(r"\item %s (\texttt{%s})" % (data["process_latex"], StringToLatex(filename)), file=outf)
    print(r"\begin{itemize}", file=outf) 
    print(r"\item %s" % StringToLatex(data["comment"]), file=outf)
    print(r"\end{itemize}", file=outf)
    
  print(r"\end{itemize}\end{document}", file=outf)
            
print("Wrote %s" % path_out)

