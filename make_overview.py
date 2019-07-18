#!/usr/bin/python
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
  print >>outf, r"""\documentclass[a4paper,10pt]{scrartcl} 
  \usepackage[utf8]{inputenc}
  \begin{document}
"""

  filenames = sorted(glob.glob("json/*.json"))
  print >>outf, r"Found %d JSON files: \begin{itemize}" % len(filenames)
  for filename in filenames:
    data = json.load(open(filename))
    print >>outf, r"\item %s (\texttt{%s})" % (data["process_latex"], StringToLatex(filename))
    print >>outf, r"\begin{itemize}" 
    print >>outf, r"\item %s" % StringToLatex(data["comment"])
    print >>outf, r"\end{itemize}"
    
  print >>outf, r"\end{itemize}\end{document}"
    
        
print "Wrote %s" % path_out

