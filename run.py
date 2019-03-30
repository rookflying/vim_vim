#!/usr/bin/env python
# encoding: utf-8
'''
@author: rookflying
@file: run.py
@time: 2019/3/8 9:42 PM
'''

import os, json, shutil


def readConf():
    with open('./config.json') as jsonFile:
        data = json.load(jsonFile)
        vimrc = data['.vimrc']
        vim = data['.vim']
        javaHome = data['JAVA_HOME']
    if vimrc[-1] == '/':
        vimrc = vimrc[0:-1]
    if vim[-1] == '/':
        vim = vim[0:-1]
    if javaHome[-1] == '/':
        javaHome = javaHome[0:-1]
    if os.path.exists(vimrc):
        os.rename(vimrc, vimrc + '_former')
    if os.path.exists(vim):
        os.rename(vim, vim + '_former')
    os.mkdir(vim)
    os.mkdir(vim + '/autoload')
    os.mkdir(vim + '/bundle')
    with open(vimrc, 'w') as f:
        pass
    return (vimrc, vim, javaHome)


if __name__ == '__main__':
    vimrc, vim, javaHome = readConf()
    # vimrc = '/Users/admin/.vimrc'
    # vim = '/Users/admin/.vim'
    shutil.copyfile('./resources/pathogen.vim', vim + '/autoload/pathogen.vim')
    os.system('git clone https://github.com/jiangmiao/auto-pairs.git ' + vim + '/bundle/auto-pairs')
    os.system('git clone https://github.com/scrooloose/nerdtree.git ' + vim + '/bundle/nerdtree')
    os.system('unzip ./resources/taglist.zip -d ' + vim + '/bundle/taglist')
    os.system('unzip ./resources/omnicppcomplete.zip -d ' + vim + '/bundle/omnicppcomplete')
    os.mkdir(vim + '/tags')
    os.system('tar jxvf ./resources/cpp_src.tar.bz2 -C ' + vim + '/tags/')
    os.system(
        'cd ' + vim + '/tags/cpp_src/ && ctags -R --sort=yes --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++')
    os.system('git clone https://github.com/ervandew/supertab.git ' + vim + '/bundle/supertab')
    os.system('git clone https://github.com/altercation/vim-colors-solarized.git ' + vim + '/bundle/vim-colors-solarized')
    os.system('unzip ./resources/javacomplete.zip -d ' + vim + '/bundle/javacomplete')
    os.system('cd ' + vim + 'bundle/javacomplete/autoload && javac Reflection.java -Xlint')
    os.system('unzip ./resources/TagHighlight.zip -d ' + vim + '/bundle/TagHighlight')
    #os.system('git clone https://github.com/magic-dot-files/TagHighlight ' + vim + '/bundle/TagHighlight')

    with open(vim + '/.bashrc', 'a') as f:
        f.write('PATH=$PATH:' + javaHome + '/bin\n')
        f.write('CLASSPATH=.:' + javaHome + '/lib/tools.jar:' + javaHome + '/lib/dt.jar:' + vim + '/bundle/javacomplete/autoload\n')
        f.write('export PATH CLASSPATH\n')
        pass
    with open('./.vimrc', 'r') as f:
        content = f.read()
    with open(vimrc, 'w') as f:
        f.write(content)
    print('done!')
