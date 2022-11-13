
base = 'https://en.wikipedia.org/wiki'
with open('urls.txt', 'w') as f:
    for i in range(1700, 1800):
        f.write(f'{base}/{i}\n')
    f.write('###')