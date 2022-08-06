# zsh and oh-my-zsh

zsh and oh-my-zsh are not mandatory dependencies but do make the terminal a bit easier to navigate.
To install go ahead and run the following commands in the terminal.
The first will install zsh or the Z-Shell
next it will install git (if not already installed)
finally it will clone the oh-my-zsh repo and set it as our default shell.
You will need to reboot for this to take effect everytime you open the shell

```
sudo apt install zsh
sudo apt install curl wget git
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone git@github.com:zsh-users/zsh-syntax-highlighting.git`
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
chsh -s $(which zsh)
```

# Python installation
now lets set up our project we will use this structure:
```
Projects
└── djangoapp
```
in the shell enter the following commands:
```
cd
mkdir Projects
cd Projects
```
This will make a new directory/folder in your Home folder and move into that directory.
Now lets install pyenv to help us manage different versions of python when we need to

`curl https://pyenv.run | bash`

Now lets install a version of python that will work with tensorflow and Django, python 
