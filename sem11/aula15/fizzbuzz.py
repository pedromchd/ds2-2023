def robot(pos):
    say = str(pos)
    if pos % 5 == 0 and pos % 3 == 0:
        say = 'FizzBuzz'
    elif pos % 5 == 0:
        say = 'Buzz'
    elif pos % 3 == 0:
        say = 'Fizz'
    return say