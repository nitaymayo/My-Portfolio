package com.example.boardnumbergame;

import android.graphics.Color;

import java.util.Random;

public class Func {
    /**
     * Helping function that are used in the code
     */

    public static int Random(int min,int max){
        Random r = new Random();
        return (r.nextInt(((max-min) + 1)) + min);
    }

    public int RandomColor(){
        Color c = new Color();
        switch (Random(1,6)){
            case 1: return c.RED;
            case 2: return c.GREEN;
            case 3: return c.BLUE;
            case 4: return c.CYAN;
            case 5: return c.MAGENTA;
            case 6: return c.YELLOW;
        }
        return 0;
    }

    public static boolean halfChance(){
        return (Math.random()<0.5);
    }
}

