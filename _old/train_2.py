def fizz_buzz(n: int) -> None:
    for i in range (1, n + 1):
        msg = ''
        if i % 3 == 0:
            msg += 'FIZZ'
        if i % 5 == 0:
            msg += 'BUZZ'
        print(i or msg)
fizz_buzz(20)