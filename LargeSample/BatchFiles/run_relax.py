import subprocess
path_oommf = 'C:/Users/jmank/Desktop/oommf12b4_20200930_86_x64/oommf/oommf.tcl'
 
mif_file = 'C:/Users/jmank/Desktop/oommf12b4_20200930_86_x64/oommf/Skyrmion/skyrmionDome2.mif'

length = 2
param_string = ' boxsi '#-parameters "integer_length % s" ' % length
threads_string = ' -threads 28 '
oommf_command = 'tclsh ' + path_oommf + param_string + threads_string + mif_file

subprocess.call(oommf_command, shell=True)
