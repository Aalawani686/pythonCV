import java.io.*;
import java.net.*;
import edu.wpi.first.wpilibj.networktables.NetworkTable;
    public class client {
    public static void main(String[] args) {

      System.out.println("waiting");
    try{
    Socket soc=new Socket("localhost", 3341);
    BufferedReader inFromServer = new BufferedReader(new InputStreamReader (soc.getInputStream()));
    String fromServer;
    NetworkTable.setClientMode();
    NetworkTable.setIPAddress("roboRIO-3341-FRC.local");
    NetworkTable table = NetworkTable.getTable("cv");

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
