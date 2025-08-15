import re


#function to extract mobile number from message
def numberExtractor(message):
    for i in range(len(message)):
        chunk=message[i:i+10]
        if isPhoneNumber(chunk):
            print(f'Phone number found: {chunk}')
            return True
    return False



#Function to check 10 digit valid mobile number
def isPhoneNumber(text):
    if len(text)!=10:
        return False
    numberpattern = re.compile(r'\d{10}')
    number = numberpattern.search(text)
    if number and len(number.group()) == 10:
        return True
    return False
    


if __name__=='__main__':

    text=input('enter message: ')
    if numberExtractor(text):
        print("Done")
    else:
        print('No number found')