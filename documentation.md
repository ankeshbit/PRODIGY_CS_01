# Caesar Cipher - Documentation

## What is a Caesar Cipher?

It's one of the oldest and simplest encryption methods. Every letter in a message gets shifted a fixed number of places down (or up) the alphabet. For example, with a shift of 3:

- A becomes D
- B becomes E
- Z becomes C (it wraps back around to the start)

It's named after Julius Caesar, who supposedly used it to send secret messages.

## How this program works

### `encrypt(text, shift)`

This function takes the message and shift value, then goes through the message one character at a time.

- If the character is a letter, it figures out whether it's uppercase or lowercase (so it knows whether to treat it as part of the A-Z range or a-z range), then shifts it by the given amount.
- The wrap-around (Z → A, z → a) is handled using the `%` (modulo) operator, so the letter position always stays between 0 and 25.
- If the character isn't a letter (space, comma, number, etc.), it's added to the result unchanged.

### `decrypt(text, shift)`

Decryption is really just encryption in reverse, so this function calls `encrypt()` again but with the shift value flipped negative. Shifting backward by the same amount undoes the original shift.

### Handling weird shift values

If someone enters a shift like 29 or -5, the program uses `shift % 26` to bring it back into a normal 0-25 range before doing anything else. This means a shift of 29 behaves exactly like a shift of 3, and a shift of -5 behaves like a shift of 21.

### The menu / main loop

The `main()` function just keeps showing the menu and asking what to do, until the user picks "Quit". For encrypt/decrypt, it asks for the message and shift value, checks that the shift value is actually a number (using `.isdigit()` after stripping off a possible minus sign), and then prints the result.

## Example walkthrough

Input: `"Hello, World!"`, shift `3`

| Original | H | e | l | l | o | , | (space) | W | o | r | l | d | ! |
|----------|---|---|---|---|---|---|---------|---|---|---|---|---|---|
| Shifted  | K | h | o | o | r | , | (space) | Z | r | u | o | g | ! |

Note how the comma, space, and exclamation mark don't change, only the letters do.

## Known limitations

- Only handles standard English letters (A-Z, a-z). Accented letters or other alphabets aren't shifted.
- Doesn't save or load files, everything happens in the terminal for one session.
- Not meant for actual security, this is just a learning exercise/classic cipher. It's easily broken by trying all 26 possible shifts.