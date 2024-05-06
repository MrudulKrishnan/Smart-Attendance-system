package com.example.smart_attendance_android;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
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
public class view_attendance extends AppCompatActivity {
    TextView attendance;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_attendance);

        attendance = findViewById(R.id.TV_Attendace);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        RequestQueue queue = Volley.newRequestQueue(view_attendance.this);

        String url = "http://" + sh.getString("ip", "") + ":5000/view_attendance_student";
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,new Response.Listener<String>()
        {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++",response);
                try {

                    JSONObject json = new JSONObject(response);
                    String res = json.getString("Attendance");
                    attendance.setText(res);


                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(getApplicationContext(),"Error_##",Toast.LENGTH_LONG).show();
            }
        }){
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String>  params = new HashMap<String, String>();
                params.put("lid", sh.getString("student_lid", ""));
                return params;
            }
        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }
    public void onBackPressed() {
        super.onBackPressed();
        Intent ik = new Intent(getApplicationContext(), student_home.class);
        startActivity(ik);
    }

}

























//package com.example.smart_attendance_android;
//
//import androidx.annotation.NonNull;
//import androidx.appcompat.app.AlertDialog;
//import androidx.appcompat.app.AppCompatActivity;
//
//import android.content.DialogInterface;
//import android.content.Intent;
//import android.content.SharedPreferences;
//import android.os.Bundle;
//import android.preference.PreferenceManager;
//import android.util.Log;
//import android.view.View;
//import android.widget.AdapterView;
//import android.widget.ArrayAdapter;
//import android.widget.ListView;
//import android.widget.TextView;
//import android.widget.Toast;
//
//import com.android.volley.Request;
//import com.android.volley.RequestQueue;
//import com.android.volley.Response;
//import com.android.volley.VolleyError;
//import com.android.volley.toolbox.StringRequest;
//import com.android.volley.toolbox.Volley;
//
//import org.json.JSONArray;
//import org.json.JSONException;
//import org.json.JSONObject;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.Map;
//
//public class view_attendance extends AppCompatActivity
//{
//    SharedPreferences sh;
//    String url,user_id_str;
//    String attendance_arr;
//    TextView tv_attendance;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_view_attendance);
//        tv_attendance = findViewById(R.id.TV_Attendace);
//        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//        url = "http://" + sh.getString("ip", "") + ":5000/view_attendance_student";
//        RequestQueue queue = Volley.newRequestQueue(view_attendance.this);
//
//        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
//            @Override
//            public void onResponse(String response) {
//                // Display the response string.
//                Log.d("+++++++++++++++++", response);
//                try {
//                    Toast.makeText(view_attendance.this, ""+response, Toast.LENGTH_SHORT).show();
//
//                    JSONArray ar = new JSONArray(response);
//
////                    date_arr = new ArrayList<>();
////                    attendance_arr = new ArrayList<>();
//
//
////                    for (int i = 0; i < ar.length(); i++) {
//                        JSONObject jo = ar.getJSONObject(0);
////                        date_arr.add(jo.getString("Date"));
//                        attendance_arr=jo.getString("Attendance");
//
////                    }
//
////                     ArrayAdapter<String> ad=new ArrayAdapter<>(Home.this,android.R.layout.simple_list_item_1,name);
////                    lv.setAdapter(ad);
//
////                    l1_view_attendance.setAdapter(new custom_view_attendance(view_attendance.this,date_arr, attendance_arr));
////                    view_product_list.setOnItemClickListener(view_product.this);
//
//                } catch (Exception e) {
//                    Toast.makeText(getApplicationContext(),"========="+e,Toast.LENGTH_LONG).show();
//                    Log.d("=========", e.toString());
//                }
//
//                tv_attendance.setText(attendance_arr);
//
//
//            }
//
//        }, new Response.ErrorListener() {
//            @Override
//            public void onErrorResponse(VolleyError error) {
//
//                Toast.makeText(view_attendance.this, "err" + error, Toast.LENGTH_SHORT).show();
//            }
//        }) {
//            @NonNull
//            @Override
//            protected Map<String, String> getParams() {
//                Map<String, String> params = new HashMap<>();
//                params.put("lid", sh.getString("student_lid", ""));
//                return params;
//            }
//        };
//        queue.add(stringRequest);
//    }
//
//    public void onBackPressed() {
//        super.onBackPressed();
//        Intent ik = new Intent(getApplicationContext(), student_home.class);
//        startActivity(ik);
//    }
//
//
//}