def check_palindrome(s:str)->bool:
    rev_s=s[::-1]
    if s==rev_s:
        return True
    else:
        return False

if __name__=='__main__':
    s1='abbaa'
    print(check_palindrome(s1))