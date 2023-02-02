package com.example.boardnumbergame;

import android.graphics.Color;

import java.util.Random;

public class Func {

    public static boolean ifExcicte(int num, int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == num)
                return true;
        }
        return false;

    }

    public static boolean isArrFull(int[] Arr) {
        for (int i = 0; i < Arr.length; i++) {
            if (Arr[i] == 0)
                return false;
        }
        return true;
    }


    public static int[] RanArr(int bound) {
        int[] Ans = new int[bound];
        Random r = new Random();
        for (int i = 0 ; i<15 ; i++){
            while (true){
                int num = (int)(Math.random()*15)+1;
                if (!ifExcicte(num,Ans)){
                    Ans[i] = num;
                    break;
                }
            }
        }


        return Ans;
    }

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

    public static boolean halfchance(){
        return (Math.random()<0.5);
    }
}

