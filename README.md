# Python-Utils
A repository of my python utils

## big_number.py
A custom class for handling large numbers up to 1x10<sup>10<sup>MAX_INT</sup></sup> when bypassing the original 4300 int to string conversion limit.<br>
Works by handling mantissa and exponent as separate values.
### Current Implementations
- arithmetic operators: +, -, *, /
- casting: float, int
- getter: getNumber
- test cases
### Planned implementations
- comparative operator overloads: <, >, <=, >=, ==, !=
- getters: getMantissa, getExponent
- setters: setNumber, setMantissa, setExponent

## str_utils.py
A custom class to handle string manipulation and actions
### Current Implementations
- to_upper: a-z -> A-Z
- to_lower: A-Z -> a-z
- capitalise: abc def -> Abc Def

## password_utils.py
A custom class to handle password checks
### Current Implementations
- match_pass_criteria: checks a string (password) against provided regex criteria in a list<br>
By default:
- at lest 1 special character
- at least 1 lowecase letter
- at least 1 uppercase letter
- at least 8 characters long
### Planned implementations
- pass_strength_check: asses strength of a given password
- gen_secure_pass: generate a secure password of a given length