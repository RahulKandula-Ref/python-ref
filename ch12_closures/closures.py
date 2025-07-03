def update_account(person, coins):
    def track_coins():
        nonlocal coins
        coins -= 1

        print(person + ' has ' + str(coins) + ' coin(s) left.' 
              if coins >= 1 
              else 
              person + ' has run out of coins.')

    return track_coins

tommy_account = update_account('tommy', 2)
jenny_account = update_account('jennny', 5)

tommy_account()
tommy_account()
tommy_account()

jenny_account()
jenny_account()