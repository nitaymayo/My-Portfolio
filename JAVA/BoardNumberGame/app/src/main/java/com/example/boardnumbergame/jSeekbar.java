package com.example.boardnumbergame;

import android.view.View;
import android.widget.SeekBar;

public class jSeekbar {

    private SeekBar viewSeekbar;

    public jSeekbar(View v){
        viewSeekbar = (SeekBar)v;
    }


    public int getValue(){
        return (viewSeekbar.getProgress()/10)*10+10;
    }
}
