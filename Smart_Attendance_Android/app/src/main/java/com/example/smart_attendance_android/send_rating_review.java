package com.example.smart_attendance_android;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RatingBar;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class send_rating_review extends AppCompatActivity{
    RatingBar et1_rating;
    EditText et2_review;
    Button b1_send_rating;
    SharedPreferences sh;
    ArrayList<String> product_arr, product_id_arr;
    String url, rating_str, review_str ;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_rating_review);

        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        et1_rating = findViewById(R.id.ET1_Rating);
        et2_review = findViewById(R.id.ET2_Review);
        b1_send_rating = findViewById(R.id.B1_SendRating);


        b1_send_rating.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view) {

                rating_str = String.valueOf(et1_rating.getRating());
                review_str = et2_review.getText().toString();
                if (rating_str.equalsIgnoreCase("")) {
                    et1_rating.getNumStars();
                } else if (review_str.equalsIgnoreCase("")) {
                    et2_review.setError("Enter your product type");
                }
                else {
                    RequestQueue queue = Volley.newRequestQueue(send_rating_review.this);
                    String url ="http://"+sh.getString("ip", "")+":5000/send_rating";
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            // Display the response string.
                            Log.d("+++++++++++++++++",response);
                            try {
                                JSONObject json=new JSONObject(response);
                                String res=json.getString("task");

                                if(res.equalsIgnoreCase("success"))
                                {
                                    Toast.makeText(getApplicationContext(),"success",Toast.LENGTH_LONG).show();
                                    Intent in=new Intent(getApplicationContext(),student_home.class)	;

                                    startActivity(in);

                                }
                                else
                                {
                                    Toast.makeText(getApplicationContext(),"registration failed",Toast.LENGTH_LONG).show();

                                }

                            } catch (JSONException e) {
                                e.printStackTrace();
                            }


                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {

                            Toast.makeText(getApplicationContext(),"Error"+error,Toast.LENGTH_LONG).show();
                        }
                    }){
                        @Override
                        protected Map<String, String> getParams()
                        {
                            Map<String, String>  params = new HashMap<String, String>();
                            params.put("Rating", rating_str);
                            params.put("Review", review_str);
                            params.put("lid", sh.getString("student_lid", ""));
                            return params;
                        }
                    };
                    // Add the request to the RequestQueue.
                    queue.add(stringRequest);

                }
            }
        });
    }

    public void onBackPressed() {
        super.onBackPressed();
        Intent ik = new Intent(getApplicationContext(), student_home.class);
        startActivity(ik);
    }


}
