package com.example.boardnumbergame;
import androidx.appcompat.app.AppCompatActivity;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.view.View;
import android.widget.TextView;
import java.util.Random;

public class Cell extends AppCompatActivity {

    public TextView cellView;


    public Cell(){
        cellView = null;
    }

    public Cell(View t){
        cellView = (TextView)t;

    }

    public void setCellBackground(int d){
        cellView.setBackgroundResource(d);
    }

    public Drawable getBackground(){
        return cellView.getBackground();
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

    public void refactorX(float num){
        cellView.setX(num+cellView.getX());
    }
    public void refactorY(float num){
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

    public String getText(){
        return (String)cellView.getText();
    }
    public int getNumber(){
        return Integer.parseInt(cellView.getText().toString());
    }

}
