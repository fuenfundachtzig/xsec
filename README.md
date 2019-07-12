# xsec
Cross sections for high-energy physics, https://github.com/fuenfundachtzig/xsec

Currently contains data for LHC, i.e. proton-proton collisions, at 13 TeV.

## Fields in JSON files
Cross-section data in stored in JSON files in the folder `json/`. (Currently some fields still need to be filled.)

The script `plot_xsecs_from_json.py` is an example how to plot some of the available cross sections. (Currently it still has a dependence on pandas that could be removed.)

Physics:
* initial state: 
  * pp: proton-proton collisions
* Ecom [GeV]: center-of-mass energy in GeV
* process_id: unique ID for process
* process_latex: process (final state) in LaTeX code
* PDF set:
* data: cross-section data as Python dictionary
  * mass_GeV: mass in GeV
  * xsec_pb: cross section in pb
  * unc_pb: (symmetric) uncertainty on cross section in pb
  * unc_up_pb, unc_down_pb: asymmetric upward- and downward uncertainties on cross section in pb

Other metadata:
* tool: tool name and version
* order: computational order
* reference: citable reference (mostly for tool used to compute the cross sections)
* comment: comment on assumptions that were used to derive the cross sections
* source: where cross-section values have been taken from or are available
* contact: contact mail address
