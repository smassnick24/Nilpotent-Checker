# Nilpotent-Checker

This program is a small program that I created to help me for a project in my Linear Algebra course in college.

-For those who are unaware, a nilpotent matrix is a matrix such that all of the entries are zero after the matrix has 
been multiplied by itself n times, n being the dimension of the matrix

-Nilpotent matrices also HAVE to be square otherwise they are not properly nilpotent

-One more piece. If the number of times that the matrix is multiplied by itself exceeds the dimension n, then the matrix
is not nilpotent

-Ex)

     | 0 1 1 | is a nilpotent matrix. 
     | 0 0 1 | this matrix is nilpotent at degree 3
     | 0 0 0 |

    to put it into a different form -> (matrix)^n = (zero matrix)

     | 0 1 1 |   | 0 1 1 |  (n = 2)  | 0 0 1 |   | 0 1 1 |  (n = 3)  | 0 0 0 |
     | 0 0 1 | * | 0 0 1 |     =     | 0 0 0 | * | 0 0 1 |     =     | 0 0 0 |
     | 0 0 0 |   | 0 0 0 |           | 0 0 0 |   | 0 0 0 |           | 0 0 0 |