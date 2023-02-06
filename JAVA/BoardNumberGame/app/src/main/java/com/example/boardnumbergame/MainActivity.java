package com.example.boardnumbergame;


import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.os.Handler;
import android.os.SystemClock;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.os.Bundle;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.TextView;


public class MainActivity extends AppCompatActivity {

    public Board Game;
    public jButton btnReturn,btnRestart;
    public TextView screenDifficulty;
    public TextView screenMoves,movesAnim, screenTimer;

    long MillisecondTime, StartTime, TimeBuff, UpdateTime = 0L ;
    Handler handler;
    int Seconds, Minutes;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);




        //Initialize the board with the tiles
        final Cell[][] Board ={{new Cell(findViewById(R.id.cell_1_1), 1), new Cell(findViewById(R.id.cell_1_2), 2), new Cell(findViewById(R.id.cell_1_3), 3), new Cell(findViewById(R.id.cell_1_4),4)},
                         {new Cell(findViewById(R.id.cell_2_1), 5), new Cell(findViewById(R.id.cell_2_2), 6), new Cell(findViewById(R.id.cell_2_3),7), new Cell(findViewById(R.id.cell_2_4), 8)},
                         {new Cell(findViewById(R.id.cell_3_1), 9), new Cell(findViewById(R.id.cell_3_2), 10), new Cell(findViewById(R.id.cell_3_3), 11), new Cell(findViewById(R.id.cell_3_4), 12)},
                         {new Cell(findViewById(R.id.cell_4_1), 13), new Cell(findViewById(R.id.cell_4_2), 14), new Cell(findViewById(R.id.cell_4_3), 15), new Cell(findViewById(R.id.cell_4_4), 16)}};

        final ConstraintLayout board = findViewById(R.id.boardlayout);
        ConstraintLayout appBackground = findViewById(R.id.appBackground);

        // Moves count animation configuration
        movesAnim = findViewById(R.id.stepAnim);
        screenMoves = findViewById(R.id.screenMoves);
        final ObjectAnimator MoveUp = ObjectAnimator.ofFloat(movesAnim,"TranslationY", 0, -70);
        final ObjectAnimator Fade = ObjectAnimator.ofFloat(movesAnim,"Alpha",1,0);
        MoveUp.setDuration(200);
        Fade.setDuration(400);
        screenMoves.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                movesAnim.setText(s);
                MoveUp.start();
                Fade.start();
                if (s.toString().equals("1")){
                    StartTime = SystemClock.uptimeMillis();
                    handler.postDelayed(runnable, 0);
                }
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        // Create the game object
        final String difficulty = getIntent().getStringExtra("difficulty");
        final String type = getIntent().getStringExtra("type");
        final float cellWidth = Float.parseFloat(getIntent().getStringExtra("cellWidth"));
        Game = new Board(Board, (ConstraintLayout) findViewById(R.id.boardlayout), findViewById(R.id.screenTime), findViewById(R.id.screenMoves), "VIEW", cellWidth);

        // Initialize the game
        Game.StartGame(Integer.parseInt(difficulty), type);

        // Initialize the buttons of the game and the timer and step counter screens
        btnRestart = new jButton(findViewById(R.id.btnRestart));
        btnReturn = new jButton(findViewById(R.id.btnReturn));
        screenDifficulty = findViewById(R.id.screenDifficulty);
        screenDifficulty.setText(""+difficulty);
        if (Integer.parseInt(difficulty)==1000){
            screenDifficulty.setText("∞");
        }


        // Configuring the Restart and Return buttons
        btnRestart.button().setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Game.StartGame(Integer.parseInt(difficulty), type);
            }
        });
        btnReturn.button().setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,HomePage.class);
                startActivity(intent);
            }
        });

        // Configuring the timer screen backend
        handler = new Handler();
        screenTimer = findViewById(R.id.screenTime);

    }

    public Runnable runnable = new Runnable() {
        /**
         * Class to control the timer
         */
        public void run() {

            MillisecondTime = SystemClock.uptimeMillis() - StartTime;

            UpdateTime = TimeBuff + MillisecondTime;

            Seconds = (int) (UpdateTime / 1000);

            Minutes = Seconds / 60;

            Seconds = Seconds % 60;

            screenTimer.setText("" + Minutes + ":" + String.format("%02d", Seconds));

            handler.postDelayed(this, 0);
            if (Game.Won()){
                handler.removeCallbacks(runnable);
            }
        }

    };

}


