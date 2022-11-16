# ATM Controller Package 

## Overview 
This project aims to control a simple ATM operations and test modules for further integration.

The main operation process is as follows.
1. Build the program
```
//
$ pip install -r requirements.txt
$ python3 -m pip install --upgrade build
$ python3 -m build
```

2. Run the program
 ```
  cd src 
  // implement main function 
  python atm_room.py 
 ```
3. Run the module
```
// Case 1. Pin authentication Error
// modify pin number "6789" -> "1234"
// You can see the following result
"""
  1. Deposit
  2. Withdraw
  3. Show Balance
  4. Exit
  Invalid PIN Number
  Please collect your card
"""

// Case 2. Deposit
// Enter number 1. deposit 
// Enter amount of deposit 
// You can see the following result
"""
Authenticated passed
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Please choose from one of the following options : 1
Deposit selected
Please enter the deposit amount : 3000
Please collect your card
Exit happens
Balance: 6500
"""

// Case 3. Withdraw
// Enter number 2. withdraw 
// Enter amount of withdraw 
// You can see the following result
"""
Authenticated passed
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Please choose from one of the following options : 2
Withdraw selected
Please enter the withdrawal amount : 3000
Please collect your card
Exit happens
Balance: 500
"""

// Case 4. Balance
// Enter number 3. balance
// You can see the following result 
"""
Authenticated passed
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Please choose from one of the following options : 3
Balance selected
Your Account Balance is: 3000
Please collect your card
Exit happens
Balance: 3500
"""
// Case 5. Exit
// Enter number 4. exit
// You can see the following result 
"""
Authenticated passed
1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Please choose from one of the following options : 4
Please collect your card
Exit happens
Balance: 3500
"""
```

## Test Code 
Unfortunately, it was not fully handled for testing all cases of modules in this project.
Mainly focused on how module work and states have been properly updated. 
```
$ pytest
```



