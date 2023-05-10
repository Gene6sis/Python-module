import time, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ft_progress(lst) :
    begin_time = time.time()
    for i in range(len(lst)) :
        sys.stdout.write('\r')
        sys.stdout.write(f"Progress: {format(i / len(lst) * 100, '.2f')}% |{bcolors.OKGREEN}{int(i / len(lst) * 30) * '█'}{bcolors.OKCYAN}{(30 - int(i / len(lst) * 30)) * '█'}{bcolors.ENDC}| {int(time.time() - begin_time)} seconds [{i}/{len(lst)}]")
        sys.stdout.flush()
        yield i
    i += 1
    sys.stdout.write('\r')
    sys.stdout.write(f"Finish : 100% |{bcolors.OKGREEN}{30 * '█'}{bcolors.ENDC}| {int(time.time() - begin_time)} seconds [{i}/{len(lst)}]    ")
    yield len(lst)

listy = range(333333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
print()
print(ret)
