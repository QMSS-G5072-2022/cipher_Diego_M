def cipher(text, shift, encrypt=True):
    
    """
    cipher is an encryption function where each letter is replaced by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text : str
        A string.
    shift : int
        An integer.
    encrypt: bool
        A boolean.
    
    Returns
    -------
    str
        The newly encrypted string.

    Examples
    --------
    >>>from cipher_dm3760 import cipher_dm3760
    >>>text = "Good morning to you"
    >>>shift = 3
    >>>cipher_dm3760.cipher(cipher(text, string),shift,encrypt = False)
    
    """
        
        
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

