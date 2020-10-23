def abv_calculator1():
    og = float(input("What is the original gravity?\n"))
    fg = float(input("What is the final gravity\n"))
    abv = (og-fg) * 131.25
    return abv

#abv = abv_calculator()
#abv = round(abv, 2)
#abv = str(abv)
#print(abv + "% ABV")

#Calculates the ABV based on user input. May have to be rewored a bit to have og and fg pull from a tkinter
#form but this works for testing purposes
def abv_calculator():
    og = float(input("What is the original gravity?\n"))
    fg = float(input("What is the final gravity\n"))
    abv = (og-fg) * 131.25
    abv = round(abv, 2)
    abv = str(abv)
    abv = (abv + "% ABV")
    return abv

#These two equations allow the user to convert Liquid Malt Extract and Dry Malt Extract if they have to substitute.
#They return an int so it can be formatted elsewhere.
def lme_to_dme(lme):
    dme = lme * (36/43)
    dme = int(round(dme, 2))
    return dme
def dme_to_lme(dme):
    lme = dme * (43/36)
    lme = int(round(lme, 2))
    return lme

    


#calculates abv and returns a string like (abv_total%ABV)

def abv_calculator():
    og = float(input("What is the original gravity?\n"))
    fg = float(input("What is the final gravity\n"))
    abv = (og-fg) * 131.25
    abv = round(abv, 2)
    abv = str(abv)
    abv = (abv + "% ABV")
    return abv

#These two equations allow the user to convert Liquid Malt Extract and Dry Malt Extract if they have to substitute.
#They return an int so it can be formatted elsewhere.
def lme_to_dme(lme):
    dme = lme * (36/43)
    dme = int(round(dme, 2))
    return dme
def dme_to_lme(dme):
    lme = dme * (43/36)
    lme = int(round(lme, 2))
    return lme