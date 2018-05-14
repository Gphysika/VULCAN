# ============================================================================= 
# Configuration file of VULCAN:  
# ============================================================================= 

# ====== Providing some default sets for quick runs ======
# e.g. NCHO with/without photochemistry
# after setting, automatically choose the default network


# ====== Setting up the elements included in the network ======
atom_list = ['H', 'O', 'C', 'He', 'N']
# ====== Set up paths and filenames for the input and output files  ======
network = 'thermo/NCHO_photo_network.txt'
gibbs_text = 'thermo/gibbs_text.txt'
# all the nasa9 files must be placed in the folder: thermo/NASA9/
cross_folder = 'thermo/leiden_cross/'
com_file = 'thermo/all_compose.txt'
atm_file = 'atm/atm_HD189_Kzz.txt'
sflux_file = 'atm/VPL_solar.txt' # HD189_Moses11.txt #VPL_solar.txt # This is the flux at the stellar surface
top_BC_mix_file = 'atm/BC_top.txt'
bot_BC_mix_file = 'atm/BC_bot.txt'
vul_ini = 'output/test.vul'
output_dir = 'output/'
plot_dir = 'plot/'
out_name =  'HD189-test.vul' #'from2nm-noC2H2-photo_Moses_HD189_nominalKzz.vul' #'photo_NCHO_Moses_HD189_nominalKzz.vul'
# storing data for every 'out_y_time_freq' step  
out_y_time_freq = 10 


# ====== Setting up the photochemistry ======
use_photo = True
excit_sp = ['O_1', 'CH2_1'] # N_D to avoid in the initial abundances by fc
scat_sp = ['H2', 'He'] #['H2', 'He'] # the molecules that contribute to Rayleigh scattering
r_star = 0.752 #0.752 HD209: 1.118
orbit_radius = 0.03142 #0.03142 # planet-star distance in A.U.
sl_angle = 48 /180.*3.14159 # the zenith angle of the star   
dbin = 0.1

# ====== Setting up the elemental abundance ======
use_solar = False # if False, using the customized elemental abundance
# default: solar abundance (from Table 10. K.Lodders 2009)

# customized elemental abundance
O_H = 6.0618E-4 *(0.793) #*1000.
C_H = 2.7761E-4 #*1000.
N_H = 8.1853E-5 #*1000.
He_H = 0.09691

 
ini_mix = 'fc' # 'fc 'const_lowT', 'fc_precal' 'vulcan_ini'
# for 'vul_ini, the T-P grids have to be exactly the same


# ====== Reactions to be switched off  ======
remove_list = [] # in pairs e.g. [1,2]
#remove_list = list(range(1,621))

# ====== Setting up parameters for the atmosphere ======
atm_base = 'H2' # the bulk gas of the atmosphere: changes molecular diffsion and some 3-body reactions
nz = 100
use_Kzz = True
use_moldiff = 0
use_fix_bot_no_moldiff = False
use_topflux = False
use_botflux = False  

atm_type = 'file' # 'isothermal', 'analytical', or 'file'
Kzz_prof = 'file' # 'const' or 'file'
g = 2140.         # HD189:2140  HD209:936 # (cm/s^2)
Tiso = 2900.
# T_int, T_irr, ka_L, ka_S, beta_S, beta_L
para_cool2 = [90.,  1000., 0.04, 0.01, 1., 1.]
para_warm = [120., 1500., 0.1, 0.02, 1., 1.]
para_hot3 = [200., 2800., 0.05, 0.15, 1., 1.]
para_anaTP = para_hot3

const_Kzz = 1.E12 # (cm^2/s)
P_b = 1.E9 #(dyne/cm^2)
P_t = 1.E-2

  
# ====== Setting up general parameters for the ODE solver ====== 
ode_solver = 'Ros2' # case sensitive
use_print_prog = True
use_height = False
print_prog_num = 200
use_live_plot = 1
use_live_flux = 0
use_save_movie = 0
use_flux_movie = 0
live_plot_frq = 10
use_plot_end = True
use_plot_evo = False
plot_TP = 1
output_humanread = False
plot_spec = ['H', 'H2', 'CH3', 'CH4', 'CO', 'CH3OH', 'CH2OH', 'He']
# live_plot_spec = ['H', 'H2', 'H2O', 'CH4', 'CO', 'CO2', 'C2H2', 'C2H4', 'C2H6', 'CH3OH']
live_plot_spec = ['H', 'H2O', 'CH4', 'CO', 'CO2', 'C2H2', 'NH3', 'HCN']
# frequency to update the flux and tau
ini_update_photo_frq = 20 #10
final_update_photo_frq = 5
update_frq = 100 # for updating dz and dzi due to change of mu

# ====== steady state check ======
st_factor = 0.5  
# Try larger st_factor when T < 1000K
count_min = 120

# ====== Setting up numerical parameters for the ODE solver ====== 
dttry = 1.E-10
dt_std = 1.
trun_min = 1e2
runtime = 1.E24
dt_min = 1.E-14
dt_max = runtime*0.01
dt_var_max = 2.
dt_var_min = 0.5
atol = 1. #1.E-3
mtol = 1.E-20
mtol_conv = 1.E-20
pos_cut = 0
nega_cut = -1.
loss_eps = 1e-1
yconv_cri = 0.01 #0.01 # for checking steady-state
slope_cri = 1.e-4
yconv_min = 0.1
# slope_min defined in conv()
# slope_min = 1.e-10
flux_cri = 1.e-2  #0.1
flux_atol = 1. # the tol for actinc flux (# photons cm-2 s-1 nm-1)

count_max = int(1E5)

# ====== Setting up numerical parameters for Ros2 ODE solver ====== 
rtol = 0.05

# ====== Setting up numerical parameters for SemiEu/SparSemiEU ODE solver ====== 
PItol = 0.1

use_PIL = True