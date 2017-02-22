Jimmy Vo
Jimmyvo866@gmail.com
CPSC 223P
Assignment 4


Classes ~ Binary Tree
----------------------


What:
-----

This is a active running program to deal and print out a Binary tree to a pdf file, based on how big the user wants it to be.


How:
1. Determine where all your files are.

2. Open up terminal and change directories according to the location of the files.
(ls (figure where your files are), cd (change directory to appropriate place))

3. Once ready, run the file through python3, along with the number on how many nodes you want in your binary tree.
(example:~/Desktop$ python3 tree.py 100)

4. If done correctly, two dot files should pop up and depending if you want a more accurate version(long), or the other, you run it through graphviz to make a pdf file with a binary tree with the amount of nodes you wanted, randomly.

5. To run the dot file and make output to a pdf file, simply get the dot filename and specify the pdf filename you want and run it through dot -Tpdf -o.
(example:~/Desktop$ dot -Tpdf -o output.pdf short.dot) ~where output.pdf is the pdf filename you want and the short.dot is the filename you made the type of binary tree you want outputted to a pdf file.

6. Once run, double click the pdf file and the binary tree should appear. ~Enjoy!
