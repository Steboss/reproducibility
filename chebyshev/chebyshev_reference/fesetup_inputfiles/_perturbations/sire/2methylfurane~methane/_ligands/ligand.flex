version 1
molecule LIG
rigidbody rotate 2.972 translate 0.147
maximumbondvariables 5  
maximumanglevariables 5  
maximumdihedralvariables 5  
bond C1   C2   flex 0.006
bond C1   H7   flex 0.025
bond C1   H8   flex 0.025
bond C1   H9   flex 0.025
bond C2   C3   flex 0.010
bond C2   O6   flex 0.020
bond C3   C4   flex 0.010
bond C3   H10  flex 0.025
bond C4   C5   flex 0.010
bond C4   H11  flex 0.025
bond C5   O6   flex 0.020
bond C5   H12  flex 0.025
angle C1   C2   C3   flex 0.025
angle C1   C2   O6   flex 0.025
angle C2   C1   H7   flex 0.250
angle C2   C1   H8   flex 0.250
angle C2   C1   H9   flex 0.250
angle C2   C3   C4   flex 0.050
angle C2   C3   H10  flex 0.100
angle C2   O6   C5   flex 0.050
angle C3   C2   O6   flex 0.100
angle C3   C4   C5   flex 0.050
angle C3   C4   H11  flex 0.100
angle C4   C3   H10  flex 0.100
angle C4   C5   O6   flex 0.100
angle C4   C5   H12  flex 0.100
angle C5   C4   H11  flex 0.100
angle O6   C5   H12  flex 0.100
angle H7   C1   H8   flex 0.250
angle H7   C1   H9   flex 0.250
angle H8   C1   H9   flex 0.250
dihedral C1   C2   C3   C4   flex 2.500
dihedral C1   C2   C3   H10  flex 2.500
dihedral C1   C2   O6   C5   flex 2.500
dihedral C2   C3   C4   C5   flex 2.500
dihedral C2   C3   C4   H11  flex 2.500
dihedral C2   O6   C5   C4   flex 2.500
dihedral C2   O6   C5   H12  flex 2.500
dihedral C3   C2   C1   H7   flex 10.000
dihedral C3   C2   C1   H8   flex 10.000
dihedral C3   C2   C1   H9   flex 10.000
dihedral C3   C2   O6   C5   flex 2.500
dihedral C3   C4   C5   O6   flex 2.500
dihedral C3   C4   C5   H12  flex 2.500
dihedral C4   C3   C2   O6   flex 2.500
dihedral C5   C4   C3   H10  flex 2.500
dihedral O6   C2   C1   H7   flex 10.000
dihedral O6   C2   C1   H8   flex 10.000
dihedral O6   C2   C1   H9   flex 10.000
dihedral O6   C2   C3   H10  flex 2.500
dihedral O6   C5   C4   H11  flex 2.500
dihedral H10  C3   C4   H11  flex 2.500
dihedral H11  C4   C5   H12  flex 2.500
