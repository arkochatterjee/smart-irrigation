package org.envision.smartwaterconservation;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.Nullable;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class FragmentFloor3 extends Fragment {


    public static FragmentFloor3 newInstance() {

        return new FragmentFloor3();
    }


    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_home, container, false);

        final TextView t = (TextView) v.findViewById(R.id.textView);
        final TextView t1 = (TextView) v.findViewById(R.id.textView1);

        final TextView t2 = (TextView) v.findViewById(R.id.textView2);

        final TextView t0 = (TextView) v.findViewById(R.id.textView0);
        String floorno = "floor3";

        t0.setText(floorno+" Real Time Status");


        FirebaseDatabase database = FirebaseDatabase.getInstance();

        final DatabaseReference myRef = database.getReference().child(floorno);
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String y = dataSnapshot.child("flowrate").getValue(String.class);
                String x = dataSnapshot.child("pH").getValue(String.class);
                String z = dataSnapshot.child("temp").getValue(String.class);

                t.setText("Flow Rate : "+y);
                t1.setText("pH : "+x);
                t2.setText("Temperature : "+z);



            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                databaseError.toException();
            }
        });







        return v;


    }
}

