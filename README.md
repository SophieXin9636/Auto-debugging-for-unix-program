# Auto-debug for UNIX homework

@ By Sophie Shin

## Why?
Just for fun! <br>
Easy debugging!

## Environment
* OS: Ubuntu 16.04 (or 18.04)
* Python2
* tcsh
```
sudo apt-get install tcsh
```

## Installation
```
cd ~/
git clone https://github.com/SophieXin9636/auto_debug_for_unix
cd auto_debug_for_unix
cp debug.py ~
cd ~/
```

* Python2 pip
```
sudo apt-get install python-pip
```
* pwntools
```shell
pip install pwntools
```


## Run
input your file name (no extension) and output filename
```
python debug.py
```

It will write output file in your directory.
This file can compare with ~/auto_debug_for_unix/debug.txt

```shell
diff your_output_file_name ~/auto_debug_for_unix/debug.txt
```

![](https://i.imgur.com/A7VVpqJ.png)
