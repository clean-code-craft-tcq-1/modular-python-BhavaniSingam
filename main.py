import ColorPairsUnittests as cput
if __name__ == '__main__':
  cput.test_number_to_pair(4, 'White', 'Brown')
  cput.test_number_to_pair(5, 'White', 'Slate')
  cput.test_pair_to_number('Black', 'Orange', 12)
  cput.test_pair_to_number('Violet', 'Slate', 25)
  cput.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
