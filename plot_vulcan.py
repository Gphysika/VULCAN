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


# Setting the 2nd input argument as the filename of vulcan output   
vul_data = sys.argv[1]
# Setting the 3rd input argument as the species names to be plotted (separated by ,)
plot_spec = sys.argv[2]
# Setting the 4th input argument as the output eps filename        
plot_name = sys.argv[3]

plot_dir = vulcan_cfg.plot_dir

# taking user input species and splitting into separate strings and then converting the list to a tuple
plot_spec = tuple(plot_spec.split(','))
nspec = len(plot_spec)

colors = ['c','b','g','r','m','y','k','orange','pink','grey','darkred','darkblue','salmon','chocolate','steelblue','plum','hotpink']

tex_labels = {'H':'H','H2':'H$_2$','O':'O','OH':'OH','H2O':'H$_2$O','CH':'CH','C':'C','CH2':'CH$_2$','CH3':'CH$_3$','CH4':'CH$_4$','HCO':'HCO','H2CO':'H$_2$CO', 'C4H2':'C$_4$H$_2$',\
'C2':'C$_2$','C2H2':'C$_2$H$_2$','C2H3':'C$_2$H$_3$','C2H':'C$_2$H','CO':'CO','CO2':'CO$_2$','He':'He','O2':'O$_2$','CH3OH':'CH$_3$OH','C2H4':'C$_2$H$_4$','C2H5':'C$_2$H$_5$','C2H6':'C$_2$H$_6$','CH3O': 'CH$_3$O'\
,'CH2OH':'CH$_2$OH'}


with open(vul_data, 'rb') as handle:
  data = pickle.load(handle)

color_index = 0
vulcan_spec = data['variable']['species']
for sp in plot_spec:
    if color_index == len(colors): # when running out of colors
        colors.append(tuple(np.random.rand(3)))
    plt.plot(data['variable']['ymix'][:,vulcan_spec.index(sp)], data['atm']['pco']/1.e6, color=colors[color_index], label=tex_labels[sp])
    color_index +=1
      
plt.gca().set_xscale('log')       
plt.gca().set_yscale('log') 
plt.gca().invert_yaxis() 
plt.xlim((1.E-20, 1.))
plt.ylim((1.E3,1.E-4))
plt.legend(frameon=0, prop={'size':12}, loc='best')
plt.xlabel("Mixing Ratio")
plt.ylabel("Pressure (bar)")
plt.savefig(plot_dir + plot_name + '.png')
plt.savefig(plot_dir + plot_name + '.eps')
if vulcan_cfg.use_PIL == True:
    plot = Image.open(plot_dir + plot_name + '.png')
    plot.show()
else: plt.show()

