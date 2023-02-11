package com.example.boardnumbergame;
import java.util.Random;

public class Func {
    /*
     * Helping function that are used in the code
     */

    public static int Random(int min,int max){
        /*
        Return a number number between min and max
         */
        Random r = new Random();
        return (r.nextInt(((max-min) + 1)) + min);
    }

    public static boolean halfChance(){
        /*
        Function that return true half of the time it is called
        Used for random scrambling
         */
        return (Math.random()<0.5);
    }
}

