import subprocess

# path to oommf
path_oommf = '/scratch/user/m0908394/Oommf/oommf/oommf.tcl'
 
# the name of the mif file
mif_file = '/scratch/user/m0908394/Oommf/oommf/Skyrmion/skyrmionDomeTransport2.mif'

#iterate through increasing current densities to find critical current
for current in range(30,41):
# current = 10
    param_string = ' boxsi -parameters "max_current % s" ' % current
    threads_string = ' -threads 28 '
    oommf_command = 'tclsh ' + path_oommf + param_string + threads_string + mif_file

subprocess.call(oommf_command, shell=True)

# Takes about 30 min per run