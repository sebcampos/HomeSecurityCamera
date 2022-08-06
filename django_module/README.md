# zsh and oh-my-zsh (Optional)

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
mkdir djangoapp
```
This will make a new directory/folder in your Home folder and move into that directory. After which it will
create an empty directory in the current Projects folder called djangoapp


Now lets install pyenv and add it to our PATH to help us manage different versions of python when we need to
pyenv dependencies:
```
sudo apt update
sudo apt install \
build-essential \
curl \
libbz2-dev \
libffi-dev \
liblzma-dev \
libncursesw5-dev \
libreadline-dev \
libsqlite3-dev \
libssl-dev \
libxml2-dev \
libxmlsec1-dev \
llvm \
make \
tk-dev \
wget \
xz-utils \
zlib1g-dev \
libbluetooth-dev
```

```
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc 
```
if you are using the zsh terminal then change the last line from `>> ~/.bashrc` to `>> ~/.zshrc`
exit and restart the terminal.
ensure pyenv has installed correctly by entering
`pyenv`
into the terminal. You should see an output similar to the following:

![pyenv](../static/pyenvoutput.png)

navigate back to out Projects directory using the `cd` command
next we will install python version 3.8.8 using pyenv so we can use Tensorflow and Django (this might take a minute)

`pyenv install 3.8.8`

Next we will move into our django app directory with the command

`cd djangoapp`


