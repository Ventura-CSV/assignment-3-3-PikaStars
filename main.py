def main():
    
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = False
    
    if (email[0].isalpha()):
        result = True
    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
