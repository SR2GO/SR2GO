package de.arsartificia.dev.sr2go;
import android.os.AsyncTask;
import android.util.Log;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.HashSet;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;


public class Character {
    private int id;
    private String firstname;
    private String lastname;
    private String nickname;

    private int age;
    private String gender;
    private Visuals visuals;
    private Personal personal;

    //region Getter / Setter


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public de.arsartificia.dev.sr2go.Visuals getVisuals() {
        return visuals;
    }

    public void setVisuals(de.arsartificia.dev.sr2go.Visuals visuals) {
        this.visuals = visuals;
    }

    public de.arsartificia.dev.sr2go.Personal getPersonal() {
        return personal;
    }

    public void setPersonal(de.arsartificia.dev.sr2go.Personal personal) {
        this.personal = personal;
    }
    //endregion

    private Character() {}
    
    public void save() {
        // // TODO: 12/1/16 Handle saving
        this.toServer();
        this.toJSON();
    }

    private void toServer() {

    }

    public static Character fromJSON(String jsonData) {
        return null;
    }

    public String toJSON() {
        ObjectMapper mapper = new ObjectMapper();
        try {
            return mapper.writeValueAsString(this);
        } catch (Exception e) {
            //todo: Should do something here ...
            return null;
        }
    }

    public static HashSet<Character> loadLocal(MainActivity context) {
        // load all locally cached Characters
        return new HashSet<>();
    }

    public static HashSet<Character> loadRemote(MainActivity context, int amount) {

        HashSet<Character> characters = new HashSet<>(amount);
        for (int i = 0; i < amount; ++i) {
            new HttpRequestTask(context).execute();
        }
        return characters;
    }

    private static class HttpRequestTask extends AsyncTask<Void, Void, Character> {
        private MainActivity context;

        public HttpRequestTask(MainActivity context) {
            this.context = context;
        }

        @Override
        protected Character doInBackground(Void... voids) {

            try {
                final String url = context.mServerAddress;
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                return restTemplate.getForObject(url, Character.class);
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute(Character character) {
            super.onPostExecute(character);
            if (character != null) {
                context.mCharacters.add(character);
                Log.i("MainActivity", character.toJSON());
            }
        }
    }
}
