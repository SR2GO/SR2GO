package de.arsartificia.dev.sr2go;

import org.springframework.util.StringUtils;

import java.util.ArrayList;

public class Personal {
    public String getMood() {return StringUtils.arrayToCommaDelimitedString(moodList.toArray());}
    public ArrayList<String> moodList;
    public String getEthics() {return StringUtils.arrayToCommaDelimitedString(ethicsList.toArray());}
    public ArrayList<String> ethicsList;
    public String getMembership() {return StringUtils.arrayToCommaDelimitedString(membershipList.toArray());}
    public ArrayList<String> membershipList;
    public String getRelationship() {return StringUtils.arrayToCommaDelimitedString(relationshipList.toArray());}
    public ArrayList<String> relationshipList;
    public String getPersonalSpecial() {return StringUtils.arrayToCommaDelimitedString(specialList.toArray());}
    public ArrayList<String> specialList;

    public Personal() {
        moodList = new ArrayList<>();
        ethicsList = new ArrayList<>();
        membershipList = new ArrayList<>();
        relationshipList = new ArrayList<>();
        specialList = new ArrayList<>();
    }
}
