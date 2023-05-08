# -*- coding :Latin -1 -*

def photosynthesis (CO2, H2O):
    """ This function returns the molecular amounts of glucose, oxygen and water from defined amounts of carbon dioxide and water, from a classical photosynthesis process."""
    global glucose
    glucose = CO2/6
    oxygen = H2O/2
    H2O = H2O/2
    print("This produces", glucose, "molecules of glucose,", oxygen, "molecules of oxygen and", H2O, "molecules of water.")

def glycolysis (glucose):
    """ This function returns the molecular products from defined amounts of glucose, from a classical glycolysis process."""
    print("We assume that", glucose, "molecule(s) of NAD+,", glucose, "molecule(s) of ADP and", glucose, "molecule(s) of inorganic P react with the defined amount of glucose (", glucose, ").")
    global pyruvate    
    pyruvate = glucose*2
    NADH = ATP = H2O = glucose
    print("This produces", pyruvate, "molecules of pyruvate,", NADH, "molecules of NADH,", ATP, "molecules of ATP and", H2O, "molecules of water.")

def lactic_fermentation (pyruvate):
    """ This function returns the molecular products from defined amounts of pyruvate, from a classical lactic acid fermentation."""
    print("We assume that", pyruvate, "molecule(s) of NADH react with the defined amount of pyruvate (", pyruvate, ").")
    lactate = pyruvate
    NAD = pyruvate
    print("This produces", lactate, "molecules of lactate and", NAD, "molecules of NAD.")

def Krebs(pyruvate):
    """ This function returns the molecular products from defined amounts of pyruvate, from a classical Citric acid cycle (Krebs cycle)."""
    AcetylCoA = pyruvate
    print("First,", pyruvate, "molecules of pyruvate produces,", AcetylCoA, "molecules of acetyl-CoA.")
   
 
