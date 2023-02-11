package com.example.boardnumbergame;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.SeekBar;
import android.widget.TextView;

public class HomePage extends AppCompatActivity {

    public jSeekbar meterDifficult;
    public jButton btnGo,btnImageSelect,btnLeaderBoard;
    public TextView screenDifficulty,screenEasy,screenMedium,screenHard;
    public String type;
    public Cell btnType;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);

        btnGo = new jButton(findViewById(R.id.btnStart));
        screenDifficulty = findViewById(R.id.difficultScreen);
        screenEasy = findViewById(R.id.screenEasy);
        screenEasy.setTextColor(Color.BLUE);
        screenMedium = findViewById(R.id.screenMedium);
        screenHard = findViewById(R.id.screenHard);
        btnType = new Cell(findViewById(R.id.imageButton));
        type = "NUM";

        SeekBar SeekView = findViewById(R.id.seekbarDifficult);
        meterDifficult = new jSeekbar(SeekView);

        // Configuring the level scale at the home screen
        SeekView.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                progress = (progress/10)*10+10;
                screenDifficulty.setText(""+progress);
                Color color = new Color();
                if (progress<=270){
                    screenEasy.setTextColor(color.BLUE);
                    screenMedium.setTextColor(color.BLACK);
                    screenHard.setTextColor(color.BLACK);
                }else if(progress<=710){
                    screenEasy.setTextColor(color.BLACK);
                    screenMedium.setTextColor(Color.rgb(255,165,0));
                    screenHard.setTextColor(color.BLACK);
                }else{
                    screenEasy.setTextColor(color.BLACK);
                    screenMedium.setTextColor(color.BLACK);
                    screenHard.setTextColor(color.RED);
                }
                if (progress==1000){
                    screenDifficulty.setText("∞");
                }

            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

        findViewById(R.id.imageButton).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switch (type){
                    case "NUM":
                        type = "VIEW";
                        btnType.setCellBackground(R.drawable.view_1_2);
                        break;
                    case "VIEW":
                        type = "NUM";
                        btnType.setCellBackground(R.mipmap.ic_launcher_foreground);
                }
            }
        });

        // Start button configuration
        findViewById(R.id.btnStart).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomePage.this,MainActivity.class);
                intent.putExtra("type", type);
                if (screenDifficulty.getText()=="∞")
                    intent.putExtra("difficulty","1000");
                else
                    intent.putExtra("difficulty",""+screenDifficulty.getText());
                startActivity(intent);
            }
        });

    }
}
