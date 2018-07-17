def unit(maxValue):
    rang = range(2, maxValue + 1);
    unitFractions = [];
    for i in rang:
        unitFractions.append(1.0/float(i));
    return unitFractions;

print(unit(11))
