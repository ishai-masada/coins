from decimal import Decimal
def denominate(target_amt):
    denoms = {'hundred': 10000, 'fifty': 5000, 'twenty': 2000, 'ten': 1000, 
              'five': 500, 'one': 100, 'quarter': 25, 'dime': 10, 'nickel': 5, 'penny': 1}
    target_amt = int(Decimal(target_amt) * 100)
    output = dict()
    for denom, val in denoms.items():
        if target_amt == 0:
            break     
        if target_amt >= val:
            count = target_amt // val
            target_amt %= val
            if count:
                output[denom] = count
    return output
