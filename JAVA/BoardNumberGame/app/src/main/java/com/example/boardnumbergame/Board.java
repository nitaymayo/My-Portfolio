package com.example.boardnumbergame;

import android.content.res.Resources;
import android.util.TypedValue;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;


public class Board extends AppCompatActivity {
    /**
     * The main class to control and display the game
     */

    private Cell[][] Cells;
    private final Cell[][] FinishedBoard;
    private ConstraintLayout board;
    private Coordinate emptyCellCord = new Coordinate(3,3);
    public Cell timeScreen,stepScreen;
    private final int[][] winCheck;
    public static int dpToPx(float dp) {
        return (int) (dp * Resources.getSystem().getDisplayMetrics().density);
    }
    float dip = 95.34f;

    private final float cellWidth = dpToPx(dip);
    public void StartGame(int difficulty){
        /**
        Function to start a new game

        Args:
         difficulty: game level
        */
        killButtons();
        Cells = FinishedBoard;
        scrambleBoard(difficulty);
        stepScreen.setText("000");
        timeScreen.setText("0:00");
        Cells[emptyCellCord.getX()][emptyCellCord.getY()].cellView.setVisibility(View.GONE);
        LoadButtons();
    }

    public Board(Cell[][] temp, ConstraintLayout board, View Timer,View stepCounter, String type, float cellSize){
        /**
         * Init Function         *
         */
        Cells = temp.clone();
        FinishedBoard = temp.clone();
        winCheck = new int[][] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
        loadGameImageType(type);
        this.board = board;
        timeScreen = new Cell(Timer);
        stepScreen = new Cell(stepCounter);
        }

    public void loadGameImageType(String type){
        /**
         * Load the game image type of the board
         */
        switch (type) {

            case "VIEW":
                //load mountain view image background for cells
            {
                Cells[0][0].setCellBackground(R.drawable.view_1_1);
                Cells[0][1].setCellBackground(R.drawable.view_1_2);
                Cells[0][2].setCellBackground(R.drawable.view_1_3);
                Cells[0][3].setCellBackground(R.drawable.view_1_4);

                Cells[1][0].setCellBackground(R.drawable.view_2_1);
                Cells[1][1].setCellBackground(R.drawable.view_2_2);
                Cells[1][2].setCellBackground(R.drawable.view_2_3);
                Cells[1][3].setCellBackground(R.drawable.view_2_4);

                Cells[2][0].setCellBackground(R.drawable.view_3_1);
                Cells[2][1].setCellBackground(R.drawable.view_3_2);
                Cells[2][2].setCellBackground(R.drawable.view_3_3);
                Cells[2][3].setCellBackground(R.drawable.view_3_4);

                Cells[3][0].setCellBackground(R.drawable.view_4_1);
                Cells[3][1].setCellBackground(R.drawable.view_4_2);
                Cells[3][2].setCellBackground(R.drawable.view_4_3);
                Cells[3][3].setCellBackground(R.drawable.view_4_4);
            }
                break;
            default:
                int count = 1;
                for (int i = 0; i<Cells.length;i++){
                    for (int j = 0; j<Cells[0].length;j++){
                        Cells[i][j].setText(Cells[i][j].getOrigin());
                        count++;
                        Cells[i][j].setCellBackground(R.drawable.defaultcellsbackground);
                    }
                }
                break;
        }
    }

    public void LoadButtons(){
        /**
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
        /**
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
        /**
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

    public void machineMove(String dir){
        /**
         * Function to make the scramble machine be able to move the tiles on the board
         */
        Cell tempCell;
        if (!canMove(dir))
            return;

        switch(dir){
            case "UP":
                Cells[emptyCellCord.getX()][emptyCellCord.getY()].refactorY(cellWidth);
                Cells[emptyCellCord.getX()+1][emptyCellCord.getY()].refactorY(-cellWidth);

                tempCell = Cells[emptyCellCord.getX()+1][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()+1][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;
                break;
            case "DOWN":
                Cells[emptyCellCord.getX()][emptyCellCord.getY()].refactorY(-cellWidth);
                Cells[emptyCellCord.getX()-1][emptyCellCord.getY()].refactorY(cellWidth);

                tempCell = Cells[emptyCellCord.getX()-1][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()-1][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = tempCell;

                break;
            case "LEFT":
                Cells[emptyCellCord.getX()][emptyCellCord.getY()].refactorX(cellWidth);
                Cells[emptyCellCord.getX()][emptyCellCord.getY()+1].refactorX(-cellWidth);

                tempCell = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()+1];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()+1] = tempCell;
                break;
            case "RIGHT":
                Cells[emptyCellCord.getX()][emptyCellCord.getY()].refactorX(-cellWidth);
                Cells[emptyCellCord.getX()][emptyCellCord.getY()-1].refactorX(cellWidth);

                tempCell = Cells[emptyCellCord.getX()][emptyCellCord.getY()];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()] = Cells[emptyCellCord.getX()][emptyCellCord.getY()-1];
                Cells[emptyCellCord.getX()][emptyCellCord.getY()-1] = tempCell;
                break;
        }
            emptyCellCord.Move(dir);
    }

    private boolean canMove(String dir){
        /**
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
        /**
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


    public void scrambleBoard(int num){
        /**
         * Function to scramble the board
         *
         * Args:
         * num: Difficulty level that is submitted by the user
         */
        num = num/2;
        int repeats = num/100+1;
        int rounds = (num%100)/10;

        for (int j = 0;j<repeats;j++) {

            //part 1 of scramble, bottom line
            int temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                machineMove("RIGHT");
                machineMove("RIGHT");
                machineMove("RIGHT");
                for (int i = 0; i < temp; i++) {
                    machineMove("DOWN");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("UP");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                }
            } else {
                machineMove("DOWN");
                machineMove("RIGHT");
                machineMove("RIGHT");
                machineMove("RIGHT");
                machineMove("UP");
                for (int i = 0; i < temp; i++) {
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("DOWN");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("UP");
                }

            }

            //part 2 of scramble, Left line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                machineMove("DOWN");
                machineMove("DOWN");
                machineMove("DOWN");
                for (int i = 0; i < temp; i++) {
                    machineMove("LEFT");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("RIGHT");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("DOWN");
                }
            } else {
                machineMove("LEFT");
                machineMove("DOWN");
                machineMove("DOWN");
                machineMove("DOWN");
                machineMove("RIGHT");
                for (int i = 0; i < temp; i++) {
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("LEFT");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("RIGHT");
                }

            }

            //part 3 of scramble, Upper line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                machineMove("LEFT");
                machineMove("LEFT");
                machineMove("LEFT");
                for (int i = 0; i < temp; i++) {
                    machineMove("UP");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("DOWN");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("LEFT");
                }
            } else {
                machineMove("UP");
                machineMove("LEFT");
                machineMove("LEFT");
                machineMove("LEFT");
                machineMove("DOWN");
                for (int i = 0; i < temp; i++) {
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("RIGHT");
                    machineMove("UP");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("LEFT");
                    machineMove("DOWN");
                }
            }

            //part 4 of scramble, Right line
            temp = (int) (Math.random() * rounds);
            if (Func.halfChance()) {
                machineMove("UP");
                machineMove("UP");
                machineMove("UP");
                for (int i = 0; i < temp; i++) {
                    machineMove("RIGHT");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("LEFT");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("UP");
                }
            } else {
                machineMove("RIGHT");
                machineMove("UP");
                machineMove("UP");
                machineMove("UP");
                machineMove("LEFT");
                for (int i = 0; i < temp; i++) {
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("DOWN");
                    machineMove("RIGHT");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("UP");
                    machineMove("LEFT");
                }
            }

        }
    }

}

