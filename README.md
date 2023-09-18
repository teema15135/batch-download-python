# Batch Downloader
## Install required packages
```
python -m pip install -r requirements.txt
```
---
## Prepare input files

### Filename Pattern & Location

Put input files in `input/`.
File name must be in this pattern `<sub_directory_name>-<something_doesnt_matter>.txt`.

Program will download and save file in `output/<sub_directory_name>` 

### File content

Each input file content should contain url(s)

#### Example:
##### input/git-1234.txt
```
https://github.com/exampleAgit.png
https://github.com/exampleBgit.png
```

##### input/hub-sometextthatdoesntmatter.txt
```
https://github.com/exampleA.jpg
https://github.com/exampleB.png
```

It will download and save `exampleAgit.png` and `exampleBgit.png` in `output/git/`.

`exampleA.jpg` and `exampleB.png` will be in `output/hub`