package com.example.smart_attendance_android;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class student_home extends AppCompatActivity {

    Button b1_view_attendance, b2_complaint_reply, b3_feedback, b4_rating, b5_logout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student_home);

        b1_view_attendance = findViewById(R.id.B1_ViewAttendance);
        b2_complaint_reply = findViewById(R.id.B2_AddComplaintReply);
        b3_feedback = findViewById(R.id.B3_SendFeedback);
        b4_rating = findViewById(R.id.B4_SendRating);
        b5_logout = findViewById(R.id.B5_Logout);


        b1_view_attendance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getApplicationContext(), view_attendance.class);
                startActivity(i);

            }
        });


        b2_complaint_reply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getApplicationContext(), send_complaints_view_reply.class);
                startActivity(i);


            }
        });


        b3_feedback.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getApplicationContext(), send_feedback.class);
                startActivity(i);


            }
        });


        b4_rating.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getApplicationContext(), send_rating_review.class);
                startActivity(i);

            }
        });

        b5_logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent i = new Intent(getApplicationContext(), login.class);
                startActivity(i);


            }
        });
    }
}