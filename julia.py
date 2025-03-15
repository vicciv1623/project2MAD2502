def get_julia(c:complex, max_iterations:int, z:complex) -> int | None:
  """
  Returns the number of iterations before the complex number following the
  Julia sequence exceeds a magnitude of c

  Input: c for the complex number calling the Julia set, max_iterations determining number of steps until to stop, and z for the complex point to test
  Output: int value for number of iterations until complex number magnitude is greater than the bigger value between 2 and absolute value of c or
            None if magnitude is lower or equal to the bigger value between 2 and absolute value of c even after completing max_iterations
  """
  if abs(z) > max(abs(c),2):
    return 0
  for i in range(max_iterations):
    z=z**2 + c
    if abs(z) > max(abs(c),2):
      return i+1
  return None


def get_julia_color_arr(z_arr: np.ndarray, c:complex, max_iterations: int) -> np.ndarray:
  """returns an nd array with float values pertaining to the escape values of each point in z_arr for a given complex number c
  input: z_arr which is the complex number grid to test
         max_iterations is the int parameter used for calculating the escape time
         c for the complex number calling the Julia set
  output: ndarray which holds the float values which when converted to gray scale will generate
          a Julia image"""
  whole_grid = np.zeros(z_arr.shape)
  row, col = whole_grid.shape
  for i in range(row):
    for j in range(col):
      escape = get_julia(c, max_iterations, z_arr[i,j])
      if escape is None:
        whole_grid[i,j] = 0
      else:
        whole_grid[i,j] = (max_iterations-escape+1) / (max_iterations+1)

  return whole_grid
