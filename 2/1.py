************* Module c2
W:  4, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
C:  5, 0: Trailing whitespace (trailing-whitespace)
W:  8, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W:  9, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
C: 10, 0: Trailing whitespace (trailing-whitespace)
W: 11, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W: 12, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
W: 13, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
C: 14, 0: Trailing whitespace (trailing-whitespace)
W: 15, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W: 16, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
C: 17, 0: Trailing whitespace (trailing-whitespace)
W: 18, 0: Bad indentation. Found 2 spaces, expected 4 (bad-indentation)
W: 19, 0: Bad indentation. Found 4 spaces, expected 8 (bad-indentation)
C: 19, 0: Trailing whitespace (trailing-whitespace)
C: 20, 0: Trailing whitespace (trailing-whitespace)
C: 21, 0: Trailing whitespace (trailing-whitespace)
C: 24, 0: Unnecessary parens after 'print' keyword (superfluous-parens)
C: 25, 0: Unnecessary parens after 'print' keyword (superfluous-parens)
C: 26, 0: Trailing whitespace (trailing-whitespace)
C: 27, 0: Trailing whitespace (trailing-whitespace)
C: 28, 0: Trailing whitespace (trailing-whitespace)
C:  1, 0: Missing module docstring (missing-docstring)
C:  3, 0: Missing function docstring (missing-docstring)
W:  4, 9: Access to a protected member __name of a client class (protected-access)
W:  4,43: Access to a protected member __year of a client class (protected-access)
C:  7, 0: Missing class docstring (missing-docstring)
C:  7, 0: Old-style class defined. (old-style-class)
C: 15, 2: Missing method docstring (missing-docstring)
E: 16,11: Instance of 'Student' has no 'name' member (no-member)
E: 16,33: Instance of 'Student' has no 'year' member (no-member)
R:  7, 0: Too few public methods (1/2) (too-few-public-methods)
C: 22, 0: Invalid constant name "st" (invalid-name)


Report
======
16 statements analysed.

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |15     |65.22 |15       |=          |
+----------+-------+------+---------+-----------+
|docstring |0      |0.00  |0        |=          |
+----------+-------+------+---------+-----------+
|comment   |1      |4.35  |1        |=          |
+----------+-------+------+---------+-----------+
|empty     |7      |30.43 |7        |=          |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |3      |3          |=          |66.67       |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |18     |21       |-3.00      |
+-----------+-------+---------+-----------+
|refactor   |1      |1        |=          |
+-----------+-------+---------+-----------+
|warning    |12     |12       |=          |
+-----------+-------+---------+-----------+
|error      |2      |2        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------------------+------------+
|message id             |occurrences |
+=======================+============+
|trailing-whitespace    |10          |
+-----------------------+------------+
|bad-indentation        |10          |
+-----------------------+------------+
|missing-docstring      |4           |
+-----------------------+------------+
|superfluous-parens     |2           |
+-----------------------+------------+
|protected-access       |2           |
+-----------------------+------------+
|no-member              |2           |
+-----------------------+------------+
|too-few-public-methods |1           |
+-----------------------+------------+
|old-style-class        |1           |
+-----------------------+------------+
|invalid-name           |1           |
+-----------------------+------------+



Global evaluation
-----------------
Your code has been rated at -15.62/10 (previous run: -17.50/10, +1.88)

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



