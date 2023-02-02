package com.example.boardnumbergame;
import android.animation.ObjectAnimator;
import android.animation.ValueAnimator;
import android.view.animation.Animation;


public class jAnimation {
    static float cellLength = 360;
    static final long duration = 50;

    public static Animation moveDown(final Cell obj){
        final ObjectAnimator move = ObjectAnimator.ofFloat(obj.cellView,"Y",obj.cellView.getY(),obj.cellView.getY()+obj.getWidth());
        move.setDuration(duration);
        Animation anim = new Animation() {
            @Override
            public void start() {
                move.start();
            }
        };
        anim.setFillAfter(true);
        anim.start();
        return anim;
    }

    public static Animation moveUp(final Cell obj){
        final ObjectAnimator move = ObjectAnimator.ofFloat(obj.cellView,"Y",obj.cellView.getY(),obj.cellView.getY()-obj.getWidth());
        move.setDuration(duration);
        Animation anim = new Animation() {
            @Override
            public void start() {
                move.start();
            }
        };
        anim.setFillAfter(true);
        anim.start();
        return anim;
    }

    public static Animation moveRight(final Cell obj){
        final ObjectAnimator move = ObjectAnimator.ofFloat(obj.cellView,"X",obj.cellView.getX(),obj.cellView.getX()+obj.getWidth());
        move.setDuration(duration);
        Animation anim = new Animation() {
            @Override
            public void start() {
                move.start();
            }
        };
        anim.setFillAfter(true);
        anim.start();
        return anim;
    }

    public static Animation moveLeft(final Cell obj){
        final ObjectAnimator move = ObjectAnimator.ofFloat(obj.cellView,"X",obj.cellView.getX(),obj.cellView.getX()-obj.getWidth());
        move.setDuration(duration);
        Animation anim = new Animation() {
            @Override
            public void start() {
                move.start();
            }
        };
        anim.setFillAfter(true);
        anim.start();
        return anim;
    }
}
