# BASIC CALCULATOR PROGRAM (v0.3-alpha)

A basic calculator program made with Python and Tkinter.

> ⚠️ This is an **early alpha** version. Features are incomplete, may have bugs, and are subject to changes.

## TIMELINE

### v0.1-alpha
- Complete calculator button layout.
- Working number buttons and text display.
- Working "clear text" button functionality.

### v0.2-alpha
- Added "input" and "output" display panels.
- Added "history", "delete", and "switch to light" buttons (no functionality yet).
- Calculator logic:
  - Does basic arithmetic for integers and floats.
  - Will not be able to type operators if no number is typed beforehand.
  - Returns syntax error for incorrect calculations.
  - Can only calculate expressions if input panel is not empty.

### v0.3-alpha
- Prevents multiple operators to be typed right next to each other.
- Can now remove single input.
- Added parenthesis button functionality.
  - Parenthesis will automatically enclose itself.
  - The amount of open parenthesis is always equal to the amount of close parenthesis.
  - Calculator will automatically interpret parenthesis as multiplication, unless preceded by an operator.
