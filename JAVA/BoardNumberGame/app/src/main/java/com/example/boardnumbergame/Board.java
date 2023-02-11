package com.example.boardnumbergame;

import android.view.View;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;


public class Board extends AppCompatActivity {
    /**
     * The main class to control and display the game
     */

    private Cell[][] Cells;
    private ConstraintLayout board;
    private Coordinate emptyCellCord = new Coordinate(3,3);
    public Cell timeScreen,stepScreen;
    private final int[][] winCheck;

    public void StartGame(int difficulty, String type){
        /*
        Function to start a new game

        Args:
         difficulty: game level
        */
        killButtons();
        int[][] scrambledBoard =  scrambleBoard(difficulty);
        loadGameImages(type, scrambledBoard);
        stepScreen.setText("0");
        timeScreen.setText("0:00");
        Cells[emptyCellCord.getX()][emptyCellCord.getY()].cellView.setVisibility(View.GONE);
        LoadButtons();
    }

    public Board(Cell[][] temp, ConstraintLayout board, View Timer,View stepCounter){
        /*
         * Init Function
         */
        Cells = temp.clone();
        winCheck = new int[][] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
        this.board = board;
        timeScreen = new Cell(Timer);
        stepScreen = new Cell(stepCounter);
        }

    public void loadGameImages(String type, int[][] scrambledBoard){
        /*
         * Load the game image type of the board
         */
        for (int i = 0; i<Cells.length;i++){
            for (int j = 0; j<Cells[0].length;j++){
                Cells[i][j].origin = scrambledBoard[i][j];
            }
        }
        switch (type) {

            case "VIEW":
                //load mountain view image background for cells
            {
                findCellByOrigin(1, scrambledBoard).setCellBackground(R.drawable.view_1_1);
                findCellByOrigin(2, scrambledBoard).setCellBackground(R.drawable.view_1_2);
                findCellByOrigin(3, scrambledBoard).setCellBackground(R.drawable.view_1_3);
                findCellByOrigin(4, scrambledBoard).setCellBackground(R.drawable.view_1_4);

                findCellByOrigin(5, scrambledBoard).setCellBackground(R.drawable.view_2_1);
                findCellByOrigin(6, scrambledBoard).setCellBackground(R.drawable.view_2_2);
                findCellByOrigin(7, scrambledBoard).setCellBackground(R.drawable.view_2_3);
                findCellByOrigin(8, scrambledBoard).setCellBackground(R.drawable.view_2_4);

                findCellByOrigin(9, scrambledBoard).setCellBackground(R.drawable.view_3_1);
                findCellByOrigin(10, scrambledBoard).setCellBackground(R.drawable.view_3_2);
                findCellByOrigin(11, scrambledBoard).setCellBackground(R.drawable.view_3_3);
                findCellByOrigin(12, scrambledBoard).setCellBackground(R.drawable.view_3_4);

                findCellByOrigin(13, scrambledBoard).setCellBackground(R.drawable.view_4_1);
                findCellByOrigin(14, scrambledBoard).setCellBackground(R.drawable.view_4_2);
                findCellByOrigin(15, scrambledBoard).setCellBackground(R.drawable.view_4_3);
                findCellByOrigin(16, scrambledBoard).setCellBackground(R.drawable.view_4_4);
            }
                break;
            default:
                // load numbers to the board for default view
                for (int i = 0; i<Cells.length;i++){
                    for (int j = 0; j<Cells[0].length;j++){
                        Cells[i][j].setText(scrambledBoard[i][j]);
                        Cells[i][j].setCellBackground(R.drawable.defaultcellsbackground);
                    }
                }
                break;
        }
    }

    public Cell findCellByOrigin(int origin, int[][] board){
        /*
         *  Function to return a cell from the board by its origin
         */
        int length = board.length;
        for (int i = 0; i<length; i++) {
            for (int j = 0; j < length; j++) {
                if (board[i][j] == origin) {
                    return Cells[i][j];
                }
            }
        }
        return null;
    }

    public void LoadButtons(){
        /*
         * Load the cells adjacent to the empty cell with "buttons"
         */
        if (canMove("UP")){
            Cells[emptyCellCord.getX()+1][emptyCellCord.getY()].cellView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    btnClick("UP");
                }
            });
        }
        if (canMove("DOWN")){
            Cells[emptyCellCord.getX()-1][emptyCellCord.getY()].cellView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    btnClick("DOWN");
                }
            });
        }
        if (canMove("RIGHT")){
            Cells[emptyCellCord.getX()][emptyCellCord.getY()-1].cellView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    btnClick("RIGHT");
                }
            });
        }
        if (canMove("LEFT")){
            Cells[emptyCellCord.getX()][emptyCellCord.getY()+1].cellView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    btnClick("LEFT");
                }
            });
        }

    }

    public void killButtons(){
        /*
         * Remove all buttons from the cells to load new ones
         */
        if (canMove("UP")){
            Cells[emptyCellCord.getX()+1][emptyCellCord.getY()].cellView.setOnClickListener(null);
        }
        if (canMove("DOWN")){
            Cells[emptyCellCord.getX()-1][emptyCellCord.getY()].cellView.setOnClickListener(null);
        }
        if (canMove("RIGHT")){
            Cells[emptyCellCord.getX()][emptyCellCord.getY()-1].cellView.setOnClickListener(null);
        }
        if (canMove("LEFT")){
            Cells[emptyCellCord.getX()][emptyCellCord.getY()+1].cellView.setOnClickListener(null);
        }
    }

    public void btnClick(String dir){
        /*
         * The function that is being called when a click is submitted by the user
         */
        if (!canMove(dir)) {
            return;
        }
        Cell tempCell;
        switch(dir){
            case "UP":
                // Making sure the cell animation has ended
                if (Cells[emptyCellCord.getX()+1][emptyCellCord.getY()].cellView.getAnimation() != null) {
                    return;
                }
                jAnimation.moveUp(Cells[emptyCellCord.getX()+1][emptyCellCord.getY()]);

                tempCell = Cells[emptyCellCord.getX()+1][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()+1][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;
                break;
            case "DOWN":
                if (Cells[emptyCellCord.getX()-1][emptyCellCord.getY()].cellView.getAnimation() != null) {
                    return;
                }
                jAnimation.moveDown(Cells[emptyCellCord.getX()-1][emptyCellCord.getY()]);

                tempCell = Cells[emptyCellCord.getX()-1][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()-1][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;
                break;
            case "LEFT":
                if (Cells[emptyCellCord.getX()][emptyCellCord.getY()+1].cellView.getAnimation() != null) {
                    return;
                }
                jAnimation.moveLeft(Cells[emptyCellCord.getX()][emptyCellCord.getY()+1]);

                tempCell = Cells[emptyCellCord.getX()][emptyCellCord.getY()+1];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()+1] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;
                break;
            case "RIGHT":
                if (Cells[emptyCellCord.getX()][emptyCellCord.getY()-1].cellView.getAnimation() != null) {
                    return;
                }
                jAnimation.moveRight(Cells[emptyCellCord.getX()][emptyCellCord.getY()-1]);

                tempCell = Cells[emptyCellCord.getX()][emptyCellCord.getY()-1];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()-1] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;
                break;
        }
        stepScreen.setText(stepScreen.getNumber()+1);
        killButtons();
        emptyCellCord.Move(dir);
        LoadButtons();

        Won();

    }

    private boolean canMove(String dir){
        /*
         * Checks if the move is possible
         */
        switch (dir) {
            case "UP":
                if (emptyCellCord.getX() == 3)
                    return false;
                break;
            case "DOWN":
                if (emptyCellCord.getX() == 0)
                    return false;
                break;
            case "RIGHT":
                if (emptyCellCord.getY() == 0)
                    return false;
                break;
            case "LEFT":
                if (emptyCellCord.getY() == 3)
                    return false;
                break;
        }
        return true;
    }

    public boolean Won(){
        /*
         * Check if the game is finished
         */

        for (int i = 0; i<=3; i++){
            for (int j = 0; j<=3; j++){
                if (Cells[i][j].getOrigin() != winCheck[i][j]){
                    return false;
                }
            }
        }

        killButtons();
        Cells[3][3].cellView.setVisibility(View.VISIBLE);
        return true;
    }

    public int[][] scrambleBoard(int num){
        /*
         * Function to scramble the board
         *
         * Args:
         * num: Difficulty level that is submitted by the user
         *
         * Returns:
         * 2 dim array of the scrambled numbers, each number represents the origin number of the tile.
         */
        int count = 1;
        int[][] resBoard = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13 ,14, 15, 16}};
        class scrambleMethods {
            /*
             * This class holds specific functions that are in use at the board scrambling stage only
             */
            public final int[][] scrambleBoard;
            // Initiating the class
            public scrambleMethods(int[][] board){
                scrambleBoard = board;
            }

            // Function to make a move on the selfBoard variable
            public void resBoardMove(String dirToMove) {
                /*
                 * Switches the number 16 with the number according to the dirToMove string provided
                 */
                if (!canMove(dirToMove)){
                    return;
                }
                int y = findEmptyCell()[0];
                int x = findEmptyCell()[1];
                switch (dirToMove){
                    case "UP":
                        scrambleBoard[y][x] = scrambleBoard[y+1][x];
                        scrambleBoard[y+1][x] = 16;
                        break;
                    case "DOWN":
                        scrambleBoard[y][x] = scrambleBoard[y-1][x];
                        scrambleBoard[y-1][x] = 16;
                        break;
                    case "LEFT":
                        scrambleBoard[y][x] = scrambleBoard[y][x+1];
                        scrambleBoard[y][x+1] = 16;
                        break;
                    case "RIGHT":
                        scrambleBoard[y][x] = scrambleBoard[y][x-1];
                        scrambleBoard[y][x-1] = 16;
                        break;
                }

            }

            // Function to return the coordinates of the cell with the 16th value
            public int[] findEmptyCell(){
                /*
                 * Returns the coordinates of the number 16 in resBoard
                 */
                for (int i = 0; i<Cells.length; i++){
                    for (int j = 0; j<Cells[0].length; j++){
                        if (scrambleBoard[i][j] == 16){
                            return new int[] {i, j};
                        }
                    }
                }
                return null;
            }

            // Function to return the scrambleBoard variable after the scrambling is done
            public int[][] getBoard(){
                return scrambleBoard;
            }

            // Function that return true if the desired move is possible, false otherwise
            private boolean canMove(String dirToMove){
                /*
                 * Returns True if the switch is possible
                 */
                int[] coordinates = findEmptyCell();
                int y = coordinates[0];
                int x = coordinates[1];
                switch (dirToMove){
                    case "UP":
                        if (y == 3){
                            return false;
                        }
                        break;
                    case "DOWN":
                        if (y == 0){
                            return false;
                        }
                        break;
                    case "LEFT":
                        if (x == 3){
                            return false;
                        }
                        break;
                    case "RIGHT":
                        if (x == 0){
                            return false;
                        }
                        break;
                }
                return true;
            }
        }
        scrambleMethods scrambleMethods = new scrambleMethods(resBoard);
        
        num = num/2;
        int repeats = num/100+1;
        int rounds = (num%100)/10;

        // Make sure the empty tile is at the lower right corner
        for (int i = 0; i<Cells.length; i++){
            btnClick("UP");
            btnClick("LEFT");
        }

        for (int j = 0;j<repeats;j++) {

            //part 1 of scramble, bottom line
            int temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("RIGHT");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                }
            } else {
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("UP");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("UP");
                }

            }


            //part 2 of scramble, Left line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("DOWN");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                }
            } else {
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("DOWN");
                scrambleMethods.resBoardMove("RIGHT");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("RIGHT");
                }
            }

            //part 3 of scramble, Upper line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("LEFT");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                }
            } else {
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("LEFT");
                scrambleMethods.resBoardMove("DOWN");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("DOWN");
                }
            }

            //part 4 of scramble, Right line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("UP");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("LEFT");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                }
            } else {
                scrambleMethods.resBoardMove("RIGHT");
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("UP");
                scrambleMethods.resBoardMove("LEFT");
                for (int i = 0; i < temp; i++) {
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("DOWN");
                    scrambleMethods.resBoardMove("RIGHT");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("UP");
                    scrambleMethods.resBoardMove("LEFT");
                }
            }

        }

        emptyCellCord = new Coordinate(scrambleMethods.findEmptyCell()[0], scrambleMethods.findEmptyCell()[1]);
        return scrambleMethods.getBoard();
    }

}

