<pre>
Instructions on use:

SETUP:
• Create a folder within the root directory of the script named "printer"
• Any image you wish to print must be placed in this folder

The root directory should be structured as follows:

root/
   ├── printer_escpos.py
   └── printer/
          ├── image1.jpg
          └── image2.jpg

Note:
   When entering the name of the file to print, the script automatically uses the path relative to the root directory by prepending printer/ to the filename.
For example, entering image1.jpg will reference the file at printer/image1.jpg.

   If your image is stored in a subdirectory within the printer folder, you must include that subdirectory in the filename.
For example, entering subfolder/image2.jpg will reference the file at printer/subfolder/image2.jpg.


PRINTING:
• Simply run the Python script and enter the name of the file you wish to print
</pre>

