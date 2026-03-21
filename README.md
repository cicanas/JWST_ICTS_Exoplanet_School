# JWST ICTS Exoplanet School (March 21, 2026)
Scripts, snippets, and config files for the WJST data reduction section. A lot built upon the work from the 2023 Sagan Summer Workshop and related notebooks (see details [here](https://nexsci.caltech.edu/workshop/2023/)).

# Prepare the workspace
- Download the [WASP-39 data](https://nasa-ext.box.com/shared/static/gmspif7rd12t0vzpquwkv45oezo9mfjy.gz)
- Ensure the *uncal* files are in the **uncalib** folder

# Running Eureka!
The pipeline can be broken into three broad steps with specific python scripts (and combined in the notebook).
1. Generation of light curves (Stages 1-4, *eureka_extraction.py*)
2. Fitting of the light curves (Stage 5, *eureka_fit.py*)
3. Generation of spectra (Stage 6, *eureka_spectra.py*)

# Outputs for Stages 1-4
You should run through all stages to ensure you understand the processing I have executed these codes and, in the interest of time, if you would like to by pass the some of the earlier stages and try binned extractions or light curve fitting then download:
- [Stage 1](https://nasa-ext.box.com/shared/static/lscbe1w2sog18pctfn0pru9o41zel4b0.gz)
- [Stage 2](https://nasa-ext.box.com/shared/static/i3w7k6sdbhz17os3wf739vm0gi3bz2d8.gz)

# Note
Running the full reduction and fits will take hours. This can run on a personal device but may be better suited for a high-performance computing cluster. 

# References
- Slides: https://docs.google.com/presentation/d/1f39cP7r3VrtojDJQdQEtGIekNVe4zilvv-84tgQUqac/edit?usp=sharing
- Search for JWST data: https://mast.stsci.edu/search/ui/#/jwst
- ERS Hackathon: https://ers-transit.github.io/pre-launch-hackathon.html
- jwst pipeline documentation: https://jwst-pipeline.readthedocs.io/en/latest/index.html
- Eureka! documentation: https://eurekadocs.readthedocs.io/en/latest/
- Specific information on the [ERS Program](https://www.stsci.edu/jwst/science-execution/approved-programs/dd-ers/program-1366)
- Programmatic information (observations, APT file, etc.) can be found [here](https://www.stsci.edu/jwst/science-execution/program-information?id=1366)
- JWST Science Publications: https://www.stsci.edu/jwst/science-execution/science-publications
- JWST Technical Documents: https://www.stsci.edu/jwst/documentation/technical-documents
