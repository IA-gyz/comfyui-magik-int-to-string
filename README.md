# Magik Int to String

Extract this folder into ComfyUI/custom_nodes/, restart ComfyUI, and refresh the browser.
Search for Magik Int to String under Magik/Utils.

Inputs:
- value: integer to convert. Use the widget or convert it to an input to connect another node.
- padding: minimum output width, from 1 to 99, default 3.

Output: string (STRING).

With padding 3: 1 → 001; 189 → 189; 123456 → 123456.
Longer numbers are never truncated. For negative values, the minus sign counts
as one character and zeros follow it: -1 → -01. Zero becomes 000.
No extra dependencies are required.
