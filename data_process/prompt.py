ONE_SHOT_STANDARD_PROMPT = """You are a professional Sudoku puzzle solver. Please solve the following Sudoku puzzle.

## Standard Sudoku Rules ##
- Each row must contain the digits 1 through 9 exactly once.
- Each column must contain the digits 1 through 9 exactly once.
- Each 3x3 sub-grid (box) must contain the digits 1 through 9 exactly once.

## Initial Sudoku Board ##
{{current_board}}

## Answer Format ##
Please provide your answer at the end of your response. Put your answer within tags <ANSWER></ANSWER>. Your answer will be a sequence of {{rows}}x{{cols}} = {{ rows * cols }} digits.

For example, the format should look like
<ANSWER>
1234567...
</ANSWER>
""".strip()

ONE_SHOT_VARIANT_PROMPT = """You are a professional Sudoku puzzle solver. Please solve the following Sudoku variant.

## Format Explanation ##
Coordinates:
- We will use r{x}c{y} coordinates. For example, r1c1 is the top-left cell at row 1 column 1, r1c2 is the cell to the right at row 1 column 2, r2c1 is the cell below at row 2 column 1, and so on.

Visual Elements:
- Any visual elements will be described in text using rxcy coordinates.
- Please note the visual elements will be described as-is. If a thermo or arrow appears on the board, the location of the circle or bulb will be listed, and the line or arrow will be listed as a separate object. But you can infer they are part of the same object by their coordinates.
- If a visual element is described as "between" two cells, it means the visual element appears on the edge between the two cells.
- In some puzzles there may be visual elements outside of the grid and these will be described using the same coordinate system. For example an arrow in r0c1 pointing to the lower right means there is an arrow above r1c1 that points in the direction of the diagonal: r1c2, r2c3, etc.

## Tips ##
- In solving the puzzle it often helps to understand that there exists a unique solution.
- It therefore helps to focus on what values must be forced given the puzzle constraints, and given the fact that the solution is unique.
- All information is provided and is sufficient to solve the puzzle.

## Size ## 
{{rows}} x {{cols}}

## Rules ##
{{rules}}

## Visual Elements ##
{{pretty_visual_elements}}

## Initial Sudoku Board ##
{{current_board}}

## Answer Format ##
Please provide your answer at the end of your response. Put your answer within tags <ANSWER></ANSWER>. Your answer will be a sequence of {{rows}}x{{cols}} = {{ rows * cols }} digits.

For example, the format should look like
<ANSWER>
1234567...
</ANSWER>
""".strip()
