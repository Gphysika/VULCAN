# ============================================================================= 
# Configuration file of VULCAN:  
# ============================================================================= 

# ====== Set up paths and filenames for the input and output files  ======
network = 'thermo/NCHO_network.txt'  
gibbs_text = 'thermo/gibbs_text.txt'
# all the nasa9 files must be placed in the folder: thermo/NASA9/
com_file = 'thermo/all_compose.txt'
atm_file = 'atm/atm_HD189.txt'
top_BC_mix_file = 'atm/BC_top.txt'

output_dir = 'output/'
plot_dir = 'plot/'
out_name = 'test.vul'
# storing data for every 'out_y_time_freq' step  
out_y_time_freq = 10 

# ====== Setting up the elemental abundance ======
use_solar = False
atom_list = ['H', 'O', 'C', 'He', 'N']
# default: solar abundance (from Table 10. K.Lodders 2009)
O_H = 6.0618E-4 *(0.793) 
C_H = 2.7761E-4 
N_H = 8.1853E-5 
He_H = 0.09691

ini_mix = 'fc'   # or 'CH4 and N2'  

# ====== Reactions to be switched off  ======
remove_list = []

# ====== Setting up parameters for the atmosphere ======
nz = 60
use_Kzz = True
atm_type = 'file' # 'isothermal', 'analytical', or 'file'
Kzz_prof = 'const' # 'const' or 'file'
Tiso = 1000.
# T_int, T_irr, ka_L, ka_S, beta_S, beta_L
hat26 = [100., 1200., 0.01 *1.2, 0.001 *0.8, 1., 1.]
gj436 = [200., 1000., 0.01 *1.2, 0.001 *0.8, 1., 1.]
para_cool = [100., 1100., 0.04, 0.01, 1., 1.]
para_warm = [120., 1500., 0.1, 0.02, 1., 1.]
para_hot = [200., 2650., 0.05, 0.15, 1., 1.]       
para_anaTP = gj436

const_Kzz = 1.E9 # (cm^2/s)
g = 2140 # (cm/s^2)
P_b = 1.E9 #(dyne/cm^2)
P_t = 1.E1  

use_fix_bot = False
use_topflux = False # setting constant flux (from top_BC_mix_file) as the top BC

# ====== Setting up general parameters for the ODE solver ====== 
ode_solver = 'Ros2' # case sensitive
use_print_prog = True
print_prog_num = 200
use_live_plot = True
live_plot_frq = 10
use_plot_end = True
use_plot_evo = False
plot_TP = 1
output_humanread = False
plot_spec = ['H', 'H2', 'CH3', 'CH4', 'C2H2', 'CO', 'CH3OH', 'CH2OH', 'He']
live_plot_spec = ['H', 'H2O', 'CH4', 'CO', 'CO2', 'N2', 'NH3', 'HCN', 'C2H2']  

# ====== steady state check ======
st_factor = 0.5  
# Try larger st_factor when T < 1000K
count_min = 100

# ====== Setting up numerical parameters for the ODE solver ====== 
dttry = 1.E-8
dt_std = 1.
trun_min = 1e2
runtime = 1.E18
dt_min = 1.E-14
dt_max = runtime*0.01
dt_var_max = 2.
dt_var_min = 0.2
atol = 1.E-3
mtol = 1.E-24
mtol_conv = 1.E-20
pos_cut = 0
nega_cut = -1.
loss_eps = 1e-1
yconv_cri = 0.01 # for checking steady-state
slope_cri = 1.e-4

yconv_min = 0.1
slope_min = 1.e-10

count_max = int(5E4)
update_frq = 100 # for updating dz and dzi due to change of mu

# ====== Setting up numerical parameters for Ros2 ODE solver ====== 
rtol = 0.05

# ====== Setting up numerical parameters for SemiEu/SparSemiEU ODE solver ====== 
PItol = 0.1

use_PIL = True