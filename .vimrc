set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
set nu
set cursorline
set cursorcolumn
set mouse=a
set laststatus=2
set ruler
set tabstop=4
set expandtab
set showmatch
set ai
set softtabstop=4
set shiftwidth=4

filetype plugin indent on

execute pathogen#infect()

set t_Co=256
let g:solarized_termcolors=256
syntax enable
set background=light
colorscheme solarized

map <C-n> :NERDTree<CR>
map <C-m> :TlistToggle<CR>

let Tlist_Show_One_File = 1
let Tlist_Exit_OnlyWindow = 1
let Tlist_Use_Right_Window = 1
let Tlist_Sort_Type = "name"

set completeopt=longest,menu
let OmniCpp_NamespaceSearch = 2
let OmniCpp_ShowPrototypeInAbbr = 1
let OmniCpp_MayCompleteScope = 1
let OmniCpp_DefaultNamespaces = ["std", "_GLIBCXX_STD"]

set tags+=~/.vim/tags/cpp_src/tags

setlocal omnifunc=javacomplete#Complete
autocmd Filetype java set omnifunc=javacomplete#Complete 
autocmd Filetype java set completefunc=javacomplete#CompleteParamsInf
inoremap <buffer> <C-X><C-U> <C-X><C-U><C-P> 
inoremap <buffer> <C-S-Space> <C-X><C-U><C-P>
autocmd Filetype java,javascript,jsp inoremap <buffer>  .  .<C-X><C-O><C-P>


