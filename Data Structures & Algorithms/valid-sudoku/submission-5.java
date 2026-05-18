class Solution {
    
    public boolean isValidSudoku(char[][] board) {
    ArrayList<HashSet<Character>> cols = new ArrayList<>();
    ArrayList<HashSet<Character>> boxes = new ArrayList<>();

    for (int i = 0; i < 9; i++) {
        cols.add(new HashSet<>());
        boxes.add(new HashSet<>());
    }

    for (int i = 0; i < board.length; i++) {

        HashSet<Character> currRow = new HashSet<>();

        for (int j = 0; j < board[i].length; j++) {

            char curr = board[i][j];

            if (curr == '.') {
                continue;
            }

            // box index:
            // rows 0-2 + cols 0-2 => box 0
            // rows 0-2 + cols 3-5 => box 1
            // etc...
            int boxIndex = (i / 3) * 3 + (j / 3);

            // check column
            if (cols.get(j).contains(curr)) {
                return false;
            }

            // check row
            if (currRow.contains(curr)) {
                return false;
            }

            // check box
            if (boxes.get(boxIndex).contains(curr)) {
                return false;
            }

            // add values
            currRow.add(curr);
            cols.get(j).add(curr);
            boxes.get(boxIndex).add(curr);
        }
    }

    return true;
        
    }
}
