import threading, time

print('Start of program.')


def take_a_nap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=take_a_nap)
threadObj.start()
print('End of program.')

print('Cats', 'Dogs', 'Frogs', sep=' & ')  # Cats & Dogs & Frogs
# arguments can be passed as a list to the args argument in threading.Thread
# The keyword argument can be specified as a dictionary to the kwargs argument in threading.Thread

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
                             kwargs={'sep': ' & '})
threadObj.start()  # Cats & Dogs & Frogs

# do not do this:
threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
# this is calling the  print() function and passing its return value ( None ) as the target argument
# It doesn't pass the  print() function itself.
# To pass arguments to a function in a new thread, use the threading.Thread() args and kwargs keyword arguments.
