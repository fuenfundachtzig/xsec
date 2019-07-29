# xsec
[This repository][1] contains cross sections for high-energy physics.

It currently contains data for the [LHC][2], i.e. proton-proton collisions, at 13 TeV. The values are taken from the [public TWiki pages][3] of the LHC SUSY Cross Section Working Group. 

If you would like to contribute by adding more cross sections or in case you find an issue with the cross sections, please get in contact or make a pull request.

[1]: https://github.com/fuenfundachtzig/xsec
[2]: https://home.cern/science/accelerators/large-hadron-collider
[3]: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections

### Scripts
Several scripts are included in the repository. The most important one is [`plot_xsecs_from_json.py`](plot_xsecs_from_json.py), which gives an example how to make a plot with the cross sections. (Currently it still has a dependence on the `pandas` Python module that could be removed.)

There are also the following helper scripts:
* `make_overview.py`: produces a PDF (using LaTeX) listing all available cross sections from the `json/` folder
* `make_TWiki_from_json.py`: makes a table in TWiki format


### Fields in JSON files
The cross-section data is stored as JSON files in the folder `json/`.

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


### Example plot

The following plot is an example output of [`plot_xsecs_from_json.py`](plot_xsecs_from_json.py):
 
![Plot of various LHC SUSY cross sections at 13 TeV](https://twiki.cern.ch/twiki/pub/LHCPhysics/SUSYCrossSections/SUSY_xsecs_20190729.png "LHC SUSY cross sections at 13 TeV")
