"""Kritsada had a brilliant idea to create his own Text Editor similar to VIM, which operates in a single mode called Command Mode (our input). The program includes 5 commands: Insert (I), Left (L), Right (R), Backspace (B), and Delete (D). (The functionality of each command is explained below.) However, Kritsada lacks programming skills, so he requested help from computer engineering students to develop the Text Editor he envisioned. The output should display the remaining word after executing the commands and the position of the cursor.
Explanation of the 5 Input Commands:

    I <word>: Inserts the word at the current cursor position. After inserting the word, the cursor moves to the end of the inserted word.

    L: Moves the cursor one position to the left. If the cursor is already at the leftmost position, nothing happens.

    R: Moves the cursor one position to the right. If the cursor is already at the rightmost position, nothing happens.

    B: Deletes the character to the left of the cursor. If the cursor is already at the leftmost position, nothing happens.

    D: Deletes the character to the right of the cursor. If the cursor is already at the rightmost position, nothing happens.


Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat | """