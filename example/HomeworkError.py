for i in ['a','b','c']:
    try:
        print(i*2)
    except:
        print('Whoops')
    else:
        print('Yeah')
    

x = 5
y = 0
try:
    z = x/y
except:
    print('Whoops')
else:
    print(z)
finally:
    print('All Done')



def ask():
    while True:
        try:
            num = int(input('input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            sqrnum = num**2
            print(f'Thank you, your number squared is: {sqrnum}')
            break

ask()


a=10
b=5

print(a)
print(b)



