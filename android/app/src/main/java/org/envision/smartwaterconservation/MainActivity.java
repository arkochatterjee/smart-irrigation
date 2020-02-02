package org.envision.smartwaterconservation;

import android.app.FragmentTransaction;
import android.os.Bundle;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.annotation.NonNull;

import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView mTextMessage;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                   // mTextMessage.setText(R.string.title_home);
                    loadHomeFragment();
                    return true;
                case R.id.navigation_dashboard:
                  loadFloor2();
                    return true;
                case R.id.navigation_notifications:
                    loadFloor3();
                    return true;
            }
            return false;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        loadHomeFragment();
        BottomNavigationView navView = findViewById(R.id.nav_view);
        mTextMessage = findViewById(R.id.message);
        navView.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }



    private void loadHomeFragment() {
        //about_hack = false;
        FragmentHome fragment = FragmentHome.newInstance();
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        ft.replace(R.id.fragment_frame, fragment);
        //setTitle("Home");
        ft.addToBackStack(null);
        ft.commit();
    }

    private void loadFloor2() {
        //about_hack = false;
        FragmentFloor2 fragment = FragmentFloor2.newInstance();
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        ft.replace(R.id.fragment_frame, fragment);
        //setTitle("Home");
        ft.addToBackStack(null);
        ft.commit();
    }

    private void loadFloor3() {
        //about_hack = false;
        FragmentFloor3 fragment = FragmentFloor3.newInstance();
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        ft.replace(R.id.fragment_frame, fragment);
        //setTitle("Home");
        ft.addToBackStack(null);
        ft.commit();
    }

}
