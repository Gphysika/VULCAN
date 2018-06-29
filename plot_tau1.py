import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.legend as lg
import vulcan_cfg
try: from PIL import Image
except ImportError: 
    try: import Image
    except: vulcan_cfg.use_PIL = False
import os, sys
import pickle
       
plot_name = 'photosphere'
vul_data = 'output/v618-OH-HD189.vul'
vul_data2 = 'output/test.vul'
#vul_data3 = 'output/scat-E6-new2_CH4_correct_flux_HD189_Moses_nominalKzz.vul'
plot_dir = vulcan_cfg.plot_dir


colors = ['c','b','g','r','m','y','darkblue','orange','pink','grey','darkred','salmon','chocolate','steelblue','plum','hotpink','k']

tex_labels = {'H':'H','H2':'H$_2$','O':'O','OH':'OH','H2O':'H$_2$O','CH':'CH','C':'C','CH2':'CH$_2$','CH3':'CH$_3$','CH4':'CH$_4$','HCO':'HCO','H2CO':'H$_2$CO', 'C4H2':'C$_4$H$_2$',\
'C2':'C$_2$','C2H2':'C$_2$H$_2$','C2H3':'C$_2$H$_3$','C2H':'C$_2$H','CO':'CO','CO2':'CO$_2$','He':'He','O2':'O$_2$','CH3OH':'CH$_3$OH','C2H4':'C$_2$H$_4$','C2H5':'C$_2$H$_5$','C2H6':'C$_2$H$_6$','CH3O': 'CH$_3$O'\
,'CH2OH':'CH$_2$OH','N2':'N$_2$','NH3':'NH$_3$', 'NO2':'NO$_2$','HCN':'HCN','NO':'NO', 'NO2':'NO$_2$' }


with open(vul_data, 'rb') as handle:
  data = pickle.load(handle)
# with open(vul_data2, 'rb') as handle:
#   data2 = pickle.load(handle)
# with open(vul_data3, 'rb') as handle:
#   data3 = pickle.load(handle)

# photosphere
tau1 = 1.


plt.figure()
vulcan_spec = data['variable']['species']

bins = data['variable']['bins']
photosph = []
photosph_abs = []

photosph2 = []
photosph3 = []

for n in range(len(bins)):
    photosph.append( data['atm']['pco'][np.argmin(np.abs(data['variable']['tau'][:,n]-tau1)) ]/1.e6 )
    #photosph_abs.append( data['atm']['pco'][np.argmin(np.abs(data['variable']['tau_abs'][:,n]-tau1)) ]/1.e6 )
    
    #photosph2.append( data2['atm']['pco'][np.argmin(np.abs(data2['variable']['tau'][:,n]-tau1)) ]/1.e6 )
    #photosph3.append( data3['atm']['pco'][np.argmin(np.abs(data3['variable']['tau'][:,n]-tau1)) ]/1.e6 )
    
plt.plot(data['variable']['bins'], photosph, lw=0.5)
#plt.plot(data['variable']['bins'], photosph2, c='g', label='conv:1e-2')
#plt.plot(data['variable']['bins'], photosph3, c='r', label='conv:1e-6')
#plt.plot(data['variable']['bins'], photosph_abs, c='red')
           
plt.gca().set_yscale('log') 
plt.gca().invert_yaxis() 
plt.ylim((1.E3,1.E-8))
plt.xlim((0,900))
plt.legend(frameon=0, prop={'size':12}, loc='best')
plt.xlabel("wavelength (nm)")
plt.ylabel("Pressure (bar)")
plt.savefig(plot_dir + plot_name + '.png')
plt.savefig(plot_dir + plot_name + '.eps')
if vulcan_cfg.use_PIL == True:
    plot = Image.open(plot_dir + plot_name + '.png')
    plot.show()
else: plt.show()

