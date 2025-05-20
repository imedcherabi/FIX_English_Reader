# FIX to English

This is a small project that reads FIX (Financial Information eXchange) messages and prints them in plain English.

The scipt prompts the user to enter a FIX message. It returns a mapped human readable version. 

**************************
Example:

Enter FIX message :
8=FIX.4.4|35=F|11=12345|41=54321|54=2|55=TSLA|38=200|60=20240519-15:00:00

Return:
8 (BeginString) = FIX.4.4
35 (MsgType) = ORDER_CANCEL_REQUEST
11 (ClOrdID) = 12345
41 (OrigClOrdID) = 54321
54 (Side) = SELL
55 (Symbol) = TSLA
38 (OrderQty) = 200
60 (TransactTime) = 20240519-15:00:00
