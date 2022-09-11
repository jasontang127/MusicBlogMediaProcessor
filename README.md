MusicBlogMediaProcessor
======

This project works with folders to filter out non-audio files, and writes audio files' information to an output text file. Primarily intended for use with this classical music blog: https://www.classicalmusic-notes.com. 

### Software Used
* Python
  * os library
    * Used to navigate local directories and files
  * sys library
    * Used to read command-line arguments when ran from the command-line
    
### Usage
* Place program in a "working folder"; each working folder (symphony) will contain subfolders (movements), which will themselves contain the files related to their respective movements
* Create an input JSON file with fields: 
  * composer 
  * targetComposerFolderName
  * workTitle
  * genre
  * workingFolder
* Compile and run this program, passing in the location of the above input JSON file as an argument
