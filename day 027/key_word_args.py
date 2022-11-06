# unlimited Key-word arguments
# key word arguments are accessible through dictionary called kwargs

def key_word_args(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("Key: ", key)
        print("Value: ", value)

def kwargies(**kwargs):
    print("print(kwargs['kappa']) = ", kwargs["kappa"])


key_word_args(kappa="kappa", argument="blyat", elon="musk")
kwargies(kappa="this is what is kappa", another="argument", and_another_one="another one")

def mixed(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

mixed(3, add=1, multiply=2)



