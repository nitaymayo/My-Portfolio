package com.example.boardnumbergame;


public class Coordinate {
    /*
    Class to control cells coordinate on the board
     */
    private int x,y;

    public Coordinate(int Line,int Col){
        x = Line;
        y = Col;
    }

    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }
    public void Move(String dir){
        switch (dir){
            case "UP":
                x++;
                break;
            case "DOWN":
                x--;
                break;
            case "LEFT":
                y++;
                break;
            case "RIGHT":
                y--;
                break;
        }
    }

}
