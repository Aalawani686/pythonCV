import java.io.*;
import java.net.*;
    public class client {
    public static void main(String[] args) {
      System.out.println("waiting");
    try{
    Socket soc=new Socket("localhost", 3341);
    BufferedReader inFromServer = new BufferedReader(new InputStreamReader (soc.getInputStream()));
    String fromServer;
    while ( true )
    {
        System.out.println("waiting");
        fromServer = inFromServer.readLine();
        if(fromServer != null){
          System.out.println( "RECEIVED:" + fromServer );
        }
    }
    }catch(Exception e){
        e.printStackTrace();}
    }
  }
