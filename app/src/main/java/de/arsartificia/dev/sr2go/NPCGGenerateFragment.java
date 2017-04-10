package de.arsartificia.dev.sr2go;

import android.databinding.DataBindingUtil;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.Unbinder;
import de.arsartificia.dev.sr2go.databinding.FragmentNpcgGenerateBinding;

public class NPCGGenerateFragment extends Fragment {

    private MainActivity mainActivity;
    private Unbinder unbinder;
    @BindView(R.id.fab_fav) FloatingActionButton fab;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.mainActivity = (MainActivity) getActivity();
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        FragmentNpcgGenerateBinding binding = DataBindingUtil.inflate(inflater, R.layout.fragment_npcg_generate, container, false);
        View view = binding.getRoot();
        unbinder = ButterKnife.bind(this, view);
        if (mainActivity.mCharacters.size() > 0) {
            binding.setCharacter(mainActivity.mCharacters.iterator().next());
        } else {
            binding.setCharacter(Character.getSample());
        }
        return view;
    }

    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        View view = getView();
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "IMPLEMENT THIS !", Snackbar.LENGTH_SHORT).setAction("Action", null).show();
            }
        });
    }

    private void randomizeAll() {

    }

    public void onShake() {
        randomizeAll();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        unbinder.unbind();
    }
}
