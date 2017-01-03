package de.arsartificia.dev.sr2go;

import org.springframework.util.StringUtils;

import java.util.ArrayList;

public class Visuals {
    public String getHair() {return StringUtils.arrayToCommaDelimitedString(hairList.toArray());}
    public ArrayList<String> hairList;
    public String getFace() {return StringUtils.arrayToCommaDelimitedString(faceList.toArray());}
    public ArrayList<String> faceList;
    public String getEyes() {return StringUtils.arrayToCommaDelimitedString(eyesList.toArray());}
    public ArrayList<String> eyesList;
    public String getVisualsSpecial() {return StringUtils.arrayToCommaDelimitedString(specialList.toArray());}
    public ArrayList<String> specialList;

    public Visuals() {
        hairList = new ArrayList<>();
        faceList = new ArrayList<>();
        eyesList = new ArrayList<>();
        specialList = new ArrayList<>();
    }
}
