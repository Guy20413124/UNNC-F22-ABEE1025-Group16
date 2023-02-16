from mypackage import FindBest
import numpy

eplus_run_path = './EnergyPlus/energyplus'
idf_path = '/root/cjw/1ZoneUncontrolled_win_test.idf'
output_dir = './result'
epjson_path = "/root/cjw/1ZoneUncontrolled_win_test.epJSON"

######################for SHGC or u_factor change################################
# parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 
# parameter_val_range = [0.25,0.75]

parameter_key = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'u_factor'] 
parameter_val_range = [1.0,2.5]
slice_num = (parameter_val_range[1]-parameter_val_range[0])/20
best_val = parameter_val_range[0]
max_tmp = -100000
for parameter_val in numpy.arange(parameter_val_range[0],parameter_val_range[1]+slice_num,slice_num):
    fd = FindBest(idf_path=idf_path,output_dir=output_dir, epjson_path=epjson_path, eplus_run_path=eplus_run_path,parameter_key = parameter_key)
    if parameter_key[-1]=="'u_factor'":
        fd.u = parameter_val
    else:
        fd.SHGC=parameter_val
    fd.calculate_mean_temperature()
    if fd.MeanTemp>max_tmp:
        max_tmp = fd.MeanTemp
        best_val = parameter_val
print("**************************************\nBest ",parameter_key[-1]," is:",best_val)

