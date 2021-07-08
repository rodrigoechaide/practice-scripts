#!/usr/bin/env python
#*-* coding: utf-8 *-*

"""
Consider a text file (i.e., a file with a .txt extension) containing a list of PNG, JPG, and GIF image file names. The extensions for each file type are as follows:

1. The extension .png denotes a PNG image file.
2. The extension .jpg denotes a JPG image file.
3. The extension .gif denotes a GIF image file.

Given a string, filename, denoting the name of a real text file that has a .txt extension, create the following three output files where filename denotes the name of the file received as input:

1. png_filename, for storing PNG file names.
2. jpg_filename, for storing JPG file names.
3. gif_filename, for storing GIF file names.

Next, process the list of file names in filename in order and, for each source code file name, append the image file name to the appropriate output file. For example, somefilename.png would go in png_filename, and somefilename.gif would go in gif_filename. Note that each line must contain only one file name, and each image file name in an output file must appear in the same order as it appeared in the input file.

Input Format

The given code in the editor reads the string denoting filename from STDIN.

Constraints

The file has a maximum of 105 lines.

Output Format

Create the three output files where filename denotes the name of the file received as input:

1. png_filename, for storing PNG file names.
2. jpg_filename, for storing JPG file names.
3. gif_filename, for storing GIF file names.

Next, process the list of file names in filename in order and, for each source code file name, append the source code file name to the appropriate output file. For example, somefilename.png would go in png_filename, and somefilename.gif would go in gif_filename. Note that each line must contain only one file name, and each source code file name in an output file must appear in the same order as it appeared in the input file.

Sample Input

names_list_00.txt
 

Sample Output

We create the following three output files:

png_names_list_00.txt:
image1.png
image3.png
image4.png
jpg_names_list_00.txt:
image1.jpg
image5.jpg
gif_names_list_00.txt:
image1.gif
image2.gif
 

Explanation

The content of the text file names_list_00.txt is:

code1.png
code1.jpg
code1.gif
code2.gif
code3.png
code4.png
code5.jpg
 

Observe that each image file name in the input file was put into the output file corresponding to its type, and the order of the image file names (with respect to other image file names corresponding to the same type) is maintained.
"""
