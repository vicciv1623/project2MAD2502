import numpy as np

def get_julia(c:complex, max_iterations:int, z:complex) -> int | None:
  """
  Returns the number of iterations before the complex number following the
  Julia sequence exceeds a magnitude of c

  Input: c for the complex number calling the Julia set
         max_iterations determining number of steps until to stop
         z for the complex point to test
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

def get_complex_grid(top_left:complex, bottom_right:complex, step:float) -> np.ndarray:
  """returns a grid of complex numbers as coordinates, each by a distance of [step]

  input: top_left which is the "beginning" complex number that will located in the top left corner
         bottom_right: which is a complex that specifies the end points of the grid laterally and longitudinally
         step: which is an int that indicates the length of a unit within the grid
  output: an ndarray with complex numbers distanced by a specific distance (step)"""
  width_dist = bottom_right.real - top_left.real
  height_dist = top_left.imag - bottom_right.imag

  width = int(width_dist // step)    #how many units there will be in the grid width-wise
  height = int(height_dist // step)  #how many units there will be in the grid height-wise

  width_side = np.arange(0,width*step+step, step)  #measuring out distances between each unit
  height_side = np.arange(0,height*step+step, step, dtype="complex128")  #measuring out distances between each unit
  height_side *= complex(0,-1)  #height wise, decreases by j from top to bottom 

  grid = width_side + height_side.reshape(height+1,1)
  grid += top_left
  return grid

def get_julia_color_arr(z_arr: np.ndarray, c:complex, max_iterations: int) -> np.ndarray:
  """returns an nd array with float values pertaining to the escape values of each point in z_arr for a given complex number c
  input: z_arr which is the complex number grid to test
         max_iterations is the int parameter used for calculating the escape time
         c for the complex number calling the Julia set
  output: ndarray which holds the float values which when converted to gray scale will generate
          a Julia image"""
  whole_grid = np.zeros(z_arr.shape)
  z=np.zeros(z_arr.shape,dtype=complex)  #beginning of sequence
  not_escaped=np.ones(z_arr.shape,dtype=bool)
  for i in range(max_iterations):
      if i == 0:
        z[not_escaped] = z_arr[not_escaped]  #first term in sequence
      else:
        z[not_escaped] = z[not_escaped]**2 + c    #nth term in sequence
      if_escaped = (np.abs(z) > max(np.abs(c),2)) & not_escaped  
      whole_grid[if_escaped] = i + 1  #updating grid where it escapes
      not_escaped = not_escaped & (if_escaped == False)
  whole_grid[not_escaped] = max_iterations + 1
  color_grid = (max_iterations - whole_grid + 1) / (max_iterations + 1)

  return color_grid
