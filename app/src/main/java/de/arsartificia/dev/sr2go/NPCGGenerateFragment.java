package de.arsartificia.dev.sr2go;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class NPCGGenerateFragment extends Fragment {

    private Button mButtonName;
    private Button mButtonGender;
    private Button mButtonAge;
    private Button mButtonMetatype;
    private Button mButtonFeatures;
    private Button mButtonSpecial;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_npcg_generate, container, false);
    }

    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        View view = getView();
        FloatingActionButton fab = (FloatingActionButton) view.findViewById(R.id.fab_fav);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "IMPLEMENT THIS !", Snackbar.LENGTH_SHORT).setAction("Action", null).show();
            }
        });
        mButtonName = (Button) view.findViewById(R.id.button_name);
        mButtonGender = (Button) view.findViewById(R.id.button_gender);
        mButtonAge = (Button) view.findViewById(R.id.button_age);
        mButtonMetatype = (Button) view.findViewById(R.id.button_metatype);
        mButtonFeatures = (Button) view.findViewById(R.id.button_features);
        mButtonSpecial = (Button) view.findViewById(R.id.button_special);

    }

    private void randomizeName() {
        String value = "Test";
        mButtonName.setText(value);
    }

    private void randomizeGender() {
        String value = "Test";
        mButtonGender.setText(value);
    }

    private void randomizeAge() {
        String value = "Test";
        mButtonAge.setText(value);
    }

    private void randomizeMetatype() {
        String value = "Test";
        mButtonMetatype.setText(value);
    }

    private void randomizeFeatures() {
        String value = "Test";
        mButtonFeatures.setText(value);
    }

    private void randomizeSpecial() {
        String value = "Test";
        mButtonSpecial.setText(value);
    }

    private void randomizeAll() {
        randomizeName();
        randomizeGender();
        randomizeAge();
        randomizeMetatype();
        randomizeFeatures();
        randomizeSpecial();
    }

    public void onShake() {
        randomizeAll();
    }
}
