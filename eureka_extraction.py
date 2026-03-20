import os, glob
import matplotlib ; matplotlib.use('Agg')
import eureka.lib.plots
import eureka.S1_detector_processing.s1_process as s1
import eureka.S2_calibrations.s2_calibrate as s2
import eureka.S3_data_reduction.s3_reduce as s3
import eureka.S4_generate_lightcurves.s4_genLC as s4

# Set up some parameters to make plots look nicer.
# You can set usetex=True if you have LaTeX installed
eureka.lib.plots.set_rc(style='eureka', usetex=False, filetype='.png')

eventlabel = glob.glob('S1*ecf')[0].replace('.ecf','').split('_')[-1] #Suffice of SX_*.ecf
ecf_path = '.'+os.sep

if __name__ == '__main__':
    s1_meta = s1.rampfitJWST(eventlabel, ecf_path=ecf_path)
    s2_meta = s2.calibrateJWST(eventlabel, ecf_path=ecf_path)
    s3_spec, s3_meta = s3.reduce(eventlabel, ecf_path=ecf_path,
                                 s2_meta=s2_meta)
    s4_spec, s4_lc, s4_meta = s4.genlc(eventlabel, ecf_path=ecf_path,
                                       s3_meta=s3_meta)
