import ColorPairsCreation

print ("{:<10} {:<10} {:<10}".format('Pair Number','Major Color', 'Minor Color'))
for majorcolor in ColorPairsCreation.MAJOR_COLORS:
  for minorcolor in ColorPairsCreation.MINOR_COLORS:
    pairnumber = ColorPairsCreation.get_pair_number_from_color(majorcolor,minorcolor)
    print ("{:<10} {:<10} {:<10}".format(pairnumber, majorcolor, minorcolor))
