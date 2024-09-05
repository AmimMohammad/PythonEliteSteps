
integer=[]
floats=[]
strings=[]
boolean=[]
others=[]


user_Inputs = [86, 81.99, True, 'awzub', {'xzbfc', 'eemkm'}, {'uwyki': 'xksru'}, (62, 80.16), ['dqcgf', True],
               75, 68.6, False, 'xdekc', {'kawbb', 'zibog'}, {'iwyof': 'qskbf'}, (14, 2.33), ['aljyz', True],
               79, 32.96, False, 'rojvt', {'abjzp', 'nndxh'}, {'kecgj': 'ojmkx'}, (1, 81.3), ['onyxy', True],
               84, 11.71, True, 'mweip', {'yhdmd', 'nhhag'}, {'kybix': 'htodj'}, (85, 43.91), ['utrfy', True],
               66, 20.08, True, 'ykzgk', {'lxqmd', 'imshh'}, {'pyigr': 'sjpmm'}, (25, 98.6), ['argli', True],
               18, 23.97, True, 'atplq', {'ggydt', 'vayng'}, {'vipjr': 'hosle'}, (93, 3.71), ['zhnoz', False],
               75, 67.07, False, 'muxwq', {'qtfxb', 'rjfyu'}, {'quvah': 'ixeys'}, (57, 30.89), ['qhdmu', False],
               98, 66.01, False, 'zosil', {'ctfjv', 'bxiuc'}, {'yzkym': 'vvdkh'}, (50, 74.13), ['oxxpt', False],
               73, 46.75, True, 'wkbos', {'viuek', 'paeuq'}, {'cjbyy': 'miimq'}, (92, 65.57), ['wnyly', False],
               65, 64.7, True, 'zhfhm', {'sllsx', 'zvtcw'}, {'tfgcu': 'doepa'}, (45, 65.36), ['fjqxc', True],
               1, 6.47, True, 'iguga', {'lsovy', 'gmscg'}, {'opaou': 'muraw'}, (1, 8.67), ['qthyo', True],
               17, 54.13, True, 'nocwn', {'mrdmv', 'baltu'}, {'ukvnb': 'cobdu'}, (65, 28.38), ['vstsb', True]]

# print(type(user_Inputs[15]))


for inputis in user_Inputs:

    if type(inputis) is int:
        integer.append(inputis)
    elif type(inputis) is str:
        strings.append(inputis)
    elif type(inputis) is bool:
        boolean.append(inputis)
    elif type(inputis) is float:
        floats.append(inputis)
    else:
        others.append(inputis)


print("Integers are :\n")
for x in integer:
    print(x)

print("\n\n\n")

print("Strings are :\n")
for x in strings:
    print(x)

print("\n\n\n")

print("Booleans are :\n")
for x in boolean:
    print(x)

print("\n\n\n")

print("Floats are :\n")
for x in floats:
    print(x)

print("\n\n\n")

print("Others are :\n")
for x in others:
    print(x)

print("\n\n\n")