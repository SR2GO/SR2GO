package de.arsartificia.dev.sr2go;
import android.os.AsyncTask;
import android.util.Log;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.HashSet;

import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;


public class Character {
    private String FirstName;
    private String LastName;
    private String NickName;

    private int Age;
    private String Gender;
    private Visuals Visuals;
    private Personal Personal;

    //region Getter / Setter
    public String getFirstName() {
        return FirstName;
    }

    public void setFirstName(String firstName) {
        FirstName = firstName;
    }

    public String getLastName() {
        return LastName;
    }

    public void setLastName(String lastName) {
        LastName = lastName;
    }

    public String getNickName() {
        return NickName;
    }

    public void setNickName(String nickName) {
        NickName = nickName;
    }

    public int getAge() {
        return Age;
    }

    public void setAge(int age) {
        Age = age;
    }

    public String getGender() {
        return Gender;
    }

    public void setGender(String gender) {
        Gender = gender;
    }

    public de.arsartificia.dev.sr2go.Visuals getVisuals() {
        return Visuals;
    }

    public void setVisuals(de.arsartificia.dev.sr2go.Visuals visuals) {
        Visuals = visuals;
    }

    public de.arsartificia.dev.sr2go.Personal getPersonal() {
        return Personal;
    }

    public void setPersonal(de.arsartificia.dev.sr2go.Personal personal) {
        Personal = personal;
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
                final String url = "url here";
                RestTemplate restTemplate = new RestTemplate();
                restTemplate.getMessageConverters().add(new MappingJackson2HttpMessageConverter());
                Character character = restTemplate.getForObject(url, Character.class);
                return character;
            } catch (Exception e) {
                Log.e("MainActivity", e.getMessage(), e);
            }

            return null;
        }

        @Override
        protected void onPostExecute(Character character) {
            super.onPostExecute(character);
            context.mCharacters.add(character);
        }
    }
}
