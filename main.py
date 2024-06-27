def main():
    
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = False
    if (email[0].isalpha()):
        if (len(email) > 5 and len(email) < 30):
            if (email.find("@") != -1):
                result = True
    
    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
