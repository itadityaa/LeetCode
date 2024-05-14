def titleToNumber(self, columnTitle: str) -> int:
  """Solution to the problem of converting a column title to a number

  Args:
      columnTitle (str): The column title to be converted to a number

  Returns:
      int: The number equivalent of the column title
  """  
  dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

  total = 0
  pow = 0
  for ind in range(len(columnTitle) - 1, -1, -1):
      total += ((26**pow)*dict[columnTitle[ind]])
      pow += 1
  return total