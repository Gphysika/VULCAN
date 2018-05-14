import numpy as np
import scipy
import vulcan_cfg
from vulcan_cfg import nz
from chem_funs import ni, nr  # number of species and reactions in the network
import chem_funs

compo = np.genfromtxt(vulcan_cfg.com_file,names=True,dtype=None)
compo_row = list(compo['species'])

for re in range(1,nr+1,2):
    
    reac_atoms, prod_atoms = np.zeros(6), np.zeros(6)
    
    for sp in chem_funs.re_dict[re][0]:        
        # 1:7 for all the atoms (H	O	C	He	N	S)
        reac_atoms += np.array(list(compo[compo_row.index(sp)])[1:7])
            
    for sp in chem_funs.re_dict[re][1]:      
        prod_atoms += np.array(list(compo[compo_row.index(sp)])[1:7])
        
    if not np.all(reac_atoms == prod_atoms):
        print 'For ' + str(re) + ' reaction:\n'
        #raise IOError ('\nElements are not conserved in the reaction. Check the network!')
    
    
#     np.sum([compo[compo_row.index(species[i])][atom] * data_var.y[:,i] for i in range(ni)])
#
#
#
# for atom in self.atom_list:
#     data_var.atom_ini[atom] = np.sum([compo[compo_row.index(species[i])][atom] * data_var.y[:,i] for i in range(ni)])
#
#


        # for i in range(ni):
        #     mu += self.mol_mass(species[i]) * var.ymix[:,i]