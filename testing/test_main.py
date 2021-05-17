try:
    from AutoFeedback.funcchecks import check_func, exists 
except:
    import subprocess
    import sys
            
    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func, exists 
           
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class check_class : 
   def first_arg(n,m) :
      low, mean, up = limit(n,m)
      return (( low - mean) / scipy.stats.norm.ppf(0.05) )**2   
   
   def second_arg(n,m) :
      low, mean, up = limit(n,m)
      return mean 
   
   def third_arg(n,m) :
      low, mean, up = limit(n,m)
      return (( up - mean) / scipy.stats.norm.ppf(0.95) )**2 

class UnitTests(unittest.TestCase) :
   def test_mean(self) :
       inputs, var  = [], []
       for i in range(2,10) :
           inputs.append((i,))
           rv = randomvar( 0.5, variance=1/12/i, vmin=0, vmax=1, isinteger=False )
           var.append(rv)
       assert( check_func("sample_mean", inputs, var ) )

   def test_exists(self) : 
       assert( exists("limit") )

   def test_first_arg(self) : 
       inputs, var  = [], []
       for j in range(10,20) :
           for i in range(2,10) :
               inputs.append((i,j,))
               myvar1 = randomvar( 0.5, variance=1/12/i, dist="chi2", isinteger=False )
               var.append(myvar1)
       assert( check_func("first_arg", inputs, var, modname=check_class) )

   def test_second_arg(self) : 
       inputs, var  = [], []
       for j in range(10,20) : 
           for i in range(2,10) :
               inputs.append((i,j,))
               myvar1 = randomvar( 0.5, variance=1/12/i, vmin=0, vmax=1, isinteger=False )
               var.append(myvar1)
       assert( check_func("second_arg", inputs, var, modname=check_class) )

   def test_third_arg(self) : 
       inputs, var  = [], []
       for j in range(10,20) :
           for i in range(2,10) :
               inputs.append((i,j,))
               myvar1 = randomvar( 0.5, variance=1/12/i, dist="chi2", isinteger=False )
               var.append(myvar1)
       assert( check_func("third_arg", inputs, var, modname=check_class) )
     
