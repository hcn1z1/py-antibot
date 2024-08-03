# RegBot

RegBot is a python package used to detect bots through attempting to recognize the real function behind the cursor movements. An advanced automation bot uses mathematical functions to create a path from `a` to `b` to deceive anti-bots.

## Our proposition

We took in consideration three different cases. We explain each in following

- **Linear Function** : This is when a bot attempt to reach `a` to `b` through a linear function. for Y a list of `n` numbers, for each Yi of Y, i <= n It exist a function F(Xi) = Yi / aXi + b = Yi where `a` and `b` are constants for all (Xi,Yi). We use **linear regression models** for this type of functions

- **Polynomial Function** : This is when a bot attempt to go from `a` to `b` in a no linear function but in a polynomial function, This attempt to complicate things but it doesn't really help a lot since polynomial function are most of the time either decreasing or increasing. We use **polynomial regression models** for this type of functions.

- **non-linear Function** : This is when a bot attempt to go from `a` to `b` through a no linear function such as `sin(x)` or `exp(x)` and so on...

## Score

A **score** is the detection score of a bot; We use different initial (max) score for each case since we noticed the usage of each is differ. We mean, that a bot is likely more to use a linear function then a non-linearr function. That's why. 

The score for this package is a float between 0 and 5


## Data collection

Data collected to use on these models have to be used when an action trigger. for example, typing something or clicking on a pixel. Bots attend to be as minimizing time and clicks as much as possible. most of time, these bots go from `a` to `b` in order to do something (trigger an event) for example clicking on signup or a form and so on..

