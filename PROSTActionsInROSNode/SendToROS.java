package rddl.competition;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;

public class SendToROS {
    static OutputStreamWriter osw = null;
    SendToROS () throws IOException {
    }

    public static void SendROSMessage(String msg) throws IOException {
        if(osw == null)
        {
            InetAddress address = InetAddress.getByName("localhost");
            Socket connection = new Socket(address, 1770);
            System.out.println("RDDL client initialized");

            BufferedOutputStream bos = new BufferedOutputStream(connection.
                    getOutputStream());
            osw = new OutputStreamWriter(bos, "US-ASCII");
        }
        Server.sendOneMessage(osw, msg);
    }

}
