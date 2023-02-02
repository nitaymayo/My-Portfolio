package com.example.boardnumbergame;

import android.net.sip.SipSession;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class jButton extends AppCompatActivity {

    private Button button;
    private String porpose;
    private float X;
    public void setX(float arg){
        this.X = arg;
    }
    public float getX(){
        return X;
    }

    public jButton(){

    }
    public jButton(View v){
        Button temp = (Button)v;
        button = temp;
        porpose = (String)temp.getText();
    }
    public String getPorpose(){
        return porpose;
    }

    public Button button(){
        return button;
    }


    public void setVisibility(boolean Vis){
        if (Vis){
            button.setVisibility(View.VISIBLE);
        } else{
            button.setVisibility(View.GONE);
        }
    }


}
