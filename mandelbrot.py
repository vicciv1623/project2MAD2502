import numpy as np

def get_escape_time(c:complex, max_iterations:int) -> int | None:
  """
  Returns the number of iterations before the complex number following the
  Mandelbrot sequence exceeds a magnitude of 2

  Input: c for starting complex number, and max_iterations determining number of steps until to stop
  Output: int value for number of iterations until complex number magnituded is greater than 2 or
            None if magnitude is lower or equal to 2 even after completing max_iterations
  """
  if abs(c) > 2:
      return 0
  else:
    z_variable=c
    for i in range(max_iterations):
      z_variable = z_variable ** 2 + c
      if abs(z_variable) > 2:
        return i+1
    return None

  
def get_complex_grid(top_left:complex, bottom_right:complex, step:float) -> np.ndarray:
    """returns a grid of complex numbers as coordinates, each by a distance of [step]

    input: top_left which is the "beginning" complex number that will located in the top left corner
            bottom_right: which is a complex that specifies the end points of the grid laterally and longitudinally
            step: which is an int that indicates the length of a unit within the grid
    output: an ndarray with complex numbers distanced by a specific distance (step)"""
    x = int((top_left.imag - bottom_right.imag) / step) #width of grid
    y = int((bottom_right.real - top_left.real) / step)    #height of grid


  

    width_side = np.arange(0,x*step+step, step)  #measuring out distances between each unit
    height_side = np.arange(0,y*step+step, step, dtype="complex128")  #measuring out distances between each unit
    
    height_side *= complex(0,-1)  #height wise, decreases by j from top to bottom 

    grid = width_side + height_side.reshape(y+1,1)
    grid += top_left
    
    return grid

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
  """returns an nd array with float values pertaining to the escape values of c_arr
  input: c_arr which is the complex number grid used to generate mandelbrot image
         max_iterations is the int parameter used for calculating the escape time
  output: ndarray which holds the float values which when converted to gray scale will generate
          a mandelbrot image"""
  whole_grid = np.zeros(c_arr.shape)
  z=np.zeros(c_arr.shape,dtype=complex)   #beginning of sequence
  not_escaped=np.ones(c_arr.shape,dtype=bool)
  for i in range(max_iterations):
      z[not_escaped] = z[not_escaped]**2 + c_arr[not_escaped]
      if_escaped = (np.abs(z) > 2) & not_escaped
      whole_grid[if_escaped] = i + 1        #updating grid where it escapes
      not_escaped = not_escaped & (if_escaped == False)
  whole_grid[not_escaped] = max_iterations + 1
  color_grid = (max_iterations - whole_grid + 1) / (max_iterations + 1)

  return color_grid