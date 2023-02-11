package com.example.boardnumbergame;

import android.net.sip.SipSession;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class jButton extends AppCompatActivity {
    /*
    Class to control the different buttons in the game
     */
    private Button button;
    private float X;
    public void setX(float arg){
        this.X = arg;
    }
    public float getX(){
        return X;
    }
    public jButton(View v){
        button = (Button)v;
    }

    public Button button(){
        return button;
    }

}
