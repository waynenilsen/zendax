# Zendax

What is Zendax and why does it exist?

## Options are bad on Ethereum and how to make things better

There are some problems with vanilla options on Ethereum and more broadly for some market participants. The markets for options are stratified across two dimensions, strike and expiry. Markets must constantly be opened up and closed based on price movements and time movements. This fragments liquidity and makes it costly for market makers to update their offers. These problems also exist in traditional markets but to a lesser degree due to the fact that there are no gas costs.

Many people trade options to get a convex payoff function with respect to the underlying asset. This means that for a small upfront investment the investor is able to get a large gain if the price increases(decreases) for a call(put). They also have limited liability. This represents the single biggest difference between leveraged products and convex products. When you trade with leverage it is entirely possible that the asset reaches your price target in your specified timeframe but a bad candle hits your stop loss and you are forced out of your position or worse yet, liquidated. This does not happen when a trader buys a convex product like an option.

## What does a great solution to this problem look like

A very good synthetic asset system is described as follows

1. pay a little for a potentially huge upside (max pnl > 100%)
2. no path dependent liquidation
3. no strike
4. no expiry
5. easy to understand and use
6. possible to offset risk with a compliment token 
7. good for ape yield farmers
8. good for degen traders

The features of a good synthetic asset system are as follows

1. Liquidity pooling across all time and prices - no need to roll markets
2. Automatic market making with incentives to hedge
3. Strong LP rewards
4. Transparent costs for traders

## Some previously investigated paths

### Power Claims

Power claims are interesting but they violate the availability of complement token principle essentially precluding a straightforward AMM.

### Trig Tokens

These are interesting however they violate the principle of being easy to understand. They also do not provide a great payoff with small upfront payment.