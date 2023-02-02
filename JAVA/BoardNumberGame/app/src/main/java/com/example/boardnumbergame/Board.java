package com.example.boardnumbergame;

import android.graphics.drawable.Drawable;
import android.text.Layout;
import android.util.Xml;
import android.view.View;
import android.view.ViewTreeObserver;

import androidx.annotation.DimenRes;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import java.util.HashMap;
import java.util.Map;


public class Board extends AppCompatActivity {


    private Cell[][] Cells;
    private final Cell[][] FinishedBoard;
    private ConstraintLayout board;
    private Coordinate emptyCellCord = new Coordinate(3,3);
    public Cell timeScreen,stepScreen;
    private int cellWidth;
    private Map<Integer, Drawable> winCheck;

    public void StartGame(int difficulty){
        killButtons();
        Cells = FinishedBoard;
        scrambleBoard(difficulty);
        Cells[emptyCellCord.getX()][emptyCellCord.getY()].cellView.setVisibility(View.GONE);
        LoadButtons();
    }

    public Board(Cell[][] temp, ConstraintLayout board, View Timer,View stepCounter, String type){
        Cells = temp.clone();
        FinishedBoard = temp.clone();
        winCheck = new HashMap<Integer, Drawable>();
        loadGameImageType(type);
        this.board = board;
        timeScreen = new Cell(Timer);
        stepScreen = new Cell(stepCounter);
        }


    public void loadGameImageType(String type){
        switch (type) {

            case "VIEW":
                //load view background for cells
            {
                Cells[0][0].setCellBackground(R.drawable.view_1_1);
                winCheck.put(1,Cells[0][0].getBackground());
                Cells[0][1].setCellBackground(R.drawable.view_1_2);
                winCheck.put(2,Cells[0][1].getBackground());
                Cells[0][2].setCellBackground(R.drawable.view_1_3);
                winCheck.put(3,Cells[0][2].getBackground());
                Cells[0][3].setCellBackground(R.drawable.view_1_4);
                winCheck.put(4,Cells[0][3].getBackground());

                Cells[1][0].setCellBackground(R.drawable.view_2_1);
                winCheck.put(5,Cells[1][0].getBackground());
                Cells[1][1].setCellBackground(R.drawable.view_2_2);
                winCheck.put(6,Cells[1][1].getBackground());
                Cells[1][2].setCellBackground(R.drawable.view_2_3);
                winCheck.put(7,Cells[1][2].getBackground());
                Cells[1][3].setCellBackground(R.drawable.view_2_4);
                winCheck.put(8,Cells[1][3].getBackground());

                Cells[2][0].setCellBackground(R.drawable.view_3_1);
                winCheck.put(9,Cells[2][0].getBackground());
                Cells[2][1].setCellBackground(R.drawable.view_3_2);
                winCheck.put(10,Cells[2][1].getBackground());
                Cells[2][2].setCellBackground(R.drawable.view_3_3);
                winCheck.put(11,Cells[2][2].getBackground());
                Cells[2][3].setCellBackground(R.drawable.view_3_4);
                winCheck.put(12,Cells[2][3].getBackground());

                Cells[3][0].setCellBackground(R.drawable.view_4_1);
                winCheck.put(13,Cells[3][0].getBackground());
                Cells[3][1].setCellBackground(R.drawable.view_4_2);
                winCheck.put(14,Cells[3][1].getBackground());
                Cells[3][2].setCellBackground(R.drawable.view_4_3);
                winCheck.put(15,Cells[3][2].getBackground());
                Cells[3][3].setCellBackground(R.drawable.view_4_4);
                winCheck.put(16,Cells[3][3].getBackground());

            }
                break;
            default:
                for (int i = 0; i<Cells.length;i++){
                    for (int j = 0; j<Cells[0].length;j++){
                        Cells[i][j].setCellBackground(R.drawable.defaultcellsbackground);
                    }
                }
                break;
        }
    }

    public void LoadButtons(){
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
        if (!canMove(dir)) {
            return;
        }
        Cell tempCell;
        switch(dir){
            case "UP":
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


        //Won();

    }

    public void machineMove(String dir){
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
        for (int i = 0; i<4;i++){
            for (int j = 0; j<4;j++){
                if (!(Cells[i][j].getBackground() == winCheck.get(4*i+j)));{
                    return false;
                }

            }
        }
        Party();
        return true;

    }

    private void Party(){
        killButtons();
        Cells[3][3].cellView.setVisibility(View.VISIBLE);

    }

    public void scrambleBoard(int num){
        num = num/2;
        int repeats = num/100+1;
        int rounds = (num%100)/10;

        for (int j = 0;j<repeats;j++) {

            //part 1 of scramble, bottom line
            int temp = (int) (Math.random() * rounds);
            if (Func.halfchance()) {
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
            if (Func.halfchance()) {
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
            if (Func.halfchance()) {
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
            if (Func.halfchance()) {
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

    public void testAct(){
        int count = 1;
        for (int i = 0;i<3;i++){
            for (int j = 0; j<4;j++){
                Cells[i][j].setText(count);
                count++;
            }
        }
        for (int j = 0; j<2;j++){
            Cells[3][j].setText(count);
            count++;
        }
        Cells[3][3].setText(0);
    }




}

