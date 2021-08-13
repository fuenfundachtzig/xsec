# xsec
[This repository][1] contains cross sections for high-energy physics.

It currently contains data for the [LHC][2], i.e. proton-proton collisions, at 13 TeV. The values are also given on the [public TWiki pages][3] of the LHC SUSY Cross Section Working Group, where also the scientific references for the tools used to compute the cross sections can be found.

If you would like to contribute by adding more cross sections or in case you find an issue with the cross sections, please get in contact or make a [pull request][4].

[1]: https://github.com/fuenfundachtzig/xsec
[2]: https://home.cern/science/accelerators/large-hadron-collider
[3]: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections
[4]: https://github.com/fuenfundachtzig/xsec/pulls

### Scripts
Several scripts are included in the repository. The most important one is [`plot_xsecs_from_json.py`](plot_xsecs_from_json.py), which gives an example how to make a plot with the cross sections. (Currently it still has a dependence on the `pandas` Python module that could be removed.)

There are also the following helper scripts:
* `make_overview.py`: produces a LaTeX file listing all available cross sections from the `json/` folder
* `make_TWiki_from_json.py`: makes a table in TWiki format


### Fields in JSON files
The cross-section data is stored as JSON files in the folder `json/`.

Physics process:
* `initial state`: 
  * pp = proton-proton collisions
* `Ecom [GeV]`: center-of-mass energy in GeV
* `process_id`: unique ID for process (matches the first two fields of the JSON filename, i.e. e.g. `pp13_slep_L`)
* `process_latex`: process (final state) in LaTeX code
* `PDF set`: PDF set used in computation of cross sections
* `data`: Cross-section data as nested dictionary (i.e. collection of key-value pairs). In our models, we usually consider production of pairs of the same (or degenerate) SUSY particles, i.e. we need only one mass parameter to define the production cross section. In these cases, we have key = mass in GeV, value = dictionary with following entries:
  * `xsec_pb`: cross section in pb
  * `unc_pb`: (symmetric) uncertainty on cross section in pb
  * `unc_up_pb`, `unc_down_pb`: asymmetric upward- and downward uncertainties on cross section in pb
* `parameters`: list of lists specifying the mass parameters used as keys for `data`, following the notation in the [`README`](https://gitlab.cern.ch/atlas-phys-susy-wg/feynmangraphs/) for the (private) git with Feynman diagrams

Additional metadata:
* `tool`: name (and version) of the tool used for computing the cross sections 
* `order`: computational order
* `reference`: citable reference (mostly for tool used to compute the cross sections)
* `comment`: comment on assumptions that were used in the setup / computation of the cross sections
* `source`: where cross-section values have been taken from or are available
* `contact`: contact mail address


### Example plot

The following plot is an example output of [`plot_xsecs_from_json.py`](plot_xsecs_from_json.py):
 
![Plot of various LHC SUSY cross sections at 13 TeV](https://twiki.cern.ch/twiki/pub/LHCPhysics/SUSYCrossSections/SUSY_xsecs_20190729.png "LHC SUSY cross sections at 13 TeV")
