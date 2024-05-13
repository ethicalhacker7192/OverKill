# OverKill

The password generator so intense, it makes you scream "What the heck?!"

Think of OverKill as the password equivalent of the Chinese telephone game—each iteration slightly warps the original until it’s tough enough to withstand digital onslaughts (or just really confusing). This genius (or madness?) is powered by Linux’s `/dev/urandom`, ensuring that "random" really means "good luck guessing this."

## Usage ##

Want to dive into the chaos? Just type:

    python3 overkill.py

For those who believe more control means better security, customize the madness:

    python3 overkill.py -i ITERATIONS -r URANDOM -p PROBABILITYOFCHANGE -o OUTPUTFILE

**ITERATIONS:** The amount of times you want to iterate over the password.

**URANDOM:** How many bytes of URANDOM you want to use.

**PROBABILITYOFCHANGE:** Controls the probability of the password overgoing a change (i.e., adding, removing a character, or more drastic changes.)

**OUTPUTFILE:** The file you want to output the password to. (default is password.txt)

## Installation ##

To install this, you'll require a linux machine since this uses `/dev/urandom` which is only available on linux.

All you need to do is run the following:

    git clone https://github.com/ethicalhacker7192/OverKill.git
    cd OverKill
    python3 overkill.py -h

At this point, it should be installed and you can use it as you please.
