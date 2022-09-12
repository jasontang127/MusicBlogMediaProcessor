## MusicBlogMediaProcessor

---

This project works with folders to filter out non-audio files, and writes audio files' information to an output text file. Primarily intended for use with this classical music blog: https://www.classicalmusic-notes.com.

### Software Used
* Python
  * os library
    * Used to navigate local directories and files
  * sys library
    * Used to read command-line arguments when ran from the command-line
   
### Usage
* Place program in a "working folder"; each working folder (symphony) will contain subfolders (movements), which will themselves contain the files related to their respective movements (theme, subject etc).

For example:

```bash
working_folder
      |
      +--I. Majestoso
      |          |
      |          +--bruckner-s6_mvt1_m02-6_main-A.png
      |          +--bruckner-s6_mvt1_m01-12_main-A.ogg
      +--II. Adagio: Sehr feierlich
                |  
                +--bruckner-s6_mvt2_m001-006_main.ogg
                +--bruckner-s6_mvt2_m001-006_main.png
```

* Create an config file in .json form with following fields:
  * composer
  * targetComposerFolderName
  * workTitle
  * genre
  * workingFolder

  For example:

  ```json
  {
    "composer": "Anton Bruckner",
    "targetComposerFolderName": "bruckner",
    "workTitle": "Symphony No. 6 in A major",
    "genre": "Symphony",
    "workingFolder": "."
  }
  ```
* Compile and run this program, passing in the location of the above input JSON file as an argument

For example:

```python
python mediaProcessor.py ./input-file.json
```

