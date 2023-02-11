package com.example.boardnumbergame;

import android.view.View;
import android.widget.SeekBar;

public class jSeekbar {
    /*
    Class that controls the difficulty slide bar on the index page
     */
    private SeekBar viewSeekbar;

    public jSeekbar(View v){
        viewSeekbar = (SeekBar)v;
    }


    public int getValue(){
        return (viewSeekbar.getProgress()/10)*10+10;
    }
}
