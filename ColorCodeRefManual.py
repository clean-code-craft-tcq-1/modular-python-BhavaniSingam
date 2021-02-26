import ColorPairsGetindex
import ColorPairsCreation

print ("{:<10} {:<10} {:<10}".format('Pair Number','Major Color', 'Minor Color'))
for majorcolor in ColorPairsGetindex.MAJOR_COLORS:
  for minorcolor in ColorPairsGetindex.MINOR_COLORS:
    pairnumber = ColorPairsCreation.get_pair_number_from_color(majorcolor,minorcolor)
    print ("{:<10} {:<10} {:<10}".format(pairnumber, majorcolor, minorcolor))
