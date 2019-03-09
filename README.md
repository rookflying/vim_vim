# vim_cim

## Introduction

This is a script that automatically configures vim(~/.vimrc and ~/.vim). For now, just support C++ coding. Don't need to configure your vim by yourself step by step. Just run the script. If you want more configuration, you can do it on your own on the basic of this, of course.

## Requirements

- catgs
- python2.7

## Plugin 

- pathogen
- auto-pairs
- nerdtree
- taglist
- omnicppcomplete
- supertab

## Colorscheme

- solarized

## Installation and run

```
git clone git@github.com:rookflying/vim_vim.git
cd vim_vim
```

> Make sure you have installed ctags and python2.7.
 
Then configure your .vimrc path and .vim path in the config.json and run the script.

```
python run.py
```
Then try your new vim.

## Note

If configuraion files(~/.vimrc,~/.vim) exist before running the script, the script will rename them to ~/.vimrc_former and ~/.vim_former. So, don't worry about your old configuration.

## C++ coding

Omnicppcomplete plugin (code autocomplete plugin) already works on STL source code. To make it also work on your own code, you need to run ctags_command which can be found in this repo at the root directory of your project.
