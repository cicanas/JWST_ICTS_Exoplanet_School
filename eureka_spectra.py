import os, glob
import eureka.lib.plots
import eureka.S6_planet_spectra.s6_spectra as s6    

# Set up some parameters to make plots look nicer.
# You can set usetex=True if you have LaTeX installed
eureka.lib.plots.set_rc(style='eureka', usetex=False, filetype='.png')
eventlabel = glob.glob('S5*ecf')[0].replace('.ecf','').split('_')[-1]  #Suffice of SX_*.ecf
ecf_path = '.'+os.sep

s6.plot_spectra(eventlabel, ecf_path=ecf_path)
