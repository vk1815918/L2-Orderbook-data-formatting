# L2-Orderbook-data-formatting
Hello Everybody!

In this project, I leverage the CCXT library for cryptocurrencies to access the endpoints of various exchanges' L2 orderbook streaming service and then transform the data to be used in any format you want.

![image](https://github.com/vk1815918/L2-Orderbook-data-formatting/assets/68977213/6e790c98-5884-407e-a881-f70618151a21)


Brief introduction:

A crypto order book is a digital record of all buy and sell orders for a particular cryptocurrency. It is used to match buyers and sellers at the best possible price. The order book lists the price of the cryptocurrency and the number of coins or tokens available at that price.

![image](https://github.com/vk1815918/L2-Orderbook-data-formatting/assets/68977213/a68997ae-a774-45ba-98b2-2d30b948135f)


In this specfic project L2 Orderbook is sourced from Cryptofeed library's BinanceUS websocket. The data is then transformed into a pandas dataframe and printed out with an optional choice of visualizing the orderbook at every update. You can change the exchange provider in the code.

