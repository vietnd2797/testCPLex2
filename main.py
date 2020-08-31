import numpy as np
from docplex.mp.model import Model

#n = 5
#m = 7
#N = np.arange(0, n+1)
#M = np.arange(0, m+1)

#E = [(i, j) for i in N for j in N if i < j] 
#E_ext = [(i,j,t) for i in N for j in N if i < j for t in M ]
#iterators = [(i,t) for i in N for t in M]
#print(E)


#mod = Model(name = 'test')
#mod.integer_var_dict(E_ext, name='y')
#mod.integer_var_dict(iterators, name='z')

# first import the Model class from docplex.mp
from docplex.mp.model import Model

# create one model instance, with a name
m = Model(name='telephone_production')

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
desk = m.continuous_var(name='desk')
cell = m.continuous_var(name='cell')

# write constraints
# constraint #1: desk production is greater than 100
m.add_constraint(desk >= 100)

# constraint #2: cell production is greater than 100
m.add_constraint(cell >= 100)

# constraint #3: assembly time limit
ct_assembly = m.add_constraint( 0.2 * desk + 0.4 * cell <= 400)

# constraint #4: paiting time limit
ct_painting = m.add_constraint( 0.5 * desk + 0.4 * cell <= 490)

m.maximize(12 * desk + 20 * cell)

#m.print_information()
m.solve()

m.print_solution()


