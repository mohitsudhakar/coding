import json

if __name__ == '__main__':

    with open('prices.json') as f:
        prices = json.load(f)
        tickers = []
        weights = []
        for price in prices:
            tickers.append(price['symbol'])
            weights.append(price['lastPrice'])

        # exceptions are USDT, TUSD, USDC, USDS
        len4 = ['USDT', 'TUSD', 'BUSD', 'USDC', 'USDS', 'BIDR', 'BKRW', 'IDRT']
        pairs = []
        for tick in tickers:
            # take last 4 if in len4 else take 3
            if tick[-4:] in len4:
                pairs.append((tick[:-4], tick[-4:]))
            else:
                pairs.append((tick[:-3], tick[-3:]))

        with open('prices.csv', 'w') as p:
            p.write('main,base,price\n')
            for i in range(len(pairs)):
                p.write(pairs[i][0] + ',' + pairs[i][1] + ',' + weights[i] + '\n')

