pom
=====

> beemind pomodoros from terminal

## why

browser extensions for pomodoros are a distraction

## how

1) create goal at [beeminder.com/[your_great_username]/pomodoro](https://www.beeminder.com/mtrazzi/pomodoro)

2) get your [auth_token](https://www.beeminder.com/api/v1/auth_token.json)

3) create ~/.config/beeminder/.pomrc  file:

```
    [account]
    auth_token: <auth_token>
```

4) run `./pom`

# credits

incr_goal.py from [coffeemug/bee](https://github.com/coffeemug/bee)
