package com.example.boardnumbergame;
import androidx.appcompat.app.AppCompatActivity;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.view.View;
import android.widget.TextView;
import java.util.Random;

public class Cell extends AppCompatActivity {
    /*
     * Class to configure and display each tile in the game
     */
    public TextView cellView;
    public int origin;

    public Cell(View t, int cell_origin){
        /*
         * Init function for tiles
         */
        origin = cell_origin;
        cellView = (TextView)t;
    }
    public Cell(View t){
        /*
         * Init function for the timer, step counter and other objects with similar behavior as the tiles
         */
        origin = -1;
        cellView = (TextView)t;
    }

    public int getOrigin(){
        /*
         * Returns the original index of the tile, -1 if the object is not a tile
         */
        return origin;
    }

    public void setCellBackground(int d){
        cellView.setBackgroundResource(d);
    }

    public Drawable getBackground(){
        return cellView.getBackground();
    }

    public void refactorX(float num){
        /*
         * Change the cell position on the x axis
         *
         * Args:
         * num: pixels to relative move the tile
         */
        cellView.setX(num+cellView.getX());
    }
    public void refactorY(float num){
        /*
         * Change the cell position on the y axis
         *
         * Args:
         * num: pixels to relative move the tile
         */
        cellView.setY(num+cellView.getY());
    }

    public int getWidth(){
        return cellView.getWidth();
    }

    public void setText(int n){
        if (n != 0) {
            cellView.setText(""+n);
            cellView.setAlpha(1);
        } else{
            cellView.setAlpha(1);
            cellView.setText(null);
        }
    }

    public void setText(String s){
        if (s != null) {
            cellView.setText(s);
            cellView.setAlpha(1);
        } else{
            cellView.setAlpha(0);
            cellView.setText(null);
        }
    }

    public String getText(){
        return (String)cellView.getText();
    }

    public int getNumber(){
        return Integer.parseInt(cellView.getText().toString());
    }

}
