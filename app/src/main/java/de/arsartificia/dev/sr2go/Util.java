package de.arsartificia.dev.sr2go;

import java.io.IOException;

public class Util {
    public static boolean isOnline(String url) {
        Runtime runtime = Runtime.getRuntime();
        try {

            Process ipProcess = runtime.exec("/system/bin/ping -c 1 "+url);
            int     exitValue = ipProcess.waitFor();
            return (exitValue == 0);

        } catch (IOException|InterruptedException e) {
            e.printStackTrace();
        }

        return false;
    }
}
