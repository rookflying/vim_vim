# vim_vim

## Introduction

This is a script that automatically configures vim(`~/.vimrc` and `~/.vim`). For now, just support C++ coding and Java coding. Don't need to configure your vim by yourself step by step. Just run the script. If you want more configuration, you can do it on your own on the basic of this, of course.

## Requirements

- ctags
- python2.7
- Linux/Mac
- Java Jre

## Plugin 

- pathogen
- auto-pairs
- nerdtree. 
- taglist. 
- omnicppcomplete
- supertab
- TagHighlight
- javacomplete
- vim-colors-solarized

## Colorscheme

- solarized

## Installation and run

```
git clone git@github.com:rookflying/vim_vim.git
cd vim_vim
```

> Make sure you have installed ctags and python2.7 and java jre.
 
Then configure your `.vimrc` path, `.vim` path, `JAVA_HOME` (`/usr/lib/jvm/java-1.8.0-openjdk-amd64`, etc) and `home` directory in the `config.json` and run the script.

```
python run.py
```
Then try your new vim.

## Note

If configuraion files(`~/.vimrc`,`~/.vim`) exist before running the script, the script will rename them to `~/.vimrc_former` and `~/.vim_former`. So, don't worry about your old configuration. Also, you can config vim on your own by downloading plugins to `~/.vim/bundle`.

## C++ coding

Omnicppcomplete plugin (code autocomplete plugin) already works on STL source code. To make it also work on your own code, you need to run ctags_command, which can be found in this repo, at the root directory of your project.

## Java coding

Using `javacomplete` plugin to finish auto-complete.

## Nerdtree

`Ctrl+N` to show the directory. 

Some operations:

- `o`: open the directory.
- `i`: open file horizontally.
- `s`: open file vertically.
- `Ctrl+w(double-click)`: switch cursor to different file.

## Taglist

`Ctrl+M` or `Enter` to show functions and classes. In this window, can jump to the function or class which is specified by thr cursor by pressing `Enter`.
