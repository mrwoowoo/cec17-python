import numpy as np
import ctypes 
import os
import platform

if platform.system().lower() == 'windows':
	cec17_object = ctypes.cdll.LoadLibrary(path.abspath(os.path.join(os.path.dirname(__file__), "cec17.dll")))
else:
	cec17_object = ctypes.cdll.LoadLibrary(path.abspath(os.path.join(os.path.dirname(__file__), "cec17.so")))

cec17_fun = cec17_object.cec17_test_func
def cec17(x, fun_nums):
	rows, cols = x.shape
	x = np.ravel(x)
	x = (ctypes.c_double * x.size)(*x)
	f = (ctypes.c_double * rows)()
	cec17_fun(x, f, cols, rows, fun_nums)
	f = np.array(f)
	return f

if __name__ == '__main__':
	x = np.array([[0, 0]])
	print(x, cec17(x, 1))
	x = np.array([[-5.5276398498228005e+01, -7.0429559718086182e+01]])
	print(x, cec17(x, 1))
	x = np.zeros((5, 10))
	print(x, cec17(x, 1))
